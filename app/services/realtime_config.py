"""Shared builder for OpenAI Realtime API session configuration.

Two consumers read from this module:

1. `POST /v1/realtime/sessions` (see `app/services/realtime_session_service.py`)
   — mints an ephemeral token whose session config is used directly by the
   browser over WebRTC. The browser streams user audio in and receives assistant
   audio/text out, so the config carries `turn_detection` (server VAD) and
   `input_audio_transcription` (Whisper) so OpenAI handles endpointing and gives
   us per-turn transcripts.

2. `app/services/realtime_service.py` — the legacy server-side WebSocket flow
   where the backend already has the full `messages` list (system + history +
   latest user transcript) and just wants OpenAI to run one response turn with
   streamed PCM16 audio out. It has no user audio input and orchestrates
   responses itself, so `turn_detection` is disabled and
   `input_audio_transcription` is omitted.

Both consumers share: model, modalities, voice, system prompt. Keeping that in
one place is the whole point — if a situation's voice or system prompt drifts
between the two flows, the user hears/experiences different things depending on
which code path they hit.
"""
from typing import Literal, Optional

from sqlalchemy.orm import Session

from app.models import Conversation, Situation
from app.services.alt_language_service import get_target_language_name
from app.services.learner_context import LearnerContext
from app.services.voice_turn_service import (
    build_realtime_system_prompt,
    get_language_mode,
)


REALTIME_MODEL = "gpt-realtime-mini"

# Server VAD params match the FE-expected endpointing behavior. Bumping the
# threshold makes the model wait longer for silence before closing a turn;
# lowering it makes barge-in more aggressive. 0.5 / 500ms is OpenAI's default
# and what the FE's useRealtimeSession hook assumes.
_DEFAULT_TURN_DETECTION = {
    "type": "server_vad",
    "threshold": 0.5,
    "silence_duration_ms": 500,
    # Don't auto-fire response.create when VAD endpoints. The FE waits for
    # the Whisper transcript event, POSTs /realtime-turn for word detection
    # + steering, injects the meta-thought via conversation.item.create, and
    # then sends response.create itself. Keeps the BE in the steering loop.
    "create_response": False,
}

# whisper-1 is what the existing `/voice-turn` STT path uses. Keeping the same
# model means per-turn transcripts from the realtime flow agree with what the
# legacy flow would have produced for the same audio.
_DEFAULT_INPUT_TRANSCRIPTION = {"model": "whisper-1"}


def resolve_voice(
    animation_type: str,
    alt_language: Optional[str] = None,
    situation_id: Optional[str] = None,
) -> tuple[str, Optional[str]]:
    """Look up (voice, tts_instructions) for this situation's animation type.

    The voice catalog lives in `app/api/v1/conversations.py` to keep it near
    the legacy `/voice-turn/respond` TTS call that originally owned it. Import
    here rather than duplicating — if the catalog moves, update this import.

    `tts_instructions` is only meaningful for the legacy server-WS flow (passed
    to the TTS model as a style directive). The ephemeral/WebRTC flow ignores
    it because OpenAI Realtime voices don't currently accept per-session TTS
    instructions the same way.
    """
    from app.api.v1.conversations import get_tts_instructions

    return get_tts_instructions(
        animation_type,
        alt_language=alt_language,
        situation_id=situation_id,
    )


def _resolve_system_prompt(
    conversation: Conversation,
    situation: Situation,
    alt_language: Optional[str],
    vocab_level: int,
    grammar_level: float,
    learner_ctx: Optional[LearnerContext] = None,
) -> str:
    """Build the realtime session's system prompt.

    Uses the new short `realtime_agent` v1 template — role-only, no
    target_steering / anti_stuck / level_rule / turn-closing rule. Those
    move into the per-turn `conversation.item.create` (role=assistant)
    meta-thought injection driven by `realtime_steering.pick_next_target`.

    `learner_ctx`, `vocab_level`, `grammar_level` are accepted for
    signature compatibility with `build_session_config` callers but
    aren't currently consumed by the realtime template.
    """
    return build_realtime_system_prompt(
        situation.animation_type,
        conversation.situation_id,
        alt_language=alt_language,
    )


