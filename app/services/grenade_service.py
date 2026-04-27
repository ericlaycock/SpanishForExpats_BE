"""Grenade service — daily one-word real-world deployment challenge.

A grenade is a single Spanish word (verb conjugation, noun, or other) that the
user learned today and is challenged to deploy in conversation with a native
speaker. The next time the user opens the app, we ask whether they used the
prior grenade and feed that into a 14-day usage strip.

Selection: prefer verbs (more interesting deployments), then random.
Generation: GPT-4.1-mini via llm_gateway, JSON output {question_es, question_en}.
Recall: most-recent grenade with used IS NULL and a crafted question — no
expiry, so a 5-day gap still surfaces the grenade from 5 days ago.
"""
from __future__ import annotations

import logging
import random
import uuid
from datetime import date, datetime, timedelta, timezone
from typing import List, Optional, Tuple

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.models import Grenade, UserWord, Word
from app.schemas import GrenadeOut, GrenadeStripCell
from app.services.llm_gateway import ConversationContext, generate_conversation

logger = logging.getLogger(__name__)

STRIP_DAYS = 14


def _today_utc() -> date:
    return datetime.now(timezone.utc).date()


def _to_out(grenade: Grenade) -> GrenadeOut:
    return GrenadeOut(
        id=grenade.id,
        target_form=grenade.target_form,
        pos=grenade.pos,
        audience=grenade.audience,
        question_es=grenade.question_es,
        question_en=grenade.question_en,
        assigned_date=grenade.assigned_date.isoformat(),
        used=grenade.used,
    )


def get_or_pick_today(db: Session, user_id: uuid.UUID) -> Optional[Grenade]:
    """Return today's grenade, picking a fresh one if none exists.

    Selection: from words the user just learned today (mastery_level == 1,
    updated_at::date == today), prefer a verb. If no candidates, returns None.
    """
    today = _today_utc()

    existing = db.query(Grenade).filter(
        Grenade.user_id == user_id,
        Grenade.assigned_date == today,
    ).first()
    if existing:
        return existing

    # Find words the user just-learned today. We look at UserWord.updated_at
    # because UserWord has no created_at column; for words that were just
    # promoted from 0 → 1 by set_initial_mastery, updated_at ≈ first_seen_at.
    rows = (
        db.query(UserWord, Word)
        .join(Word, Word.id == UserWord.word_id)
        .filter(
            UserWord.user_id == user_id,
            UserWord.mastery_level == 1,
        )
        .all()
    )
    todays = [
        (uw, w) for (uw, w) in rows
        if uw.updated_at and uw.updated_at.astimezone(timezone.utc).date() == today
    ]
    if not todays:
        return None

    verbs = [pair for pair in todays if (pair[1].word_type == "verb")]
    pool = verbs if verbs else todays
    user_word, word = random.choice(pool)

    target_form = (user_word.last_seen_form or word.spanish).strip()
    grenade = Grenade(
        id=uuid.uuid4(),
        user_id=user_id,
        word_id=word.id,
        target_form=target_form,
        pos=word.word_type,
        assigned_date=today,
    )
    db.add(grenade)
    db.commit()
    db.refresh(grenade)
    return grenade


def find_pending_recall(db: Session, user_id: uuid.UUID) -> Optional[Grenade]:
    """Most recent grenade awaiting a yes/no answer.

    Only crafted grenades (question_es populated) and only those assigned
    before today qualify — today's grenade is shown via `today`, not as
    pending recall.
    """
    today = _today_utc()
    return (
        db.query(Grenade)
        .filter(
            Grenade.user_id == user_id,
            Grenade.used.is_(None),
            Grenade.assigned_date < today,
            Grenade.question_es.isnot(None),
        )
        .order_by(Grenade.assigned_date.desc())
        .first()
    )


def build_strip(db: Session, user_id: uuid.UUID) -> List[GrenadeStripCell]:
    """14-day strip ending today (oldest → newest).

    Cell states:
      - 'used'    — grenade existed and user confirmed deployment
      - 'missed'  — grenade existed and user said no
      - 'pending' — today's grenade exists but isn't yet answered (only today)
      - 'none'    — no grenade that day (or uncrafted, or unanswered past day)
    """
    today = _today_utc()
    start = today - timedelta(days=STRIP_DAYS - 1)

    rows = (
        db.query(Grenade)
        .filter(
            Grenade.user_id == user_id,
            Grenade.assigned_date >= start,
            Grenade.assigned_date <= today,
        )
        .all()
    )
    by_date = {g.assigned_date: g for g in rows}

    cells: List[GrenadeStripCell] = []
    for offset in range(STRIP_DAYS):
        d = start + timedelta(days=offset)
        g = by_date.get(d)
        if g is None or g.question_es is None:
            # No grenade, or never crafted — render as empty regardless of day.
            state: str = "pending" if (d == today and g is not None) else "none"
        elif g.used is True:
            state = "used"
        elif g.used is False:
            state = "missed"
        else:
            state = "pending" if d == today else "none"
        cells.append(GrenadeStripCell(date=d.isoformat(), state=state))  # type: ignore[arg-type]
    return cells


# ── LLM generation ────────────────────────────────────────────────────────────

