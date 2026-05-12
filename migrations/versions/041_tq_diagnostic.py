"""Tense Quest: placement-diagnostic results per tense group.

Revision ID: 041_tq_diagnostic
Revises: 040_tq_review_coins
Create Date: 2026-05-11

One row per (user, tense_group): `result` is 'ok' (got all 3 sampled warmup
conjugations right) or 'needs_work'. Re-taking the diagnostic overwrites it.

Revision ID kept short — alembic_version.version_num is varchar(32).
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


revision = "041_tq_diagnostic"
down_revision = "040_tq_review_coins"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "tense_quest_diagnostic",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("tense_group_id", sa.String(), nullable=False),
        sa.Column("result", sa.String(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("user_id", "tense_group_id", name="uq_tq_diagnostic"),
        sa.CheckConstraint("result IN ('ok','needs_work')", name="ck_tq_diagnostic_result"),
    )
    op.create_index("ix_tq_diagnostic_user", "tense_quest_diagnostic", ["user_id"])


def downgrade() -> None:
    op.drop_index("ix_tq_diagnostic_user", table_name="tense_quest_diagnostic")
    op.drop_table("tense_quest_diagnostic")