def build_session_config(
    conversation: Conversation,
    phase: str,
    db: Session,
    *,
    alt_language: Optional[str] = None,
    vocab_level: int = 0,
    grammar_level: float = 0.0,
    learner_ctx: Optional[LearnerContext] = None,
    mode: Literal["ephemeral", "server_ws"] = "ephemeral",
) -> dict:
    """Assemble the Realtime session configuration for a conversation.

    Args:
        conversation: The Conversation this session is for. Must have
            `situation_id` populated; the situation is loaded from `db`.
        phase: Learning phase string ("2", "3", …). Currently informational —
            carried through for observability and future prompt variants. The
            FE passes this as the `X-Learning-Phase` header today.
        db: SQLAlchemy session used to load the Situation row.
        alt_language: `None` for Spanish, `"catalan"`, or `"swedish"`. Drives
            both voice TTS accent and the prompt language.
        vocab_level / grammar_level: used to pick the right
            `language_mode` for system prompt templating. Callers should pass
            the same values they'd use in `/voice-turn/respond`.
        mode:
            - `"ephemeral"` (default): the config minted into a client_secret
              for WebRTC. Includes `model`, `input_audio_transcription`, and
              server-VAD `turn_detection`. This is the dict posted to
              `POST https://api.openai.com/v1/realtime/sessions`.
            - `"server_ws"`: the config sent as the `session.update` payload
              over a server-owned WebSocket. Includes `output_audio_format`
              `pcm16` (the server re-encodes to MP3) and disables
              `turn_detection` (the server calls `response.create` itself).

    Returns:
        A JSON-serializable dict ready to send to OpenAI. Callers don't wrap it
        — for ephemeral, POST it as the body directly; for server_ws, nest it
        under `{"type": "session.update", "session": <this>}`.
    """
    situation = (
        db.query(Situation).filter(Situation.id == conversation.situation_id).first()
    )
    if not situation:
        raise ValueError(
            f"Conversation {conversation.id} references missing situation "
            f"{conversation.situation_id}"
        )

    voice, tts_instructions = resolve_voice(
        situation.animation_type,
        alt_language=alt_language,
        situation_id=situation.id,
    )
    system_prompt = _resolve_system_prompt(
        conversation, situation, alt_language, vocab_level, grammar_level,
        learner_ctx=learner_ctx,
    )

    base = {
        "modalities": ["text", "audio"],
        "voice": voice,
        "instructions": system_prompt,
    }

    if mode == "ephemeral":
        # The browser connects directly to OpenAI over WebRTC. We need VAD
        # and Whisper transcription turned on so OpenAI handles endpointing
        # and gives us per-turn text to forward to `/realtime-turn` for word
        # detection + persistence.
        return {
            "model": REALTIME_MODEL,
            **base,
            "input_audio_transcription": dict(_DEFAULT_INPUT_TRANSCRIPTION),
            "turn_detection": dict(_DEFAULT_TURN_DETECTION),
        }

    # server_ws: we have the full message list already and want one streamed
    # response turn out with raw PCM so ffmpeg can re-encode to MP3.
    return {
        **base,
        "output_audio_format": "pcm16",
        "turn_detection": None,
    }


def build_ws_session_update(
    voice: str,
    instructions: str,
    tts_instructions: Optional[str] = None,
) -> dict:
    """Low-level helper for the legacy WS flow in `realtime_service.stream_realtime`.

    That function receives a pre-built `messages` list (system + history +
    latest user turn) and doesn't load the Conversation, so it can't call
    `build_session_config` directly. This helper returns the same shape
    `build_session_config(..., mode="server_ws")` produces from just voice +
    instructions. Keeping both in this module means the WS payload stays in
    sync if the schema evolves.

    `tts_instructions`, when provided, is appended to `instructions` as a
    voice-style directive — matches the pre-refactor inline behavior.
    """
    full_instructions = instructions
    if tts_instructions:
        full_instructions = f"{instructions}\n\n[Voice style: {tts_instructions}]"

    return {
        "modalities": ["text", "audio"],
        "voice": voice,
        "instructions": full_instructions,
        "output_audio_format": "pcm16",
        "turn_detection": None,
    }
