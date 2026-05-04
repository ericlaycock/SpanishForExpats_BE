"""Add freeflow milestone tracking columns and table

Revision ID: 019
Revises: 018
Create Date: 2026-04-22
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "019_freeflow_timestamps"
down_revision = "018_stripe_fields"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("onboarding_completed_at", sa.DateTime(timezone=True), nullable=True))
    op.add_column("conversations", sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True))

    op.create_table(
        "user_milestone_events",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("milestone_key", sa.String(), nullable=False),
        sa.Column("situation_id", sa.String(), nullable=True),
        sa.Column("conversation_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("occurred_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["conversation_id"], ["conversations.id"]),
        sa.ForeignKeyConstraint(["situation_id"], ["situations.id"]),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "milestone_key", "situation_id", name="uq_user_milestone_situation"),
    )
    op.create_index("ix_user_milestone_events_user_id", "user_milestone_events", ["user_id"])


def downgrade():
    op.drop_index("ix_user_milestone_events_user_id", table_name="user_milestone_events")
    op.drop_table("user_milestone_events")
    op.drop_column("conversations", "completed_at")
    op.drop_column("users", "onboarding_completed_at")
