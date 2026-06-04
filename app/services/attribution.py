"""Campaign-source attribution helpers (shared).

`resolve_source_from_session` maps a funnel session_id → its utm_source from the
anonymous funnel events (the first event that carries one). `resolve_onboarding_source`
is the register-time resolver used to credit a paying student to the partner who
referred them: it tries the browser's funnel session first, then a prior
trial-reminder source, then a Calendly booking's funnel session.
"""
import logging

from sqlalchemy import text
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


def resolve_source_from_session(db: Session, session_id: str | None) -> str | None:
    """The campaign source (utm_source) for a funnel session, taken from the
    earliest event row that carries one. Returns None if unknown."""
    if not session_id:
        return None
    row = db.execute(
        text(
            """
            SELECT event_metadata ->> 'utm_source' AS src
            FROM anonymous_funnel_events
            WHERE session_id = :sid
              AND event_metadata ->> 'utm_source' IS NOT NULL
            ORDER BY occurred_at ASC
            LIMIT 1
            """
        ),
        {"sid": session_id},
    ).fetchone()
    return row.src if row else None


def resolve_onboarding_source(
    db: Session, *, user_id, email: str | None = None, session_id: str | None = None
) -> str | None:
    """Best-effort: which affiliate source should this newly-registered user be
    credited to? Tries (1) the browser funnel session, (2) a prior TrialReminder
    source, (3) a Calendly BookedCall's funnel session. Returns None if unknown.
    Each fallback is isolated so a missing column / table never raises."""
    # 1) funnel session passed from the browser at register
    src = resolve_source_from_session(db, session_id)
    if src:
        return src
    # 2) a phone-first trial user already has a resolved source
    try:
        from app.models import TrialReminder
        row = (
            db.query(TrialReminder.source)
            .filter(TrialReminder.user_id == user_id, TrialReminder.source.isnot(None))
            .order_by(TrialReminder.created_at.desc())
            .first()
        )
        if row and row[0]:
            return row[0]
    except Exception as e:  # pragma: no cover - defensive
        logger.debug("trial-reminder source lookup failed: %s", e)
    # 3) a Calendly booking carries a funnel_session_id (matched by user_id/email)
    try:
        from app.models import BookedCall
        q = db.query(BookedCall.funnel_session_id).filter(
            BookedCall.funnel_session_id.isnot(None)
        )
        if email:
            q = q.filter(
                (BookedCall.user_id == user_id) | (BookedCall.invitee_email == email)
            )
        else:
            q = q.filter(BookedCall.user_id == user_id)
        row = q.first()
        if row and row[0]:
            return resolve_source_from_session(db, row[0])
    except Exception as e:  # pragma: no cover - defensive
        logger.debug("booked-call source lookup failed: %s", e)
    return None
