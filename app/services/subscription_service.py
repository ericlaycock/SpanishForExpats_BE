from datetime import datetime, timezone
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models import User, Subscription, UserSituation, Situation, UserMilestoneEvent

FREE_ENCOUNTERS_LIMIT = 30


def _record_paywall_hit(db: Session, user_id: str, situation_id: str) -> None:
    try:
        db.add(UserMilestoneEvent(
            user_id=user_id,
            milestone_key='paywall_hit',
            situation_id=situation_id,
            occurred_at=datetime.now(timezone.utc),
        ))
        db.commit()
    except IntegrityError:
        db.rollback()  # uq_user_milestone_situation already satisfied — no-op


def _count_completed_encounters(db: Session, user_id: str) -> int:
    """Count completed encounters, excluding grammar situations auto-completed during onboarding."""
    return db.query(UserSituation).join(
        Situation, UserSituation.situation_id == Situation.id
    ).filter(
        UserSituation.user_id == user_id,
        UserSituation.completed_at.isnot(None),
        Situation.animation_type != 'grammar',
    ).count()


def get_subscription_status(db: Session, user_id: str) -> dict:
    """Get subscription status and free situations info"""
    subscription = db.query(Subscription).filter(Subscription.user_id == user_id).first()

    if not subscription:
        # Create default subscription if it doesn't exist
        subscription = Subscription(user_id=user_id, active=False)
        db.add(subscription)
        db.commit()
        db.refresh(subscription)

    # Count completed encounters (excluding grammar auto-completes)
    completed_encounters = _count_completed_encounters(db, user_id)
    
    free_encounters_remaining = max(0, FREE_ENCOUNTERS_LIMIT - completed_encounters)
    
    return {
        "active": subscription.active,
        "free_situations_limit": FREE_ENCOUNTERS_LIMIT,
        "free_situations_completed": completed_encounters,
        "free_situations_remaining": free_encounters_remaining,
        "plan": subscription.plan,
        "billing_cycle": subscription.billing_cycle,
        "cancel_at_period_end": subscription.cancel_at_period_end,
        "current_period_end": subscription.current_period_end,
        "canceled_at": subscription.canceled_at,
    }


def check_paywall(db: Session, user_id: str, situation_id: str) -> tuple[bool, str]:
    """
    Check if user can access an encounter.
    Returns (allowed, error_message)
    Business rule: Free users get FREE_ENCOUNTERS_LIMIT (=30) free encounters total.
    If subscription.active = false AND user completed >= FREE_ENCOUNTERS_LIMIT, return PAYWALL.
    """
    situation = db.query(Situation).filter(Situation.id == situation_id).first()
    if not situation:
        return False, "SITUATION_NOT_FOUND"
    
    # Check subscription
    subscription = db.query(Subscription).filter(Subscription.user_id == user_id).first()

    # Pronounce-only users get no app access
    if subscription and subscription.tier == "pronounce":
        _record_paywall_hit(db, user_id, situation_id)
        return False, "PAYWALL"

    # If subscription is active (app or app_pronounce), allow access
    if subscription and subscription.active:
        return True, None

    # If no active subscription, check total completed encounters (excluding grammar auto-completes)
    completed_encounters = _count_completed_encounters(db, user_id)
    
    # If user hit the free limit without active subscription, block
    if completed_encounters >= FREE_ENCOUNTERS_LIMIT:
        _record_paywall_hit(db, user_id, situation_id)
        return False, "PAYWALL"
    
    # User hasn't hit the free limit yet, allow access
    return True, None

