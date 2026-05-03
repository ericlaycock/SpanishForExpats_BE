import re
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
from app.services.grammar_elicitation import format_target_steering
from app.services.learner_context import ChipTarget, LearnerContext
from app.services.learner_level import level_rules_for_conversation
from app.services.word_detection import normalize_text


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


# Threshold for the tactics menu. Fires after a single consecutive
# no-progress turn so a native-English learner gets explicit scaffolding
# early rather than after 2 unhelpful turns. The translate-tactic
# (last-resort English parenthetical) still requires 3 stuck turns.
_STUCK_THRESHOLD_NUDGE = 1
_STUCK_THRESHOLD_TRANSLATE = 3


def _render_goal_block(goal: Optional[str]) -> str:
    if not goal:
        return ""
    return f"Your job is to make the student arrive at this outcome: {goal}\n\n"


def _render_anti_stuck_rule(consecutive_no_progress_turns: int) -> str:
    """Inject a stronger scaffolding directive once the learner has skipped
    the target one or more turns in a row.

    Below the nudge threshold the section is empty so the prompt isn't
    polluted on the very first turn. At the nudge level we surface a
    menu of alternative elicitation tactics (synonym / define / contrast
    / fill-in-blank / embedded yes/no) so the LLM has options instead
    of repeating its instinct verbatim. Above the translate threshold
    we authorise English glossing of the form as a last resort.

    Why a menu: from the avatar-dynamics screenshots we saw the LLM
    looping on the same elicitation pattern ("¿Cuál es el vuelo?")
    when the student didn't progress, exhausting the learner. A menu
    forces tactic rotation.
    """
    n = consecutive_no_progress_turns or 0
    if n < _STUCK_THRESHOLD_NUDGE:
        return ""
    if n < _STUCK_THRESHOLD_TRANSLATE:
        return (
            f"ANTI-STUCK: the student skipped the target {n} turn(s) in a row. "
            "Switch tactic this turn — pick ONE you haven't used in the last "
            "2 turns:\n"
            "- Synonym: use a near-synonym, ask the student to rephrase "
            "('Yo diría que va demorado — ¿tú cómo lo describirías?').\n"
            "- Define: describe the meaning, ask the student to name it "
            "('Cuando un vuelo no sale a tiempo, ¿cómo le decimos?').\n"
            "- Contrast: state your own side, ask the student's "
            "('Mi vuelo está a tiempo — ¿y el suyo?').\n"
            "- Fill-in-blank: leave a blank, ask the student to complete "
            "('Su vuelo va con un ___ de dos horas, ¿correcto?').\n"
            "- Embedded yes/no (last resort): include the form in a yes/no "
            "so the student echoes it ('¿Su vuelo está retrasado?'); only "
            "if the others already failed."
        )
    return (
        f"ANTI-STUCK: the student skipped the target {n} turns in a row. "
        "Drop indirectness completely — translate the target form into "
        "English in parentheses inside your question, e.g. '¿Tú cantas "
        "(do you sing) en la ducha?'."
    )


# Spanish function words that are too common to flag as "leaks" even when
# they appear as a target chip. The v3 prompt's "do not produce the target
# form" rule is meaningful for content words (verbs, nouns, named phrases)
# — for articles, pronouns, prepositions, and conjunctions the avatar will
# use them constantly in normal speech and flagging would be noise.
_FUNCTION_WORD_STOPLIST = frozenset({
    # articles
    "el", "la", "los", "las", "un", "una", "unos", "unas",
    # prepositions
    "a", "de", "en", "con", "por", "para", "sin", "sobre", "entre",
    "hasta", "desde",
    # conjunctions / connectors
    "y", "e", "o", "u", "que", "si", "no",
    # pronouns / possessives
    "yo", "tu", "el", "ella", "mi", "ti", "su", "se", "le", "lo", "me",
    "te", "nos",
})


