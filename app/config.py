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
    stripe_price_pro_monthly: str = "price_STUB_pro_monthly"
    stripe_price_pro_6month: str = "price_STUB_pro_6month"
    stripe_price_fluency_monthly: str = "price_STUB_fluency_monthly"
    stripe_price_fluency_6month: str = "price_STUB_fluency_6month"
    frontend_url: str = "https://www.spanishforexpats.com"

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



