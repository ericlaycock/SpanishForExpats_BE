"""Add Stripe fields to subscriptions table

Revision ID: 018
Revises: 017
Create Date: 2026-04-22
"""
from alembic import op
import sqlalchemy as sa

revision = "018_stripe_fields"
down_revision = "017_pron_daily_usage"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("subscriptions", sa.Column("stripe_customer_id", sa.String(), nullable=True))
    op.add_column("subscriptions", sa.Column("stripe_subscription_id", sa.String(), nullable=True))
    op.add_column("subscriptions", sa.Column("plan", sa.String(), nullable=True))
    op.add_column("subscriptions", sa.Column("billing_cycle", sa.String(), nullable=True))
    op.create_index("ix_subscriptions_stripe_customer_id", "subscriptions", ["stripe_customer_id"])
    op.create_index("ix_subscriptions_stripe_subscription_id", "subscriptions", ["stripe_subscription_id"])


def downgrade():
    op.drop_index("ix_subscriptions_stripe_subscription_id", table_name="subscriptions")
    op.drop_index("ix_subscriptions_stripe_customer_id", table_name="subscriptions")
    op.drop_column("subscriptions", "billing_cycle")
    op.drop_column("subscriptions", "plan")
    op.drop_column("subscriptions", "stripe_subscription_id")
    op.drop_column("subscriptions", "stripe_customer_id")