def _chip_should_be_leak_checked(chip: ChipTarget) -> bool:
    """Decide whether to enforce the no-leak rule for a given chip.

    Multi-word chips and grammar chips (verb conjugations) are always
    checked. Single-word vocab chips are checked only when they are not
    in the function-word stoplist — the stoplist is a small set of
    high-frequency function words (articles, prepositions, common
    pronouns/conjunctions) that the avatar cannot reasonably avoid in
    natural speech.
    """
    spanish_norm = normalize_text(chip.spanish or "")
    if not spanish_norm:
        return False
    if " " in spanish_norm:
        return True
    if chip.is_grammar:
        return True
    return spanish_norm not in _FUNCTION_WORD_STOPLIST


def find_leaked_chips(
    assistant_text: str, pending_chips: List[ChipTarget],
) -> List[str]:
    """Return ids of pending chips whose exact Spanish form leaks into the
    assistant's reply.

    A leak removes the student's chance to earn the chip — the v3 prompt
    forbids it explicitly. Detection mirrors `detect_words_in_text`:
    accent-insensitive, case-insensitive, word-boundary match for single
    words and substring match for multi-word phrases. Function-word
    chips are skipped (see `_chip_should_be_leak_checked`).
    """
    if not assistant_text or not pending_chips:
        return []
    normalized_text = normalize_text(assistant_text)
    leaked: List[str] = []
    for chip in pending_chips:
        if not _chip_should_be_leak_checked(chip):
            continue
        normalized_chip = normalize_text(chip.spanish or "")
        if not normalized_chip:
            continue
        if " " in normalized_chip:
            if normalized_chip in normalized_text:
                leaked.append(chip.id)
        else:
            pattern = r"\b" + re.escape(normalized_chip) + r"\b"
            if re.search(pattern, normalized_text):
                leaked.append(chip.id)
    return leaked


def is_dead_end_turn(assistant_text: str) -> bool:
    """Return True when the avatar's reply closes the floor instead of
    handing it back to the student.

    The v3 prompt's TURN-CLOSING RULE requires every reply to end with a
    question mark. Empty replies are not flagged — the upstream caller
    handles "no text" cases. We strip trailing whitespace and inspect
    the final character; both ASCII `?` and full-width `？` are
    accepted.
    """
    if not assistant_text:
        return False
    stripped = assistant_text.rstrip()
    if not stripped:
        return False
    return stripped[-1] not in ("?", "？")


def validate_assistant_reply(
    assistant_text: str, pending_chips: List[ChipTarget],
) -> Tuple[bool, List[str], List[str]]:
    """Run both v3-prompt-rule checks against an assistant reply.

    Returns a tuple `(flagged, leaked_chip_ids, reasons)`:

    - `flagged` is True if either the leak check or the dead-end check
      tripped — callers use it to bump `avatar_dead_end_turns` and to
      surface a flag in the API response.
    - `leaked_chip_ids` is the list of pending chip ids whose Spanish
      form appeared in the reply (empty when no leak).
    - `reasons` is a short, human-readable list (one entry per failing
      check) intended for logs and telemetry. Stable strings — safe to
      grep for or alert on.
    """
    leaked = find_leaked_chips(assistant_text, pending_chips)
    dead_end = is_dead_end_turn(assistant_text)
    reasons: List[str] = []
    if leaked:
        reasons.append(f"chip_leak:{','.join(leaked)}")
    if dead_end:
        reasons.append("no_question_mark")
    return (bool(reasons), leaked, reasons)


def _render_target_steering(learner_ctx: Optional[LearnerContext]) -> str:
    if not learner_ctx:
        return "(no pending items — keep the conversation flowing naturally)"
    block = format_target_steering(
        learner_ctx.target_chips, learner_ctx.completed_chip_ids,
    )
    return block or "(all items complete — wrap up the conversation gracefully)"


