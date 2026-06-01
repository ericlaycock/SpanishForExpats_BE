"""Free-trial follow-up: users.phone_number + trial_reminders table.

Revision ID: 053_freetrial_followup
Revises: 052_teacher_portal
Create Date: 2026-05-30

Passwordless phone signup at the end of the free-trial memorize flow stores a
phone number on the user (nullable + unique; NULLs don't collide) and a
trial_reminders row scheduling the next-day "do you remember this word?" SMS.

Revision ID kept short — alembic_version.version_num is varchar(32).
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


revision = "053_freetrial_followup"
down_revision = "052_teacher_portal"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone_number", sa.String(), nullable=True))
    op.create_index(
        "uq_users_phone_number", "users", ["phone_number"], unique=True
    )

    op.create_table(
        "trial_reminders",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "user_id",
            UUID(as_uuid=True),
            sa.ForeignKey("users.id"),
            nullable=False,
            index=True,
        ),
        sa.Column("phone_number", sa.String(), nullable=False),
        sa.Column("word_es", sa.String(500), nullable=False),
        sa.Column("word_en", sa.String(500), nullable=False),
        sa.Column("channel", sa.String(16), nullable=False, server_default="sms"),
        sa.Column("scheduled_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("sent_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )
    op.create_index(
        "ix_trial_reminders_scheduled_at", "trial_reminders", ["scheduled_at"]
    )


def downgrade() -> None:
    op.drop_index("ix_trial_reminders_scheduled_at", table_name="trial_reminders")
    op.drop_table("trial_reminders")
    op.drop_index("uq_users_phone_number", table_name="users")
    op.drop_column("users", "phone_number")
