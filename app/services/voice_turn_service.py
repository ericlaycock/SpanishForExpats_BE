from typing import List, Optional, Tuple
from uuid import UUID

from sqlalchemy.orm import Session

from app.models import Conversation, Word, Situation
from app.data.grammar_situations import get_grammar_config
from app.data.situation_roles import (
    get_roles_for_situation,
    get_grammar_structure,
    GRAMMAR_SCENE_MAP,
)
from app.services.alt_language_service import get_target_language_name


# Hard limit on persisted turns per voice conversation. Mirrors the FE's
# ImmersiveVoiceScene EXCHANGE_HARD_LIMIT — keeping them in lockstep means
# the client and server agree on when the session must close. Realtime
# sessions need this as an explicit backstop because the backend doesn't
# orchestrate each round-trip; legacy /voice-turn picks it up too so
# behavior converges across flows.
EXCHANGE_HARD_LIMIT = 30

# FE-facing value for the "N turns left" countdown. FE shows warnings as
# turns_remaining decreases from this baseline; stays at 0 once passed.
EXCHANGE_WARNING_THRESHOLD = 25


def get_language_mode(encounter_number: int, vocab_level: int, grammar_level: float = 0) -> str:
    """AI always speaks in the target language now."""
    return "spanish_text"


def is_advanced_mode(language_mode: str) -> bool:
    """Return True if the language mode means the AI should speak in the target language."""
    return language_mode in (
        "spanish_text", "spanish_audio",
        "catalan_text", "catalan_audio",
        "swedish_text", "swedish_audio",
    )


def build_system_prompt(
    animation_type: str,
    situation_id: str,
    language_mode: str = "spanish_text",
    alt_language: Optional[str] = None,
) -> str:
    """Build the system prompt for conversation or grammar agents.

    Uses role data from situation_roles.py and templates from prompts.json.
    Always uses target-language prompts (no beginner English mode).
    """
    from app.services.llm_gateway import load_prompt

    language = get_target_language_name(alt_language)
    roles = get_roles_for_situation(animation_type, situation_id)

    # Check if this is a grammar situation
    grammar_struct = get_grammar_structure(situation_id)
    grammar_config = get_grammar_config(situation_id)

    if grammar_struct or grammar_config:
        template = load_prompt("grammar_agent", "v2")
        try:
            return template.format(language=language)
        except KeyError:
            return template
    else:
        template = load_prompt("conversation_agent", "v2")
        return template.format(
            ai_role=roles["ai_role"],
            user_role=roles["user_role"],
            situation_description=roles["situation_description"],
            language=language,
        )


def build_transcription_prompt(situation_title: str, words: List[Word], alt_language: Optional[str] = None) -> str:
    """Build a context prompt for STT transcription (whisper-style format).

    Benchmark showed this format gives 0.997 accuracy + 100% Spanish word
    detection on gpt-4o-mini-transcribe, beating both whisper-1 and
    gpt-4o-transcribe.
    """
    word_phrase_list = ", ".join([w.spanish for w in words])
    lang = get_target_language_name(alt_language)
    return (
        f"This is a conversation about {situation_title}. "
        f"The user is learning {lang} and may use these {lang} words and phrases: {word_phrase_list}. "
        f"The conversation is in {lang} and English."
    )


# ── Legacy functions (kept for backward compatibility during transition) ──────

def build_grammar_system_prompt(situation_id: str, language_mode: str = "spanish_text", alt_language: Optional[str] = None) -> Optional[str]:
    """Build a system prompt for grammar conversation phases (2/3)."""
    config = get_grammar_config(situation_id)
    if not config:
        return None
    if alt_language and language_mode in ("spanish_text", "spanish_audio"):
        language_mode = language_mode.replace("spanish_", f"{alt_language}_")
    return build_system_prompt("grammar", situation_id, language_mode, alt_language)


def build_grammar_user_prompt(
    situation_title: str,
    used_spoken_word_ids: List[str],
    user_transcript: str,
    config: dict,
) -> str:
    """Build user prompt for grammar conversation turn."""
    p2_config = config.get("phase_2_config", {}) or {}
    description = p2_config.get("description", "Practice grammar structures")

    return (
        f"Grammar Situation: {situation_title}\n"
        f"Goal: {description}\n"
        f"User said: {user_transcript}\n\n"
        f"Continue the practice session."
    )


def get_conversation_system_prompt(
    language_mode: str = "spanish_text",
    alt_language: Optional[str] = None,
    animation_type: str = "",
    situation_id: str = "",
) -> str:
    """Build the conversation system prompt with role context."""
    return build_system_prompt(animation_type, situation_id, language_mode, alt_language)


def build_conversation_prompt(
    situation_title: str,
    words: List[Word],
    used_spoken_word_ids: List[str],
    user_transcript: str,
    alt_language: Optional[str] = None,
) -> str:
    """Build the user prompt for the conversation LLM (used when no message history)."""
    used_words = [w.spanish for w in words if w.id in used_spoken_word_ids]
    missing_words_info = [
        f"{w.spanish} ({w.english})"
        for w in words
        if w.id not in used_spoken_word_ids
    ]
    lang = get_target_language_name(alt_language)

    return (
        f"Situation: {situation_title}\n"
        f"Still need: {', '.join(missing_words_info) if missing_words_info else 'All words used'}\n"
        f"Already used: {', '.join(used_words) if used_words else 'None'}\n"
        f"User said: {user_transcript}\n\n"
        f"Ask a natural question requiring a missing {lang} word. Do NOT mention the {lang} word."
    )


