"""Add pron_daily_usage table for pronunciation trainer

Revision ID: 017
Revises: 016
Create Date: 2026-04-20
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

revision = "017"
down_revision = "016"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "pron_daily_usage",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=False, index=True),
        sa.Column("date", sa.Date, nullable=False, server_default=sa.text("CURRENT_DATE")),
        sa.Column("seconds_used", sa.Integer, nullable=False, server_default="0"),
        sa.UniqueConstraint("user_id", "date", name="uq_pron_user_date"),
    )


def downgrade():
    op.drop_table("pron_daily_usage")
