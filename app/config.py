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

    # Registration whitelist (comma-separated tokens, empty = open registration)
    # All whitelist_tokens grant 'app' plan (backward compat).
    whitelist_tokens: str = ""

    # Plan tokens: JSON mapping token → plan ('app' | 'pronounce' | 'app_pronounce')
    # Example: {"abc123": "app", "def456": "pronounce", "ghi789": "app_pronounce"}
    plan_tokens: str = ""

    # SMTP for password reset emails (Gmail App Password)
    smtp_email: Optional[str] = None
    smtp_app_password: Optional[str] = None

    # R2 / S3 storage for TTS audio (optional — falls back to local /tmp)
    r2_endpoint_url: Optional[str] = None
    r2_access_key_id: Optional[str] = None
    r2_secret_access_key: Optional[str] = None
    r2_bucket_name: str = "audio"
    r2_public_url: Optional[str] = None

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



