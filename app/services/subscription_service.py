from sqlalchemy.orm import Session
from app.models import User, Subscription, UserSituation, Situation

FREE_ENCOUNTERS_LIMIT = 25


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
        "free_situations_remaining": free_encounters_remaining
    }


def check_paywall(db: Session, user_id: str, situation_id: str) -> tuple[bool, str]:
    """
    Check if user can access an encounter.
    Returns (allowed, error_message)
    Business rule: Free users get 25 free encounters total.
    If subscription.active = false AND user completed >= 25 encounters, return PAYWALL.
    """
    situation = db.query(Situation).filter(Situation.id == situation_id).first()
    if not situation:
        return False, "SITUATION_NOT_FOUND"
    
    # Check subscription
    subscription = db.query(Subscription).filter(Subscription.user_id == user_id).first()

    # Pronounce-only users get no app access
    if subscription and subscription.tier == "pronounce":
        return False, "PAYWALL"

    # If subscription is active (app or app_pronounce), allow access
    if subscription and subscription.active:
        return True, None

    # If no active subscription, check total completed encounters (excluding grammar auto-completes)
    completed_encounters = _count_completed_encounters(db, user_id)
    
    # If user completed 25+ encounters without active subscription, block
    if completed_encounters >= FREE_ENCOUNTERS_LIMIT:
        return False, "PAYWALL"
    
    # User hasn't completed 25 yet, allow access
    return True, None

