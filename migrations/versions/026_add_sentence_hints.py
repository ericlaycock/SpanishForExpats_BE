"""Add sentence_hints table and sentence_hints_used counter

Revision ID: 026_sentence_hints
Revises: 025_sub_lifecycle_explainers
Create Date: 2026-04-29

Backs the "Need help?" feature in /voice-chat. The conversation gets a
counter (`sentence_hints_used`) to enforce the per-encounter cap, and
every generated hint is persisted to `sentence_hints` for analytics —
text, English gloss, the items the model claimed to use, and pointers
back to the LLM/TTS rows so we can replay or investigate later.
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB


revision = "026_sentence_hints"
down_revision = "025_sub_lifecycle_explainers"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "conversations",
        sa.Column(
            "sentence_hints_used",
            sa.Integer(),
            nullable=False,
            server_default="0",
        ),
    )

    op.create_table(
        "sentence_hints",
        sa.Column("id", UUID(as_uuid=True), nullable=False),
        sa.Column(
            "conversation_id",
            UUID(as_uuid=True),
            sa.ForeignKey("conversations.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "user_id",
            UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column(
            "situation_id",
            sa.String(),
            sa.ForeignKey("situations.id"),
            nullable=True,
        ),
        sa.Column("spanish", sa.Text(), nullable=False),
        sa.Column("english_gloss", sa.Text(), nullable=False),
        sa.Column("audio_url", sa.Text(), nullable=True),
        sa.Column(
            "used_item_ids",
            JSONB(),
            server_default=sa.text("'[]'::jsonb"),
            nullable=False,
        ),
        sa.Column("pending_count", sa.Integer(), nullable=True),
        sa.Column(
            "llm_request_id",
            UUID(as_uuid=True),
            sa.ForeignKey("llm_requests.id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column(
            "tts_request_id",
            UUID(as_uuid=True),
            sa.ForeignKey("tts_requests.id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "ix_sentence_hints_conversation_id",
        "sentence_hints",
        ["conversation_id"],
    )
    op.create_index(
        "ix_sentence_hints_user_id",
        "sentence_hints",
        ["user_id"],
    )
    op.create_index(
        "ix_sentence_hints_created_at",
        "sentence_hints",
        [sa.text("created_at DESC")],
    )


def downgrade() -> None:
    op.drop_index("ix_sentence_hints_created_at", table_name="sentence_hints")
    op.drop_index("ix_sentence_hints_user_id", table_name="sentence_hints")
    op.drop_index(
        "ix_sentence_hints_conversation_id", table_name="sentence_hints"
    )
    op.drop_table("sentence_hints")
    op.drop_column("conversations", "sentence_hints_used")
