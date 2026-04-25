"""Subscription lifecycle fields + users.seen_explainers JSONB

Adds the columns needed to power the in-app cancel/resume flow and the
server-side first-time explainer flags. Both belong to the same migration
because they're shipped as one product change ("subscription management +
onboarding upgrade") and that keeps the alembic graph compact.

Revision ID: 025_subscription_lifecycle_and_explainers
Revises: 024_restructure_grenades
Create Date: 2026-04-25
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


revision = "025_subscription_lifecycle_and_explainers"
down_revision = "024_restructure_grenades"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "subscriptions",
        sa.Column("cancel_at_period_end", sa.Boolean(), nullable=False, server_default=sa.false()),
    )
    op.add_column(
        "subscriptions",
        sa.Column("current_period_end", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "subscriptions",
        sa.Column("canceled_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "subscriptions",
        sa.Column("cancel_reason", sa.Text(), nullable=True),
    )

    op.add_column(
        "users",
        sa.Column(
            "seen_explainers",
            JSONB(),
            nullable=False,
            server_default=sa.text("'{}'::jsonb"),
        ),
    )


def downgrade():
    op.drop_column("users", "seen_explainers")
    op.drop_column("subscriptions", "cancel_reason")
    op.drop_column("subscriptions", "canceled_at")
    op.drop_column("subscriptions", "current_period_end")
    op.drop_column("subscriptions", "cancel_at_period_end")
