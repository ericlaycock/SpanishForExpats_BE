from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import List, Optional
from app.database import get_db
from app.auth import get_current_user
from app.models import User, UserWord, Word
from app.schemas import (
    DemoteWordResponse,
    HintRequest,
    HintResponse,
    MessageOnlyResponse,
    TypedCorrectRequest,
    UnknownWordSchema,
    UnknownWordsResponse,
    UserWordSchema,
)
from app.services.alt_language_service import apply_alt_language

router = APIRouter()


@router.get("", response_model=list[UserWordSchema])
async def get_user_words(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all user word progress"""
    user_words = db.query(UserWord).filter(
        UserWord.user_id == current_user.id
    ).all()
    
    # Get word details
    word_ids = [uw.word_id for uw in user_words]
    words = db.query(Word).filter(Word.id.in_(word_ids)).all()
    words = apply_alt_language(words, current_user.alt_language, db)
    word_dict = {w.id: w for w in words}

    result = []
    for uw in user_words:
        word = word_dict.get(uw.word_id)
        if word:
            result.append(UserWordSchema(
                id=uw.word_id,
                word_id=uw.word_id,
                spanish=word.spanish,
                english=word.english,
                notes=word.notes,
                seen_count=uw.seen_count,
                typed_correct_count=uw.typed_correct_count,
                spoken_correct_count=uw.spoken_correct_count,
                hint_count=uw.hint_count,
                status=uw.status,
                mastery_level=uw.mastery_level,
                next_refresh_at=uw.next_refresh_at,
                word_category=word.word_category,
                frequency_rank=word.frequency_rank,
            ))

    return result


@router.post("/typed-correct", response_model=MessageOnlyResponse)
async def mark_typed_correct(
    request: TypedCorrectRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Increment typed_correct_count for specified words"""
    # Validate all word IDs exist
    existing_ids = {
        row[0] for row in db.query(Word.id).filter(Word.id.in_(request.word_ids)).all()
    }
    invalid_ids = set(request.word_ids) - existing_ids
    if invalid_ids:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid word IDs: {sorted(invalid_ids)}"
        )

    for word_id in request.word_ids:
        user_word = db.query(UserWord).filter(
            UserWord.user_id == current_user.id,
            UserWord.word_id == word_id
        ).first()
        
        if user_word:
            user_word.typed_correct_count += 1
        else:
            # Create if doesn't exist
            user_word = UserWord(
                user_id=current_user.id,
                word_id=word_id,
                typed_correct_count=1
            )
            db.add(user_word)
    
    db.commit()
    return {"message": "Updated"}


@router.post("/hint", response_model=HintResponse)
async def record_hint(
    request: HintRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Increment hint_count for a word during voice chat."""
    user_word = db.query(UserWord).filter(
        UserWord.user_id == current_user.id,
        UserWord.word_id == request.word_id
    ).first()
    if user_word:
        user_word.hint_count += 1
        db.commit()
        return {"hint_count": user_word.hint_count}
    return {"hint_count": 0}


@router.post("/demote", response_model=DemoteWordResponse)
async def demote_word(
    request: HintRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Demote a word's mastery level by 1 during refresh (user clicked 'I forgot').
    Floor at mastery_level=1 (word was learned at least once). Recalculates next_refresh_at."""
    from app.services.refresh_service import SRS_INTERVALS
    from datetime import datetime, timezone

    user_word = db.query(UserWord).filter(
        UserWord.user_id == current_user.id,
        UserWord.word_id == request.word_id
    ).first()
    if not user_word:
        raise HTTPException(status_code=404, detail="Word not found")

    old_level = user_word.mastery_level
    new_level = max(1, old_level - 1)
    user_word.mastery_level = new_level
    user_word.status = "learning"
    # Reset SRS timer based on new level
    interval = SRS_INTERVALS.get(new_level)
    user_word.next_refresh_at = datetime.now(timezone.utc) + interval if interval else None
    db.commit()
    return {"word_id": request.word_id, "old_level": old_level, "new_level": new_level}


@router.get("/unknown", response_model=UnknownWordsResponse)
async def get_unknown_words(
    category: Optional[str] = Query(None, description="Filter by category: 'high_frequency' or 'encounter'"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get unknown words (words user hasn't learned yet) grouped by category"""
    
    # Get all words user has learned (has UserWord entry)
    learned_word_ids = set(
        word_id[0] for word_id in 
        db.query(UserWord.word_id).filter(UserWord.user_id == current_user.id).all()
    )
    
    # Build query for unknown words
    query = db.query(Word).filter(
        ~Word.id.in_(learned_word_ids) if learned_word_ids else True
    )
    
    # Filter by category if provided. Grammar-verb rows (word_category="grammar")
    # are intentionally excluded — they're learned through grammar lessons, not
    # the word-bank flow, so they don't belong in either bucket.
    if category:
        query = query.filter(Word.word_category == category)
    else:
        query = query.filter(Word.word_category.in_(['high_frequency', 'encounter']))

    unknown_words = query.order_by(Word.frequency_rank.asc().nullslast(), Word.spanish.asc()).all()
    unknown_words = apply_alt_language(unknown_words, current_user.alt_language, db)

    # Group by category
    high_frequency = []
    encounter = []

    for word in unknown_words:
        word_data = UnknownWordSchema(
            id=word.id,
            word_id=word.id,
            spanish=word.spanish,
            english=word.english,
            word_category=word.word_category,
            frequency_rank=word.frequency_rank
        )

        if word.word_category == 'high_frequency':
            high_frequency.append(word_data)
        elif word.word_category == 'encounter':
            encounter.append(word_data)

    return UnknownWordsResponse(
        high_frequency=high_frequency,
        encounter=encounter,
    )