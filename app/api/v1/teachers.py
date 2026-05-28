"""Teachers-only portal API.

A tutor (User.is_teacher) gets a roster of assigned students and a manual
tri-state mastery overlay per topic. The overlay is fully decoupled from the
student's real progress — it only reads/writes `teacher_student_topic_state`,
keyed to the roster row so it works even for students without an app account.

Endpoints (all gated by `_require_teacher`):
  GET  /v1/teachers/students                     → the caller's roster
  GET  /v1/teachers/students/{roster_id}         → roster row + non-default states
  PUT  /v1/teachers/students/{roster_id}/state   → upsert one topic's state
  GET  /v1/teachers/topics                        → static verb (tense-group) taxonomy
"""
from __future__ import annotations

from typing import Literal, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.data import tense_quest as tq
from app.database import get_db
from app.models import TeacherStudent, TeacherStudentTopicState, User

router = APIRouter()


def _require_teacher(user: User) -> None:
    # Admins are implicitly allowed (same convenience the rest of the app uses).
    if not (user.is_teacher or user.is_admin):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Teacher access required")


# ── schemas ───────────────────────────────────────────────────────────────────

class RosterStudent(BaseModel):
    id: str            # teacher_student.id (the roster row — used as the URL key)
    student_email: str
    student_name: Optional[str] = None
    has_account: bool  # whether the student is linked to a real app user


class TopicState(BaseModel):
    topic_type: Literal["vocab_module", "tense_group"]
    topic_id: str
    state: Literal["no_aprendido", "aprendiendo", "aprendido"]


class StudentDetail(BaseModel):
    id: str
    student_email: str
    student_name: Optional[str] = None
    has_account: bool
    states: list[TopicState]  # only non-default (non-'no_aprendido') rows


class SetStateRequest(BaseModel):
    topic_type: Literal["vocab_module", "tense_group"]
    topic_id: str
    state: Literal["no_aprendido", "aprendiendo", "aprendido"]


class TenseGroupTopic(BaseModel):
    id: str
    title: str
    family: str
    family_label: str
    gl: Optional[float] = None


class TopicsResponse(BaseModel):
    tense_groups: list[TenseGroupTopic]


# ── helpers ───────────────────────────────────────────────────────────────────

def _roster_row(db: Session, teacher_id, roster_id: str) -> TeacherStudent:
    row = (
        db.query(TeacherStudent)
        .filter(TeacherStudent.id == roster_id, TeacherStudent.teacher_id == teacher_id)
        .one_or_none()
    )
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return row


# ── endpoints ─────────────────────────────────────────────────────────────────

@router.get("/students", response_model=list[RosterStudent])
async def list_students(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _require_teacher(current_user)
    rows = (
        db.query(TeacherStudent)
        .filter(TeacherStudent.teacher_id == current_user.id)
        .order_by(TeacherStudent.student_name.asc().nullslast(), TeacherStudent.student_email.asc())
        .all()
    )
    return [
        RosterStudent(
            id=str(r.id),
            student_email=r.student_email,
            student_name=r.student_name,
            has_account=r.student_user_id is not None,
        )
        for r in rows
    ]


@router.get("/students/{roster_id}", response_model=StudentDetail)
async def get_student(
    roster_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _require_teacher(current_user)
    row = _roster_row(db, current_user.id, roster_id)
    states = (
        db.query(TeacherStudentTopicState)
        .filter(TeacherStudentTopicState.teacher_student_id == row.id)
        .all()
    )
    return StudentDetail(
        id=str(row.id),
        student_email=row.student_email,
        student_name=row.student_name,
        has_account=row.student_user_id is not None,
        states=[
            TopicState(topic_type=s.topic_type, topic_id=s.topic_id, state=s.state)
            for s in states
        ],
    )


@router.put("/students/{roster_id}/state", response_model=TopicState)
async def set_topic_state(
    roster_id: str,
    body: SetStateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Upsert one topic's state for a student. 'no_aprendido' is the implicit
    default, so setting it deletes the row to keep the table sparse."""
    _require_teacher(current_user)
    row = _roster_row(db, current_user.id, roster_id)

    if body.state == "no_aprendido":
        db.query(TeacherStudentTopicState).filter(
            TeacherStudentTopicState.teacher_student_id == row.id,
            TeacherStudentTopicState.topic_type == body.topic_type,
            TeacherStudentTopicState.topic_id == body.topic_id,
        ).delete(synchronize_session=False)
        db.commit()
        return TopicState(topic_type=body.topic_type, topic_id=body.topic_id, state=body.state)

    stmt = (
        insert(TeacherStudentTopicState)
        .values(
            teacher_student_id=row.id,
            topic_type=body.topic_type,
            topic_id=body.topic_id,
            state=body.state,
        )
        .on_conflict_do_update(
            constraint="uq_teacher_topic_state",
            set_={"state": body.state, "updated_at": func.now()},
        )
    )
    db.execute(stmt)
    db.commit()
    return TopicState(topic_type=body.topic_type, topic_id=body.topic_id, state=body.state)


@router.get("/topics", response_model=TopicsResponse)
async def list_topics(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Static verb taxonomy (tense groups) so the FE verb board renders without
    student-scoped data. Vocab modules live in the FE's vocabData.ts."""
    _require_teacher(current_user)
    groups = [
        TenseGroupTopic(
            id=g["id"],
            title=g["title"],
            family=g["family"],
            family_label=g["family_label"],
            gl=g.get("gl"),
        )
        for g in tq.list_tense_groups()
    ]
    return TopicsResponse(tense_groups=groups)
