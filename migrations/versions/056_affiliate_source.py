"""Affiliate scoping: per-user funnel source.

Revision ID: 056_affiliate_source
Revises: 055_trial_reminder_source
Create Date: 2026-06-02

Adds users.affiliate_source — when set, the user is an external affiliate scoped
to exactly one funnel source (utm_source, e.g. "pan"). Powers the read-only
affiliate metrics portal (/v1/affiliate/metrics, FE /affiliate) without granting
admin. NULL for everyone who isn't an affiliate.
"""
from alembic import op
import sqlalchemy as sa


revision = "056_affiliate_source"
down_revision = "055_trial_reminder_source"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "users", sa.Column("affiliate_source", sa.String(64), nullable=True)
    )
    op.create_index(
        "ix_users_affiliate_source", "users", ["affiliate_source"]
    )


def downgrade() -> None:
    op.drop_index("ix_users_affiliate_source", table_name="users")
    op.drop_column("users", "affiliate_source")
