"""Cohort registration — replaces the standalone signup at the end of the
marketing webflow.

Flow:
  1. POST /v1/cohorts/{id}/register {name, email}
       Creates a CohortRegistration with user_id=NULL. Sends the .ics +
       sessions email immediately so the user has it even if they bounce
       before claiming an account. Returns a registration_token.
  2. POST /v1/cohorts/registrations/{token}/claim {password, confirm_password}
       Creates the User account, links it to the existing registration,
       returns a normal LoginResponse-shaped payload so the FE can call
       /v1/onboarding/save-selections and login() the same way it always has.

The .ics download URL is token-gated and works as soon as step 1 completes —
no auth required.
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
    CohortClaimAccountRequest,
    CohortClaimAccountResponse,
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
    """List active cohorts visible to the marketing flow."""
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
    """Create a passwordless CohortRegistration. Sends the confirmation
    email + .ics immediately. The User account is created later via /claim.
    """
    email = request.email.strip().lower()
    name = request.name.strip()

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

    existing = (
        db.query(CohortRegistration)
        .filter(
            CohortRegistration.cohort_id == cohort.id,
            CohortRegistration.email == email,
        )
        .first()
    )
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This email is already registered for this cohort",
        )

    confirmation_token = secrets.token_urlsafe(32)
    registration = CohortRegistration(
        cohort_id=cohort.id,
        user_id=None,
        name=name,
        email=email,
        confirmation_token=confirmation_token,
    )
    db.add(registration)
    db.commit()
    db.refresh(cohort)

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

    return CohortRegisterResponse(
        registration_token=confirmation_token,
        email=email,
        cohort=_to_public(cohort, reg_count + 1),
    )


@router.post(
    "/registrations/{token}/claim",
    response_model=CohortClaimAccountResponse,
)
def claim_account(
    token: str,
    request: CohortClaimAccountRequest,
    db: Session = Depends(get_db),
):
    """Activate app access for a previously-registered cohort attendee.

    Looks up the CohortRegistration by token, creates the User account
    with the provided password, links the registration row to the new
    user, and returns a JWT so the FE can log the user in.
    """
    if request.password != request.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    registration = (
        db.query(CohortRegistration)
        .filter(CohortRegistration.confirmation_token == token)
        .first()
    )
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")

    if registration.user_id is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account already exists for this registration",
        )

    # create_user raises 400 if email already exists. That's possible if the
    # same email registered for the cohort and ALSO holds a separate account
    # — surface the conflict cleanly so the FE can prompt them to log in.
    user = create_user(db, registration.email, request.password)
    user.name = registration.name
    db.flush()

    registration.user_id = user.id
    db.commit()

    sub = db.query(Subscription).filter(Subscription.user_id == user.id).first()
    plan = (sub.tier if sub and sub.tier else "free")

    access_token = create_access_token(data={"sub": str(user.id), "plan": plan})
    return CohortClaimAccountResponse(
        access_token=access_token,
        user_id=user.id,
        is_admin=user.is_admin,
        email=user.email,
        plan=plan,
    )


@router.get("/registrations/{token}/calendar.ics")
def download_calendar(token: str, db: Session = Depends(get_db)):
    """Token-gated public download of the registrant's .ics file."""
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
