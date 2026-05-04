"""Track assistant turns that fail the turn-closing / no-leak rules.

Revision ID: 028_avatar_dead_end
Revises: 027_avatar_dynamics
Create Date: 2026-05-02

`avatar_dead_end_turns` counts assistant turns flagged by
`voice_turn_service.validate_assistant_reply` for either:

- producing the exact Spanish form of any pending chip (a "leak" — the
  v3 prompt forbids this because it removes the student's chance to
  earn the chip), or
- ending the turn without a question mark (a "dead end" — the v3
  prompt's TURN-CLOSING RULE requires every reply to hand the floor
  back).

Telemetry-only today: the FE doesn't read it yet, but capturing it
lets us measure how often the LLM ignores the v3 prompt rules and
spot regressions when we tune the prompt.
"""
from alembic import op
import sqlalchemy as sa


revision = "028_avatar_dead_end"
down_revision = "027_avatar_dynamics"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "conversations",
        sa.Column(
            "avatar_dead_end_turns",
            sa.Integer(),
            nullable=False,
            server_default="0",
        ),
    )


def downgrade() -> None:
    op.drop_column("conversations", "avatar_dead_end_turns")
