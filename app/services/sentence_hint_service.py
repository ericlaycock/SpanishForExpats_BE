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

import json
import logging
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from sqlalchemy.orm import Session

from app.models import Conversation, SentenceHint
from app.services.alt_language_service import (
    apply_alt_language,
    get_target_language_name,
)
from app.services.conversation_service import get_missing_word_ids
from app.services.llm_gateway import ConversationContext, generate_conversation
from app.services.openai_media_gateway import PROVIDER, sha256_hash
from app.services.realtime_config import REALTIME_MODEL
from app.services.realtime_service import generate_with_realtime, pcm16_to_mp3
from app.services.word_detection import get_words_by_ids
from app.utils.audio import generate_audio_filename, get_audio_path, upload_to_r2

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


def _level_rules(spanish_level: Optional[str]) -> str:
    """Length/complexity rule for the prompt, keyed on q0_spanish_level.

    A 14-word hint is unspeakable for an absolute beginner, so we tighten
    word budget and forbid subordinates as the level drops. Null/unknown
    falls back to 'c' (intermediate) — safe middle ground for legacy
    users who never went through V2 onboarding.
    """
    level = (spanish_level or "c").lower()
    if level == "a":
        return (
            "- LEARNER LEVEL: absolute beginner. The sentence MUST be 5–7 words "
            "and use EXACTLY ONE pending item. No subordinate clauses, no "
            "compound sentences, no embedded questions. Keep it as simple as "
            "physically possible to say out loud."
        )
    if level == "b":
        return (
            "- LEARNER LEVEL: novice. The sentence MUST be 7–9 words and use 1 "
            "pending item (a second only if it fits naturally). No complex "
            "subordinates."
        )
    if level == "d":
        return (
            "- LEARNER LEVEL: advanced. Sentence may be up to ~14 words and "
            "use 1 or 2 pending items with natural complexity."
        )
    return (
        "- LEARNER LEVEL: intermediate. The sentence MUST be 9–12 words and "
        "use 1 or 2 pending items. Simple subordinates allowed."
    )


