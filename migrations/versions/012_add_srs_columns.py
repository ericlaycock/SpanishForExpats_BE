"""Add SRS columns: mastery_level, next_refresh_at, source_situation_id, conversation_type

Revision ID: 012_add_srs
Revises: 011_catalan_mode
Create Date: 2026-03-11 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '012_add_srs'
down_revision = '011_catalan_mode'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # UserWord columns
    op.add_column('user_words', sa.Column('mastery_level', sa.Integer(), nullable=False, server_default='0'))
    op.add_column('user_words', sa.Column('next_refresh_at', sa.DateTime(timezone=True), nullable=True))
    op.add_column('user_words', sa.Column('source_situation_id', sa.String(), sa.ForeignKey('situations.id'), nullable=True))

    # Conversation column
    op.add_column('conversations', sa.Column('conversation_type', sa.String(), nullable=False, server_default='lesson'))

    # Backfill mastery_level from existing status
    op.execute("UPDATE user_words SET mastery_level = 1 WHERE status = 'learning'")
    op.execute("UPDATE user_words SET mastery_level = 4 WHERE status = 'mastered'")


def downgrade() -> None:
    op.drop_column('conversations', 'conversation_type')
    op.drop_column('user_words', 'source_situation_id')
    op.drop_column('user_words', 'next_refresh_at')
    op.drop_column('user_words', 'mastery_level')
