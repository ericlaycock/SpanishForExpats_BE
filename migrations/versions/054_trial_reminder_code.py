"""Free-trial reminder short link code.

Revision ID: 054_trial_reminder_code
Revises: 053_freetrial_followup
Create Date: 2026-05-31

A short, unique URL-safe code per reminder so the SMS can use a tiny link
(/r/<code>) instead of a long JWT in the query string.
"""
from alembic import op
import sqlalchemy as sa


revision = "054_trial_reminder_code"
down_revision = "053_freetrial_followup"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("trial_reminders", sa.Column("code", sa.String(16), nullable=True))
    op.create_index(
        "uq_trial_reminders_code", "trial_reminders", ["code"], unique=True
    )


def downgrade() -> None:
    op.drop_index("uq_trial_reminders_code", table_name="trial_reminders")
    op.drop_column("trial_reminders", "code")
