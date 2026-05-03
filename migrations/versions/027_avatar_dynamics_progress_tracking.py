"""Track per-conversation stuck state and chip targets for grammar chats.

Revision ID: 027_avatar_dynamics
Revises: 026_sentence_hints
Create Date: 2026-05-02

Backs the avatar conversation dynamics overhaul:

- `consecutive_no_progress_turns` counts user turns since the last new
  target was detected. Used by `voice_turn_service.persist_turn` to
  drive the v3 system prompt's anti-stuck rule and the FE's nudge toast.

- `chat_target_forms_json` snapshots the FE's per-(verb, pronoun) chip
  list at conversation creation for grammar `*_chat` lessons. Reading
  it server-side lets `check_chat_chip_completion` gate completion on
  the same chips the FE shows, so vocab encounters stop \"completing\"
  before all chips tick green. NULL for vocab encounters and non-chat
  grammar — those keep the legacy infinitive-level completion path.

Both columns are populated lazily; existing rows default safely.
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


revision = "027_avatar_dynamics"
down_revision = "026_sentence_hints"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "conversations",
        sa.Column(
            "consecutive_no_progress_turns",
            sa.Integer(),
            nullable=False,
            server_default="0",
        ),
    )
    op.add_column(
        "conversations",
        sa.Column(
            "chat_target_forms_json",
            JSONB(),
            nullable=True,
        ),
    )
    op.add_column(
        "conversations",
        sa.Column(
            "completed_chip_ids",
            JSONB(),
            nullable=False,
            server_default=sa.text("'[]'::jsonb"),
        ),
    )


def downgrade() -> None:
    op.drop_column("conversations", "completed_chip_ids")
    op.drop_column("conversations", "chat_target_forms_json")
    op.drop_column("conversations", "consecutive_no_progress_turns")
