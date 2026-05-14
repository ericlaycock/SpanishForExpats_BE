"""Per-user grammar-category unlock state, plus grandfather backfill for
existing users.

Revision ID: 044_user_category_progress
Revises: 043_tq_diag_slow_sentence_coins
Create Date: 2026-05-14

Adds `user_category_progress(user_id, category)`. A row exists for every
(user, category) pair the user has either grandfathered into or completed a
diagnostic for. `unlocked_at` IS NULL means the row exists (a future
diagnostic could decide it) but the category is still locked; non-null means
unlocked.

Backfill: every existing user gets one row per category with
`unlocked_at = NOW()` so current learners see no lock overlays. New users
created after this migration get rows (lazily, in the BE endpoint) with
`unlocked_at = NULL` until their per-category diagnostic runs.

Revision ID kept short — alembic_version.version_num is varchar(32).
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


revision = "044_user_category_progress"
down_revision = "043_tq_diag_slow_sentence_coins"
branch_labels = None
depends_on = None


_CATEGORIES = ("present", "past", "future", "modals", "subjunctive")


def upgrade() -> None:
    op.create_table(
        "user_category_progress",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("category", sa.String(), nullable=False),
        sa.Column("diagnostic_result", sa.String(), nullable=True),  # 'ok' | 'needs_work' | NULL
        sa.Column("unlocked_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("diagnostic_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("user_id", "category", name="uq_user_category"),
        sa.CheckConstraint(
            "category IN ('present','past','future','modals','subjunctive')",
            name="ck_user_category_value",
        ),
        sa.CheckConstraint(
            "diagnostic_result IS NULL OR diagnostic_result IN ('ok','ok_slow','needs_work')",
            name="ck_user_category_diag_result",
        ),
    )
    op.create_index("ix_user_category_user", "user_category_progress", ["user_id"])

    # Grandfather all existing users: every (user, category) row exists with
    # `unlocked_at = NOW()` so current learners encounter zero lock overlays.
    # `gen_random_uuid()` requires the pgcrypto extension; if it isn't
    # available, switch this to using `uuid_generate_v4()` from uuid-ossp
    # (the rest of the schema uses default UUIDs at the application layer).
    values_clause = ", ".join(f"('{cat}')" for cat in _CATEGORIES)
    op.execute(
        f"""
        INSERT INTO user_category_progress (id, user_id, category, unlocked_at)
        SELECT gen_random_uuid(), u.id, cat.category, NOW()
        FROM users u
        CROSS JOIN (VALUES {values_clause}) AS cat(category)
        ON CONFLICT (user_id, category) DO NOTHING
        """
    )


def downgrade() -> None:
    op.drop_index("ix_user_category_user", table_name="user_category_progress")
    op.drop_table("user_category_progress")
