"""Add hint_count to user_words

Revision ID: 013_hint_count
Revises: 012_add_srs
Create Date: 2026-03-24 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '013_hint_count'
down_revision = '012_add_srs'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('user_words', sa.Column('hint_count', sa.Integer(), nullable=False, server_default='0'))


def downgrade() -> None:
    op.drop_column('user_words', 'hint_count')
