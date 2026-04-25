from datetime import datetime, timedelta, timezone
from typing import Optional, List, Dict
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import UserWord, Situation, Word


# Intervals: after reaching level N, next refresh is due in this many time
SRS_INTERVALS = {
    1: timedelta(hours=24),
    2: timedelta(days=7),
    3: timedelta(days=30),
}


def get_next_refresh_at(mastery_level: int) -> Optional[datetime]:
    """Return the next refresh datetime for a given mastery level, or None if done."""
    interval = SRS_INTERVALS.get(mastery_level)
    if interval is None:
        return None
    return datetime.now(timezone.utc) + interval


def set_initial_mastery(
    db: Session,
    user_id,
    word_ids: List[str],
    situation_id: str,
) -> None:
    """Set words from level 0 → level 1 after a lesson is completed."""
    next_refresh = datetime.now(timezone.utc) + SRS_INTERVALS[1]

    db.query(UserWord).filter(
        UserWord.user_id == user_id,
        UserWord.word_id.in_(word_ids),
        UserWord.mastery_level == 0,
    ).update(
        {
            UserWord.mastery_level: 1,
            UserWord.next_refresh_at: next_refresh,
            UserWord.source_situation_id: situation_id,
            UserWord.status: "learning",
        },
        synchronize_session="fetch",
    )
    # Seed last_seen_form with the lemma for any UserWord still missing one.
    # Grammar/voice flows may overwrite with the actual conjugated form later.
    word_rows = db.query(Word).filter(Word.id.in_(word_ids)).all()
    lemma_by_id = {w.id: w.spanish for w in word_rows}
    db.query(UserWord).filter(
        UserWord.user_id == user_id,
        UserWord.word_id.in_(word_ids),
        UserWord.last_seen_form.is_(None),
    ).all()
    for wid, lemma in lemma_by_id.items():
        db.query(UserWord).filter(
            UserWord.user_id == user_id,
            UserWord.word_id == wid,
            UserWord.last_seen_form.is_(None),
        ).update({UserWord.last_seen_form: lemma}, synchronize_session=False)
    db.flush()


def get_pending_refreshes(db: Session, user_id) -> List[Dict]:
    """Return situations that have words due for refresh, grouped by source_situation_id."""
    now = datetime.now(timezone.utc)

    rows = (
        db.query(
            UserWord.source_situation_id,
            func.count(UserWord.word_id).label("due_count"),
        )
        .filter(
            UserWord.user_id == user_id,
            UserWord.next_refresh_at <= now,
            UserWord.mastery_level < 4,
            UserWord.source_situation_id.isnot(None),
        )
        .group_by(UserWord.source_situation_id)
        .all()
    )

    if not rows:
        return []

    situation_ids = [r.source_situation_id for r in rows]
    situations = {
        s.id: s
        for s in db.query(Situation).filter(Situation.id.in_(situation_ids)).all()
    }

    result = []
    for row in rows:
        sit = situations.get(row.source_situation_id)
        if sit:
            result.append({
                "situation_id": sit.id,
                "title": sit.title,
                "animation_type": sit.animation_type,
                "due_word_count": row.due_count,
            })

    return result


def get_due_word_ids(db: Session, user_id, situation_id: str) -> List[str]:
    """Get word IDs due for refresh for a specific situation."""
    now = datetime.now(timezone.utc)
    rows = (
        db.query(UserWord.word_id)
        .filter(
            UserWord.user_id == user_id,
            UserWord.source_situation_id == situation_id,
            UserWord.next_refresh_at <= now,
            UserWord.mastery_level < 4,
        )
        .all()
    )
    return [r.word_id for r in rows]


def bump_mastery_after_refresh(db: Session, user_id, situation_id: str) -> tuple[int, int]:
    """Bump mastery level for all due words in a situation. Returns (count, new_level)."""
    now = datetime.now(timezone.utc)

    words = (
        db.query(UserWord)
        .filter(
            UserWord.user_id == user_id,
            UserWord.source_situation_id == situation_id,
            UserWord.next_refresh_at <= now,
            UserWord.mastery_level < 4,
        )
        .with_for_update()
        .all()
    )

    if not words:
        return 0, 0

    new_level = words[0].mastery_level + 1
    for word in words:
        word.mastery_level = new_level
        word.next_refresh_at = get_next_refresh_at(new_level)
        if new_level >= 4:
            word.status = "mastered"
            word.next_refresh_at = None

    db.flush()
    return len(words), new_level
