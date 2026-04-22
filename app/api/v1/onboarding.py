from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert
from pydantic import BaseModel
from typing import List
from datetime import datetime, timezone
from app.database import get_db
from app.auth import get_current_user
from app.models import User, Situation, UserWord, UserSituation, Word
from app.schemas import (
    AvailableCategoriesResponse,
    AvailableCategory,
    UpdateAnimationTypesResponse,
)
from app.data.grammar_situations import GRAMMAR_SITUATIONS, get_all_grammar_situation_ids, GL_VL_THRESHOLDS
import logging

# Maps onboarding quiz grammar score IDs to grammar levels.
QUIZ_SCORE_TO_GL: dict[str, float] = {
    "G1": 0,       # Can't conjugate present tense
    "G101": 3,     # Knows regular present tense
    "G701": 9,     # Knows through Ir A + Infinitive
    "G2001": 20,   # Knows subjunctive-level grammar
}

logger = logging.getLogger(__name__)

router = APIRouter()

def _parse_score_level(score: str | None) -> int:
    """Extract numeric level from score ID like 'V151' or 'G701'."""
    if not score:
        return 0
    digits = ''.join(c for c in score if c.isdigit())
    return int(digits) if digits else 0


class SaveOnboardingSelectionsRequest(BaseModel):
    selected_category: str | None = None  # FE sends this name
    selected_animation_type: str | None = None  # Legacy name

    @property
    def animation_type(self) -> str:
        value = self.selected_category or self.selected_animation_type
        if not value:
            raise ValueError("Either selected_category or selected_animation_type is required")
        return value

    dialect: str  # 'mexico', 'colombia', 'costa_rica'
    grammar_score: str | None = None  # Quiz grammar score
    vocab_score: str | None = None  # Quiz vocab score


def _seed_hf_words(db: Session, user_id, count: int) -> int:
    """Seed top-N high-frequency words with mastery_level=2 for placement skip-ahead."""
    hf_words = (
        db.query(Word)
        .filter(Word.word_category == "high_frequency")
        .order_by(Word.frequency_rank.asc())
        .limit(count)
        .all()
    )

    if not hf_words:
        return 0

    for word in hf_words:
        stmt = insert(UserWord).values(
            user_id=user_id,
            word_id=word.id,
            seen_count=1,
            typed_correct_count=1,
            spoken_correct_count=2,
            mastery_level=4,
            next_refresh_at=None,
            status="mastered",
        ).on_conflict_do_nothing(index_elements=["user_id", "word_id"])
        db.execute(stmt)

    return len(hf_words)


def _auto_complete_grammar(db: Session, user_id, target_gl: float) -> int:
    """Auto-complete grammar situations whose grammar_level <= target_gl."""
    now = datetime.now(timezone.utc)
    completed = 0

    for sid in get_all_grammar_situation_ids():
        cfg = GRAMMAR_SITUATIONS[sid]
        if cfg["grammar_level"] > target_gl:
            continue

        # Check if already completed
        existing = db.query(UserSituation).filter(
            UserSituation.user_id == user_id,
            UserSituation.situation_id == sid,
        ).first()

        if existing and existing.completed_at:
            continue

        if not existing:
            existing = UserSituation(
                user_id=user_id,
                situation_id=sid,
                started_at=now,
                completed_at=now,
            )
            db.add(existing)
        else:
            existing.completed_at = now

        completed += 1

    return completed


class OnboardingStatusResponse(BaseModel):
    onboarding_completed: bool
    selected_animation_types: List[str] | None


