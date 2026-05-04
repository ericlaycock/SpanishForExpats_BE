"""Add onboarding V2 user profile fields

Revision ID: 021
Revises: 020
Create Date: 2026-04-23
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "021_onboarding_v2_fields"
down_revision = "020_conversation_turn_count"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("name", sa.String(), nullable=True))
    op.add_column("users", sa.Column("q0_spanish_level", sa.String(), nullable=True))
    op.add_column("users", sa.Column("q1_situation", sa.String(), nullable=True))
    op.add_column("users", sa.Column("q1_1_time_in_latam", sa.String(), nullable=True))
    op.add_column("users", sa.Column("q2_country", sa.String(), nullable=True))
    op.add_column("users", sa.Column("q3_tools", postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    op.add_column("users", sa.Column("q4_proximity", sa.String(), nullable=True))
    op.add_column("users", sa.Column("q6_conversations", sa.String(), nullable=True))


def downgrade():
    op.drop_column("users", "q6_conversations")
    op.drop_column("users", "q4_proximity")
    op.drop_column("users", "q3_tools")
    op.drop_column("users", "q2_country")
    op.drop_column("users", "q1_1_time_in_latam")
    op.drop_column("users", "q1_situation")
    op.drop_column("users", "q0_spanish_level")
    op.drop_column("users", "name")
