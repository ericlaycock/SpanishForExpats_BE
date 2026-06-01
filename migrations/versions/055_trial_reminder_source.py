"""Free-trial reminder: funnel session + campaign source.

Revision ID: 055_trial_reminder_source
Revises: 054_trial_reminder_code
Create Date: 2026-05-31

Links a phone signup back to the anonymous funnel session it came from and the
campaign source (utm_source) resolved from that session — so admin can map a
real signed-up user to the link they started on (e.g. /freetrial/pan → "pan").
"""
from alembic import op
import sqlalchemy as sa


revision = "055_trial_reminder_source"
down_revision = "054_trial_reminder_code"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "trial_reminders", sa.Column("funnel_session_id", sa.String(64), nullable=True)
    )
    op.add_column(
        "trial_reminders", sa.Column("source", sa.String(64), nullable=True)
    )
    op.create_index(
        "ix_trial_reminders_funnel_session_id",
        "trial_reminders",
        ["funnel_session_id"],
    )
    op.create_index(
        "ix_trial_reminders_source", "trial_reminders", ["source"]
    )


def downgrade() -> None:
    op.drop_index("ix_trial_reminders_source", table_name="trial_reminders")
    op.drop_index("ix_trial_reminders_funnel_session_id", table_name="trial_reminders")
    op.drop_column("trial_reminders", "source")
    op.drop_column("trial_reminders", "funnel_session_id")
