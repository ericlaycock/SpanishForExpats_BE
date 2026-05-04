"""Replace `daily_grenades` with the production-shape `grenades` table.

The 023 placeholder restored the orphaned schema from the reverted attempt
so QA's alembic_version could resolve. This migration drops that scratch
table and creates the real one used by app/services/grenade_service.py:
unique on (user_id, assigned_date), nullable question fields (LLM filled
on demand), and recall tracking via `used` + `answered_at`.

`user_words.last_seen_form` is left in place — both the old and new code
need it, and the column type (TEXT) is compatible with the SQLAlchemy
String mapping.

Revision ID: 024_restructure_grenades
Revises: 023_add_daily_grenades
Create Date: 2026-04-25
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


revision = "024_restructure_grenades"
down_revision = "023_add_daily_grenades"
branch_labels = None
depends_on = None


def upgrade():
    # Drop the scratch table from the reverted attempt. CASCADE in case any
    # FK was created against it; IF EXISTS so this is safe on fresh DBs that
    # walked through 023 cleanly (table will exist there too).
    op.execute("DROP TABLE IF EXISTS daily_grenades CASCADE")

    op.create_table(
        "grenades",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "user_id",
            UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        sa.Column("word_id", sa.String(), sa.ForeignKey("words.id"), nullable=False),
        sa.Column("target_form", sa.String(), nullable=False),
        sa.Column("pos", sa.String(), nullable=True),
        sa.Column("audience", sa.String(), nullable=True),
        sa.Column("question_es", sa.Text(), nullable=True),
        sa.Column("question_en", sa.Text(), nullable=True),
        sa.Column("assigned_date", sa.Date(), nullable=False, index=True),
        sa.Column("used", sa.Boolean(), nullable=True),
        sa.Column("answered_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.UniqueConstraint("user_id", "assigned_date", name="uq_grenades_user_date"),
    )


def downgrade():
    op.drop_table("grenades")
