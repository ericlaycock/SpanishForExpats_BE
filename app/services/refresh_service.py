import random
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


def _pick_grammar_form(word_spanish: str, situation_id: str) -> Optional[str]:
    """Pick a representative conjugated form for a grammar-lesson verb.

    Drives the daily Grenade so a user who just drilled "hablar" gets a
    deployable form like "hablas" / "habla" / "hablamos" rather than the bare
    infinitive. Prefers non-masculine, non-default pronouns to keep grenades
    varied across ella/ellas/nosotras/usted/ustedes (matches the project-wide
    pronoun-diversity preference).

    Returns None if no grammar config / no answers / no drill_targets — caller
    should fall back to the lemma.
    """
    from app.data.grammar_situations import get_grammar_config

    config = get_grammar_config(situation_id) or {}
    answers = (config.get("drill_config") or {}).get("answers") or {}
    forms_for_verb: Dict[str, str] = answers.get(word_spanish) or {}
    if not forms_for_verb:
        return None

    # Bias toward varied pronouns — matches the diversity preference for
    # generated grammar content. Falls back to whatever the verb has.
    preferred = ["ella", "ellas", "nosotras", "usted", "ustedes", "tú", "yo"]
    drill_targets = config.get("drill_targets") or []
    drilled_pronouns = [t.get("pronoun") for t in drill_targets if t.get("verb") == word_spanish]
    candidate_pronouns = [p for p in preferred if p in drilled_pronouns and forms_for_verb.get(p)]
    if not candidate_pronouns:
        # Use any drilled pronoun the verb actually has a form for.
        candidate_pronouns = [p for p in drilled_pronouns if forms_for_verb.get(p)]
    if not candidate_pronouns:
        candidate_pronouns = [p for p in forms_for_verb.keys()]
    chosen = random.choice(candidate_pronouns)
    return forms_for_verb.get(chosen)


def set_initial_mastery(
    db: Session,
    user_id,
    word_ids: List[str],
    situation_id: str,
) -> None:
    """Set words from level 0 → level 1 after a lesson is completed.

    Also seeds `last_seen_form` so the daily Grenade can deploy the conjugated
    form the user drilled (for grammar verbs) rather than a bare infinitive.
    Non-verbs and non-grammar contexts default to the lemma.
    """
    next_refresh = datetime.now(timezone.utc) + SRS_INTERVALS[1]

    rows = (
        db.query(UserWord, Word)
        .join(Word, Word.id == UserWord.word_id)
        .filter(
            UserWord.user_id == user_id,
            UserWord.word_id.in_(word_ids),
            UserWord.mastery_level == 0,
        )
        .with_for_update(of=UserWord)
        .all()
    )

    for user_word, word in rows:
        form: Optional[str] = None
        if word.word_type == "verb":
            form = _pick_grammar_form(word.spanish, situation_id)
        if not form:
            form = word.spanish

        user_word.mastery_level = 1
        user_word.next_refresh_at = next_refresh
        user_word.source_situation_id = situation_id
        user_word.status = "learning"
        user_word.last_seen_form = form

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
