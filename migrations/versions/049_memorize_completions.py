"""Memorize completions table.

Revision ID: 049_memorize_completions
Revises: 048_vocab_recall_coins
Create Date: 2026-05-23

Backs the Memorize utility's "Finished" → "Yes, absolutely" → +1 sun flow.
One row per user-confirmed memorisation. `coins_earned` is fixed at 1 today
but kept as a column in case the reward shape evolves. `english_phrase`
is nullable so we can still log a completion even if the user didn't fill
the English field (UX shouldn't block on it).
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


revision = "049_memorize_completions"
down_revision = "048_vocab_recall_coins"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "memorize_completions",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("spanish_phrase", sa.String(length=500), nullable=False),
        sa.Column("english_phrase", sa.String(length=500), nullable=True),
        sa.Column("coins_earned", sa.Integer(), nullable=False, server_default="1"),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.CheckConstraint("coins_earned > 0", name="ck_memorize_coins_positive"),
    )
    op.create_index(
        "ix_memorize_completions_user_id",
        "memorize_completions",
        ["user_id"],
    )


def downgrade() -> None:
    op.drop_index("ix_memorize_completions_user_id", table_name="memorize_completions")
    op.drop_table("memorize_completions")
