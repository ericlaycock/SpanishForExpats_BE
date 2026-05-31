"""Free-trial next-day reminder model."""
import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class TrialReminder(Base):
    """One row per free-trial phone signup. The cron dispatcher finds rows whose
    `scheduled_at` has passed and `sent_at` is null, texts the user a recall
    link for `word_en`/`word_es`, and stamps `sent_at`."""
    __tablename__ = "trial_reminders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    phone_number = Column(String, nullable=False)
    # Short URL-safe code for the tiny SMS link (/r/<code>).
    code = Column(String(16), unique=True, nullable=True, index=True)
    word_es = Column(String(500), nullable=False)
    word_en = Column(String(500), nullable=False)
    channel = Column(String(16), nullable=False, default="sms")
    scheduled_at = Column(DateTime(timezone=True), nullable=False, index=True)
    sent_at = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
