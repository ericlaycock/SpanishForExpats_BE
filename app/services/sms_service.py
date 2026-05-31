"""Twilio SMS service for the free-trial next-day reminder.

Optional config — if Twilio env vars are missing, send_sms() is a no-op that
logs (mirrors email_service's SMTP-optional pattern), so the app runs fine
without messaging configured. Auth uses an API key:
Client(api_key_sid, api_key_secret, account_sid).
"""
import logging

from app.config import settings

logger = logging.getLogger(__name__)


def sms_configured() -> bool:
    return bool(
        settings.twilio_account_sid
        and settings.twilio_api_key_sid
        and settings.twilio_api_key_secret
        and settings.twilio_from_number
    )


def send_sms(to: str, body: str) -> bool:
    """Send an SMS. Returns True on success, False if unconfigured or on error."""
    if not sms_configured():
        logger.warning("[SMS] Twilio not configured — skipping send to %s", to)
        return False
    try:
        # Imported lazily so the app still boots if the dependency isn't
        # installed in a given environment.
        from twilio.rest import Client

        client = Client(
            settings.twilio_api_key_sid,
            settings.twilio_api_key_secret,
            settings.twilio_account_sid,
        )
        msg = client.messages.create(
            to=to,
            from_=settings.twilio_from_number,
            body=body,
        )
        logger.info("[SMS] sent to %s sid=%s", to, getattr(msg, "sid", "?"))
        return True
    except Exception as exc:  # noqa: BLE001
        logger.error("[SMS] send to %s failed: %s", to, exc)
        return False
