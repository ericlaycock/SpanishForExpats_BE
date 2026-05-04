"""Add anonymous_funnel_events table for pre-signup funnel tracking.

Revision ID: 030_add_anonymous_funnel_events
Revises: 029_merge_028s
Create Date: 2026-05-04

Captures the anonymous wizard funnel from landing-page visit through to
signup. One row per (session_id, event_key) — the unique constraint is
the idempotency mechanism so re-firing the same step is a no-op.

Post-signup tracking lives in `user_milestone_events` (see admin freeflow);
this table is the pre-identity counterpart.
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB


revision = "030_add_anonymous_funnel_events"
down_revision = "029_merge_028s"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "anonymous_funnel_events",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("session_id", sa.String(64), nullable=False),
        sa.Column("event_key", sa.String(64), nullable=False),
        sa.Column(
            "occurred_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "event_metadata",
            JSONB(),
            server_default=sa.text("'{}'::jsonb"),
            nullable=False,
        ),
        sa.UniqueConstraint(
            "session_id", "event_key", name="uq_funnel_session_event"
        ),
    )
    op.create_index(
        "ix_funnel_event_key", "anonymous_funnel_events", ["event_key"]
    )
    op.create_index(
        "ix_funnel_session_id", "anonymous_funnel_events", ["session_id"]
    )


def downgrade() -> None:
    op.drop_index("ix_funnel_session_id", table_name="anonymous_funnel_events")
    op.drop_index("ix_funnel_event_key", table_name="anonymous_funnel_events")
    op.drop_table("anonymous_funnel_events")
