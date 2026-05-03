"""Merge avatar dead-end and grammar consolidation chains.

Revision ID: 029_merge_028s
Revises: 028_avatar_dead_end, 028_drop_merged_lessons
Create Date: 2026-05-02

Two parallel branches forked from `026_sentence_hints`:

- avatar dynamics chain: `027_avatar_dynamics` → `028_avatar_dead_end`
- grammar consolidation chain: `027_drop_poss_adj_plural` → `028_drop_merged_lessons`

Both landed on the `qa` branch around the same time, leaving alembic
with two heads and `alembic upgrade head` failing with "Multiple
head revisions are present". This migration has no schema changes —
it only joins the two chains so alembic has a single head again.
"""
from alembic import op  # noqa: F401  (kept for parity with sibling migrations)
import sqlalchemy as sa  # noqa: F401


revision = "029_merge_028s"
down_revision = ("028_avatar_dead_end", "028_drop_merged_lessons")
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