def build_hint_messages(
    pending_items: List[PendingItem],
    recent_messages: Optional[List[Dict[str, str]]],
    situation_title: Optional[str],
    alt_language: Optional[str],
    spanish_level: Optional[str] = None,
) -> List[Dict[str, str]]:
    """Build the LLM messages for hint generation.

    Returns a `messages` list ready for `ConversationContext`. Includes a
    system prompt with formatting rules and a user prompt with the
    pending items + the last 4 turns of conversation context.
    """
    target_language = get_target_language_name(alt_language)
    items_block = _format_items_for_prompt(pending_items)

    history_block = _format_history_for_prompt(recent_messages or [])

    title = situation_title or "this conversation"
    level_rule = _level_rules(spanish_level)

    # The learner is stuck in a real roleplay and needs help unblocking
    # the conversation. The prompt deliberately fights the model's
    # default "Quiero/Necesito el <word>" stitching by anchoring every
    # suggestion in a concrete real-world need, with explicit bad/good
    # contrast so the few-shot grounding actually transfers. Without
    # these examples GPT happily produces flat vocab-quiz sentences.
    system = (
        f"You are a {target_language} tutor helping a learner who is STUCK "
        "mid-conversation in a live roleplay. They need a natural sentence they "
        "can say RIGHT NOW that moves the scene forward AND uses 1 or 2 of "
        "the pending items.\n\n"
        "The sentence must feel like something a real traveler / customer / "
        "patient / student would actually say in this exact situation. Anchor "
        "it in a concrete real-world need (a problem, a request, a question) "
        "that motivates the words.\n\n"
        "AVOID flat vocab-quiz formulas like \"Quiero el X\" / \"Necesito el X\" "
        "/ \"Tengo el X\". Those are correct but feel mechanical and don't "
        "actually help the learner converse.\n\n"
        "Examples:\n"
        "- pending: número, vuelo, perdón, ayuda\n"
        "    BAD:  \"Quiero el número de vuelo, por favor.\"\n"
        "    GOOD: \"Perdón, perdí mi número de vuelo. ¿Me podría ayudar?\"\n"
        "- pending: pasaporte, mostrar\n"
        "    BAD:  \"Le muestro mi pasaporte.\"\n"
        "    GOOD: \"Aquí tiene mi pasaporte, ¿lo ve bien?\"\n"
        "- pending: mesa, reservar\n"
        "    BAD:  \"Quiero una mesa.\"\n"
        "    GOOD: \"Tengo una reserva a las ocho, ¿la mesa está lista?\"\n\n"
        "Rules:\n"
        "- ONE sentence, first person — the LEARNER is the speaker.\n"
        f"{level_rule}\n"
        "- Match the register of the last assistant turn (formal \"usted\" vs "
        "informal \"tú\").\n"
        "- For grammar items, use the EXACT conjugated form from the item list. "
        "Never substitute another tense, person, or verb.\n"
        "- The English gloss should be a faithful, natural translation — not "
        "stiff or word-for-word.\n"
        "- No greeting, no narration, no \"You could say…\" framing.\n\n"
        "Return ONLY valid JSON with this exact shape:\n"
        '{"spanish": "<the sentence>", "english_gloss": "<English translation>", '
        '"used_item_ids": ["<id from pending items>"]}'
    )

    user = (
        f"Scenario: {title}\n\n"
        f"Pending items the learner still needs to use:\n{items_block}\n\n"
        f"Recent turns:\n{history_block}\n\n"
        "Suggest the learner's next sentence."
    )

    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def _format_items_for_prompt(items: List[PendingItem]) -> str:
    if not items:
        return "(none)"
    lines = []
    for it in items[:MAX_CANDIDATE_ITEMS]:
        if it.kind == "grammar":
            lines.append(
                f"- {it.id}: \"{it.conjugated}\"  ({it.pronoun} + {it.verb} = \"{it.english}\")"
            )
        else:
            lines.append(f"- {it.id}: \"{it.spanish}\"  ({it.english})")
    return "\n".join(lines)


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
    situation_title: Optional[str],
    alt_language: Optional[str],
    spanish_level: Optional[str] = None,
) -> Tuple[str, str, List[str], Optional[str]]:
    """Call the LLM to produce a hint sentence. Returns (spanish,
    english_gloss, used_item_ids, llm_request_id).

    The `llm_request_id` is the `id` of the persisted `LLMRequest` row
    so the caller can attach it to the `sentence_hints` audit row.
    Falls back to a defensive item-pair-only sentence if the LLM
    returns malformed JSON; the upstream handler raises if items are
    empty so we never ship "(none)" to the user.
    """
    messages = build_hint_messages(
        pending_items, recent_messages, situation_title, alt_language,
        spanish_level=spanish_level,
    )

    context = ConversationContext(
        request_id=request_id,
        user_id=user_id,
        system_prompt="",  # overridden by `messages` below
        user_prompt="",
        agent_id="sentence_hint",
        prompt_version="v2",
        messages=messages,
        return_json=True,
        # Bumped from 200 → 300 to give the model headroom for natural
        # 12–14 word sentences plus the gloss without truncating mid-JSON.
        max_tokens=300,
    )

    # gpt-5.4-mini's Responses API + reasoning: low + return_json
    # occasionally hands back an empty `output_text` (the LLM gateway
    # then chokes on `json.loads("")`). Treat any failure here as
    # "model didn't produce parseable output" and let the parser fall
    # back to a first-pending-item suggestion — better than 500'ing the
    # user out of the encounter.
    content: Any = None
    llm_request_id: Optional[str] = None
    try:
        result = await generate_conversation(context, db)
        if isinstance(result, dict):
            content = result.get("content")
            llm_request_id = result.get("llm_request_id")
    except json.JSONDecodeError as e:
        logger.warning(f"[SentenceHint] LLM returned unparseable JSON: {e}")
    except Exception as e:
        logger.warning(f"[SentenceHint] LLM call failed: {type(e).__name__}: {e}")

    spanish, english_gloss, used_item_ids = _parse_hint_payload(content, pending_items)
    return spanish, english_gloss, used_item_ids, llm_request_id


def _parse_hint_payload(
    content: Any,
    pending_items: List[PendingItem],
) -> Tuple[str, str, List[str]]:
    """Coerce the LLM payload into (spanish, english_gloss, used_item_ids).

    The Responses API returns dict directly when `return_json=True`. If
    the model misbehaves and returns a string, we try one JSON parse
    pass; otherwise we fall back to the first pending item (so the user
    always gets something usable instead of a 500).
    """
    payload: Dict[str, Any] = {}
    if isinstance(content, dict):
        payload = content
    elif isinstance(content, str):
        try:
            payload = json.loads(content)
        except (json.JSONDecodeError, TypeError):
            payload = {}

    spanish = (payload.get("spanish") or "").strip()
    english_gloss = (payload.get("english_gloss") or "").strip()
    used_raw = payload.get("used_item_ids") or []
    if not isinstance(used_raw, list):
        used_raw = []

    valid_ids = {it.id for it in pending_items}
    used_item_ids = [str(i) for i in used_raw if str(i) in valid_ids]

    if not spanish or not english_gloss:
        # Fall back to the first pending item so we never ship empty
        # text to the FE. Keeps the UI honest if the model misfires.
        if pending_items:
            it = pending_items[0]
            spanish = it.spanish if not spanish else spanish
            english_gloss = it.english if not english_gloss else english_gloss
            if not used_item_ids:
                used_item_ids = [it.id]

    return spanish, english_gloss, used_item_ids


