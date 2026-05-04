"""Tests for `app/services/realtime_config.py`.

Phase 1 of the realtime voice-chat migration: a single source of truth for
the OpenAI Realtime session config so the new ephemeral/WebRTC endpoint and
the legacy server-WS flow agree on system prompt + voice + model.

These tests use the real `Conversation`/`Situation` models against the test
Postgres (per `tests/conftest.py`) and snapshot the resulting config for
representative situations and phases. No network calls — `build_session_config`
is pure given a DB session.
"""
import uuid

import pytest

from app.auth import get_password_hash
from app.models import Conversation, Situation, User
from app.services.realtime_config import (
    REALTIME_MODEL,
    build_session_config,
    build_ws_session_update,
    resolve_voice,
)


# ── Fixtures ──────────────────────────────────────────────────────────────────


def _make_user(db) -> User:
    user = User(
        id=uuid.uuid4(),
        email=f"rt_{uuid.uuid4().hex[:8]}@test.com",
        password_hash=get_password_hash("testpass123"),
    )
    db.add(user)
    db.flush()
    return user


def _make_situation(db, sid: str, animation_type: str, encounter_number: int = 1) -> Situation:
    situation = Situation(
        id=sid,
        title=f"Test {sid}",
        animation_type=animation_type,
        encounter_number=encounter_number,
        order_index=1,
        is_free=True,
    )
    db.add(situation)
    db.flush()
    return situation


def _make_conversation(db, user: User, situation: Situation) -> Conversation:
    conv = Conversation(
        id=uuid.uuid4(),
        user_id=user.id,
        situation_id=situation.id,
        mode="voice",
        target_word_ids=[],
        used_typed_word_ids=[],
        used_spoken_word_ids=[],
    )
    db.add(conv)
    db.flush()
    return conv


# ── resolve_voice ─────────────────────────────────────────────────────────────


def test_resolve_voice_known_animation_type():
    """Banking situations get shimmer; restaurant gets ash. Catalog lives in
    SITUATION_VOICE_CONFIG — this test pins the contract."""
    voice, instructions = resolve_voice("banking")
    assert voice == "shimmer"
    assert "Mexican Spanish" in instructions

    voice, instructions = resolve_voice("restaurant")
    assert voice == "ash"


def test_resolve_voice_swaps_accent_for_alt_language():
    """Catalan/Swedish modes replace the Mexican accent directive."""
    _, es_instr = resolve_voice("banking")
    _, ca_instr = resolve_voice("banking", alt_language="catalan")
    _, sv_instr = resolve_voice("banking", alt_language="swedish")

    assert "Mexican Spanish" in es_instr
    assert "Catalan accent" in ca_instr
    assert "Swedish accent" in sv_instr


def test_resolve_voice_unknown_animation_type_falls_back():
    """Unknown types default to alloy, no instructions — matches
    get_tts_instructions behavior."""
    voice, instructions = resolve_voice("nonexistent_animation_type_xyz")
    assert voice == "alloy"
    assert instructions is None


# ── build_session_config: ephemeral mode ──────────────────────────────────────


def test_ephemeral_config_carries_model_vad_and_whisper(db):
    """Ephemeral config (browser → OpenAI WebRTC) must include the model name,
    server VAD turn detection, and whisper transcription. Without these the
    browser session can't endpoint user speech or hand transcripts back to us."""
    user = _make_user(db)
    situation = _make_situation(db, "bank_open_test", "banking")
    conv = _make_conversation(db, user, situation)

    cfg = build_session_config(conv, phase="2", db=db)

    assert cfg["model"] == REALTIME_MODEL
    assert cfg["modalities"] == ["text", "audio"]
    assert cfg["voice"] == "shimmer"
    assert cfg["turn_detection"] == {
        "type": "server_vad",
        "threshold": 0.5,
        "silence_duration_ms": 500,
    }
    assert cfg["input_audio_transcription"] == {"model": "whisper-1"}
    assert isinstance(cfg["instructions"], str) and cfg["instructions"]
    # Ephemeral never sets output_audio_format — that's only meaningful when
    # the server is decoding raw PCM from a WS stream.
    assert "output_audio_format" not in cfg


def test_ephemeral_config_for_grammar_situation_uses_grammar_prompt(db):
    """Grammar situations have their own template — pin that the right one
    flows into the ephemeral session so the model behaves as a drill agent."""
    user = _make_user(db)
    # `grammar_pronouns` is defined in app/data/grammar_situations.py
    situation = _make_situation(db, "grammar_pronouns", "grammar")
    conv = _make_conversation(db, user, situation)

    cfg = build_session_config(conv, phase="2", db=db)

    assert cfg["voice"] == "ash"  # grammar voice config
    # Grammar prompt template is loaded from prompts.json — its content is
    # implementation detail, but the prompt must exist and be non-empty.
    assert cfg["instructions"]


