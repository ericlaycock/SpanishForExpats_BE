"""Add subscriptions.beta_redeemed_at + grandfather existing rows.

Revision ID: 036_subscription_beta_redeemed_at
Revises: 035_cohort_seed_thu_may7
Create Date: 2026-05-08

Beta-code gate is enforced on the FE based on subscription.active OR
subscription.beta_redeemed_at IS NOT NULL. Existing users all came in via
the (now-removed) cohort flow and should bypass the new prompt — backfill
their subscriptions to NOW() so they're grandfathered.
"""
from alembic import op
import sqlalchemy as sa


revision = "036_subscription_beta_redeemed_at"
down_revision = "035_cohort_seed_thu_may7"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "subscriptions",
        sa.Column("beta_redeemed_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.execute(
        "UPDATE subscriptions SET beta_redeemed_at = NOW() WHERE beta_redeemed_at IS NULL"
    )


def downgrade() -> None:
    op.drop_column("subscriptions", "beta_redeemed_at")
