"""Tense Quest: per-user public quester name.

Revision ID: 042_tq_username
Revises: 041_tq_diagnostic
Create Date: 2026-05-12

`users.tq_username` is the name shown publicly on the Tense Quest leaderboard
(so we never expose the email or the real onboarding name there). Nullable —
the FE forces players to pick one before they see the map. Unique
case-insensitively via a functional index; NULLs are ignored by the index so
un-set users don't collide.

Revision ID kept short — alembic_version.version_num is varchar(32).
"""
from alembic import op
import sqlalchemy as sa


revision = "042_tq_username"
down_revision = "041_tq_diagnostic"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("tq_username", sa.String(length=20), nullable=True))
    op.create_index(
        "uq_users_tq_username_lower",
        "users",
        [sa.text("lower(tq_username)")],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("uq_users_tq_username_lower", table_name="users")
    op.drop_column("users", "tq_username")
