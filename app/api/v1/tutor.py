from fastapi import APIRouter, Depends, HTTPException, Query, Header
from sqlalchemy.orm import Session
from collections import defaultdict
from app.database import get_db
from app.models import User, UserWord, UserSituation, Word

router = APIRouter()

TUTOR_CODE = "223401"


@router.get("/student")
async def get_student_progress(
    email: str = Query(..., description="Student email address"),
    x_tutor_code: str = Header(..., alias="X-Tutor-Code"),
    db: Session = Depends(get_db),
):
    """Tutor-only: get a student's word mastery and grammar progress."""
    if x_tutor_code != TUTOR_CODE:
        raise HTTPException(status_code=403, detail="Invalid tutor code")

    user = db.query(User).filter(User.email == email.strip().lower()).first()
    if not user:
        raise HTTPException(status_code=404, detail="Student not found")

    # Vocab & grammar level
    from app.api.v1.situations import get_vocab_level, get_grammar_level
    vocab_level = get_vocab_level(db, user.id)
    grammar_level = get_grammar_level(db, user.id)

    # Words grouped by mastery level
    user_words = (
        db.query(UserWord, Word)
        .join(Word, UserWord.word_id == Word.id)
        .filter(UserWord.user_id == user.id)
        .order_by(Word.spanish)
        .all()
    )

    words_by_level = defaultdict(list)
    for uw, w in user_words:
        words_by_level[uw.mastery_level].append({
            "spanish": w.spanish,
            "english": w.english,
            "word_category": w.word_category,
            "next_refresh_at": uw.next_refresh_at.isoformat() if uw.next_refresh_at else None,
        })

    # Grammar progress
    from app.data.grammar_situations import GRAMMAR_SITUATIONS, GL_TITLES, GL_SORTED, get_situations_for_gl

    completed_situation_ids = {
        us.situation_id
        for us in db.query(UserSituation).filter(
            UserSituation.user_id == user.id,
            UserSituation.completed_at.isnot(None),
        ).all()
    }

    grammar_levels = []
    for gl in GL_SORTED:
        lessons = get_situations_for_gl(gl)
        if not lessons:
            continue
        completed_lessons = [sid for sid in lessons if sid in completed_situation_ids]
        grammar_levels.append({
            "level": gl,
            "title": GL_TITLES.get(gl, f"Level {gl}"),
            "total_lessons": len(lessons),
            "completed_lessons": len(completed_lessons),
            "completed_ids": completed_lessons,
        })

    return {
        "email": user.email,
        "created_at": user.created_at.isoformat() if user.created_at else None,
        "vocab_level": vocab_level,
        "grammar_level": grammar_level,
        "words": {str(k): v for k, v in sorted(words_by_level.items(), reverse=True)},
        "grammar": grammar_levels,
    }
