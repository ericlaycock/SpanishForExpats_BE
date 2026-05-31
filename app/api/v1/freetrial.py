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
from urllib.parse import quote

from fastapi import APIRouter, Depends, Header, HTTPException, Request
from pydantic import BaseModel, Field
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

    reminder = TrialReminder(
        user_id=user.id,
        phone_number=phone,
        word_es=body.word_es.strip(),
        word_en=body.word_en.strip(),
        channel="sms",
        scheduled_at=datetime.now(timezone.utc)
        + timedelta(minutes=settings.trial_reminder_delay_minutes),
    )
    db.add(reminder)
    db.commit()

    token = create_access_token({"sub": str(user.id)})
    logger.info(
        "freetrial/signup phone=%s user=%s word=%r delay_min=%d",
        phone, user.id, body.word_es, settings.trial_reminder_delay_minutes,
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
    base = settings.frontend_url.rstrip("/")
    for r in due:
        token = create_access_token(
            {"sub": str(r.user_id)}, expires_delta=timedelta(days=MAGIC_TOKEN_DAYS)
        )
        link = (
            f"{base}/freetrial/recall?token={token}"
            f"&es={quote(r.word_es)}&en={quote(r.word_en)}"
        )
        body = f'How do you say "{r.word_en}" in Spanish? {link}'
        if send_sms(r.phone_number, body):
            r.sent_at = now
            sent += 1
    db.commit()
    logger.info("freetrial/dispatch-reminders due=%d sent=%d", len(due), sent)
    return DispatchResponse(sent=sent)


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
