"""Tense Quest persistence — drill completions (= leaderboard points) and the
per-user SRS review deck of conjugation cards.

See `app/data/tense_quest.py` for the (derived) content layer and
`app/services/tense_quest_srs.py` for the spaced-repetition transitions.
"""
import uuid

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class TenseQuestDrillCompletion(Base):
    """One row per (user, drill) the user has finished. Count == leaderboard
    points. `drill_id` is a grammar situation id; `tense_group_id` is the
    Tense-Quest group slug it belongs to (denormalised for cheap progress
    queries)."""

    __tablename__ = "tense_quest_drill_completions"
    __table_args__ = (
        UniqueConstraint("user_id", "drill_id", name="uq_tq_drill_completion"),
        Index("ix_tq_completions_user", "user_id"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    drill_id = Column(String, nullable=False)
    tense_group_id = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class TenseQuestCard(Base):
    """A single conjugation card in a user's review deck.

    `card_key` == "{tense_group_id}:{verb}:{pronoun}". `box` is a 1..5 Leitner
    box; `due_at` is when the card next wants reviewing; `deck_position` is the
    flip-through order (randomised by the Shuffle button). A "lapse" (wrong, or
    correct-but-slow) resets `box` to 1 and pulls `due_at` in close.
    """

    __tablename__ = "tense_quest_cards"
    __table_args__ = (
        UniqueConstraint("user_id", "card_key", name="uq_tq_card"),
        Index("ix_tq_cards_user_due", "user_id", "due_at"),
        Index("ix_tq_cards_user_pos", "user_id", "deck_position"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    card_key = Column(String, nullable=False)
    tense_group_id = Column(String, nullable=False)
    verb = Column(String, nullable=False)
    pronoun = Column(String, nullable=False)

    box = Column(Integer, nullable=False, server_default="1", default=1)
    reps = Column(Integer, nullable=False, server_default="0", default=0)
    lapses = Column(Integer, nullable=False, server_default="0", default=0)
    deck_position = Column(Integer, nullable=False, server_default="0", default=0)

    due_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    last_result = Column(String, nullable=True)  # 'great' | 'good' | 'lapse'
    last_response_ms = Column(Integer, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