# ── Post-turn ingestion primitives ────────────────────────────────────────────
# Three focused helpers consumed by the legacy /voice-turn flow AND the new
# /realtime-turn endpoint. Splitting them here (instead of inlining as before)
# means word detection, persistence, and completion logic can't drift between
# the two flows — a parity bug that the realtime migration would otherwise
# quietly introduce.


def detect_words(
    db: Session,
    conversation: Conversation,
    transcript: str,
    alt_language: Optional[str] = None,
) -> List[str]:
    """Deterministic word/phrase detection against this conversation's targets.

    Preserves the grammar-aware matching behavior the legacy /voice-turn used:
    for grammar situations with a populated `drill_config.answers`, any
    conjugated form matches its infinitive's `grammar_<verb>` id (mirrors the
    FE logic at ImmersiveVoiceScene.tsx:452-462). Non-grammar situations fall
    back to word-boundary matching on the target words.

    Returns only the detected target ids — deduped, empty on empty transcript.
    """
    if not transcript:
        return []

    # Local imports to avoid circulars at module load time.
    from app.services.alt_language_service import apply_alt_language
    from app.services.word_detection import (
        detect_grammar_words_in_text,
        detect_words_in_text,
        get_words_by_ids,
    )

    words = get_words_by_ids(db, conversation.target_word_ids or [])
    words = apply_alt_language(words, alt_language, db)

    grammar_config = get_grammar_config(conversation.situation_id)
    answers = (grammar_config or {}).get("drill_config", {}).get("answers")
    if grammar_config and answers:
        return detect_grammar_words_in_text(transcript, words, answers)
    return detect_words_in_text(transcript, words)


def persist_turn(
    db: Session,
    conversation: Conversation,
    user_id: UUID,
    user_transcript: str,
    assistant_text: str = "",
    alt_language: Optional[str] = None,
) -> Tuple[Conversation, List[str]]:
    """Record one user turn: detect, extend used_spoken_word_ids, increment turn_count.

    Shared between legacy `/voice-turn` (called after STT) and the new
    `/realtime-turn` endpoint (called by the FE after each completed WebRTC
    turn). The caller is responsible for committing the session and for
    running `check_completion` afterward — those two concerns are kept
    separate so tests can introspect intermediate state and so the legacy
    flow can defer the completion check to its second-step endpoint.

    Side effects:
    - Appends detected ids to `used_spoken_word_ids` (deduped).
    - Increments `turn_count` by 1.
    - Upserts `user_words` spoken counters for each detected id.
    - Records the `first_word` milestone the first time a target word lands
      in a lesson-type conversation (idempotent via unique constraint).

    `assistant_text` is accepted for parity with the `/realtime-turn`
    contract but NOT persisted today — the `conversations` table doesn't
    store message text (FE owns the transcript log). Kept in the signature
    so we can start persisting without changing callers when we need to.

    Returns `(conversation, detected_word_ids)` so callers can build their
    response shape without re-computing detection.
    """
    # Local imports to keep this module import-safe.
    from sqlalchemy.dialects.postgresql import insert as pg_insert
    from app.models import UserMilestoneEvent
    from app.services.conversation_service import update_user_word_stats

    detected_word_ids = detect_words(db, conversation, user_transcript, alt_language)

    was_empty = len(conversation.used_spoken_word_ids or []) == 0
    current_used = set(conversation.used_spoken_word_ids or [])
    current_used.update(detected_word_ids)
    conversation.used_spoken_word_ids = list(current_used)
    conversation.turn_count = (conversation.turn_count or 0) + 1

    if detected_word_ids:
        update_user_word_stats(db, str(user_id), detected_word_ids, "voice")

    if was_empty and detected_word_ids and conversation.conversation_type == "lesson":
        target_set = set(conversation.target_word_ids or [])
        if any(w in target_set for w in detected_word_ids):
            db.execute(
                pg_insert(UserMilestoneEvent)
                .values(
                    user_id=user_id,
                    milestone_key="first_word",
                    situation_id=conversation.situation_id,
                    conversation_id=conversation.id,
                )
                .on_conflict_do_nothing(constraint="uq_user_milestone_situation")
            )

    return conversation, detected_word_ids


def check_completion(conversation: Conversation) -> Tuple[bool, int]:
    """Return (complete, turns_remaining) for a voice conversation.

    `complete` fires when EITHER:
      - every target word has been spoken at least once, OR
      - `turn_count >= EXCHANGE_HARD_LIMIT` — safety net for open-ended
        realtime sessions (and, by convergence, any legacy /voice-turn that
        runs past the threshold).

    `turns_remaining` counts down from `EXCHANGE_WARNING_THRESHOLD` so the FE
    can surface a "N turns left" warning before the hard limit. Stays at 0
    once the threshold is passed; consumers that don't need it can ignore it.
    """
    target = set(conversation.target_word_ids or [])
    used = set(conversation.used_spoken_word_ids or [])
    words_complete = bool(target) and target.issubset(used)

    turn_count = conversation.turn_count or 0
    turn_limit_hit = turn_count >= EXCHANGE_HARD_LIMIT

    complete = words_complete or turn_limit_hit
    turns_remaining = max(0, EXCHANGE_WARNING_THRESHOLD - turn_count)
    return complete, turns_remaining
