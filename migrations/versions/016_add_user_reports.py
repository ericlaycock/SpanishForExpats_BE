"""Add user_reports table

Revision ID: 016_user_reports
Revises: 015_swedish_alt_language
Create Date: 2026-04-20 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB

# revision identifiers, used by Alembic.
revision = '016_user_reports'
down_revision = '015_swedish_alt_language'
branch_labels = None
depends_on = None


CATEGORY_VALUES = (
    'platform', 'translation', 'pronunciation',
    'voice_chat', 'subscription', 'suggestion', 'other',
)
STATUS_VALUES = ('new', 'investigating', 'resolved', 'dismissed')


def upgrade() -> None:
    op.create_table(
        'user_reports',
        sa.Column('id', UUID(as_uuid=True), nullable=False),
        sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='SET NULL'), nullable=True),
        sa.Column('category', sa.String(length=32), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('context', JSONB(), server_default=sa.text("'{}'::jsonb"), nullable=False),
        sa.Column('status', sa.String(length=16), server_default=sa.text("'new'"), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('resolved_at', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.CheckConstraint(
            "category IN ('" + "','".join(CATEGORY_VALUES) + "')",
            name='ck_user_reports_category',
        ),
        sa.CheckConstraint(
            "status IN ('" + "','".join(STATUS_VALUES) + "')",
            name='ck_user_reports_status',
        ),
    )
    op.create_index('ix_user_reports_user_id', 'user_reports', ['user_id'])
    op.create_index('ix_user_reports_status', 'user_reports', ['status'])
    op.create_index(
        'ix_user_reports_created_at',
        'user_reports',
        [sa.text('created_at DESC')],
    )


def downgrade() -> None:
    op.drop_index('ix_user_reports_created_at', table_name='user_reports')
    op.drop_index('ix_user_reports_status', table_name='user_reports')
    op.drop_index('ix_user_reports_user_id', table_name='user_reports')
    op.drop_table('user_reports')
