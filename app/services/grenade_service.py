"""Daily Grenade service.

A grenade = one word the user newly learned today that they're challenged to
deploy in a real-world conversation with a native speaker. Generated once per
day; recall (used yes/no) is recorded the next time the user shows up.
"""
from datetime import datetime, date, timedelta, timezone, time
from typing import Optional, List, Dict, Any
from uuid import UUID, uuid4
import logging

from sqlalchemy.orm import Session

from app.models import DailyGrenade, UserWord, Word, DailyEncounterLog
from app.services.llm_gateway import generate_conversation, ConversationContext

logger = logging.getLogger(__name__)


def _today_utc() -> date:
    return datetime.now(timezone.utc).date()


def _today_start_utc() -> datetime:
    return datetime.combine(_today_utc(), time.min, tzinfo=timezone.utc)


def first_lesson_done_today(db: Session, user_id) -> bool:
    """True if the user has consumed at least one daily encounter today (UTC)."""
    return (
        db.query(DailyEncounterLog)
        .filter(
            DailyEncounterLog.user_id == user_id,
            DailyEncounterLog.created_at >= _today_start_utc(),
        )
        .first()
        is not None
    )


def _audience_for(word: Word) -> str:
    return "merchant" if (word.word_type or "") == "noun" else "friend"


def pick_or_get_todays_grenade(db: Session, user_id) -> Optional[DailyGrenade]:
    """Return today's grenade for the user; create one if eligible.

    Selection: most recently learned word (mastery_level == 1, updated today).
    Verbs preferred over nouns over other types.
    """
    today = _today_utc()
    existing = (
        db.query(DailyGrenade)
        .filter(DailyGrenade.user_id == user_id, DailyGrenade.grenade_date == today)
        .first()
    )
    if existing:
        return existing

    today_start = _today_start_utc()
    rows = (
        db.query(UserWord, Word)
        .join(Word, UserWord.word_id == Word.id)
        .filter(
            UserWord.user_id == user_id,
            UserWord.mastery_level == 1,
            UserWord.updated_at >= today_start,
        )
        .all()
    )
    if not rows:
        return None

    rank = {"verb": 0, "noun": 1}
    rows.sort(key=lambda r: (rank.get(r[1].word_type or "", 2), -r[0].updated_at.timestamp()))
    uw, word = rows[0]

    surface = uw.last_seen_form or word.spanish
    grenade = DailyGrenade(
        id=uuid4(),
        user_id=user_id,
        grenade_date=today,
        user_word_id=word.id,
        word_id=word.id,
        surface_form=surface,
        audience=_audience_for(word),
    )
    db.add(grenade)
    db.commit()
    db.refresh(grenade)
    return grenade


_SYSTEM_PROMPT = (
    "You generate one-sentence Spanish yes/no questions for a Spanish learner "
    "to ask a native speaker in real life. The question must (1) use the target "
    "word in the form provided, (2) be answerable with sí or no, (3) be natural "
    "for the given audience, (4) be 12 words or fewer. "
    'Return JSON: {"sentence_es": "...", "sentence_en": "..."}.'
)


async def generate_sentence(db: Session, user_id, grenade: DailyGrenade) -> DailyGrenade:
    """Generate (or return cached) Spanish + English sentence for a grenade."""
    if grenade.sentence_es and grenade.sentence_en:
        return grenade

    word = db.query(Word).filter(Word.id == grenade.word_id).first()
    audience_label = "point-of-sale clerk / merchant" if grenade.audience == "merchant" else "friend"
    user_prompt = (
        f"Target word: {grenade.surface_form}\n"
        f"Audience: {audience_label}\n"
        f"Word context (don't echo): lemma={word.spanish if word else grenade.surface_form}, "
        f"type={word.word_type if word else 'unknown'}, "
        f"English={word.english if word else ''}\n"
        f"Generate the question."
    )

    ctx = ConversationContext(
        request_id=str(uuid4()),
        user_id=str(user_id),
        system_prompt=_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        agent_id="grenade_agent",
        return_json=True,
    )
    result = await generate_conversation(ctx, db)
    content = result["content"]
    if isinstance(content, dict):
        grenade.sentence_es = content.get("sentence_es") or ""
        grenade.sentence_en = content.get("sentence_en") or ""
    else:
        grenade.sentence_es = str(content)
        grenade.sentence_en = ""
    grenade.generated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(grenade)
    return grenade


def record_recall(db: Session, user_id, grenade_id: UUID, used: bool) -> Optional[DailyGrenade]:
    grenade = (
        db.query(DailyGrenade)
        .filter(DailyGrenade.id == grenade_id, DailyGrenade.user_id == user_id)
        .first()
    )
    if not grenade:
        return None
    grenade.used = used
    grenade.answered_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(grenade)
    return grenade


def get_prior_unanswered(db: Session, user_id) -> Optional[DailyGrenade]:
    """Most recent past (not today) grenade the user hasn't answered yet."""
    today = _today_utc()
    return (
        db.query(DailyGrenade)
        .filter(
            DailyGrenade.user_id == user_id,
            DailyGrenade.grenade_date < today,
            DailyGrenade.used.is_(None),
            DailyGrenade.sentence_es.isnot(None),
        )
        .order_by(DailyGrenade.grenade_date.desc())
        .first()
    )


def get_recent_grenades(db: Session, user_id, days: int = 14) -> List[Dict[str, Any]]:
    """Return a list of {date, status} for the last `days` days, oldest first.

    status: 'used' | 'missed' | 'pending' | 'none'
      - used: answered yes
      - missed: answered no
      - pending: grenade existed but no answer yet
      - none: no grenade that day
    """
    today = _today_utc()
    start = today - timedelta(days=days - 1)
    rows = (
        db.query(DailyGrenade)
        .filter(
            DailyGrenade.user_id == user_id,
            DailyGrenade.grenade_date >= start,
            DailyGrenade.grenade_date <= today,
        )
        .all()
    )
    by_date = {g.grenade_date: g for g in rows}
    result = []
    for i in range(days):
        d = start + timedelta(days=i)
        g = by_date.get(d)
        if g is None:
            status = "none"
        elif g.used is True:
            status = "used"
        elif g.used is False:
            status = "missed"
        else:
            status = "pending"
        result.append({"date": d.isoformat(), "status": status})
    return result
