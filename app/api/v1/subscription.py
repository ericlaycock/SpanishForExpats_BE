import json
import logging
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app.models import User, Subscription
from app.services.subscription_service import get_subscription_status
from app.schemas import (
    SubscriptionStatusResponse,
    CheckoutRequest,
    CheckoutResponse,
    CancelSubscriptionRequest,
    InvoiceItem,
    InvoiceListResponse,
)
from app.config import settings

logger = logging.getLogger(__name__)

router = APIRouter()

_PRICE_MAP = {
    ("pro", "monthly"): lambda: settings.stripe_price_pro_monthly,
    ("pro", "6month"): lambda: settings.stripe_price_pro_6month,
    ("fluency", "monthly"): lambda: settings.stripe_price_fluency_monthly,
    ("fluency", "6month"): lambda: settings.stripe_price_fluency_6month,
}


@router.get("/status", response_model=SubscriptionStatusResponse)
async def get_subscription_status_endpoint(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get subscription status and free encounter count."""
    status_info = get_subscription_status(db, str(current_user.id))
    return SubscriptionStatusResponse(**status_info)


@router.post("/checkout", response_model=CheckoutResponse)
async def create_checkout_session(
    body: CheckoutRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create a Stripe Checkout Session and return the redirect URL."""
    if not settings.stripe_secret_key:
        raise HTTPException(status_code=503, detail="Payment not configured")

    import stripe
    stripe.api_key = settings.stripe_secret_key

    price_fn = _PRICE_MAP.get((body.plan, body.billing_cycle))
    if not price_fn:
        raise HTTPException(status_code=400, detail="Invalid plan or billing cycle")
    price_id = price_fn()

    # Reuse existing Stripe customer if we have one
    sub = db.query(Subscription).filter(Subscription.user_id == current_user.id).first()
    if sub and sub.stripe_customer_id:
        customer_id = sub.stripe_customer_id
    else:
        customer = stripe.Customer.create(email=current_user.email)
        customer_id = customer.id

    session = stripe.checkout.Session.create(
        customer=customer_id,
        payment_method_types=["card"],
        line_items=[{"price": price_id, "quantity": 1}],
        mode="subscription",
        success_url=(
            f"{settings.frontend_url}/app/checkout/success"
            "?session_id={CHECKOUT_SESSION_ID}"
        ),
        cancel_url=f"{settings.frontend_url}/app/paywall",
        metadata={
            "user_id": str(current_user.id),
            "plan": body.plan,
            "billing_cycle": body.billing_cycle,
        },
    )

    return CheckoutResponse(checkout_url=session.url)


def _epoch_to_datetime(value) -> datetime | None:
    """Stripe returns unix epoch seconds; convert to tz-aware UTC datetimes
    so the column round-trips through SQLAlchemy without warnings."""
    if value is None:
        return None
    return datetime.fromtimestamp(int(value), tz=timezone.utc)


@router.post("/cancel", response_model=SubscriptionStatusResponse)
async def cancel_subscription(
    body: CancelSubscriptionRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Schedule cancellation at the current period end.

    Honors the user's existing access — Stripe keeps the subscription active
    until `current_period_end`, then the `customer.subscription.deleted`
    webhook flips `active` to false. Reactivating before that point
    (`POST /reactivate`) is a free undo.
    """
    sub = db.query(Subscription).filter(Subscription.user_id == current_user.id).first()
    if not sub or not sub.stripe_subscription_id:
        raise HTTPException(status_code=400, detail="No active subscription to cancel")

    if not settings.stripe_secret_key:
        raise HTTPException(status_code=503, detail="Payment not configured")

    import stripe
    stripe.api_key = settings.stripe_secret_key

    try:
        stripe_sub = stripe.Subscription.modify(
            sub.stripe_subscription_id,
            cancel_at_period_end=True,
        )
    except stripe.error.StripeError as e:
        logger.error(f"Stripe cancel failed for sub {sub.stripe_subscription_id}: {e}")
        raise HTTPException(status_code=502, detail="Stripe cancel failed")

    sub.cancel_at_period_end = True
    sub.current_period_end = _epoch_to_datetime(getattr(stripe_sub, "current_period_end", None))
    sub.canceled_at = _epoch_to_datetime(getattr(stripe_sub, "canceled_at", None)) or datetime.now(timezone.utc)
    if body.reason:
        # Store reason + optional note as a small JSON-ish blob in the text
        # column so analytics can inspect both without a separate table.
        sub.cancel_reason = body.reason if not body.note else f"{body.reason}: {body.note}"
    db.commit()

    return SubscriptionStatusResponse(**get_subscription_status(db, str(current_user.id)))


@router.post("/reactivate", response_model=SubscriptionStatusResponse)
async def reactivate_subscription(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Undo a pending cancellation if the period hasn't ended yet."""
    sub = db.query(Subscription).filter(Subscription.user_id == current_user.id).first()
    if not sub or not sub.stripe_subscription_id:
        raise HTTPException(status_code=400, detail="No subscription found")
    if not sub.cancel_at_period_end:
        # Already active and not pending cancel — nothing to undo. Return
        # current status rather than 4xx so the FE can be optimistic.
        return SubscriptionStatusResponse(**get_subscription_status(db, str(current_user.id)))

    if not settings.stripe_secret_key:
        raise HTTPException(status_code=503, detail="Payment not configured")

    import stripe
    stripe.api_key = settings.stripe_secret_key

    try:
        stripe.Subscription.modify(
            sub.stripe_subscription_id,
            cancel_at_period_end=False,
        )
    except stripe.error.StripeError as e:
        logger.error(f"Stripe reactivate failed for sub {sub.stripe_subscription_id}: {e}")
        raise HTTPException(status_code=502, detail="Stripe reactivate failed")

    sub.cancel_at_period_end = False
    sub.canceled_at = None
    sub.cancel_reason = None
    db.commit()

    return SubscriptionStatusResponse(**get_subscription_status(db, str(current_user.id)))


@router.get("/invoices", response_model=InvoiceListResponse)
async def list_invoices(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """List recent Stripe invoices for the current user.

    Read-only — Stripe is the source of truth, we don't cache them locally.
    Returns an empty list for users who never had a Stripe customer (e.g.
    free-tier users who never reached checkout).
    """
    sub = db.query(Subscription).filter(Subscription.user_id == current_user.id).first()
    if not sub or not sub.stripe_customer_id:
        return InvoiceListResponse(invoices=[])

    if not settings.stripe_secret_key:
        raise HTTPException(status_code=503, detail="Payment not configured")

    import stripe
    stripe.api_key = settings.stripe_secret_key

    try:
        result = stripe.Invoice.list(customer=sub.stripe_customer_id, limit=20)
    except stripe.error.StripeError as e:
        logger.error(f"Stripe invoice list failed for customer {sub.stripe_customer_id}: {e}")
        raise HTTPException(status_code=502, detail="Stripe invoice list failed")

    invoices = [
        InvoiceItem(
            id=inv.id,
            amount_paid=inv.amount_paid or 0,
            currency=(inv.currency or "usd").lower(),
            status=getattr(inv, "status", None),
            hosted_invoice_url=getattr(inv, "hosted_invoice_url", None),
            invoice_pdf=getattr(inv, "invoice_pdf", None),
            created=_epoch_to_datetime(inv.created),
        )
        for inv in result.data
    ]
    return InvoiceListResponse(invoices=invoices)


@router.post("/webhook")
async def stripe_webhook(request: Request, db: Session = Depends(get_db)):
    """Handle Stripe webhook events. Verified via Stripe-Signature header."""
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature", "")

    import stripe
    stripe.api_key = settings.stripe_secret_key

    if settings.stripe_webhook_secret:
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.stripe_webhook_secret
            )
        except (ValueError, stripe.error.SignatureVerificationError):
            raise HTTPException(status_code=400, detail="Invalid webhook signature")
    else:
        # Stub/dev mode — no signature verification
        event = stripe.Event.construct_from(json.loads(payload), stripe.api_key)

    if event.type == "checkout.session.completed":
        _handle_checkout_completed(db, event.data.object)

    elif event.type == "customer.subscription.updated":
        _handle_subscription_updated(db, event.data.object)

    elif event.type == "customer.subscription.deleted":
        _handle_subscription_deleted(db, event.data.object)

    return {"status": "ok"}


# ── Private helpers ──────────────────────────────────────────────────────────

def _handle_checkout_completed(db: Session, session_obj) -> None:
    meta = session_obj.metadata or {}
    user_id = meta.get("user_id")
    if not user_id:
        return

    sub = db.query(Subscription).filter(Subscription.user_id == user_id).first()
    if not sub:
        sub = Subscription(user_id=user_id)
        db.add(sub)

    sub.active = True
    sub.plan = meta.get("plan")
    sub.billing_cycle = meta.get("billing_cycle")
    sub.tier = meta.get("plan")              # keep tier in sync for check_paywall
    sub.stripe_customer_id = session_obj.customer
    sub.stripe_subscription_id = session_obj.subscription
    db.commit()


def _handle_subscription_updated(db: Session, stripe_sub) -> None:
    sub = db.query(Subscription).filter(
        Subscription.stripe_subscription_id == stripe_sub.id
    ).first()
    if not sub:
        return
    sub.active = stripe_sub.status in ("active", "trialing")
    sub.cancel_at_period_end = bool(getattr(stripe_sub, "cancel_at_period_end", False))
    period_end = getattr(stripe_sub, "current_period_end", None)
    if period_end is not None:
        sub.current_period_end = _epoch_to_datetime(period_end)
    canceled = getattr(stripe_sub, "canceled_at", None)
    if canceled is not None:
        sub.canceled_at = _epoch_to_datetime(canceled)
    elif not sub.cancel_at_period_end:
        # User reactivated outside the in-app flow (Stripe Dashboard etc.)
        sub.canceled_at = None
        sub.cancel_reason = None
    db.commit()


def _handle_subscription_deleted(db: Session, stripe_sub) -> None:
    sub = db.query(Subscription).filter(
        Subscription.stripe_subscription_id == stripe_sub.id
    ).first()
    if not sub:
        return
    sub.active = False
    sub.cancel_at_period_end = False
    if sub.canceled_at is None:
        sub.canceled_at = datetime.now(timezone.utc)
    db.commit()
