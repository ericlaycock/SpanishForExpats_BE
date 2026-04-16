"""Add swedish column to words, replace catalan_mode with alt_language on users

Revision ID: 015_swedish_alt_language
Revises: 014_add_daily_encounter_logs
Create Date: 2026-04-10 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '015_swedish_alt_language'
down_revision = '014_daily_enc_log'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add swedish column to words
    op.add_column('words', sa.Column('swedish', sa.String(), nullable=True))

    # Add alt_language column to users
    op.add_column('users', sa.Column('alt_language', sa.String(), nullable=True))

    # Migrate existing catalan_mode data
    op.execute("UPDATE users SET alt_language = 'catalan' WHERE catalan_mode = true")

    # Drop old catalan_mode column
    op.drop_column('users', 'catalan_mode')


def downgrade() -> None:
    # Re-add catalan_mode column
    op.add_column('users', sa.Column('catalan_mode', sa.Boolean(), nullable=False, server_default='false'))

    # Migrate data back
    op.execute("UPDATE users SET catalan_mode = true WHERE alt_language = 'catalan'")

    # Drop new columns
    op.drop_column('users', 'alt_language')
    op.drop_column('words', 'swedish')
