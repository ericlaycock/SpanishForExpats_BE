import logging
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert
from app.models import Conversation, UserWord, Word
from typing import List

logger = logging.getLogger(__name__)


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



