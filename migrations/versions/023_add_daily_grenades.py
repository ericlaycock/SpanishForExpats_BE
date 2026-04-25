"""Add daily_grenades table + last_seen_form on user_words

Revision ID: 023
Revises: 022
Create Date: 2026-04-25
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

revision = "023_add_daily_grenades"
down_revision = "022_add_word_type"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "user_words",
        sa.Column("last_seen_form", sa.Text(), nullable=True),
    )

    op.create_table(
        "daily_grenades",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=False, index=True),
        sa.Column("grenade_date", sa.Date(), nullable=False),
        sa.Column("user_word_id", sa.String(), nullable=False),
        sa.Column("word_id", sa.String(), sa.ForeignKey("words.id"), nullable=False),
        sa.Column("surface_form", sa.Text(), nullable=False),
        sa.Column("audience", sa.String(16), nullable=False),
        sa.Column("sentence_es", sa.Text(), nullable=True),
        sa.Column("sentence_en", sa.Text(), nullable=True),
        sa.Column("generated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("used", sa.Boolean(), nullable=True),
        sa.Column("answered_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("user_id", "grenade_date", name="uq_daily_grenades_user_date"),
        sa.CheckConstraint("audience IN ('friend', 'merchant')", name="ck_daily_grenades_audience"),
    )
    op.create_index("ix_daily_grenades_user_date", "daily_grenades", ["user_id", "grenade_date"])


def downgrade():
    op.drop_index("ix_daily_grenades_user_date", table_name="daily_grenades")
    op.drop_table("daily_grenades")
    op.drop_column("user_words", "last_seen_form")
