"""Tense Quest: review attempts earn coins.

Revision ID: 040_tq_review_coins
Revises: 039_tq_sentence_cards
Create Date: 2026-05-11

A review card now accumulates `coins_earned` (2 per fast correct review, 1 per
medium one, 0 for slow/wrong). The user's coin total = drill completions + the
sum of this column across their deck.

Revision ID kept short — alembic_version.version_num is varchar(32).
"""
from alembic import op
import sqlalchemy as sa


revision = "040_tq_review_coins"
down_revision = "039_tq_sentence_cards"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "tense_quest_cards",
        sa.Column("coins_earned", sa.Integer(), server_default="0", nullable=False),
    )


def downgrade() -> None:
    op.drop_column("tense_quest_cards", "coins_earned")