@router.post("/save-selections")
async def save_onboarding_selections(
    request: SaveOnboardingSelectionsRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Save user's selected animation type, dialect, and quiz scores from onboarding"""
    # Validate animation type exists
    valid_types = db.query(Situation.animation_type).distinct().all()
    valid_type_list = [t[0] for t in valid_types]

    if request.animation_type not in valid_type_list:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid animation type: {request.animation_type}"
        )

    # Validate dialect
    valid_dialects = ['mexico', 'colombia', 'costa_rica', 'ecuador']
    if request.dialect not in valid_dialects:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid dialect: {request.dialect}"
        )

    current_user.selected_animation_types = [request.animation_type]
    current_user.dialect = request.dialect
    current_user.grammar_score = request.grammar_score
    current_user.vocab_score = request.vocab_score
    current_user.onboarding_completed = True
    current_user.onboarding_completed_at = datetime.now(timezone.utc)

    # Determine starting vocab level from quiz scores
    vocab_target = _parse_score_level(request.vocab_score)
    grammar_implied = _parse_score_level(request.grammar_score)
    starting_vl = max(vocab_target, grammar_implied)

    # Map quiz grammar score to grammar level
    target_gl = QUIZ_SCORE_TO_GL.get(request.grammar_score, 0) if request.grammar_score else 0

    seeded_words = 0
    completed_grammar = 0

    if starting_vl > 0:
        seeded_words = _seed_hf_words(db, current_user.id, starting_vl)

    if target_gl > 0:
        completed_grammar = _auto_complete_grammar(db, current_user.id, target_gl)

    db.commit()

    logger.info(
        "Onboarding saved: user=%s grammar_score=%s vocab_score=%s starting_vl=%d target_gl=%.1f seeded_words=%d completed_grammar=%d",
        current_user.id, request.grammar_score, request.vocab_score,
        starting_vl, target_gl, seeded_words, completed_grammar,
    )

    return {
        "status": "success",
        "message": "Onboarding data saved",
        "starting_vocab_level": starting_vl,
        "grammar_level": target_gl,
        "seeded_words": seeded_words,
        "completed_grammar_units": completed_grammar,
    }


@router.get("/status", response_model=OnboardingStatusResponse)
async def get_onboarding_status(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get user's onboarding status"""
    return OnboardingStatusResponse(
        onboarding_completed=current_user.onboarding_completed,
        selected_animation_types=current_user.selected_animation_types or []
    )


@router.get("/available-categories", response_model=AvailableCategoriesResponse)
async def get_available_categories(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get list of available animation types for onboarding"""

    # Only show these 10 animation types for onboarding
    allowed_types = {
        "airport": {
            "name": "Airport",
            "description": "Checking in, going through security"
        },
        "banking": {
            "name": "Banking",
            "description": "Withdrawing cash, currency exchange"
        },
        "clothing": {
            "name": "Clothing Shopping",
            "description": "Finding sizes, trying on clothes"
        },
        "core": {
            "name": "Core",
            "description": "Essential everyday phrases and expressions"
        },
        "internet": {
            "name": "Internet",
            "description": "Setting up WiFi, phone plans"
        },
        "small_talk": {
            "name": "Small Talk",
            "description": "Meeting neighbors, casual conversations"
        },
        "contractor": {
            "name": "Home Renovation",
            "description": "Hiring contractors, discussing work"
        },
        "groceries": {
            "name": "Groceries",
            "description": "Shopping for food, asking for items"
        },
        "mechanic": {
            "name": "Mechanic",
            "description": "Car repairs, maintenance issues"
        },
        "police": {
            "name": "Police Stop",
            "description": "Traffic stops, document checks"
        },
        "restaurant": {
            "name": "Eating Out",
            "description": "Ordering food, reading menus"
        },
    }

    result: List[AvailableCategory] = []
    for type_id, type_info in allowed_types.items():
        # Verify animation type exists in database
        exists = db.query(Situation).filter(Situation.animation_type == type_id).first()
        if exists:
            result.append(AvailableCategory(
                id=type_id,
                name=type_info["name"],
                description=type_info["description"],
            ))

    # Sort by name for consistent ordering
    result.sort(key=lambda c: c.name)

    return AvailableCategoriesResponse(categories=result)


class UpdateAnimationTypesRequest(BaseModel):
    animation_type: str
    action: str  # 'add' or 'remove'


@router.patch("/animation-types", response_model=UpdateAnimationTypesResponse)
async def update_animation_types(
    request: UpdateAnimationTypesRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Add or remove an animation type from the user's selected list."""
    # Validate animation type exists in DB
    exists = db.query(Situation).filter(Situation.animation_type == request.animation_type).first()
    if not exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid animation type: {request.animation_type}"
        )

    current = list(current_user.selected_animation_types or [])

    if request.action == "add":
        if request.animation_type not in current:
            current.append(request.animation_type)
    elif request.action == "remove":
        if request.animation_type in current:
            current.remove(request.animation_type)
        if not current:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot remove last animation type"
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="action must be 'add' or 'remove'"
        )

    current_user.selected_animation_types = current
    db.commit()

    return UpdateAnimationTypesResponse(selected_animation_types=current)
