from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, timezone
from app.database import get_db
from app.auth import get_current_user
from app.models import User, Situation, UserWord, UserSituation, Word
from app.schemas import (
    AvailableCategoriesResponse,
    AvailableCategory,
    UpdateAnimationTypesResponse,
)
from app.data.grammar_situations import GRAMMAR_SITUATIONS, get_all_grammar_situation_ids, GL_VL_THRESHOLDS, GL_SORTED
import logging

# Maps old onboarding quiz grammar score IDs to grammar levels.
QUIZ_SCORE_TO_GL: dict[str, float] = {
    "G1": 0,       # Can't conjugate present tense
    "G101": 3,     # Knows regular present tense
    "G701": 9,     # Knows through Ir A + Infinitive
    "G2001": 20,   # Knows subjunctive-level grammar
}

# Maps new onboarding V2 GL string labels to backend numeric GL.
NEW_GL_LABEL_TO_GL: dict[str, float] = {
    "pronouns + gender": 2,
    "present regular": 3,
    "present irregular": 8,
    "ir a": 11,
    "imperfect": 12,
    "reflexive": 13,
    "future": 14,
    "conditional": 15,
    "preterite regular": 17,        # GL 16 intentionally skipped — left as first lesson
    "preterite irregular 1": 17.3,  # 17.1 + 17.2 + 17.3
    "preterite irregular 2": 17.5,  # 17.4 + 17.5
    "gerund": 18,
    "perfect tenses": 18.5,         # New GL added for V2
    "dir + indir": 19,
    "dir + indir 2": 19,            # Same unit, label stored for analytics
    "subjunctive 1": 20,
    "subjunctive 2": 20,            # Same unit, label stored for analytics
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
    # V2 onboarding profile fields
    name: Optional[str] = None
    q0_spanish_level: Optional[str] = None
    q1_situation: Optional[str] = None
    q1_1_time_in_latam: Optional[str] = None
    q2_country: Optional[str] = None
    q3_tools: Optional[List[str]] = None
    q4_proximity: Optional[str] = None
    q6_conversations: Optional[str] = None

    # V2 assessment results
    grammar_level_v2: Optional[str] = None   # GLLevel string from new grammar tree
    vocab_level_v2: Optional[int] = None     # Integer VL from new vocab tree

    # V2 situation selection (multi-select, replaces single category)
    selected_animation_types_v2: Optional[List[str]] = None

    # V1 legacy fields (backward compat — old in-app onboarding wizard)
    selected_category: Optional[str] = None
    selected_animation_type: Optional[str] = None
    dialect: Optional[str] = None
    grammar_score: Optional[str] = None
    vocab_score: Optional[str] = None

    @property
    def animation_type(self) -> str | None:
        return self.selected_category or self.selected_animation_type


def _seed_hf_words(db: Session, user_id, count: int) -> int:
    """Seed top-N high-frequency words with mastery_level=4 for placement skip-ahead."""
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


def _auto_complete_grammar(db: Session, user_id, target_gl: float, skip_gls: set[float] | None = None) -> int:
    """Auto-complete grammar situations whose grammar_level <= target_gl, skipping any in skip_gls."""
    skip_gls = skip_gls or set()
    now = datetime.now(timezone.utc)
    completed = 0

    for sid in get_all_grammar_situation_ids():
        cfg = GRAMMAR_SITUATIONS[sid]
        if cfg["grammar_level"] > target_gl:
            continue
        if cfg["grammar_level"] in skip_gls:
            continue

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


def _find_first_situation(db: Session, user_id, selected_animation_types: list[str] | None) -> str | None:
    """Find the first uncompleted situation for the user after onboarding.

    Priority: grammar situations (by GL ascending), then selected animation type situations.
    """
    completed_ids = {
        us.situation_id
        for us in db.query(UserSituation).filter(
            UserSituation.user_id == user_id,
            UserSituation.completed_at.isnot(None),
        ).all()
    }

    # Check grammar situations in GL order
    for sid in get_all_grammar_situation_ids():
        if sid not in completed_ids:
            return sid

    # Fall back to first situation in selected animation types
    if selected_animation_types:
        for anim_type in selected_animation_types:
            sit = (
                db.query(Situation)
                .filter(
                    Situation.animation_type == anim_type,
                    Situation.situation_type == 'main',
                )
                .order_by(Situation.order_index.asc())
                .first()
            )
            if sit and sit.id not in completed_ids:
                return sit.id

    return None


class OnboardingStatusResponse(BaseModel):
    onboarding_completed: bool
    selected_animation_types: List[str] | None


@router.post("/save-selections")
async def save_onboarding_selections(
    request: SaveOnboardingSelectionsRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Save user's onboarding selections. Supports both V1 (legacy) and V2 (new) formats."""

    # --- Store V2 profile fields ---
    if request.name is not None:
        current_user.name = request.name.strip() or None
    if request.q0_spanish_level is not None:
        current_user.q0_spanish_level = request.q0_spanish_level
    if request.q1_situation is not None:
        current_user.q1_situation = request.q1_situation
    if request.q1_1_time_in_latam is not None:
        current_user.q1_1_time_in_latam = request.q1_1_time_in_latam
    if request.q2_country is not None:
        current_user.q2_country = request.q2_country
    if request.q3_tools is not None:
        current_user.q3_tools = request.q3_tools
    if request.q4_proximity is not None:
        current_user.q4_proximity = request.q4_proximity
    if request.q6_conversations is not None:
        current_user.q6_conversations = request.q6_conversations

    # --- Dialect (V1 only) ---
    if request.dialect is not None:
        valid_dialects = ['mexico', 'colombia', 'costa_rica', 'ecuador']
        if request.dialect not in valid_dialects:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid dialect: {request.dialect}"
            )
        current_user.dialect = request.dialect

    # --- Situation selection ---
    if request.selected_animation_types_v2 is not None:
        # V2: multi-select list
        current_user.selected_animation_types = request.selected_animation_types_v2
        current_user.grammar_score = request.grammar_level_v2  # store raw label for analytics
    elif request.animation_type is not None:
        # V1: single animation type
        valid_types = db.query(Situation.animation_type).distinct().all()
        valid_type_list = [t[0] for t in valid_types]
        if request.animation_type not in valid_type_list:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid animation type: {request.animation_type}"
            )
        current_user.selected_animation_types = [request.animation_type]
        current_user.grammar_score = request.grammar_score
        current_user.vocab_score = request.vocab_score

    seeded_words = 0
    completed_grammar = 0
    target_gl = 0.0

    # --- V2 assessment: new GL label + numeric VL ---
    if request.grammar_level_v2 is not None:
        target_gl = NEW_GL_LABEL_TO_GL.get(request.grammar_level_v2, 0)
        skip_gls = {16.0} if target_gl >= 17 else None
        completed_grammar = _auto_complete_grammar(db, current_user.id, target_gl, skip_gls=skip_gls)

    if request.vocab_level_v2 is not None and request.vocab_level_v2 > 0:
        seeded_words = _seed_hf_words(db, current_user.id, request.vocab_level_v2)

    # --- V1 assessment: old score strings (fallback when V2 not present) ---
    if request.grammar_level_v2 is None and request.grammar_score is not None:
        target_gl = QUIZ_SCORE_TO_GL.get(request.grammar_score, 0)
        if target_gl > 0:
            completed_grammar = _auto_complete_grammar(db, current_user.id, target_gl)

    if request.vocab_level_v2 is None and request.vocab_score is not None:
        vocab_target = _parse_score_level(request.vocab_score)
        grammar_implied = _parse_score_level(request.grammar_score)
        starting_vl = max(vocab_target, grammar_implied)
        if starting_vl > 0:
            seeded_words = _seed_hf_words(db, current_user.id, starting_vl)

    current_user.onboarding_completed = True
    current_user.onboarding_completed_at = datetime.now(timezone.utc)

    db.flush()

    first_situation_id = _find_first_situation(
        db,
        current_user.id,
        current_user.selected_animation_types,
    )

    db.commit()

    logger.info(
        "Onboarding saved: user=%s grammar_level_v2=%s vocab_level_v2=%s target_gl=%.1f "
        "seeded_words=%d completed_grammar=%d first_situation=%s",
        current_user.id, request.grammar_level_v2, request.vocab_level_v2,
        target_gl, seeded_words, completed_grammar, first_situation_id,
    )

    return {
        "status": "success",
        "message": "Onboarding data saved",
        "starting_vocab_level": request.vocab_level_v2 or 0,
        "grammar_level": target_gl,
        "seeded_words": seeded_words,
        "completed_grammar_units": completed_grammar,
        "first_situation_id": first_situation_id,
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

    # Only show these animation types for onboarding
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
        exists = db.query(Situation).filter(Situation.animation_type == type_id).first()
        if exists:
            result.append(AvailableCategory(
                id=type_id,
                name=type_info["name"],
                description=type_info["description"],
            ))

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
