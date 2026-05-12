"""Tense Quest game tables — drill completions (leaderboard points) + SRS deck.

Revision ID: 038_tense_quest
Revises: 037_booked_calls
Create Date: 2026-05-11

Backs the `/v1/tensequest/*` endpoints. `tense_quest_drill_completions`: one row
per (user, drill) finished — the row count is the user's leaderboard point
total. `tense_quest_cards`: the per-user spaced-repetition deck of conjugation
cards (one per group:verb:pronoun), with a Leitner box, a due time, and a
deck_position the Shuffle button randomises.

Revision ID kept short — alembic_version.version_num is varchar(32).
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


revision = "038_tense_quest"
down_revision = "037_booked_calls"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "tense_quest_drill_completions",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("drill_id", sa.String(), nullable=False),
        sa.Column("tense_group_id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("user_id", "drill_id", name="uq_tq_drill_completion"),
    )
    op.create_index("ix_tq_completions_user", "tense_quest_drill_completions", ["user_id"])

    op.create_table(
        "tense_quest_cards",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("card_key", sa.String(), nullable=False),
        sa.Column("tense_group_id", sa.String(), nullable=False),
        sa.Column("verb", sa.String(), nullable=False),
        sa.Column("pronoun", sa.String(), nullable=False),
        sa.Column("box", sa.Integer(), server_default="1", nullable=False),
        sa.Column("reps", sa.Integer(), server_default="0", nullable=False),
        sa.Column("lapses", sa.Integer(), server_default="0", nullable=False),
        sa.Column("deck_position", sa.Integer(), server_default="0", nullable=False),
        sa.Column("due_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("last_result", sa.String(), nullable=True),
        sa.Column("last_response_ms", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("user_id", "card_key", name="uq_tq_card"),
    )
    op.create_index("ix_tq_cards_user_due", "tense_quest_cards", ["user_id", "due_at"])
    op.create_index("ix_tq_cards_user_pos", "tense_quest_cards", ["user_id", "deck_position"])


def downgrade() -> None:
    op.drop_index("ix_tq_cards_user_pos", table_name="tense_quest_cards")
    op.drop_index("ix_tq_cards_user_due", table_name="tense_quest_cards")
    op.drop_table("tense_quest_cards")
    op.drop_index("ix_tq_completions_user", table_name="tense_quest_drill_completions")
    op.drop_table("tense_quest_drill_completions")
