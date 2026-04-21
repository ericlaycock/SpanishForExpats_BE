"""Admin endpoints — user management and plan assignment."""
import logging
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.auth import get_current_user
from app.database import get_db
from app.models import User, Subscription

logger = logging.getLogger(__name__)
router = APIRouter()

VALID_PLANS = {"free", "app", "pronounce", "app_pronounce"}


def _require_admin(user: User):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")


@router.get("/users")
def list_users(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _require_admin(current_user)

    rows = db.execute(text("""
        SELECT u.id, u.email, u.created_at, u.is_admin,
               s.tier, s.active
        FROM users u
        LEFT JOIN subscriptions s ON s.user_id = u.id
        ORDER BY u.created_at DESC
    """)).fetchall()

    return [
        {
            "id": str(r.id),
            "email": r.email,
            "created_at": r.created_at.isoformat() if r.created_at else None,
            "is_admin": r.is_admin,
            "plan": r.tier or "free",
            "subscription_active": r.active,
        }
        for r in rows
    ]


@router.patch("/users/{user_id}/plan")
def set_user_plan(
    user_id: str,
    body: dict,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _require_admin(current_user)

    plan = (body.get("plan") or "free").strip().lower()
    if plan not in VALID_PLANS:
        raise HTTPException(status_code=400, detail=f"Invalid plan. Must be one of: {', '.join(sorted(VALID_PLANS))}")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    sub = db.query(Subscription).filter(Subscription.user_id == user_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="Subscription record not found")

    sub.tier = plan if plan != "free" else None
    sub.active = plan in ("app", "app_pronounce")
    db.commit()

    logger.info(f"[Admin] {current_user.email} changed {user.email} plan to '{plan}'")
    return {"id": user_id, "plan": plan, "subscription_active": sub.active}
