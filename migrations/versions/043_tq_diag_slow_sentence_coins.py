"""Tense Quest: diagnostic 'ok_slow' tier + per-sentence coins.

Revision ID: 043_tq_diag_slow_sentence_coins
Revises: 042_tq_username
Create Date: 2026-05-12

1. Widen `tense_quest_diagnostic.result` to allow a third value, `ok_slow`
   ("all conjugations right but at least one was slow → needs work, bit slow").
2. New `tense_quest_sentence_completions`: one row per (user, drill, sentence)
   answered correctly in the in-drill sentence gauntlet — worth +1 coin each,
   idempotent. Feeds the coin total / leaderboard alongside drill completions
   and review-card coins.

Revision ID kept short — alembic_version.version_num is varchar(32).
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


revision = "043_tq_diag_slow_sentence_coins"
down_revision = "042_tq_username"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_constraint("ck_tq_diagnostic_result", "tense_quest_diagnostic", type_="check")
    op.create_check_constraint(
        "ck_tq_diagnostic_result",
        "tense_quest_diagnostic",
        "result IN ('ok','ok_slow','needs_work')",
    )

    op.create_table(
        "tense_quest_sentence_completions",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("drill_id", sa.String(), nullable=False),
        sa.Column("sentence_id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("user_id", "drill_id", "sentence_id", name="uq_tq_sentence_completion"),
    )
    op.create_index("ix_tq_sentence_completion_user", "tense_quest_sentence_completions", ["user_id"])


def downgrade() -> None:
    op.drop_index("ix_tq_sentence_completion_user", table_name="tense_quest_sentence_completions")
    op.drop_table("tense_quest_sentence_completions")

    op.drop_constraint("ck_tq_diagnostic_result", "tense_quest_diagnostic", type_="check")
    op.create_check_constraint(
        "ck_tq_diagnostic_result",
        "tense_quest_diagnostic",
        "result IN ('ok','needs_work')",
    )
