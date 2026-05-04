from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert

from app.auth import get_current_user
from app.database import get_db
from app.models import User, UserMilestoneEvent
from app.schemas import MilestoneEventRequest

router = APIRouter()


@router.post("")
async def record_milestone(
    body: MilestoneEventRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    stmt = (
        insert(UserMilestoneEvent)
        .values(
            user_id=current_user.id,
            milestone_key=body.milestone_key,
            situation_id=body.situation_id,
            conversation_id=body.conversation_id,
        )
        .on_conflict_do_nothing(constraint="uq_user_milestone_situation")
    )
    db.execute(stmt)
    db.commit()
    return {"status": "ok"}
