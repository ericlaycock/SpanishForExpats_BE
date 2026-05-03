"""Drop orphaned rows for the deleted grammar_possessive_adj_plural lesson

Revision ID: 027_drop_poss_adj_plural
Revises: 026_sentence_hints
Create Date: 2026-05-02

The grammar_possessive_adj_plural lesson was merged into
grammar_possessive_adj (drill_sentences combined; word_workload extended).
The lesson's situation_id no longer exists in GRAMMAR_SITUATIONS, so any
DB row pointing at it is orphaned and would cause runtime errors if
loaded. This migration garbage-collects those rows from every table that
holds a situations.id FK.

Tables enumerated from app/models.py grep for `ForeignKey("situations.id")`:
  - user_situations          (PK on situation_id, so DELETE not nullify)
  - user_words               (source_situation_id, nullable — set NULL)
  - conversations            (situation_id, NOT NULL — delete row)
  - lesson_completions / similar tables that key on situation_id
"""
from alembic import op


revision = "027_drop_poss_adj_plural"
down_revision = "026_sentence_hints"
branch_labels = None
depends_on = None

DEAD_SID = "grammar_possessive_adj_plural"


def upgrade() -> None:
    # NOT NULL situation_id → delete row.
    op.execute(f"DELETE FROM conversations WHERE situation_id = '{DEAD_SID}'")
    op.execute(f"DELETE FROM daily_encounter_logs WHERE situation_id = '{DEAD_SID}'")
    # PK includes situation_id → delete row.
    op.execute(f"DELETE FROM situation_words WHERE situation_id = '{DEAD_SID}'")
    op.execute(f"DELETE FROM user_situations WHERE situation_id = '{DEAD_SID}'")
    # Nullable FKs → null out, keep the parent row.
    op.execute(f"UPDATE user_words SET source_situation_id = NULL WHERE source_situation_id = '{DEAD_SID}'")
    op.execute(f"UPDATE user_milestone_events SET situation_id = NULL WHERE situation_id = '{DEAD_SID}'")
    op.execute(f"UPDATE sentence_hints SET situation_id = NULL WHERE situation_id = '{DEAD_SID}'")


def downgrade() -> None:
    # Irreversible — the data is gone and the lesson dict is gone too.
    pass
