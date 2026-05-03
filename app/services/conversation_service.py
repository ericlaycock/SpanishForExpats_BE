import logging
import re
import unicodedata
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert
from app.models import Conversation, UserWord, Word
from typing import Iterable, List, Tuple

logger = logging.getLogger(__name__)


def _normalize_for_match(text: str) -> str:
    """Lowercase + strip punctuation + drop diacritics for chip matching.

    Mirrors `app/services/word_detection.normalize_text` so chip detection
    treats accents and casing the same way the per-verb infinitive
    detection does. Kept private here because it has one consumer
    (`check_chat_chip_completion`) and importing the public version
    would create a circular import on this module.
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return text


def check_conversation_complete(conversation: Conversation, mode: str) -> bool:
    """Check if conversation is complete based on mode"""
    if mode == "text":
        used_word_ids = set(conversation.used_typed_word_ids or [])
    else:  # voice
        used_word_ids = set(conversation.used_spoken_word_ids or [])
    
    target_word_ids = set(conversation.target_word_ids or [])
    
    return target_word_ids.issubset(used_word_ids)


def update_user_word_stats(
    db: Session,
    user_id: str,
    word_ids: List[str],
    mode: str
):
    """Update user word statistics.

    Defensively filters out any word_ids that don't exist in the `words` table
    to avoid FK violations on `user_words.word_id_fkey`. Unknown ids are
    logged and silently skipped — callers should not need to pre-validate.
    """
    if not word_ids:
        db.commit()
        return

    known_ids = {
        row[0] for row in db.query(Word.id).filter(Word.id.in_(word_ids)).all()
    }
    unknown_ids = [w for w in word_ids if w not in known_ids]
    if unknown_ids:
        logger.warning(
            "update_user_word_stats: skipping unknown word_ids %s for user %s (mode=%s)",
            unknown_ids, user_id, mode,
        )
    word_ids = [w for w in word_ids if w in known_ids]

    for word_id in word_ids:
        if mode == "text":
            stmt = insert(UserWord).values(
                user_id=user_id,
                word_id=word_id,
                seen_count=1,
                typed_correct_count=1,
                spoken_correct_count=0,
                status="learning"
            ).on_conflict_do_update(
                index_elements=["user_id", "word_id"],
                set_={"typed_correct_count": UserWord.typed_correct_count + 1}
            )
            db.execute(stmt)
        else:  # voice
            stmt = insert(UserWord).values(
                user_id=user_id,
                word_id=word_id,
                seen_count=1,
                typed_correct_count=0,
                spoken_correct_count=1,
                status="learning"
            ).on_conflict_do_update(
                index_elements=["user_id", "word_id"],
                set_={"spoken_correct_count": UserWord.spoken_correct_count + 1}
            )
            db.execute(stmt)

    db.commit()


def get_missing_word_ids(conversation: Conversation, mode: str) -> List[str]:
    """Get list of word IDs that haven't been used yet"""
    if mode == "text":
        used_word_ids = set(conversation.used_typed_word_ids or [])
    else:  # voice
        used_word_ids = set(conversation.used_spoken_word_ids or [])

    target_word_ids = set(conversation.target_word_ids or [])
    missing = target_word_ids - used_word_ids

    return list(missing)


def check_chat_chip_completion(
    conversation: Conversation,
    user_transcripts: Iterable[str],
) -> Tuple[bool, List[str]]:
    """Per-chip completion check for grammar `*_chat` lessons.

    Vocab encounters and non-chat grammar lessons keep the legacy
    `check_conversation_complete` path (`target_word_ids` ⊆
    `used_spoken_word_ids`). Chat lessons need finer granularity: the FE
    shows a sample of 8 (verb, pronoun) chips and the conversation
    should not complete until each chip has actually been uttered. The
    server-side snapshot of those chips lives in
    `Conversation.chat_target_forms_json`; we scan the user's full
    transcript log for each chip's exact `spanish` form (word-boundary,
    accent-insensitive) and report which chip ids are now ticked.

    Returns `(complete, completed_chip_ids)`. `complete` is True only
    when every chip has been ticked. Returns `(False, [])` when the
    conversation has no chip snapshot — caller should fall back to the
    legacy completion check.
    """
    chips = conversation.chat_target_forms_json or []
    if not chips:
        return False, []

    haystack = " ".join(_normalize_for_match(t or "") for t in user_transcripts)
    if not haystack:
        return False, []

    completed: List[str] = []
    for chip in chips:
        spanish = chip.get("spanish") or ""
        # Persistence stores the FE chip id alongside the form so the BE
        # never has to synthesize one. Fall back to `form:{spanish}:{pronoun}`
        # for older rows that pre-date the id field — same convention the
        # FE uses in ImmersiveVoiceScene.applyDetectedWords.
        chip_id = chip.get("id") or chip.get("chip_id")
        if not chip_id and spanish:
            pronoun = chip.get("pronoun") or ""
            chip_id = f"form:{spanish}:{pronoun}"
        if not spanish or not chip_id:
            continue
        normalized = _normalize_for_match(spanish)
        if not normalized:
            continue
        if " " in normalized:
            if normalized in haystack:
                completed.append(chip_id)
        else:
            pattern = r"\b" + re.escape(normalized) + r"\b"
            if re.search(pattern, haystack):
                completed.append(chip_id)

    complete = len(completed) == len(chips)
    return complete, completed



