"""Vocab recall coins on vocab_card.

Revision ID: 048_vocab_recall_coins
Revises: 047_vocab_progress
Create Date: 2026-05-21

A 5th coin source feeds the leaderboard: 1 coin per word recalled correctly
during the chapter's Recall phase. Implementation rides on the existing
`vocab_card` row: when a chapter is completed (the POST already seeds 5
module-status cards on first pass, ON CONFLICT DO NOTHING idempotency), each
newly seeded row writes `recall_coins_earned = 1`. Replays don't double-credit
because the row is no-op'd by the conflict clause.

`_user_points` (see app/api/v1/tense_quest.py) is updated in code to add
`SUM(vocab_card.recall_coins_earned)` to the lifetime-earned total.
"""
from alembic import op
import sqlalchemy as sa


revision = "048_vocab_recall_coins"
down_revision = "047_vocab_progress"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "vocab_card",
        sa.Column(
            "recall_coins_earned",
            sa.Integer(),
            nullable=False,
            server_default="0",
        ),
    )


def downgrade() -> None:
    op.drop_column("vocab_card", "recall_coins_earned")
