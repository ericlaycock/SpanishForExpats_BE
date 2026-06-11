"""Affiliate payouts ledger.

Revision ID: 058_affiliate_payouts
Revises: 057_user_onboarding_source
Create Date: 2026-06-04

One row per referred paying student: a pending $100 payout created by the Stripe
webhook at first payment, marked paid by an admin once the partner is paid. The
unique constraint on user_id enforces one payout per student and makes the
webhook insert idempotent across event re-fires.
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "058_affiliate_payouts"
down_revision = "057_user_onboarding_source"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "affiliate_payouts",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("affiliate_source", sa.String(64), nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True),
                  sa.ForeignKey("users.id"), nullable=False),
        sa.Column("subscription_id", sa.String(), nullable=True),
        sa.Column("amount_cents", sa.Integer(), nullable=False, server_default="10000"),
        sa.Column("currency", sa.String(8), nullable=False, server_default="usd"),
        sa.Column("status", sa.String(16), nullable=False, server_default="pending"),
        sa.Column("created_at", sa.DateTime(timezone=True),
                  server_default=sa.func.now(), nullable=False),
        sa.Column("paid_at", sa.DateTime(timezone=True), nullable=True),
        sa.UniqueConstraint("user_id", name="uq_affiliate_payout_user"),
    )
    op.create_index("ix_affiliate_payouts_affiliate_source",
                    "affiliate_payouts", ["affiliate_source"])
    op.create_index("ix_affiliate_payouts_user_id", "affiliate_payouts", ["user_id"])
    op.create_index("ix_affiliate_payouts_status", "affiliate_payouts", ["status"])


def downgrade() -> None:
    op.drop_index("ix_affiliate_payouts_status", table_name="affiliate_payouts")
    op.drop_index("ix_affiliate_payouts_user_id", table_name="affiliate_payouts")
    op.drop_index("ix_affiliate_payouts_affiliate_source", table_name="affiliate_payouts")
    op.drop_table("affiliate_payouts")
