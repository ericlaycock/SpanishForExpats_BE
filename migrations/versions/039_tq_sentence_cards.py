"""Tense Quest: review deck holds sentence cards, not conjugation cards.

Revision ID: 039_tq_sentence_cards
Revises: 038_tense_quest
Create Date: 2026-05-11

`tense_quest_cards` now keys on `(drill_id, sentence_id)` instead of
`(verb, pronoun)` — reviewing a card means producing that practice sentence,
not a bare conjugation. The drill's sentences are seeded into the deck on
completion. Existing rows are throwaway (the feature shipped hours ago, only
QA-test data), so the upgrade just clears the table before reshaping it.

Revision ID kept short — alembic_version.version_num is varchar(32).
"""
from alembic import op
import sqlalchemy as sa


revision = "039_tq_sentence_cards"
down_revision = "038_tense_quest"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("DELETE FROM tense_quest_cards")
    op.add_column("tense_quest_cards", sa.Column("drill_id", sa.String(), nullable=False))
    op.add_column("tense_quest_cards", sa.Column("sentence_id", sa.String(), nullable=False))
    op.drop_column("tense_quest_cards", "verb")
    op.drop_column("tense_quest_cards", "pronoun")


def downgrade() -> None:
    op.execute("DELETE FROM tense_quest_cards")
    op.add_column("tense_quest_cards", sa.Column("verb", sa.String(), nullable=False))
    op.add_column("tense_quest_cards", sa.Column("pronoun", sa.String(), nullable=False))
    op.drop_column("tense_quest_cards", "drill_id")
    op.drop_column("tense_quest_cards", "sentence_id")
