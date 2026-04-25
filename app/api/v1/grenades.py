"""Daily grenade endpoints — see app/services/grenade_service.py."""
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import User
from app.schemas import (
    GrenadeRecallRequest,
    GrenadeSchema,
    GrenadeTodayResponse,
)
from app.services import grenade_service

router = APIRouter()


@router.get("/today", response_model=GrenadeTodayResponse)
async def get_today(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    first_done = grenade_service.first_lesson_done_today(db, current_user.id)
    grenade = grenade_service.pick_or_get_todays_grenade(db, current_user.id) if first_done else None
    prior = grenade_service.get_prior_unanswered(db, current_user.id)
    recent = grenade_service.get_recent_grenades(db, current_user.id, days=14)
    return GrenadeTodayResponse(
        grenade=GrenadeSchema.model_validate(grenade) if grenade else None,
        prior_unanswered=GrenadeSchema.model_validate(prior) if prior else None,
        first_lesson_done=first_done,
        recent=recent,
    )


@router.post("/today/generate", response_model=GrenadeSchema)
async def generate_today(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if not grenade_service.first_lesson_done_today(db, current_user.id):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Finish today's first lesson first")
    grenade = grenade_service.pick_or_get_todays_grenade(db, current_user.id)
    if not grenade:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No eligible word for today")
    grenade = await grenade_service.generate_sentence(db, current_user.id, grenade)
    return GrenadeSchema.model_validate(grenade)


@router.post("/{grenade_id}/recall", response_model=GrenadeSchema)
async def recall_grenade(
    grenade_id: UUID,
    body: GrenadeRecallRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    grenade = grenade_service.record_recall(db, current_user.id, grenade_id, body.used)
    if not grenade:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grenade not found")
    return GrenadeSchema.model_validate(grenade)
