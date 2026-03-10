"""Add catalan column to words and catalan_mode to users

Revision ID: 011_catalan_mode
Revises: 010_rename_fields
Create Date: 2026-03-10 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '011_catalan_mode'
down_revision = '010_rename_fields'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('words', sa.Column('catalan', sa.String(), nullable=True))
    op.add_column('users', sa.Column('catalan_mode', sa.Boolean(), nullable=False, server_default='false'))


def downgrade() -> None:
    op.drop_column('users', 'catalan_mode')
    op.drop_column('words', 'catalan')