async def synthesize_hint_audio(
    db: Session,
    *,
    text: str,
    voice: str,
    instructions: Optional[str],
    request_id: str,
    user_id: str,
) -> Tuple[Optional[str], Optional[str]]:
    """TTS the hint sentence via the OpenAI Realtime API and upload to R2.

    The live voice-chat session runs on the Realtime API (`gpt-realtime-mini`)
    and ignores `tts_instructions`, so the standard TTS model
    (`gpt-4o-mini-tts`) the legacy hint flow used produced a noticeably
    different voice — same `voice` id, different rendering model, plus the
    persona styling instructions only the legacy flow applies. Mid-conversation
    that voice swap is jarring. Routing the hint through the same Realtime
    pipeline (and dropping `tts_instructions`) keeps the voice identical to
    what the user just heard from the avatar.

    The model is coaxed into parrot mode via a strict system prompt; we use
    the `voice` to pick the speaker but skip `tts_instructions` so the styling
    matches the live ephemeral session, which also ignores them.

    Returns `(audio_url, tts_request_id)`. Either may be None if Realtime,
    ffmpeg, or R2 upload fails — the endpoint already handles that gracefully
    (FE shows text only).

    `instructions` is accepted for API parity with callers that still hand it
    through, but intentionally not forwarded to the Realtime call.
    """
    import time
    import uuid as _uuid

    from app.models import TTSRequest

    filename = f"hint_{generate_audio_filename()}"
    output_path = str(get_audio_path(filename))

    user_id_uuid: Optional[_uuid.UUID]
    if isinstance(user_id, str):
        try:
            user_id_uuid = _uuid.UUID(user_id)
        except ValueError:
            user_id_uuid = None
    else:
        user_id_uuid = user_id

    # Insert audit row up front so failed attempts still leave a trail with
    # latency + error info — mirrors the pattern in
    # `openai_media_gateway.synthesize_speech`.
    tts_record = TTSRequest(
        id=_uuid.uuid4(),
        request_id=request_id or "unknown",
        user_id=user_id_uuid,
        provider=PROVIDER,
        model=REALTIME_MODEL,
        voice=voice,
        input_text_sha256=sha256_hash(text.encode("utf-8")),
        input_chars=len(text),
        output_format="mp3",
        success=False,
    )
    db.add(tts_record)
    db.commit()
    db.refresh(tts_record)

    # Strict parrot-mode prompt — we ship the user's hint as a `user` turn
    # and tell the model to read it back verbatim. Empirically the realtime
    # model honors this for short single-sentence inputs; longer or more
    # ambiguous inputs may drift, which is fine because we still render the
    # canonical Spanish text alongside the audio.
    parrot_messages = [
        {
            "role": "system",
            "content": (
                "You are a text-to-speech engine. Read the user's message "
                "aloud verbatim in the same language. Do not add greetings, "
                "commentary, translation, or rephrase the text. Output only "
                "the words the user gave you, exactly as written."
            ),
        },
        {"role": "user", "content": text},
    ]

    start = time.time()
    try:
        result = await generate_with_realtime(
            messages=parrot_messages,
            voice=voice,
            # Intentionally omitted — the live ephemeral session also ignores
            # these, so feeding them here would re-introduce the styling drift
            # we are trying to eliminate.
            tts_instructions=None,
            request_id=request_id or "hint",
        )
        audio_bytes = result.get("audio_bytes") or b""
        if not audio_bytes:
            raise RuntimeError("Realtime returned no audio bytes")
        pcm16_to_mp3(audio_bytes, output_path)
    except Exception as e:
        latency_ms = int((time.time() - start) * 1000)
        tts_record.latency_ms = latency_ms
        tts_record.error_code = type(e).__name__
        tts_record.error_message = str(e)
        db.commit()
        logger.error(f"[SentenceHint] Realtime TTS failed: {e}")
        return None, None

    latency_ms = int((time.time() - start) * 1000)
    audio_bytes_written = len(audio_bytes)
    tts_record.success = True
    tts_record.audio_bytes = audio_bytes_written
    tts_record.audio_path = output_path
    tts_record.latency_ms = latency_ms
    db.commit()

    # If the model deviated from the requested text, log it but ship the audio
    # anyway — the FE shows the canonical Spanish next to the bubble, and an
    # imperfect read still beats no audio. Significant drift is rare and worth
    # spotting in logs so we can tune the parrot prompt if it surfaces.
    spoken_text = (result.get("text") or "").strip()
    if spoken_text and spoken_text != text.strip():
        logger.warning(
            "[SentenceHint] Realtime drifted from input — wanted %r, heard %r",
            text,
            spoken_text,
        )

    audio_url = upload_to_r2(output_path, filename)
    return audio_url, str(tts_record.id)


def persist_hint_audit(
    db: Session,
    *,
    conversation: Conversation,
    user_id: str,
    spanish: str,
    english_gloss: str,
    audio_url: Optional[str],
    used_item_ids: List[str],
    pending_count: int,
    llm_request_id: Optional[str],
    tts_request_id: Optional[str],
) -> SentenceHint:
    """Insert the audit row. Caller is responsible for the commit."""
    row = SentenceHint(
        conversation_id=conversation.id,
        user_id=user_id,
        situation_id=conversation.situation_id,
        spanish=spanish,
        english_gloss=english_gloss,
        audio_url=audio_url,
        used_item_ids=used_item_ids,
        pending_count=pending_count,
        llm_request_id=llm_request_id,
        tts_request_id=tts_request_id,
    )
    db.add(row)
    db.flush()
    return row