def build_system_prompt(
    animation_type: str,
    situation_id: str,
    language_mode: str = "spanish_text",
    alt_language: Optional[str] = None,
    learner_ctx: Optional[LearnerContext] = None,
) -> str:
    """Build the system prompt for conversation or grammar agents.

    Uses role data from situation_roles.py and templates from prompts.json.
    Always uses target-language prompts (no beginner English mode).

    `learner_ctx` carries level / goal / chip targeting / stuck counter
    into the v3 templates. Optional for backwards compatibility — when
    omitted, the level rule defaults to intermediate, the goal/anti-stuck
    sections collapse to empty strings, and target steering shows a
    placeholder line. Every production call-site should populate it.
    """
    from app.services.llm_gateway import load_prompt

    language = get_target_language_name(alt_language)
    roles = get_roles_for_situation(animation_type, situation_id)

    grammar_struct = get_grammar_structure(situation_id)
    grammar_config = get_grammar_config(situation_id)

    spanish_level = learner_ctx.spanish_level if learner_ctx else None
    goal = learner_ctx.goal if learner_ctx else None
    no_progress_turns = (
        learner_ctx.consecutive_no_progress_turns if learner_ctx else 0
    )

    common_kwargs = {
        "language": language,
        "goal_block": _render_goal_block(goal),
        "level_rule": level_rules_for_conversation(spanish_level),
        "target_steering": _render_target_steering(learner_ctx),
        "anti_stuck_rule": _render_anti_stuck_rule(no_progress_turns),
    }

    if grammar_struct or grammar_config:
        template = load_prompt("grammar_agent", "v3")
        return template.format(**common_kwargs)

    template = load_prompt("conversation_agent", "v3")
    return template.format(
        ai_role=roles["ai_role"],
        user_role=roles["user_role"],
        situation_description=roles["situation_description"],
        **common_kwargs,
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

def build_grammar_system_prompt(
    situation_id: str,
    language_mode: str = "spanish_text",
    alt_language: Optional[str] = None,
    learner_ctx: Optional[LearnerContext] = None,
) -> Optional[str]:
    """Build a system prompt for grammar conversation phases (2/3)."""
    config = get_grammar_config(situation_id)
    if not config:
        return None
    if alt_language and language_mode in ("spanish_text", "spanish_audio"):
        language_mode = language_mode.replace("spanish_", f"{alt_language}_")
    return build_system_prompt(
        "grammar", situation_id, language_mode, alt_language,
        learner_ctx=learner_ctx,
    )


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
    learner_ctx: Optional[LearnerContext] = None,
) -> str:
    """Build the conversation system prompt with role context."""
    return build_system_prompt(
        animation_type, situation_id, language_mode, alt_language,
        learner_ctx=learner_ctx,
    )


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
    used_before = set(conversation.used_spoken_word_ids or [])
    current_used = set(used_before)
    current_used.update(detected_word_ids)
    conversation.used_spoken_word_ids = list(current_used)
    conversation.turn_count = (conversation.turn_count or 0) + 1

    # Chip-level progress for grammar chats. Scan THIS turn's transcript for
    # any chip's exact Spanish form and union into completed_chip_ids — the
    # column is the source of truth so /realtime-turn doesn't need history.
    new_chip_ids: set[str] = set()
    if conversation.chat_target_forms_json:
        from app.services.conversation_service import check_chat_chip_completion

        _, ticked_this_turn = check_chat_chip_completion(
            conversation, [user_transcript or ""],
        )
        chips_before = set(conversation.completed_chip_ids or [])
        new_chip_ids = set(ticked_this_turn) - chips_before
        if new_chip_ids:
            conversation.completed_chip_ids = list(chips_before | new_chip_ids)

    # Stuck counter: any turn that adds a brand-new id to used_spoken_word_ids
    # OR a brand-new chip is "progress" and resets the counter. Otherwise we
    # tick up so the v3 system prompt's anti-stuck rule can kick in once the
    # learner has been missing the target a few turns in a row.
    new_word_ids = set(detected_word_ids) - used_before
    progress = bool(new_word_ids or new_chip_ids)
    if progress:
        conversation.consecutive_no_progress_turns = 0
    else:
        conversation.consecutive_no_progress_turns = (
            conversation.consecutive_no_progress_turns or 0
        ) + 1

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
