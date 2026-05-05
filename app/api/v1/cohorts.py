"""Cohort registration — replaces the standalone signup at the end of the
marketing webflow. A single POST creates the User account and the
CohortRegistration in one transaction, mirrors the post-signup token
shape so the FE can log the user in immediately, and queues a
confirmation email + .ics attachment.
"""
from __future__ import annotations

import logging
import secrets
from datetime import timedelta
from typing import List, Sequence

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Query, Response, status
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.auth import create_access_token, create_user
from app.config import settings
from app.database import get_db
from app.models import Cohort, CohortRegistration, Subscription
from app.schemas import (
    CohortListResponse,
    CohortPublic,
    CohortRegisterRequest,
    CohortRegisterResponse,
    CohortSession,
)
from app.services.email_service import send_cohort_confirmation
from app.services.ics import IcsEvent, build_calendar

router = APIRouter()
logger = logging.getLogger(__name__)


def _sessions_for(cohort: Cohort) -> List[CohortSession]:
    duration = timedelta(minutes=cohort.duration_minutes)
    return [
        CohortSession(
            index=i + 1,
            start_utc=start,
            end_utc=start + duration,
        )
        for i, start in enumerate(
            (cohort.session_1_start, cohort.session_2_start, cohort.session_3_start)
        )
    ]


def _to_public(cohort: Cohort, registration_count: int) -> CohortPublic:
    return CohortPublic(
        id=cohort.id,
        slug=cohort.slug,
        name=cohort.name,
        visibility=cohort.visibility,
        timezone=cohort.timezone,
        duration_minutes=cohort.duration_minutes,
        capacity=cohort.capacity,
        spots_left=max(0, cohort.capacity - registration_count),
        sessions=_sessions_for(cohort),
    )


def _build_ics(cohort: Cohort, token: str) -> str:
    zoom = settings.cohort_zoom_url or "Zoom link will be sent before session 1."
    events = [
        IcsEvent(
            uid=f"{token}-{i}@spanishforexpats.com",
            start_utc=session.start_utc,
            end_utc=session.end_utc,
            summary=f"Spanish for Expats — {cohort.name} (Session {i})",
            description=(
                f"Session {i} of 3 for the {cohort.name} cohort.\n"
                f"Zoom: {zoom}\n"
                "All times shown in your local calendar timezone."
            ),
            location=zoom,
        )
        for i, session in enumerate(_sessions_for(cohort), start=1)
    ]
    return build_calendar(events)


@router.get("", response_model=CohortListResponse)
def list_cohorts(
    include_business: bool = Query(False),
    db: Session = Depends(get_db),
):
    """List active cohorts visible to the marketing flow.

    Public cohorts are always returned. The business-owner cohorts are
    revealed only when the user toggles the "Are you a business owner?"
    disclosure in the FE.
    """
    visibilities = ["public"]
    if include_business:
        visibilities.append("business_owner")

    rows = (
        db.query(
            Cohort,
            func.count(CohortRegistration.id).label("reg_count"),
        )
        .outerjoin(CohortRegistration, CohortRegistration.cohort_id == Cohort.id)
        .filter(Cohort.is_active.is_(True))
        .filter(Cohort.visibility.in_(visibilities))
        .group_by(Cohort.id)
        .order_by(Cohort.session_1_start.asc(), Cohort.id.asc())
        .all()
    )
    return CohortListResponse(
        cohorts=[_to_public(c, count) for c, count in rows]
    )


@router.post("/{cohort_id}/register", response_model=CohortRegisterResponse)
def register_for_cohort(
    cohort_id: int,
    request: CohortRegisterRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    """Atomically create the user account + cohort registration.

    Mirrors the response shape of /v1/auth/register so the FE can call
    `login(access_token, is_admin, email)` exactly as it did before, and
    then proceed to call /v1/onboarding/save-selections to persist the
    quiz state with the new auth token.
    """
    if request.password != request.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match",
        )

    email = request.email.strip().lower()
    name = request.name.strip()

    # Lock the cohort row so capacity checks aren't racy under concurrent registrations.
    cohort = (
        db.query(Cohort)
        .filter(Cohort.id == cohort_id, Cohort.is_active.is_(True))
        .with_for_update()
        .first()
    )
    if not cohort:
        raise HTTPException(status_code=404, detail="Cohort not found")

    reg_count = (
        db.query(func.count(CohortRegistration.id))
        .filter(CohortRegistration.cohort_id == cohort.id)
        .scalar()
    )
    if reg_count >= cohort.capacity:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This cohort is full",
        )

    # create_user handles the duplicate-email check (raises 400 if email exists).
    user = create_user(db, email, request.password)
    user.name = name
    db.flush()

    sub = db.query(Subscription).filter(Subscription.user_id == user.id).first()
    plan = (sub.tier if sub and sub.tier else "free")

    confirmation_token = secrets.token_urlsafe(32)
    registration = CohortRegistration(
        cohort_id=cohort.id,
        user_id=user.id,
        name=name,
        email=email,
        confirmation_token=confirmation_token,
    )
    db.add(registration)
    db.commit()
    db.refresh(cohort)

    # Send the confirmation email out-of-band so the response doesn't block on SMTP.
    session_starts: Sequence = (
        cohort.session_1_start,
        cohort.session_2_start,
        cohort.session_3_start,
    )
    ics_payload = _build_ics(cohort, confirmation_token)
    background_tasks.add_task(
        send_cohort_confirmation,
        to_email=email,
        name=name,
        cohort=cohort,
        session_starts=session_starts,
        zoom_url=settings.cohort_zoom_url,
        ics_payload=ics_payload,
    )

    access_token = create_access_token(data={"sub": str(user.id), "plan": plan})
    return CohortRegisterResponse(
        access_token=access_token,
        user_id=user.id,
        is_admin=user.is_admin,
        email=user.email,
        plan=plan,
        registration_token=confirmation_token,
        cohort=_to_public(cohort, reg_count + 1),
    )


@router.get("/registrations/{token}/calendar.ics")
def download_calendar(token: str, db: Session = Depends(get_db)):
    """Token-gated public download of the registrant's .ics file.

    No JWT required — the unguessable token in the URL is the credential.
    """
    registration = (
        db.query(CohortRegistration)
        .filter(CohortRegistration.confirmation_token == token)
        .first()
    )
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")

    cohort = db.query(Cohort).filter(Cohort.id == registration.cohort_id).first()
    if not cohort:
        raise HTTPException(status_code=404, detail="Cohort not found")

    payload = _build_ics(cohort, token)
    return Response(
        content=payload,
        media_type="text/calendar; charset=utf-8",
        headers={
            "Content-Disposition": 'attachment; filename="spanish-cohort.ics"',
            "Cache-Control": "no-store",
        },
    )
