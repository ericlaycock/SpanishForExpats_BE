"""Admin endpoints — user management and plan assignment."""
import logging
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.auth import get_current_user
from app.database import get_db
from app.models import User, Subscription
from app.schemas import FreeflowResponse, FreeflowUserRow, MilestoneInfo

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


@router.get("/freeflow", response_model=FreeflowResponse)
def get_freeflow(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _require_admin(current_user)

    rows = db.execute(text("""
        WITH
        user_m2 AS (
            SELECT user_id, MIN(started_at) AS m2_ts
            FROM user_situations
            GROUP BY user_id
        ),
        user_m3 AS (
            SELECT user_id, MIN(occurred_at) AS m3_ts
            FROM user_milestone_events
            WHERE milestone_key IN ('phase_1a', 'phase_video')
            GROUP BY user_id
        ),
        user_m4 AS (
            SELECT user_id, MIN(occurred_at) AS m4_ts
            FROM user_milestone_events
            WHERE milestone_key IN ('phase_1b', 'phase_drill')
            GROUP BY user_id
        ),
        user_m5 AS (
            SELECT user_id, MIN(occurred_at) AS m5_ts
            FROM user_milestone_events
            WHERE milestone_key = 'first_word'
            GROUP BY user_id
        ),
        user_m6 AS (
            SELECT user_id, MIN(completed_at) AS m6_ts
            FROM conversations
            WHERE conversation_type = 'lesson' AND completed_at IS NOT NULL
            GROUP BY user_id
        ),
        ranked_situations AS (
            SELECT user_id, started_at, completed_at,
                   ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY started_at ASC) AS rn
            FROM user_situations
        ),
        user_m7 AS (
            SELECT user_id, started_at AS m7_ts FROM ranked_situations WHERE rn = 2
        ),
        user_m8 AS (
            SELECT user_id, completed_at AS m8_ts FROM ranked_situations WHERE rn = 2
        ),
        user_pathway AS (
            SELECT user_id,
                MAX(CASE WHEN milestone_key IN ('phase_1a', 'phase_1b') THEN 'V' END) AS v_path,
                MAX(CASE WHEN milestone_key IN ('phase_video', 'phase_drill') THEN 'G' END) AS g_path
            FROM user_milestone_events
            GROUP BY user_id
        )
        SELECT
            u.id AS user_id,
            u.email,
            u.created_at AS m0_ts,
            u.onboarding_completed_at AS m1_ts,
            u.dialect,
            u.grammar_score,
            u.vocab_score,
            u.selected_animation_types,
            COALESCE(s.active, false) AS subscription_active,
            m2.m2_ts,
            m3.m3_ts,
            m4.m4_ts,
            m5.m5_ts,
            m6.m6_ts,
            m7.m7_ts,
            m8.m8_ts,
            COALESCE(pw.v_path, pw.g_path) AS pathway
        FROM users u
        LEFT JOIN subscriptions s ON s.user_id = u.id
        LEFT JOIN user_m2 m2 ON m2.user_id = u.id
        LEFT JOIN user_m3 m3 ON m3.user_id = u.id
        LEFT JOIN user_m4 m4 ON m4.user_id = u.id
        LEFT JOIN user_m5 m5 ON m5.user_id = u.id
        LEFT JOIN user_m6 m6 ON m6.user_id = u.id
        LEFT JOIN user_m7 m7 ON m7.user_id = u.id
        LEFT JOIN user_m8 m8 ON m8.user_id = u.id
        LEFT JOIN user_pathway pw ON pw.user_id = u.id
        WHERE u.is_admin = false
        ORDER BY u.created_at DESC
    """)).fetchall()

    def _delta(ts, prev_ts):
        if ts is None or prev_ts is None:
            return None
        return int((ts - prev_ts).total_seconds())

    def _mi(ts, prev_ts):
        return MilestoneInfo(
            timestamp=ts,
            delta_seconds=_delta(ts, prev_ts),
        )

    users = []
    for r in rows:
        timestamps = [r.m0_ts, r.m1_ts, r.m2_ts, r.m3_ts, r.m4_ts, r.m5_ts, r.m6_ts, r.m7_ts, r.m8_ts]
        current_milestone = 0
        for i, ts in enumerate(timestamps):
            if ts is not None:
                current_milestone = i

        users.append(FreeflowUserRow(
            user_id=str(r.user_id),
            email=r.email,
            subscription_active=bool(r.subscription_active),
            pathway=r.pathway,
            dialect=r.dialect,
            grammar_score=r.grammar_score,
            vocab_score=r.vocab_score,
            selected_animation_types=r.selected_animation_types or [],
            m0=_mi(r.m0_ts, None),
            m1=_mi(r.m1_ts, r.m0_ts),
            m2=_mi(r.m2_ts, r.m1_ts),
            m3=_mi(r.m3_ts, r.m2_ts),
            m4=_mi(r.m4_ts, r.m3_ts),
            m5=_mi(r.m5_ts, r.m4_ts),
            m6=_mi(r.m6_ts, r.m5_ts),
            m7=_mi(r.m7_ts, r.m6_ts),
            m8=_mi(r.m8_ts, r.m7_ts),
            current_milestone=current_milestone,
        ))

    return FreeflowResponse(users=users)
