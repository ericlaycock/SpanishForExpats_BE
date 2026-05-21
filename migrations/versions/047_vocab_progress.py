"""Vocab learning + SRS tables.

Revision ID: 047_vocab_progress
Revises: 046_dragon_and_avatars
Create Date: 2026-05-20

Two new tables back the chapter-by-chapter vocab learning flow + the
segregated vocab review stack:

- `vocab_chapter_completion` — one row per (user, module, chapter) the user
  has finished the 5-word press-and-speak gauntlet for. Idempotent.
- `vocab_card` — one row per learnable word. Starts at `status='module'`
  (lives in the module-only SRS deck the user reviews after completing all
  chapters); a fast+correct review promotes it to `status='main'`, box=1,
  putting it in the main vocab review pool surfaced on the dashboard. The
  main vocab pool is intentionally segregated from the verb review deck in
  `tense_quest_cards`.

Both tables key on (user_id, module_id, ...) so they cleanly partition by
the FE vocabData.ts slugs (e.g. 'common-phrases-1-25').
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


revision = "047_vocab_progress"
down_revision = "046_dragon_and_avatars"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "vocab_chapter_completion",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("module_id", sa.String(), nullable=False),
        sa.Column("chapter_index", sa.Integer(), nullable=False),
        sa.Column("completed_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("user_id", "module_id", "chapter_index", name="uq_vocab_chapter"),
    )
    op.create_index("ix_vocab_chapter_user_mod", "vocab_chapter_completion", ["user_id", "module_id"])

    op.create_table(
        "vocab_card",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("module_id", sa.String(), nullable=False),
        sa.Column("word_es", sa.String(), nullable=False),
        sa.Column("word_en", sa.String(), nullable=False),
        sa.Column("status", sa.String(), nullable=False, server_default="module"),
        sa.Column("box", sa.Integer(), nullable=False, server_default="1"),
        sa.Column("due_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("last_seen_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("last_response_ms", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("user_id", "module_id", "word_es", name="uq_vocab_card"),
        sa.CheckConstraint("status IN ('module','main')", name="ck_vocab_card_status"),
        sa.CheckConstraint("box >= 1 AND box <= 5", name="ck_vocab_card_box"),
    )
    op.create_index("ix_vocab_card_user_status", "vocab_card", ["user_id", "status"])
    op.create_index("ix_vocab_card_user_due", "vocab_card", ["user_id", "due_at"])


def downgrade() -> None:
    op.drop_index("ix_vocab_card_user_due", table_name="vocab_card")
    op.drop_index("ix_vocab_card_user_status", table_name="vocab_card")
    op.drop_table("vocab_card")
    op.drop_index("ix_vocab_chapter_user_mod", table_name="vocab_chapter_completion")
    op.drop_table("vocab_chapter_completion")