_GRENADE_SYSTEM_PROMPT = """\
You craft one-sentence Spanish questions a beginner can drop into a real
conversation as an OPENER — out of the blue, with no shared prior context
between the speakers.

You will be given a Spanish target word (sometimes a conjugated verb form,
sometimes a noun) and an audience. Output a JSON object with exactly two keys:
  - "question_es": a single natural Spanish question (≤ 15 words) that
    organically uses the EXACT target form. Yes/no or open-ended both fine.
    Do not paraphrase the target form. If a conjugation was given, keep the
    conjugation — do not retreat to the infinitive.
  - "question_en": a faithful English translation of question_es.

CRITICAL — the question must work as a conversation starter:
- A stranger or someone you just sat down with must be able to answer it
  WITHOUT any prior context. Imagine bumping into someone at a café or
  approaching a shopkeeper for the first time.
- Forbidden: referential pronouns or possessives that depend on context the
  listener doesn't have. Bad examples (DO NOT generate these patterns):
    * "¿Son sus llaves?" / "Are those his/her/your keys?"
    * "¿Es tu perro?" / "Is that your dog?"  (assumes a visible animal)
    * "¿Te gusta esto?" / "Do you like this?"  (esto = unknown referent)
    * "¿Vives aquí?" / "Do you live here?"  (aquí needs a shared location)
    * Anything with "ese / esa / eso / esto / aquí / allí / él / ella" as
      the subject when the listener has no idea what's being pointed to.
- Prefer general / hypothetical / habitual / preference / opinion framings:
    * "¿Tienes perro?" / "Do you have a dog?"
    * "¿Vas mucho a la playa?" / "Do you go to the beach a lot?"
    * "¿Comes carne?" / "Do you eat meat?"
    * "¿Viajas por trabajo?" / "Do you travel for work?"
    * "¿Prefieres té o café?" / "Do you prefer tea or coffee?"
- For nouns, ask about the listener's relationship to the noun in general
  (do you have one, do you like them, how often, etc.), NOT about a specific
  one in front of you.
- For verbs (already conjugated for a pronoun), the conjugation tells you
  the subject. If "comes" (you eat informal), ask the listener directly:
  "¿Comes pescado?". If "come" (he/she eats), ask about a hypothetical 3rd
  person you might both know about: "¿Tu hermano come pescado?".

Audience rules:
- "friend" → casual tú register, conversational tone.
- "merchant" → polite usted register, framed for a shop, market, café, or
  checkout. Still must work as a cold open with the merchant.

Output JSON only — no commentary, examples, or extra fields.
"""


def _build_user_prompt(target_form: str, pos: Optional[str], audience: str) -> str:
    pos_label = pos or "word"
    return (
        f"Target form: {target_form}\n"
        f"Part of speech: {pos_label}\n"
        f"Audience: {audience}\n\n"
        f"Return JSON: {{\"question_es\": \"...\", \"question_en\": \"...\"}}."
    )


async def generate_question(
    db: Session,
    grenade: Grenade,
    audience: str,
    request_id: str,
) -> Grenade:
    """Fill grenade.question_es/question_en/audience via LLM.

    Always regenerates when called — the FE only hits this endpoint on
    explicit user action ("Make a grenade" / "Re-craft" buttons), so a
    short-circuit on unchanged audience would silently no-op the
    re-craft button (which was the bug).
    """
    user_prompt = _build_user_prompt(grenade.target_form, grenade.pos, audience)
    context = ConversationContext(
        request_id=request_id,
        user_id=str(grenade.user_id),
        system_prompt=_GRENADE_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        agent_id="grenade_agent",
        prompt_version="v2",
        return_json=True,
        # Crank temperature for variety — Re-craft should produce a notably
        # different question on each tap, not a near-identical rephrasing.
        temperature=1.5,
    )
    result = await generate_conversation(context, db)
    content = result.get("content")
    if not isinstance(content, dict):
        raise ValueError(f"grenade LLM returned non-dict content: {content!r}")

    question_es = (content.get("question_es") or "").strip()
    question_en = (content.get("question_en") or "").strip()
    if not question_es or not question_en:
        raise ValueError(f"grenade LLM missing fields: {content!r}")

    grenade.question_es = question_es
    grenade.question_en = question_en
    grenade.audience = audience
    db.commit()
    db.refresh(grenade)
    return grenade


def record_recall(
    db: Session,
    user_id: uuid.UUID,
    grenade_id: uuid.UUID,
    used: bool,
) -> Grenade:
    grenade = (
        db.query(Grenade)
        .filter(Grenade.id == grenade_id, Grenade.user_id == user_id)
        .first()
    )
    if grenade is None:
        raise LookupError("Grenade not found")
    grenade.used = used
    grenade.answered_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(grenade)
    return grenade


def build_today_response(
    db: Session,
    user_id: uuid.UUID,
) -> Tuple[Optional[Grenade], Optional[Grenade], List[GrenadeStripCell]]:
    """Bundled accessor for the GET /today endpoint."""
    today = get_or_pick_today(db, user_id)
    pending = find_pending_recall(db, user_id)
    strip = build_strip(db, user_id)
    return today, pending, strip


__all__ = [
    "build_strip",
    "build_today_response",
    "find_pending_recall",
    "generate_question",
    "get_or_pick_today",
    "record_recall",
    "STRIP_DAYS",
]