def test_ephemeral_config_alt_language_swaps_accent(db):
    """Catalan mode rewrites the voice accent directive but keeps the same
    voice slot. The system prompt also flips to Catalan."""
    user = _make_user(db)
    situation = _make_situation(db, "bank_open_alt", "banking")
    conv = _make_conversation(db, user, situation)

    es_cfg = build_session_config(conv, phase="2", db=db, alt_language=None)
    ca_cfg = build_session_config(conv, phase="2", db=db, alt_language="catalan")

    assert es_cfg["voice"] == ca_cfg["voice"] == "shimmer"
    # System prompt should differ — alt-language flips the language token in
    # the conversation_agent template.
    assert es_cfg["instructions"] != ca_cfg["instructions"]


def test_ephemeral_config_phase_does_not_affect_dict_today(db):
    """Phase is carried through for observability today (no behavioral effect).
    Pin that so a future change to make phase load-bearing has to update this
    test deliberately."""
    user = _make_user(db)
    situation = _make_situation(db, "bank_open_phase", "banking")
    conv = _make_conversation(db, user, situation)

    cfg_p2 = build_session_config(conv, phase="2", db=db)
    cfg_p3 = build_session_config(conv, phase="3", db=db)

    assert cfg_p2 == cfg_p3


def test_build_session_config_raises_for_missing_situation(db):
    """If the situation row is gone (data integrity bug), fail loudly rather
    than mint a session with a broken prompt."""
    user = _make_user(db)
    # Build a Conversation pointing at a nonexistent situation_id, bypassing
    # the FK by not flushing it through the DB.
    conv = Conversation(
        id=uuid.uuid4(),
        user_id=user.id,
        situation_id="does_not_exist_xyz",
        mode="voice",
        target_word_ids=[],
        used_typed_word_ids=[],
        used_spoken_word_ids=[],
    )

    with pytest.raises(ValueError, match="missing situation"):
        build_session_config(conv, phase="2", db=db)


# ── build_session_config: server_ws mode ──────────────────────────────────────


def test_server_ws_config_disables_vad_and_omits_model(db):
    """server_ws mode is for the legacy backend-orchestrated flow. The server
    issues `response.create` itself, so VAD must be off; the model is encoded
    in the WS URL, not the session payload."""
    user = _make_user(db)
    situation = _make_situation(db, "bank_open_ws", "banking")
    conv = _make_conversation(db, user, situation)

    cfg = build_session_config(conv, phase="2", db=db, mode="server_ws")

    assert "model" not in cfg
    assert cfg["turn_detection"] is None
    assert cfg["output_audio_format"] == "pcm16"
    assert "input_audio_transcription" not in cfg
    assert cfg["voice"] == "shimmer"


# ── build_ws_session_update ───────────────────────────────────────────────────


def test_ws_session_update_matches_legacy_inline_payload():
    """Pre-refactor, `realtime_service.stream_realtime` inlined this exact
    payload. The helper must produce a byte-identical dict so the WS flow
    behaves the same."""
    voice = "shimmer"
    system_prompt = "You are a helpful Spanish tutor."

    payload = build_ws_session_update(voice=voice, instructions=system_prompt)

    assert payload == {
        "modalities": ["text", "audio"],
        "voice": "shimmer",
        "instructions": "You are a helpful Spanish tutor.",
        "output_audio_format": "pcm16",
        "turn_detection": None,
    }


def test_ws_session_update_appends_tts_style_directive():
    """When tts_instructions is provided, the legacy code appended a
    `[Voice style: ...]` block to the system prompt. Preserve that exactly —
    the realtime model has been tuned around this directive shape."""
    payload = build_ws_session_update(
        voice="ash",
        instructions="System prompt body.",
        tts_instructions="Speak with a warm tone.",
    )

    assert payload["instructions"] == (
        "System prompt body.\n\n[Voice style: Speak with a warm tone.]"
    )


def test_ws_session_update_no_tts_instructions_leaves_prompt_untouched():
    """Falsy tts_instructions must not modify the prompt — guards against a
    stray `\\n\\n[Voice style: None]` regression."""
    payload = build_ws_session_update(
        voice="ash",
        instructions="Just the system prompt.",
        tts_instructions=None,
    )
    assert payload["instructions"] == "Just the system prompt."

    payload_empty = build_ws_session_update(
        voice="ash",
        instructions="Just the system prompt.",
        tts_instructions="",
    )
    assert payload_empty["instructions"] == "Just the system prompt."
