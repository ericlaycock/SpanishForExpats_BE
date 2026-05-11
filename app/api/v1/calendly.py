"""Calendly integration — webhook receiver + booked-count endpoint.

The webhook is the source of truth for founder-call bookings. The FE's
postMessage listener for `calendly.event_scheduled` is best-effort UX;
when ad blockers or strict-tracking browsers block the widget, this
webhook still records the booking and keeps the funnel measurable.

`MANUAL_OFFSET` represents bookings made before this system existed.
The counter shown to users is `MANUAL_OFFSET + count(rows this month)`.
"""
import hmac
import hashlib
import logging
import time
from datetime import datetime, timezone
from typing import Optional, Tuple

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import BookedCall
from app.config import settings

logger = logging.getLogger(__name__)
router = APIRouter()

# Bookings made through Calendly before this webhook existed. Surfaced in
# the live counter so "X of 30" reflects total founder availability used.
MANUAL_OFFSET = 14
MONTHLY_CAP = 30

# In-memory TTL cache for the booked-count endpoint. Single-region
# deployment, so per-replica staleness is acceptable.
_BOOKED_COUNT_CACHE: dict = {"value": None, "expires_at": 0.0}
_BOOKED_COUNT_TTL_SECONDS = 60


def _verify_calendly_signature(raw_body: bytes, sig_header: str, signing_key: str) -> bool:
    """Verify Calendly's HMAC-SHA256 signature.

    Header format: `t=<unix_seconds>,v1=<hex_digest>`. Signed payload is
    `f"{t}.{raw_body}"`.
    """
    parts = dict(p.split("=", 1) for p in sig_header.split(",") if "=" in p)
    t = parts.get("t")
    v1 = parts.get("v1")
    if not t or not v1:
        return False
    signed_payload = f"{t}.{raw_body.decode('utf-8', errors='replace')}".encode("utf-8")
    expected = hmac.new(
        signing_key.encode("utf-8"),
        signed_payload,
        hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(expected, v1)


def _parse_invitee(payload: dict) -> Tuple[Optional[str], Optional[str], Optional[str], Optional[datetime], Optional[str], Optional[str]]:
    """Extract the fields we need from a Calendly webhook payload.

    Returns (invitee_uuid, invitee_email, event_uri, scheduled_at, invitee_tz, utm_session).
    Tolerant of missing fields — the caller decides what's required.
    """
    invitee = (payload.get("payload") or {}).get("invitee") or payload.get("invitee") or {}
    event = (payload.get("payload") or {}).get("event") or payload.get("event") or {}

    # Calendly invitee URI ends with `/invitees/<uuid>`. Take the trailing
    # segment as the idempotency key.
    invitee_uri = invitee.get("uri") or invitee.get("invitee") or ""
    invitee_uuid = invitee_uri.rstrip("/").rsplit("/", 1)[-1] if invitee_uri else None
    invitee_email = (invitee.get("email") or "").strip().lower() or None
    event_uri = event.get("uri") or invitee.get("event")
    invitee_tz = invitee.get("timezone")

    scheduled_at_raw = event.get("start_time") or invitee.get("start_time")
    scheduled_at: Optional[datetime] = None
    if scheduled_at_raw:
        try:
            scheduled_at = datetime.fromisoformat(scheduled_at_raw.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            scheduled_at = None

    # Pull the funnel session id from Calendly's tracking object if present.
    # Calendly forwards `utm_*` query params under `tracking` for new
    # bookings — we send `utm_session=<funnelSessionId>` from the FE.
    tracking = invitee.get("tracking") or {}
    utm_session = tracking.get("utm_session") or tracking.get("salesforce_uuid")

    return invitee_uuid, invitee_email, event_uri, scheduled_at, invitee_tz, utm_session


@router.post("/webhook")
async def calendly_webhook(request: Request, db: Session = Depends(get_db)):
    """Receive Calendly invitee.created / invitee.canceled events.

    Idempotent on `invitee_uuid`. Reschedules fire canceled+created with
    the same UUID — we soft-flag and re-clear `canceled_at` accordingly.
    """
    raw_body = await request.body()
    sig_header = request.headers.get("calendly-webhook-signature", "")

    if settings.calendly_webhook_signing_key:
        if not _verify_calendly_signature(raw_body, sig_header, settings.calendly_webhook_signing_key):
            raise HTTPException(status_code=400, detail="Invalid Calendly signature")
    else:
        # Stub/dev mode — accept unsigned events. Don't enable in prod.
        logger.warning("calendly_webhook_signing_key not set — webhook signature NOT verified")

    import json
    try:
        payload = json.loads(raw_body)
    except (ValueError, TypeError):
        raise HTTPException(status_code=400, detail="Invalid JSON payload")

    event_type = payload.get("event") or payload.get("type") or ""
    invitee_uuid, invitee_email, event_uri, scheduled_at, invitee_tz, utm_session = _parse_invitee(payload)

    if not invitee_uuid:
        # Nothing actionable, but ack so Calendly doesn't keep retrying.
        logger.warning("calendly_webhook event missing invitee uuid: type=%s", event_type)
        return {"status": "ignored"}

    row = db.query(BookedCall).filter(BookedCall.invitee_uuid == invitee_uuid).first()

    if event_type.endswith("invitee.created") or event_type == "invitee_created":
        if row is None:
            if not invitee_email or scheduled_at is None:
                logger.warning("calendly_webhook invitee.created missing email/scheduled_at: uuid=%s", invitee_uuid)
                return {"status": "ignored"}
            row = BookedCall(
                invitee_uuid=invitee_uuid,
                invitee_email=invitee_email,
                calendly_event_uri=event_uri,
                scheduled_at=scheduled_at,
                invitee_timezone=invitee_tz,
                funnel_session_id=utm_session,
            )
            db.add(row)
        else:
            # Reschedule path — restore the row.
            row.canceled_at = None
            if scheduled_at is not None:
                row.scheduled_at = scheduled_at
            if invitee_tz:
                row.invitee_timezone = invitee_tz
            if event_uri:
                row.calendly_event_uri = event_uri
        db.commit()
        _BOOKED_COUNT_CACHE["expires_at"] = 0.0
        return {"status": "ok", "action": "created"}

    if event_type.endswith("invitee.canceled") or event_type == "invitee_canceled":
        if row is not None and row.canceled_at is None:
            row.canceled_at = datetime.now(timezone.utc)
            db.commit()
            _BOOKED_COUNT_CACHE["expires_at"] = 0.0
        return {"status": "ok", "action": "canceled"}

    return {"status": "ignored", "event_type": event_type}


@router.get("/booked-count")
async def booked_count(db: Session = Depends(get_db)):
    """Public — current month's booking count for the founder-spots counter.

    `booked = MANUAL_OFFSET + count(BookedCall this month, not canceled)`.
    Cached in-memory for 60s.
    """
    now_mono = time.monotonic()
    if _BOOKED_COUNT_CACHE["value"] is not None and now_mono < _BOOKED_COUNT_CACHE["expires_at"]:
        return _BOOKED_COUNT_CACHE["value"]

    now = datetime.now(timezone.utc)
    start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    rows = (
        db.query(BookedCall)
        .filter(BookedCall.created_at >= start_of_month)
        .filter(BookedCall.canceled_at.is_(None))
        .count()
    )
    value = {"booked": MANUAL_OFFSET + int(rows), "cap": MONTHLY_CAP}
    _BOOKED_COUNT_CACHE["value"] = value
    _BOOKED_COUNT_CACHE["expires_at"] = now_mono + _BOOKED_COUNT_TTL_SECONDS
    return value
