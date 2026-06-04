"""User onboarding source: which affiliate referred a user.

Revision ID: 057_user_onboarding_source
Revises: 056_affiliate_source
Create Date: 2026-06-04

Adds users.onboarding_source — the affiliate source (utm_source) a user was
REFERRED BY, resolved at registration from their funnel session (with trial /
booking fallbacks). Distinct from affiliate_source ("this user IS an affiliate").
Powers $100-per-paying-student affiliate payouts. NULL for organic users.
"""
from alembic import op
import sqlalchemy as sa


revision = "057_user_onboarding_source"
down_revision = "056_affiliate_source"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "users", sa.Column("onboarding_source", sa.String(64), nullable=True)
    )
    op.create_index(
        "ix_users_onboarding_source", "users", ["onboarding_source"]
    )


def downgrade() -> None:
    op.drop_index("ix_users_onboarding_source", table_name="users")
    op.drop_column("users", "onboarding_source")
