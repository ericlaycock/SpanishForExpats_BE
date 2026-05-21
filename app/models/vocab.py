"""Vocab learning + spaced-repetition persistence.

Vocab Map modules are organised into chapters of 5 words each (up to 5
chapters = 25 words per module). Two tables back the flow:

- `vocab_chapter_completion` — one row per (user, module_id, chapter_index)
  the user has finished the press-and-speak gauntlet for. Idempotent on the
  unique constraint; used to derive the sidebar "x/5 chapters" + the
  module-SRS unlock.

- `vocab_card` — one row per (user, module_id, word_es). Created on chapter
  completion with `status='module'`. Promoted to `status='main'` (with Leitner
  box) when the user nails it fast in the module-SRS review. The "main" pool
  is the dashboard's vocab review stack, intentionally segregated from the
  verb review deck in `tense_quest_cards`.
"""
import uuid

from sqlalchemy import (
    CheckConstraint,
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


class VocabChapterCompletion(Base):
    """A finished chapter of a vocab module — the user passed the 5-word
    press-and-speak gauntlet for chapter `chapter_index` of `module_id`.
    `module_id` is the FE vocabData.ts slug (e.g. 'common-phrases-1-25')."""

    __tablename__ = "vocab_chapter_completion"
    __table_args__ = (
        UniqueConstraint("user_id", "module_id", "chapter_index", name="uq_vocab_chapter"),
        Index("ix_vocab_chapter_user_mod", "user_id", "module_id"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    module_id = Column(String, nullable=False)
    chapter_index = Column(Integer, nullable=False)
    completed_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class VocabCard(Base):
    """A single vocab word in either the module-SRS deck (pre-promotion) or
    the user's main vocab review stack (post-promotion).

    `status='module'` cards sit in the module's own deck — the user reviews
    them after completing all chapters, and a fast+correct attempt promotes
    them to `status='main'` with `box=1`. `status='main'` cards live in the
    main vocab SRS pool, surfaced as the dashboard's Vocab review stack
    (segregated from the verb stack in `tense_quest_cards`).
    """

    __tablename__ = "vocab_card"
    __table_args__ = (
        UniqueConstraint("user_id", "module_id", "word_es", name="uq_vocab_card"),
        CheckConstraint("status IN ('module','main')", name="ck_vocab_card_status"),
        CheckConstraint("box >= 1 AND box <= 5", name="ck_vocab_card_box"),
        Index("ix_vocab_card_user_status", "user_id", "status"),
        Index("ix_vocab_card_user_due", "user_id", "due_at"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    module_id = Column(String, nullable=False)
    word_es = Column(String, nullable=False)
    word_en = Column(String, nullable=False)
    status = Column(String, nullable=False, server_default="module", default="module")
    box = Column(Integer, nullable=False, server_default="1", default=1)
    due_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    last_seen_at = Column(DateTime(timezone=True), nullable=True)
    last_response_ms = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
