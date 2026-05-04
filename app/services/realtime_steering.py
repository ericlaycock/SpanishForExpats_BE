"""Per-turn steering for the realtime voice-chat (Option C).

Replaces the v3 system prompt's static target_steering block. After each
user turn, `pick_next_target` consults the chip state on the Conversation
row and decides what to elicit next, with 2-turn stickiness so the LLM
gets two shots at landing the same target before we re-roll.

`build_meta_thought` formats that target into a short assistant turn the
FE injects via `conversation.item.create` (role=assistant) before firing
`response.create`. The model sees: "I planned to get them to say X, here's
how I'd do it" — and continues with the actual elicitation question.

This module is intentionally side-effect light: `pick_next_target`
mutates the Conversation row in memory but the caller commits.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from sqlalchemy.orm import Session

from app.models import Conversation


def _vocab_pending_forms(db: Session, conversation: Conversation) -> List[Dict[str, Any]]:
    """Build a chip-shaped form list for vocab encounters.

    Vocab Conversation rows don't have `chat_target_forms_json`; the chip
    state is the union of `target_word_ids` minus `used_spoken_word_ids`.
    Pull each missing word's spanish + english from the words table so
    `pick_next_target` can speak the same shape it does for grammar chats.
    """
    from app.models import Word

    targets = conversation.target_word_ids or []
    used = set(conversation.used_spoken_word_ids or [])
    missing_ids = [wid for wid in targets if wid not in used]
    if not missing_ids:
        return []
    rows = db.query(Word).filter(Word.id.in_(missing_ids)).all()
    by_id = {w.id: w for w in rows}
    out: List[Dict[str, Any]] = []
    for wid in missing_ids:
        w = by_id.get(wid)
        if not w or not w.spanish:
            continue
        out.append({
            "id": w.id,
            "spanish": w.spanish,
            "english": w.english or "",
        })
    return out


def _pending_forms(db: Session, conversation: Conversation) -> List[Dict[str, Any]]:
    """Pending chip forms for either grammar chat or vocab encounter.

    Grammar chats: filter `chat_target_forms_json` by `completed_chip_ids`.
    Vocab encounters: project `target_word_ids` − `used_spoken_word_ids`.
    """
    chat_forms = conversation.chat_target_forms_json or []
    if chat_forms:
        completed = set(conversation.completed_chip_ids or [])
        return [f for f in chat_forms if f.get("id") and f["id"] not in completed]
    return _vocab_pending_forms(db, conversation)


def reset_steering_if_landed(conversation: Conversation) -> None:
    """If the active steering target is now in completed_chip_ids /
    used_spoken_word_ids, clear the steering state so the next pick rolls
    a fresh target. Idempotent.
    """
    target_id = conversation.steering_target_id
    if not target_id:
        return
    completed = set(conversation.completed_chip_ids or [])
    used = set(conversation.used_spoken_word_ids or [])
    if target_id in completed or target_id in used:
        conversation.steering_target_id = None
        conversation.steering_target_age = 0


def pick_next_target(
    db: Session,
    conversation: Conversation,
    *,
    max_age_turns: int = 2,
) -> Tuple[Optional[str], Optional[Dict[str, Any]]]:
    """Pick the chip we want the model to elicit next.

    Returns `(target_id, target_form_dict)` or `(None, None)` if nothing
    pending. Mutates `conversation.steering_target_id` and
    `conversation.steering_target_age` in place; caller commits.

    Stickiness: if the existing `steering_target_id` is still pending and
    we've held it fewer than `max_age_turns` user turns, reuse it
    (incrementing age). Otherwise pick a fresh random pending form and
    set age=1.
    """
    pending = _pending_forms(db, conversation)
    if not pending:
        conversation.steering_target_id = None
        conversation.steering_target_age = 0
        return None, None

    sticky = next(
        (f for f in pending if f["id"] == conversation.steering_target_id),
        None,
    )
    age = conversation.steering_target_age or 0
    if sticky and age < max_age_turns:
        conversation.steering_target_age = age + 1
        return sticky["id"], sticky

    pick = random.choice(pending)
    conversation.steering_target_id = pick["id"]
    conversation.steering_target_age = 1
    return pick["id"], pick


def build_meta_thought(target_form: Dict[str, Any], language: str) -> str:
    """The assistant-role meta-thought we inject before `response.create`.

    The model treats this as a turn it just thought through, then
    generates the actual reply on the next `response.create`. The two
    examples lock the elicit-without-saying-the-form pattern.
    """
    spanish = (target_form.get("spanish") or "").strip()
    english = (target_form.get("english") or "").strip()
    return (
        f'The user must say "{spanish}" ({english}) next. I will ask them a '
        f"question in {language} that elicits it without me saying the form "
        f'myself. For example, if they needed to say "ustedes abren", I might '
        f'say "Es posible que nosotros abramos una botella de vino esta '
        f'noche." If they needed to say "gato", I might say "¿Tienes '
        f'mascotas?" I never say their target word myself. I will come up '
        f"with my response to them now."
    )
