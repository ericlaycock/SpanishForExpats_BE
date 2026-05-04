"""Add per-conversation realtime steering state.

Revision ID: 031_realtime_steering
Revises: 030_add_anonymous_funnel_events
Create Date: 2026-05-04

Used by the new realtime steering flow (Option C): after each user turn
the BE picks the next chip to elicit, sticks with it for up to 2 turns,
and injects a meta-thought assistant message before the model's reply.

`steering_target_id` is the chip the model is currently trying to elicit
(matches `chat_target_forms_json[].id` for grammar chats, or the
`Word.id` for vocab encounters). NULL means "no active steer" — first
turn or the user just landed the previous target.

`steering_target_age` is the user-turn count we've held this target.
Resets to 0 (with id → NULL) on landing; otherwise increments per
/realtime-turn call until it hits 2, then a fresh target is rolled.
"""
from alembic import op
import sqlalchemy as sa


revision = "031_realtime_steering"
down_revision = "030_add_anonymous_funnel_events"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "conversations",
        sa.Column("steering_target_id", sa.Text(), nullable=True),
    )
    op.add_column(
        "conversations",
        sa.Column(
            "steering_target_age",
            sa.Integer(),
            nullable=False,
            server_default="0",
        ),
    )


def downgrade() -> None:
    op.drop_column("conversations", "steering_target_age")
    op.drop_column("conversations", "steering_target_id")
