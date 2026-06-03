from pydantic_settings import BaseSettings
from typing import Optional
import os
import warnings


class Settings(BaseSettings):
    database_url: str
    openai_api_key: str
    jwt_secret: str = "CHANGE_THIS_IN_PRODUCTION"  # Default for development
    jwt_algorithm: str = "HS256"
    jwt_expiration_hours: int = 72
    mastery_spoken_threshold: int = 2

    # Registration whitelist (comma-separated tokens) — all grant 'app' plan
    whitelist_tokens: str = ""
    # Tokens that grant 'pronounce' plan (pronunciation trainer only, no app lessons)
    pronounce_tokens: str = ""
    # Tokens that grant 'app_pronounce' plan (app lessons + pronunciation trainer)
    app_pronounce_tokens: str = ""

    # SMTP for password reset emails (Gmail App Password)
    smtp_email: Optional[str] = None
    smtp_app_password: Optional[str] = None

    # Single shared Zoom URL used for every cohort session (3-day live cohorts).
    cohort_zoom_url: Optional[str] = None

    # Azure Speech (pronunciation trainer)
    speech_key: Optional[str] = None
    speech_region: Optional[str] = None

    # HuggingFace token for wav2vec2 Inference API
    hf_token: Optional[str] = None

    # R2 / S3 storage for TTS audio (optional — falls back to local /tmp)
    r2_endpoint_url: Optional[str] = None
    r2_access_key_id: Optional[str] = None
    r2_secret_access_key: Optional[str] = None
    r2_bucket_name: str = "audio"
    r2_public_url: Optional[str] = None

    # Stripe (payment)
    stripe_secret_key: Optional[str] = None
    stripe_webhook_secret: Optional[str] = None

    # Calendly (founder onboarding-call webhook)
    calendly_webhook_signing_key: Optional[str] = None

    # Twilio SMS (free-trial next-day reminder). All optional — the SMS service
    # no-ops + logs when unset (mirrors the SMTP email pattern). API key auth:
    # Client(api_key_sid, api_key_secret, account_sid).
    twilio_account_sid: Optional[str] = None
    twilio_api_key_sid: Optional[str] = None
    twilio_api_key_secret: Optional[str] = None
    twilio_from_number: Optional[str] = None
    # Shared secret guarding the reminder-dispatch cron endpoint.
    cron_secret: Optional[str] = None
    # Seconds after signup to schedule the next-day SMS. ⚠️ TESTING DEFAULT is
    # 30s — set TRIAL_REMINDER_DELAY_SECONDS=86400 (24h) for production.
    trial_reminder_delay_seconds: int = 30
    stripe_price_pro_monthly: str = "price_STUB_pro_monthly"
    stripe_price_pro_6month: str = "price_STUB_pro_6month"
    stripe_price_fluency_monthly: str = "price_STUB_fluency_monthly"
    stripe_price_fluency_6month: str = "price_STUB_fluency_6month"
    frontend_url: str = "https://www.spanishforexpats.com"

    # Affiliate portal seed — on boot the app upserts a single read-only
    # affiliate account scoped to AFFILIATE_SOURCE (see main.py lifespan).
    # The password is supplied PRE-HASHED (bcrypt) so no plaintext credential
    # ever lives in the repo or env in clear form. All three must be set for
    # the seed to run; otherwise it no-ops (mirrors the SMS/SMTP optional
    # pattern). Multiple affiliates would graduate to a real seed table.
    affiliate_email: Optional[str] = None
    affiliate_password_hash: Optional[str] = None
    affiliate_source: Optional[str] = None

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()

# Warn if using default JWT secret
if settings.jwt_secret == "CHANGE_THIS_IN_PRODUCTION":
    warnings.warn(
        "WARNING: Using default JWT_SECRET. Set JWT_SECRET environment variable for production!",
        UserWarning
    )



