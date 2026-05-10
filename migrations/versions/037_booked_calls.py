"""Add booked_calls table — Calendly invitee bookings for the founder call.

Revision ID: 037_booked_calls
Revises: 036_beta_redeemed_at
Create Date: 2026-05-10

Backs the `POST /v1/calendly/webhook` receiver. One row per invitee UUID
(Calendly's idempotency key). `user_id` is nullable because the booking
arrives before account creation and is backfilled at register time.
Reschedules clear `canceled_at` on the existing row.

Revision ID kept short — Alembic's alembic_version.version_num is
varchar(32), so longer slugs fail the post-upgrade UPDATE.
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


revision = "037_booked_calls"
down_revision = "036_beta_redeemed_at"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "booked_calls",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("invitee_uuid", sa.String(64), nullable=False),
        sa.Column("invitee_email", sa.String(), nullable=False),
        sa.Column("calendly_event_uri", sa.String(), nullable=True),
        sa.Column("scheduled_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("invitee_timezone", sa.String(), nullable=True),
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=True),
        sa.Column("funnel_session_id", sa.String(64), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column("canceled_at", sa.DateTime(timezone=True), nullable=True),
        sa.UniqueConstraint("invitee_uuid", name="uq_booked_calls_invitee_uuid"),
    )
    op.create_index("ix_booked_calls_invitee_email", "booked_calls", ["invitee_email"])
    op.create_index("ix_booked_calls_user_id", "booked_calls", ["user_id"])
    op.create_index("ix_booked_calls_funnel_session_id", "booked_calls", ["funnel_session_id"])
    op.create_index("ix_booked_calls_invitee_uuid", "booked_calls", ["invitee_uuid"])


def downgrade() -> None:
    op.drop_index("ix_booked_calls_invitee_uuid", table_name="booked_calls")
    op.drop_index("ix_booked_calls_funnel_session_id", table_name="booked_calls")
    op.drop_index("ix_booked_calls_user_id", table_name="booked_calls")
    op.drop_index("ix_booked_calls_invitee_email", table_name="booked_calls")
    op.drop_table("booked_calls")
