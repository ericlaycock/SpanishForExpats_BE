"""Free-trial follow-up: passwordless phone signup + next-day SMS dispatch.

Signup captures a phone number at the end of the memorize flow (passwordless —
we synthesize a placeholder email + random password so the existing non-null
email/password columns are satisfied; the real identity is the phone) and
schedules a reminder for ~24h later. A cron hits the dispatch endpoint to text
due reminders a one-time login link back into the recall flow.
"""
import logging
import re
import secrets
import uuid
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, Header, HTTPException, Request
from pydantic import BaseModel, Field
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.auth import create_access_token, get_current_user, get_password_hash
from app.config import settings
from app.database import get_db
from app.models import Subscription, TrialReminder, User
from app.services.sms_service import send_sms

logger = logging.getLogger(__name__)
router = APIRouter()

# Public signup shares the translate per-IP limiter to cap account creation.
from app.api.v1.memorize import _enforce_translate_rate_limit  # noqa: E402

MAGIC_TOKEN_DAYS = 7


def _normalize_phone(raw: str) -> str:
    """Light E.164-ish normalization: keep a leading +, strip other formatting."""
    s = raw.strip()
    plus = s.startswith("+")
    digits = re.sub(r"\D", "", s)
    if not digits:
        raise HTTPException(status_code=400, detail="A valid phone number is required.")
    return ("+" if plus else "") + digits


class SignupRequest(BaseModel):
    phone: str = Field(..., min_length=5, max_length=32)
    word_es: str = Field(..., min_length=1, max_length=500)
    word_en: str = Field(..., min_length=1, max_length=500)
    # Anonymous funnel session id (from the browser) so we can map this signup
    # back to the campaign link it started on.
    session_id: str | None = Field(default=None, max_length=64)


def _resolve_source(db: Session, session_id: str | None) -> str | None:
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


class SignupResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/signup", response_model=SignupResponse)
def freetrial_signup(body: SignupRequest, request: Request, db: Session = Depends(get_db)):
    """Find-or-create a passwordless user by phone, schedule the next-day SMS,
    and return a session token so the just-memorized word can be saved."""
    _enforce_translate_rate_limit(request)
    phone = _normalize_phone(body.phone)

    user = db.query(User).filter(User.phone_number == phone).first()
    if user is None:
        synthetic_email = f"trial+{re.sub(r'[^0-9]', '', phone)}@phone.spanishforexpats.local"
        user = User(
            email=synthetic_email,
            password_hash=get_password_hash(secrets.token_urlsafe(24)),
            phone_number=phone,
            name="Free trial",
        )
        db.add(user)
        db.flush()  # assign user.id
        db.add(Subscription(user_id=user.id, active=False))

    source = _resolve_source(db, body.session_id)
    reminder = TrialReminder(
        user_id=user.id,
        phone_number=phone,
        code=secrets.token_urlsafe(6),
        word_es=body.word_es.strip(),
        word_en=body.word_en.strip(),
        channel="sms",
        funnel_session_id=body.session_id,
        source=source,
        scheduled_at=datetime.now(timezone.utc)
        + timedelta(seconds=settings.trial_reminder_delay_seconds),
    )
    db.add(reminder)
    db.commit()

    token = create_access_token({"sub": str(user.id)})
    logger.info(
        "freetrial/signup phone=%s user=%s word=%r source=%s delay_s=%d",
        phone, user.id, body.word_es, source, settings.trial_reminder_delay_seconds,
    )
    return SignupResponse(access_token=token)


class DispatchResponse(BaseModel):
    sent: int


@router.post("/dispatch-reminders", response_model=DispatchResponse)
def dispatch_reminders(
    db: Session = Depends(get_db),
    x_cron_secret: str | None = Header(default=None),
):
    """Cron-triggered: text every due, unsent reminder a one-time recall link."""
    if not settings.cron_secret or x_cron_secret != settings.cron_secret:
        raise HTTPException(status_code=403, detail="Forbidden")

    now = datetime.now(timezone.utc)
    due = (
        db.query(TrialReminder)
        .filter(TrialReminder.sent_at.is_(None), TrialReminder.scheduled_at <= now)
        .order_by(TrialReminder.scheduled_at)
        .limit(200)
        .all()
    )

    sent = 0
    seen_users: set = set()
    base = settings.frontend_url.rstrip("/")
    # `due` is newest-first; send one reminder per user and supersede any older
    # duplicates (e.g. a retried signup) so nobody gets two texts. The link
    # carries ONLY the token — the answer (word_es) is fetched server-side via
    # /recall-word so it never appears in the SMS.
    for r in due:
        if r.user_id in seen_users:
            r.sent_at = now  # supersede; don't send a duplicate
            continue
        seen_users.add(r.user_id)
        if not r.code:
            r.code = secrets.token_urlsafe(6)  # backfill older rows
        link = f"{base}/r/{r.code}"
        body = (
            "It's Eric from Spanish for Expats \U0001f44b Yesterday you memorized "
            "your first Spanish word. Bet you still remember it — 10-sec "
            f"test \U0001f449 {link}"
        )
        if send_sms(r.phone_number, body):
            r.sent_at = now
            sent += 1
    db.commit()
    logger.info("freetrial/dispatch-reminders due=%d sent=%d", len(due), sent)
    return DispatchResponse(sent=sent)


class RedeemResponse(BaseModel):
    access_token: str
    es: str
    en: str


@router.get("/redeem/{code}", response_model=RedeemResponse)
def redeem(code: str, db: Session = Depends(get_db)):
    """Exchange a short SMS-link code for a session token + the word. Public —
    the code is the secret (8 random url-safe chars)."""
    reminder = db.query(TrialReminder).filter(TrialReminder.code == code).first()
    if not reminder:
        raise HTTPException(status_code=404, detail="Link not found or expired")
    token = create_access_token(
        {"sub": str(reminder.user_id)}, expires_delta=timedelta(days=MAGIC_TOKEN_DAYS)
    )
    return RedeemResponse(
        access_token=token, es=reminder.word_es, en=reminder.word_en
    )


class RecallWordResponse(BaseModel):
    es: str
    en: str


@router.get("/recall-word", response_model=RecallWordResponse)
def recall_word(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Return the word for the user's most recent reminder. Lets the recall page
    fetch the answer via the magic-link token instead of carrying it in the URL."""
    reminder = (
        db.query(TrialReminder)
        .filter(TrialReminder.user_id == current_user.id)
        .order_by(TrialReminder.created_at.desc())
        .first()
    )
    if not reminder:
        raise HTTPException(status_code=404, detail="No reminder found")
    return RecallWordResponse(es=reminder.word_es, en=reminder.word_en)


@router.post("/recall-complete")
def recall_complete(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Stamp the user's most recent reminder as completed — the conversion
    signal that they returned via the SMS and finished the recall/application."""
    reminder = (
        db.query(TrialReminder)
        .filter(TrialReminder.user_id == current_user.id)
        .order_by(TrialReminder.created_at.desc())
        .first()
    )
    if reminder and reminder.completed_at is None:
        reminder.completed_at = datetime.now(timezone.utc)
        db.commit()
    logger.info("freetrial/recall-complete user=%s word=%r", current_user.id,
                reminder.word_es if reminder else None)
    return {"ok": True}
