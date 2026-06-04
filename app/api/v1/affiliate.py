"""Affiliate portal — read-only funnel metrics scoped to ONE source.

An affiliate user (User.affiliate_source set, e.g. "pan") may read the conversion
funnel for exactly their own source and nothing else. The source is taken from
the authenticated user's record — never from a client-supplied parameter — so an
affiliate can't widen their view to other campaigns. Non-affiliates (including
regular users) get 403. This is deliberately separate from /v1/admin, which an
affiliate must never reach.
"""
import logging
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text, func

from app.auth import get_current_user
from app.database import get_db
from app.models import User, TrialReminder
from app.schemas import WebpageflowStep
# Single source of truth for the canonical funnel step order + labels.
from app.api.v1.admin import WEBPAGEFLOW_STEPS

logger = logging.getLogger(__name__)
router = APIRouter()


def _require_affiliate(user: User) -> str:
    """Return the caller's bound source, or 403 if they aren't an affiliate."""
    if not user.affiliate_source:
        raise HTTPException(status_code=403, detail="Affiliate access required")
    return user.affiliate_source


class AffiliateMetricsResponse(BaseModel):
    source: str
    # Full pre-signup funnel for THIS source, in canonical order.
    steps: list[WebpageflowStep]
    # Headline conversion counts (all scoped to this source).
    visits: int            # landing_view
    trial_starts: int      # ft_start
    memorize_started: int  # ft_memorize_start
    mastered: int          # ft_mastered
    calls_booked: int      # book_call_click
    phone_signups: int     # distinct users who gave a phone number
    texts_sent: int        # reminders actually texted
    returned: int          # reminders completed (came back + finished recall)
    paying_students: int   # referred users who became paying (one payout each)
    estimated_earnings_cents: int  # sum of this source's payout amounts


@router.get("/metrics", response_model=AffiliateMetricsResponse)
def get_affiliate_metrics(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Conversion funnel for the affiliate's own source only."""
    source = _require_affiliate(current_user)

    # Pre-signup funnel: count distinct sessions per event, restricted to
    # sessions that ever fired ANY event tagged with this source. EXISTS (not a
    # join) keeps COUNT(DISTINCT) honest. Mirrors /v1/admin/webpageflow?source=.
    rows = db.execute(
        text("""
            SELECT a.event_key, COUNT(DISTINCT a.session_id) AS n
            FROM anonymous_funnel_events a
            WHERE EXISTS (
                SELECT 1 FROM anonymous_funnel_events b
                WHERE b.session_id = a.session_id
                  AND b.event_metadata ->> 'utm_source' = :source
            )
            GROUP BY a.event_key
        """),
        {"source": source},
    ).fetchall()
    counts = {r.event_key: int(r.n) for r in rows}

    steps = [
        WebpageflowStep(event_key=key, label=label, count=counts.get(key, 0))
        for key, label in WEBPAGEFLOW_STEPS
    ]

    # Per-person SMS follow-up, scoped to this source via trial_reminders.source.
    signups = (
        db.query(func.count(func.distinct(TrialReminder.user_id)))
        .filter(TrialReminder.source == source)
        .scalar()
        or 0
    )
    texts = (
        db.query(func.count(TrialReminder.id))
        .filter(TrialReminder.source == source, TrialReminder.sent_at.isnot(None))
        .scalar()
        or 0
    )
    returned = (
        db.query(func.count(TrialReminder.id))
        .filter(TrialReminder.source == source, TrialReminder.completed_at.isnot(None))
        .scalar()
        or 0
    )

    # Paying students attributed to this source (one AffiliatePayout row each,
    # created by the Stripe webhook at first payment) + estimated earnings.
    payout = db.execute(
        text("""
            SELECT COUNT(*) AS n, COALESCE(SUM(amount_cents), 0) AS cents
            FROM affiliate_payouts WHERE affiliate_source = :source
        """),
        {"source": source},
    ).fetchone()

    return AffiliateMetricsResponse(
        source=source,
        steps=steps,
        visits=counts.get("landing_view", 0),
        trial_starts=counts.get("ft_start", 0),
        memorize_started=counts.get("ft_memorize_start", 0),
        mastered=counts.get("ft_mastered", 0),
        calls_booked=counts.get("book_call_click", 0),
        phone_signups=int(signups),
        texts_sent=int(texts),
        returned=int(returned),
        paying_students=int(payout.n),
        estimated_earnings_cents=int(payout.cents),
    )
