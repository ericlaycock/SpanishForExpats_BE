"""Add conversation_id to llm/stt/tts request tables.

Revision ID: 032_ai_requests_conversation_id
Revises: 031_realtime_steering
Create Date: 2026-05-05

Adds a nullable, indexed `conversation_id` (UUID, FK → conversations.id
with ON DELETE SET NULL) to llm_requests, stt_requests, tts_requests.

Why nullable: not every AI request runs inside a conversation —
`/check-pronunciation` STT, the standalone `/v1/tts` endpoint, and
grenade LLM calls all happen outside any conversation. Pre-existing
rows also have no association.

Why ON DELETE SET NULL: audit rows should survive even if the
originating conversation is deleted (rare, but possible if a user
purges their account). Setting the FK to NULL preserves the row for
analytics while marking that the linkage is gone.

Why indexed: the primary use is "give me every AI request for this
conversation," which without an index is a full-table scan filtered by
JSONB user_id matching — slow at any meaningful row count.
"""
from alembic import op
import sqlalchemy as sa


revision = "032_ai_requests_conversation_id"
down_revision = "031_realtime_steering"
branch_labels = None
depends_on = None


_TABLES = ("llm_requests", "stt_requests", "tts_requests")


def upgrade() -> None:
    for table in _TABLES:
        op.add_column(
            table,
            sa.Column(
                "conversation_id",
                sa.dialects.postgresql.UUID(as_uuid=True),
                sa.ForeignKey("conversations.id", ondelete="SET NULL"),
                nullable=True,
            ),
        )
        op.create_index(
            f"ix_{table}_conversation_id",
            table,
            ["conversation_id"],
        )


def downgrade() -> None:
    for table in _TABLES:
        op.drop_index(f"ix_{table}_conversation_id", table_name=table)
        op.drop_column(table, "conversation_id")
