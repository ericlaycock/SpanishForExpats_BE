"""Add grenades table and user_words.last_seen_form column

Revision ID: 023_add_grenades
Revises: 022_add_word_type
Create Date: 2026-04-25
"""
from alembic import op
import sqlalchemy as sa


revision = "023_add_grenades"
down_revision = "022_add_word_type"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "user_words",
        sa.Column("last_seen_form", sa.String(), nullable=True),
    )

    op.create_table(
        "grenades",
        sa.Column("id", sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "user_id",
            sa.dialects.postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        sa.Column(
            "word_id",
            sa.String(),
            sa.ForeignKey("words.id"),
            nullable=False,
        ),
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
    op.drop_column("user_words", "last_seen_form")
