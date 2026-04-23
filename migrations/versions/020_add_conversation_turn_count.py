"""Add turn_count to conversations

Revision ID: 020_conversation_turn_count
Revises: 019_freeflow_timestamps
Create Date: 2026-04-22

Backs the hard-limit enforcement introduced alongside the realtime voice-chat
flow. The realtime path can't be implicitly bounded by per-turn REST calls
(the browser talks to OpenAI directly), so `persist_turn` increments this
counter on every ingested turn and `check_completion` fires
conversation_complete once it hits 30 — matching the FE's
EXCHANGE_HARD_LIMIT.
"""
from alembic import op
import sqlalchemy as sa


revision = "020_conversation_turn_count"
down_revision = "019_freeflow_timestamps"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "conversations",
        sa.Column(
            "turn_count",
            sa.Integer(),
            nullable=False,
            server_default="0",
        ),
    )


def downgrade() -> None:
    op.drop_column("conversations", "turn_count")
