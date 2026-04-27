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

from app.data.grammar_situations import get_grammar_config
from app.models import Conversation, Situation
from app.services.alt_language_service import get_target_language_name
from app.services.voice_turn_service import (
    build_grammar_system_prompt,
    get_conversation_system_prompt,
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
) -> str:
    """Build the system prompt the model should carry for the whole session.

    Mirrors the logic used by `/voice-turn/respond` for a new turn without any
    existing message history: pick grammar template if the situation is a
    grammar drill, otherwise the conversation template. Alt-language mode
    swaps the language_mode suffix so prompts render in Catalan/Swedish.
    """
    language_mode = get_language_mode(
        situation.encounter_number, vocab_level, grammar_level
    )
    if alt_language and language_mode in ("spanish_text", "spanish_audio"):
        language_mode = language_mode.replace("spanish_", f"{alt_language}_")

    if get_grammar_config(conversation.situation_id):
        return build_grammar_system_prompt(
            conversation.situation_id,
            language_mode=language_mode,
            alt_language=alt_language,
        )
    return get_conversation_system_prompt(
        language_mode=language_mode,
        alt_language=alt_language,
        animation_type=situation.animation_type,
        situation_id=conversation.situation_id,
    )


def build_session_config(
    conversation: Conversation,
    phase: str,
    db: Session,
    *,
    alt_language: Optional[str] = None,
    vocab_level: int = 0,
    grammar_level: float = 0.0,
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
        conversation, situation, alt_language, vocab_level, grammar_level
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
