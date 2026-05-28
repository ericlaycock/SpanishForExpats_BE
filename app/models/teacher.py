"""Teachers-portal persistence — a tutor's student roster and the manual,
per-topic mastery overlay the tutor maintains.

This is intentionally decoupled from every student-facing table: the toggle
state lives only here and never reads or writes the student's real SRS/mastery
data. Two tables:

- `teacher_student` — one row per (teacher, assigned student). The student is
  identified by email + display name and links to a `users` row via
  `student_user_id` *when one exists* (nullable), so a tutor can be assigned a
  paying customer who has not yet created an app account.

- `teacher_student_topic_state` — the tri-state overlay, keyed to the roster
  row (not the student user, so it works for account-less students). One row per
  (roster, topic). `topic_type` is 'vocab_module' (id = FE vocabData.ts slug,
  e.g. 'freq-500-514') or 'tense_group' (id = app/data/tense_quest.py group id,
  e.g. 'subjunctive_imperfect'). An ABSENT row means 'no_aprendido'; the API
  deletes rows set back to 'no_aprendido' to keep the table sparse.
"""
import uuid

from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Index,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base

TOPIC_TYPES = ("vocab_module", "tense_group")
TOPIC_STATES = ("no_aprendido", "aprendiendo", "aprendido")


class TeacherStudent(Base):
    __tablename__ = "teacher_student"
    __table_args__ = (
        UniqueConstraint("teacher_id", "student_email", name="uq_teacher_student"),
        Index("ix_teacher_student_teacher", "teacher_id"),
        Index("ix_teacher_student_user", "student_user_id"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    teacher_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    student_email = Column(String, nullable=False)  # stored lowercased
    student_name = Column(String, nullable=True)     # display name (from the roster list)
    # Linked to a real app account when one matches by email/name; NULL means
    # the student hasn't registered yet (the overlay still works without it).
    student_user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class TeacherStudentTopicState(Base):
    __tablename__ = "teacher_student_topic_state"
    __table_args__ = (
        UniqueConstraint(
            "teacher_student_id", "topic_type", "topic_id", name="uq_teacher_topic_state"
        ),
        CheckConstraint(
            "topic_type IN ('vocab_module','tense_group')", name="ck_teacher_topic_type"
        ),
        CheckConstraint(
            "state IN ('no_aprendido','aprendiendo','aprendido')", name="ck_teacher_topic_state"
        ),
        Index("ix_teacher_topic_state_roster", "teacher_student_id"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    teacher_student_id = Column(
        UUID(as_uuid=True),
        ForeignKey("teacher_student.id", ondelete="CASCADE"),
        nullable=False,
    )
    topic_type = Column(String, nullable=False)
    topic_id = Column(String, nullable=False)
    state = Column(String, nullable=False)
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )
