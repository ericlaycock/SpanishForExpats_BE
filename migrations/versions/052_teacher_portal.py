"""Teachers portal — is_teacher flag + roster + per-topic mastery overlay.

Revision ID: 052_teacher_portal
Revises: 051_vocab_box_cap_7
Create Date: 2026-05-28

Backs the teachers-only portal:
- `users.is_teacher` — boolean role flag (same shape as is_admin).
- `teacher_student` — a tutor's roster. Students are identified by email +
  display name; `student_user_id` links a real app account when one exists
  (nullable, so account-less paying customers can still be assigned).
- `teacher_student_topic_state` — the manual tri-state overlay, keyed to the
  roster row. One row per (roster, topic_type, topic_id); an absent row means
  'no_aprendido'. Fully decoupled from the student's real SRS data.
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


revision = "052_teacher_portal"
down_revision = "051_vocab_box_cap_7"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("is_teacher", sa.Boolean(), nullable=False, server_default="false"),
    )

    op.create_table(
        "teacher_student",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("teacher_id", UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("student_email", sa.String(), nullable=False),
        sa.Column("student_name", sa.String(), nullable=True),
        sa.Column("student_user_id", UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("teacher_id", "student_email", name="uq_teacher_student"),
    )
    op.create_index("ix_teacher_student_teacher", "teacher_student", ["teacher_id"])
    op.create_index("ix_teacher_student_user", "teacher_student", ["student_user_id"])

    op.create_table(
        "teacher_student_topic_state",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "teacher_student_id",
            UUID(as_uuid=True),
            sa.ForeignKey("teacher_student.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("topic_type", sa.String(), nullable=False),
        sa.Column("topic_id", sa.String(), nullable=False),
        sa.Column("state", sa.String(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint(
            "teacher_student_id", "topic_type", "topic_id", name="uq_teacher_topic_state"
        ),
        sa.CheckConstraint(
            "topic_type IN ('vocab_module','tense_group')", name="ck_teacher_topic_type"
        ),
        sa.CheckConstraint(
            "state IN ('no_aprendido','aprendiendo','aprendido')", name="ck_teacher_topic_state"
        ),
    )
    op.create_index(
        "ix_teacher_topic_state_roster", "teacher_student_topic_state", ["teacher_student_id"]
    )


def downgrade() -> None:
    op.drop_index("ix_teacher_topic_state_roster", table_name="teacher_student_topic_state")
    op.drop_table("teacher_student_topic_state")
    op.drop_index("ix_teacher_student_user", table_name="teacher_student")
    op.drop_index("ix_teacher_student_teacher", table_name="teacher_student")
    op.drop_table("teacher_student")
    op.drop_column("users", "is_teacher")
