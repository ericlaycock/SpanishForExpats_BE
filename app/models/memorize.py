"""Memorize utility models."""
import uuid

from sqlalchemy import CheckConstraint, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class MemorizeCompletion(Base):
    """One row per user-confirmed memorisation. `coins_earned` rolls into
    `_user_points()` in app/api/v1/tense_quest.py alongside drill / vocab
    rewards, so a memorize completion increments the user's lifetime sun
    count visible in the ExpatQuest header HUD."""
    __tablename__ = "memorize_completions"
    __table_args__ = (
        CheckConstraint("coins_earned > 0", name="ck_memorize_coins_positive"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    spanish_phrase = Column(String(500), nullable=False)
    english_phrase = Column(String(500), nullable=True)
    coins_earned = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
