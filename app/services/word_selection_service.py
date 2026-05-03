from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert
from app.models import Word, Situation, SituationWord, UserWord
from typing import List, Optional, Set, Tuple


# Cold-start vocab-level floor by q0_spanish_level. The DB-tracked VL is the
# count of mastered HF words; brand-new users have VL=0 regardless of how
# much Spanish they actually know. Without this floor a self-reported
# advanced user gets the same first 2 HF words as a true beginner.
_LEVEL_VL_FLOOR = {"a": 5, "b": 25, "c": 60, "d": 100}

# How wide a band around the user's VL to search for fresh HF words.
# `LOW` clamps to >= 1 so we never cycle back to negative ranks.
_HF_BAND_LOW = 50
_HF_BAND_HIGH = 100


def get_learned_word_ids(db: Session, user_id) -> Set[str]:
    """Get set of word IDs the user has already encountered."""
    return {
        row[0] for row in
        db.query(UserWord.word_id).filter(UserWord.user_id == user_id).all()
    }


def select_words_for_grammar_situation(
    db: Session,
    situation_id: str,
) -> Tuple[List[str], List[str]]:
    """Select all words for a grammar situation (no high-freq onboarding).

    Returns (grammar_word_ids, []) — empty list for high-freq to match interface.
    """
    situation_words = db.query(SituationWord).filter(
        SituationWord.situation_id == situation_id
    ).order_by(SituationWord.position).all()
    grammar_word_ids = [sw.word_id for sw in situation_words]
    return grammar_word_ids, []


def _resolve_effective_vl(vocab_level: int, spanish_level: Optional[str]) -> int:
    """Floor the user's effective VL by their self-reported level.

    Brand-new users have DB-tracked `vocab_level == 0` regardless of how
    much Spanish they actually know. Without this floor, a self-reported
    advanced learner ('d') gets the same first 2 HF words as an absolute
    beginner ('a'). Once they earn a real VL the DB number wins.
    """
    if vocab_level > 0:
        return vocab_level
    if not spanish_level:
        return 0
    return _LEVEL_VL_FLOOR.get(spanish_level.lower(), 0)


def select_words_for_situation(
    db: Session,
    user_id,
    situation_id: str,
    encounter_limit: int = 3,
    high_freq_limit: int = 2,
    *,
    vocab_level: int = 0,
    spanish_level: Optional[str] = None,
) -> Tuple[List[str], List[str]]:
    """Select encounter + high-frequency words for a situation.

    Returns (encounter_word_ids, high_freq_word_ids).
    For grammar situations, returns all grammar words with no high-freq.

    HF selection prefers words near the learner's vocab level (within a
    [VL-50, VL+100] band) so beginners don't drown in obscure top-1000
    words and advanced learners don't get given vocabulary they already
    know. Falls back to the global frequency-rank order when the band
    doesn't yield enough candidates — never starves a user of HF words.
    """
    situation = db.query(Situation).filter(Situation.id == situation_id).first()
    if situation and situation.situation_type == 'grammar':
        return select_words_for_grammar_situation(db, situation_id)

    situation_words = db.query(SituationWord).filter(
        SituationWord.situation_id == situation_id
    ).order_by(SituationWord.position).limit(encounter_limit).all()
    encounter_word_ids = [sw.word_id for sw in situation_words]

    learned_word_ids = get_learned_word_ids(db, user_id)
    base_filter = [
        Word.word_category == "high_frequency",
    ]
    if learned_word_ids:
        base_filter.append(~Word.id.in_(learned_word_ids))

    effective_vl = _resolve_effective_vl(vocab_level, spanish_level)

    high_freq_words: list[Word] = []
    if effective_vl > 0:
        band_low = max(1, effective_vl - _HF_BAND_LOW)
        band_high = effective_vl + _HF_BAND_HIGH
        high_freq_words = (
            db.query(Word)
            .filter(
                *base_filter,
                Word.frequency_rank.isnot(None),
                Word.frequency_rank >= band_low,
                Word.frequency_rank <= band_high,
            )
            .order_by(Word.frequency_rank.asc())
            .limit(high_freq_limit)
            .all()
        )

    if len(high_freq_words) < high_freq_limit:
        already_picked = {w.id for w in high_freq_words}
        backfill = (
            db.query(Word)
            .filter(
                *base_filter,
                ~Word.id.in_(already_picked) if already_picked else True,
            )
            .order_by(Word.frequency_rank.asc().nullslast())
            .limit(high_freq_limit - len(high_freq_words))
            .all()
        )
        high_freq_words.extend(backfill)

    high_freq_word_ids = [w.id for w in high_freq_words]
    return encounter_word_ids, high_freq_word_ids


def sort_words_encounter_first(
    words: List[Word],
    situation_id: str,
    db: Session,
    target_word_ids: List[str],
) -> List[Word]:
    """Sort words: encounter words by position first, then high-frequency."""
    word_dict = {w.id: w for w in words}
    situation_words = db.query(SituationWord).filter(
        SituationWord.situation_id == situation_id
    ).order_by(SituationWord.position).all()
    encounter_word_ids = {sw.word_id for sw in situation_words}

    sorted_encounter = [word_dict[sw.word_id] for sw in situation_words if sw.word_id in word_dict]
    sorted_high_freq = [word_dict[wid] for wid in target_word_ids if wid not in encounter_word_ids and wid in word_dict]

    return sorted_encounter + sorted_high_freq


def ensure_user_words(db: Session, user_id, words: List[Word]) -> None:
    """Create UserWord entries if they don't exist, increment seen_count."""
    for word in words:
        stmt = insert(UserWord).values(
            user_id=user_id,
            word_id=word.id,
            seen_count=1,
        ).on_conflict_do_update(
            index_elements=["user_id", "word_id"],
            set_={"seen_count": UserWord.seen_count + 1},
        )
        db.execute(stmt)
