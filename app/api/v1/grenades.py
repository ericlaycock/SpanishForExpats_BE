"""Daily grenade routes — see services/grenade_service.py for behavior."""
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.core.request_utils import get_request_id_from_request
from app.database import get_db
from app.models import Grenade, User
from app.schemas import (
    GrenadeGenerateRequest,
    GrenadeOut,
    GrenadeRecallRequest,
    GrenadeTodayResponse,
)
from app.services import grenade_service

router = APIRouter()


def _to_out(grenade: Grenade) -> GrenadeOut:
    return GrenadeOut(
        id=grenade.id,
        target_form=grenade.target_form,
        pos=grenade.pos,
        audience=grenade.audience,
        question_es=grenade.question_es,
        question_en=grenade.question_en,
        assigned_date=grenade.assigned_date.isoformat(),
        used=grenade.used,
    )


@router.get("/today", response_model=GrenadeTodayResponse)
async def get_today(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Today's grenade + most-recent unanswered prior grenade + 14-day strip."""
    today, pending, strip = grenade_service.build_today_response(db, current_user.id)
    return GrenadeTodayResponse(
        today=_to_out(today) if today else None,
        pending_recall=_to_out(pending) if pending else None,
        strip=strip,
    )


@router.post("/{grenade_id}/generate", response_model=GrenadeOut)
async def generate(
    grenade_id: UUID,
    body: GrenadeGenerateRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Craft (or recraft for a different audience) the question for a grenade."""
    grenade = (
        db.query(Grenade)
        .filter(Grenade.id == grenade_id, Grenade.user_id == current_user.id)
        .first()
    )
    if grenade is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grenade not found")

    request_id = get_request_id_from_request(request) or str(grenade_id)
    grenade = await grenade_service.generate_question(
        db=db,
        grenade=grenade,
        audience=body.audience,
        request_id=request_id,
    )
    return _to_out(grenade)


@router.post("/recall", response_model=GrenadeOut)
async def recall(
    body: GrenadeRecallRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Record whether the user deployed a prior grenade in real conversation."""
    try:
        grenade = grenade_service.record_recall(
            db, current_user.id, body.grenade_id, body.used
        )
    except LookupError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grenade not found")
    return _to_out(grenade)
