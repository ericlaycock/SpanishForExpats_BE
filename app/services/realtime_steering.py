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
    max_age_turns: int = 1,
) -> Tuple[Optional[str], Optional[Dict[str, Any]]]:
    """Pick the chip we want the model to elicit next.

    Returns `(target_id, target_form_dict)` or `(None, None)` if nothing
    pending. Mutates `conversation.steering_target_id` and
    `conversation.steering_target_age` in place; caller commits.

    Stickiness: if the existing `steering_target_id` is still pending and
    we've held it fewer than `max_age_turns` user turns, reuse it
    (incrementing age). Otherwise pick a fresh random pending form and
    set age=1. Default `max_age_turns=1` — every user turn rolls a fresh
    target unless the previous turn's pick is still pending and we want
    a single retry.
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


# Pronoun → (instruction-pronoun, template) map for the per-turn
# response.instructions override. The model uses the *flipped* pronoun's
# form so the user is forced into producing the chip's form to respond.
# {form} substitutes the conjugated verb in the flipped pronoun.
_BREVITY_TAG = " Keep it 2 short sentences max in simple Spanish."

_PRONOUN_INSTRUCTIONS: Dict[str, tuple[str, str]] = {
    "yo": (
        "tú",
        "Ask the user a relevant question with \"{form}\" in your question."
        + _BREVITY_TAG,
    ),
    "tú": (
        "yo",
        "Connecting with what the user just said, share how you "
        "\"{form}\", and ask for the user's opinion." + _BREVITY_TAG,
    ),
    "usted": (
        "yo",
        "Connecting with what the user just said, share how you "
        "\"{form}\", and ask for the user's opinion." + _BREVITY_TAG,
    ),
    "nosotros": (
        "ustedes",
        "Ask the user a relevant question using the verb \"{form}\" about "
        "something they and a friend/family member do." + _BREVITY_TAG,
    ),
    "nosotras": (
        "ustedes",
        "Ask the user a relevant question using the verb \"{form}\" about "
        "something they and a friend/family member do." + _BREVITY_TAG,
    ),
    "ustedes": (
        "nosotros",
        "Connecting with what the user just said, share how you + a close "
        "family member/friend \"{form}\" and ask for the user's opinion."
        + _BREVITY_TAG,
    ),
    # Third-person targets: model speaks ABOUT a third party using the
    # SAME pronoun, so the user mirrors back the same conjugation.
    "él": (
        "él",
        "Connecting with what the user just said, state an opinion (or ask "
        "a question) about a male person/thing doing \"{form}\"."
        + _BREVITY_TAG,
    ),
    "ella": (
        "ella",
        "Connecting with what the user just said, state an opinion (or ask "
        "a question) about a female person/thing doing \"{form}\"."
        + _BREVITY_TAG,
    ),
    "ellos": (
        "ellos",
        "Connecting with what the user just said, state an opinion (or ask "
        "a question) about a male person/thing doing \"{form}\"."
        + _BREVITY_TAG,
    ),
    "ellas": (
        "ellas",
        "Connecting with what the user just said, state an opinion (or ask "
        "a question) about a female person/thing doing \"{form}\"."
        + _BREVITY_TAG,
    ),
}


def build_response_instructions(target_form: Dict[str, Any]) -> Optional[str]:
    """Per-turn response.instructions override for the realtime steering.

    Maps the chip's pronoun to a flipped pronoun + template, looks up the
    flipped conjugation via grammar_situations.find_grammar_form, and
    returns the rendered instruction. Returns None when:
      - target lacks pronoun/verb metadata (vocab encounter, no override)
      - the pronoun isn't in our flip map
      - find_grammar_form can't resolve the flipped (verb, pronoun) pair

    Caller should fall through to firing response.create with no
    instructions in those cases.
    """
    from app.data.grammar_situations import find_grammar_form

    pronoun = target_form.get("pronoun")
    verb = target_form.get("verb")
    if not pronoun or not verb:
        return None
    rule = _PRONOUN_INSTRUCTIONS.get(pronoun)
    if not rule:
        return None
    flipped_pronoun, template = rule
    flipped_form = find_grammar_form(verb, flipped_pronoun)
    if not flipped_form:
        return None
    return template.format(form=flipped_form)


def build_meta_thought(target_form: Dict[str, Any], language: str) -> str:
    """The assistant-role meta-thought we inject before `response.create`.

    Heavier on examples of person-flipping (1st ↔ 2nd, plural ↔ singular)
    so the model learns the elicitation pattern: never produce the target
    form yourself, instead say a related form in a different person to
    bait the user into saying theirs.
    """
    spanish = (target_form.get("spanish") or "").strip()
    return (
        f'The user must say "{spanish}" next. I will ask them a question in '
        f"{language} that elicits it without me saying the form myself. For "
        f'example, if they needed to say "ustedes abren", I might say "Es '
        f'cierto que nosotros abremos una botella de vino esta noche." If '
        f'they needed to say "gato", I might say "¿Tienes mascotas?". If '
        f'they need to say "yo escribo", I might say "escribes a menudo?" '
        f'If they need to say "You write", I would say "Sabes, me gusta '
        f'escribir." -> this invites them to ask me a follow-up question. I '
        f"never say their target word myself - I FLIP between 1st/2nd "
        f"person plural to get them to say the right person. I will come up "
        f"with my response to them now."
    )
