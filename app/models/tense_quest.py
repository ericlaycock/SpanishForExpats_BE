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
    """A single practice-sentence card in a user's review deck.

    `card_key` == "{drill_id}:{sentence_id}". `box` is a 1..5 Leitner box;
    `due_at` is when the card next wants reviewing; `deck_position` is the
    flip-through order (randomised by the Shuffle button). A "lapse" (wrong, or
    correct-but-slow) resets `box` to 1 and pulls `due_at` in close. The
    sentence's English/Spanish text is resolved on read from the grammar data,
    so only the keys are stored here.
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
    drill_id = Column(String, nullable=False)
    sentence_id = Column(String, nullable=False)

    box = Column(Integer, nullable=False, server_default="1", default=1)
    reps = Column(Integer, nullable=False, server_default="0", default=0)
    lapses = Column(Integer, nullable=False, server_default="0", default=0)
    deck_position = Column(Integer, nullable=False, server_default="0", default=0)
    # Coins this card has earned across reviews (2 for a fast hit, 1 for a
    # medium one, 0 for slow/wrong). The user's total coins = drill completions
    # + the sum of this across their deck.
    coins_earned = Column(Integer, nullable=False, server_default="0", default=0)

    due_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    last_result = Column(String, nullable=True)  # 'great' | 'good' | 'lapse'
    last_response_ms = Column(Integer, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


class TenseQuestDiagnostic(Base):
    """A user's placement-diagnostic result for one tense group:
    'ok' (all sampled conjugations right *and* each answered in <7s),
    'ok_slow' (all right but at least one was slow → "needs work, bit slow"),
    or 'needs_work' (missed ≥1). Re-taking the diagnostic overwrites the row.
    Independent of drill progress."""

    __tablename__ = "tense_quest_diagnostic"
    __table_args__ = (
        UniqueConstraint("user_id", "tense_group_id", name="uq_tq_diagnostic"),
        Index("ix_tq_diagnostic_user", "user_id"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    tense_group_id = Column(String, nullable=False)
    result = Column(String, nullable=False)  # 'ok' | 'ok_slow' | 'needs_work'
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


class TenseQuestSentenceCompletion(Base):
    """One row per (user, drill, sentence) the user has answered correctly in
    the in-drill sentence gauntlet. Worth +1 coin each (idempotent — replaying
    a drill doesn't re-award). Count feeds the user's coin total / leaderboard
    alongside drill completions and review-card coins."""

    __tablename__ = "tense_quest_sentence_completions"
    __table_args__ = (
        UniqueConstraint("user_id", "drill_id", "sentence_id", name="uq_tq_sentence_completion"),
        Index("ix_tq_sentence_completion_user", "user_id"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    drill_id = Column(String, nullable=False)
    sentence_id = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
