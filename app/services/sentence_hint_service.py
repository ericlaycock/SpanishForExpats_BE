"""Sentence-hint generation for the /voice-chat "Need help?" button.

The FE asks the BE for a single short Spanish sentence the learner could
say next, using 1 or 2 items they haven't completed yet (vocab words for
non-grammar encounters, conjugation chips for grammar encounters). The
result is rendered in the avatar's speech bubble; the FE owns the
display.

Per-conversation cap (5 hints) lives on the conversation row
(`sentence_hints_used`); this module is concerned with assembling the
candidate item list, calling the LLM, synthesizing TTS, and persisting
the audit row in `sentence_hints`. The endpoint orchestrates the cap
check, the increment, and the response shape.

Grammar nuance: BE doesn't know which specific `(verb, pronoun)` chips
the user has already ticked — only the FE does, since detection happens
on the conjugated form. We therefore expose ALL drill_targets whose
verb is still in `missing_word_ids` (i.e., the infinitive isn't mastered
in this conversation yet) and let the LLM pick 1–2. Worst case the model
suggests a (verb, pronoun) chip the user already said; we never suggest
items for an already-mastered verb.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from sqlalchemy.orm import Session

from app.models import Conversation, SentenceHint
from app.services.alt_language_service import apply_alt_language
from app.services.conversation_service import get_missing_word_ids
from app.services.llm_gateway import ConversationContext, generate_conversation
from app.services.word_detection import get_words_by_ids

logger = logging.getLogger(__name__)


# Cap enforced at the endpoint; surfaced here for tests to import.
SENTENCE_HINT_CAP_PER_CONVERSATION = 5

# Anything beyond this many candidate items gets truncated to keep the
# prompt small and the LLM focused. The cap is generous enough to cover
# every realistic vocab + grammar encounter.
MAX_CANDIDATE_ITEMS = 12


@dataclass
class PendingItem:
    """Candidate item the LLM may use in the suggested sentence.

    `kind` discriminates between vocab and grammar items; `id` is the FE
    chip id (vocab `word_*` or grammar `conj_<verb>_<pronoun>`); the
    optional fields are populated per-kind for the prompt.
    """
    kind: str  # "vocab" | "grammar"
    id: str
    spanish: str
    english: str
    # grammar-only
    verb: Optional[str] = None
    pronoun: Optional[str] = None
    conjugated: Optional[str] = None


def compute_pending_items(
    db: Session,
    conversation: Conversation,
    alt_language: Optional[str],
) -> List[PendingItem]:
    """Build the candidate item list for the hint prompt.

    Vocab path: take `missing_word_ids`, hydrate via `get_words_by_ids`,
    apply alt-language swap so `spanish` reflects what the chip actually
    shows (catalan/swedish swaps).

    Grammar path: for each drill_target whose verb is still missing, emit
    one candidate per `(verb, pronoun)` with the conjugated form pulled
    from `drill_config.answers`.
    """
    from app.data.grammar_situations import (
        GRAMMAR_WORD_TRANSLATIONS,
        get_grammar_config,
    )

    grammar_cfg = get_grammar_config(conversation.situation_id)
    if grammar_cfg and grammar_cfg.get("drill_targets"):
        return _grammar_pending_items(conversation, grammar_cfg)

    return _vocab_pending_items(db, conversation, alt_language)


def _vocab_pending_items(
    db: Session,
    conversation: Conversation,
    alt_language: Optional[str],
) -> List[PendingItem]:
    missing_ids = get_missing_word_ids(conversation, "voice")
    if not missing_ids:
        return []
    words = get_words_by_ids(db, missing_ids)
    words = apply_alt_language(words, alt_language, db)
    return [
        PendingItem(
            kind="vocab",
            id=w.id,
            spanish=w.spanish,
            english=w.english,
        )
        for w in words
    ]


def _grammar_pending_items(
    conversation: Conversation,
    grammar_cfg: Dict[str, Any],
) -> List[PendingItem]:
    from app.data.grammar_situations import GRAMMAR_WORD_TRANSLATIONS

    answers = (grammar_cfg.get("drill_config") or {}).get("answers") or {}
    drill_targets = grammar_cfg.get("drill_targets") or []

    used = set(conversation.used_spoken_word_ids or [])
    target_ids = set(conversation.target_word_ids or [])
    # A verb is "still pending" if its base id is in target_word_ids and
    # not yet in used_spoken_word_ids. This mirrors the FE's chip state
    # at the verb level — granularity per (verb, pronoun) lives only on
    # the FE; see module docstring.
    items: List[PendingItem] = []
    for t in drill_targets:
        verb = t.get("verb")
        pronoun = t.get("pronoun")
        if not verb or not pronoun:
            continue
        base_id = f"grammar_{verb}"
        if base_id not in target_ids:
            continue
        if base_id in used:
            continue
        conjugated = (answers.get(verb) or {}).get(pronoun)
        if not conjugated:
            continue
        # `|` is a stem/ending separator used only for UI rendering of drill
        # answers; the LLM and any downstream consumer must see the plain form.
        conjugated = conjugated.replace("|", "")
        items.append(
            PendingItem(
                kind="grammar",
                id=f"conj_{verb}_{pronoun}",
                spanish=conjugated,
                english=GRAMMAR_WORD_TRANSLATIONS.get(verb, verb),
                verb=verb,
                pronoun=pronoun,
                conjugated=conjugated,
            )
        )
    return items


def build_hint_messages(
    pending_items: List[PendingItem],
    recent_messages: Optional[List[Dict[str, str]]],
) -> List[Dict[str, str]]:
    """Build the LLM messages for hint generation.

    Returns a single user message: the recent turns + the list of remaining
    English words the learner still needs. The model returns a plain English
    sentence (no JSON, no Spanish, no audio) with the chosen keyword wrapped
    in markdown bold.
    """
    history_block = _format_history_for_prompt(recent_messages or [])
    words_block = _format_words_for_prompt(pending_items)

    prompt = (
        "Write a very simple, very short English sentence/question that is a "
        f"natural continuation to:\n\n{history_block}\n\n"
        f"Your sentence/question must contain one of these words: {words_block}. "
        "The sentence/question you provide should have the keyword/phrase in "
        "**markdown bold format**."
    )

    return [{"role": "user", "content": prompt}]


def _format_words_for_prompt(items: List[PendingItem]) -> str:
    """Comma-separated English words from the pending item list, deduped."""
    if not items:
        return "(none)"
    seen: set[str] = set()
    out: list[str] = []
    for it in items[:MAX_CANDIDATE_ITEMS]:
        word = (it.english or "").strip()
        if not word or word in seen:
            continue
        seen.add(word)
        out.append(word)
    return ", ".join(out) if out else "(none)"


def _format_history_for_prompt(messages: List[Dict[str, str]]) -> str:
    """Render the last 4 non-system turns for the prompt context."""
    trimmed = [m for m in messages if m.get("role") != "system"][-4:]
    if not trimmed:
        return "(no prior turns)"
    return "\n".join(
        f"[{m.get('role', 'unknown')}] {m.get('content', '')}" for m in trimmed
    )


async def generate_sentence_hint(
    db: Session,
    *,
    user_id: str,
    request_id: str,
    pending_items: List[PendingItem],
    recent_messages: Optional[List[Dict[str, str]]],
) -> Tuple[str, Optional[str]]:
    """Call the LLM to produce a single English hint sentence with the
    target keyword wrapped in markdown bold. Returns (english_text,
    llm_request_id). On any LLM failure, falls back to the first
    pending item's English so the user always gets something usable.
    """
    messages = build_hint_messages(pending_items, recent_messages)

    context = ConversationContext(
        request_id=request_id,
        user_id=user_id,
        system_prompt="",  # overridden by `messages` below
        user_prompt="",
        agent_id="sentence_hint",
        prompt_version="v3",
        messages=messages,
        return_json=False,
        model="gpt-4.1-mini",
        max_tokens=120,
    )

    english_text = ""
    llm_request_id: Optional[str] = None
    try:
        result = await generate_conversation(context, db)
        if isinstance(result, dict):
            content = result.get("content")
            llm_request_id = result.get("llm_request_id")
            if isinstance(content, str):
                english_text = content.strip()
    except Exception as e:
        logger.warning(f"[SentenceHint] LLM call failed: {type(e).__name__}: {e}")

    if not english_text and pending_items:
        # Defensive fallback so we never ship empty text to the FE.
        english_text = f"Try saying something using **{pending_items[0].english}**."

    return english_text, llm_request_id


def persist_hint_audit(
    db: Session,
    *,
    conversation: Conversation,
    user_id: str,
    english_gloss: str,
    pending_count: int,
    llm_request_id: Optional[str],
) -> SentenceHint:
    """Insert the audit row. Caller is responsible for the commit.

    `audio_url`, `tts_request_id`, `spanish`, `used_item_ids` columns on
    SentenceHint stay in the schema for historical rows but new rows
    leave them empty (no TTS in the current pipeline).
    """
    row = SentenceHint(
        conversation_id=conversation.id,
        user_id=user_id,
        situation_id=conversation.situation_id,
        spanish="",
        english_gloss=english_gloss,
        audio_url=None,
        used_item_ids=[],
        pending_count=pending_count,
        llm_request_id=llm_request_id,
        tts_request_id=None,
    )
    db.add(row)
    db.flush()
    return row
