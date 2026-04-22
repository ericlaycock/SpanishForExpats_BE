import json
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app.models import User, Subscription
from app.services.subscription_service import get_subscription_status
from app.schemas import SubscriptionStatusResponse, CheckoutRequest, CheckoutResponse
from app.config import settings

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
    if sub:
        sub.active = stripe_sub.status in ("active", "trialing")
        db.commit()


def _handle_subscription_deleted(db: Session, stripe_sub) -> None:
    sub = db.query(Subscription).filter(
        Subscription.stripe_subscription_id == stripe_sub.id
    ).first()
    if sub:
        sub.active = False
        db.commit()
