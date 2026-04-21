"""Pronunciation trainer endpoints.

Issues 10-minute Azure Speech tokens and tracks daily usage (500s/user/day).
Only users with plan 'pronounce' or 'app_pronounce' (subscription.tier) can access.
"""
import uuid
import logging
from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
import httpx
from app.auth import get_current_user
from app.database import get_db
from app.models import User, Subscription
from app.config import settings

logger = logging.getLogger(__name__)
router = APIRouter()

DAILY_LIMIT = 500
MAX_RECORDING = 20
PRONOUNCE_PLANS = {"pronounce", "app_pronounce"}


def _require_pronounce(user: User, db: Session) -> Subscription:
    sub = db.query(Subscription).filter(Subscription.user_id == user.id).first()
    if not sub or sub.tier not in PRONOUNCE_PLANS:
        raise HTTPException(status_code=403, detail="Your account does not include pronunciation trainer access")
    return sub


def _get_seconds_used(db: Session, user_id: uuid.UUID) -> int:
    row = db.execute(
        text("SELECT seconds_used FROM pron_daily_usage WHERE user_id = :uid AND date = CURRENT_DATE"),
        {"uid": str(user_id)},
    ).first()
    return row.seconds_used if row else 0


@router.get("/token")
async def get_azure_token(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _require_pronounce(current_user, db)

    seconds_used = _get_seconds_used(db, current_user.id)
    if seconds_used >= DAILY_LIMIT:
        raise HTTPException(status_code=429, detail=f"Daily limit of {DAILY_LIMIT}s reached. Resets at midnight.")

    if not settings.speech_key or not settings.speech_region:
        raise HTTPException(status_code=503, detail="Azure Speech not configured on this server")

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(
                f"https://{settings.speech_region}.api.cognitive.microsoft.com/sts/v1.0/issueToken",
                headers={"Ocp-Apim-Subscription-Key": settings.speech_key},
            )
        r.raise_for_status()
    except httpx.HTTPStatusError as e:
        logger.error(f"[Pronounce] Azure token failed: {e.response.status_code}")
        raise HTTPException(status_code=502, detail="Azure Speech service unavailable")
    except httpx.RequestError as e:
        logger.error(f"[Pronounce] Azure token error: {e}")
        raise HTTPException(status_code=502, detail="Azure Speech service unreachable")

    return {
        "token": r.text,
        "region": settings.speech_region,
        "seconds_remaining": max(0, DAILY_LIMIT - seconds_used),
        "max_recording": MAX_RECORDING,
    }


@router.post("/usage")
def record_usage(
    body: dict,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _require_pronounce(current_user, db)

    seconds = min(int(body.get("seconds", 0)), MAX_RECORDING)
    if seconds <= 0:
        seconds_used = _get_seconds_used(db, current_user.id)
        return {"seconds_used": seconds_used, "seconds_remaining": max(0, DAILY_LIMIT - seconds_used)}

    db.execute(
        text("""
            INSERT INTO pron_daily_usage (id, user_id, date, seconds_used)
            VALUES (:id, :uid, CURRENT_DATE, :s)
            ON CONFLICT (user_id, date)
            DO UPDATE SET seconds_used = LEAST(pron_daily_usage.seconds_used + :s, :limit)
        """),
        {"id": str(uuid.uuid4()), "uid": str(current_user.id), "s": seconds, "limit": DAILY_LIMIT},
    )
    db.commit()

    seconds_used = _get_seconds_used(db, current_user.id)
    return {"seconds_used": seconds_used, "seconds_remaining": max(0, DAILY_LIMIT - seconds_used)}


@router.get("/usage")
def get_usage(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _require_pronounce(current_user, db)
    seconds_used = _get_seconds_used(db, current_user.id)
    return {"seconds_used": seconds_used, "seconds_remaining": max(0, DAILY_LIMIT - seconds_used), "limit": DAILY_LIMIT}
