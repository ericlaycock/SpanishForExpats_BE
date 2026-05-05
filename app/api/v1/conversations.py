import json as json_module
import os
from datetime import datetime, timezone
from typing import Optional
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert as pg_insert
from app.database import get_db
from app.auth import get_current_user, get_current_user_from_query
from app.models import User, Conversation, Situation, Word, UserMilestoneEvent
from app.services.word_selection_service import select_words_for_situation, sort_words_encounter_first
from app.schemas import (
    CreateConversationRequest,
    CreateConversationResponse,
    MessageRequest,
    MessageResponse,
    RealtimeTurnRequest,
    RealtimeTurnResponse,
    SentenceHintResponse,
    VoiceTurnResponse,
    WordSchema
)
from app.services.llm_gateway import generate_conversation, ConversationContext, load_prompt
from app.services.openai_media_gateway import transcribe_audio as gateway_transcribe_audio, synthesize_speech as gateway_synthesize_speech
from fastapi import Request
from app.services.word_detection import detect_words_in_text, get_words_by_ids
from app.services.conversation_service import (
    check_chat_chip_completion,
    check_conversation_complete,
    update_user_word_stats,
    get_missing_word_ids
)
from app.services.encounter_messages import get_initial_message_for_encounter
from app.api.v1.situations import get_vocab_level, get_grammar_level
from app.services.learner_context import ChipTarget, LearnerContext
from app.services.voice_turn_service import (
    EXCHANGE_HARD_LIMIT,
    build_transcription_prompt,
    build_conversation_prompt,
    build_grammar_system_prompt,
    build_grammar_user_prompt,
    get_language_mode,
    get_conversation_system_prompt,
    build_system_prompt,
    check_completion,
    persist_turn,
    validate_assistant_reply,
)
from app.data.grammar_situations import get_chat_target_forms, get_grammar_config
from app.services.alt_language_service import apply_alt_language, get_target_language_name
from app.services.closing_message_service import pick_closing_message
from app.utils.audio import generate_audio_filename, get_audio_path, get_audio_url, upload_to_r2
router = APIRouter()


def _enriched_chat_target_forms(situation_id: str) -> list[dict]:
    """Return `get_chat_target_forms` items with a stable BE chip id.

    The backend stores these on `Conversation.chat_target_forms_json`
    so completion can be checked server-side. The id convention matches
    what the FE synthesizes in `ImmersiveVoiceScene.applyDetectedWords`
    (`form:{spanish}:{pronoun}`) so chip ticks stay consistent across
    the API boundary.
    """
    forms = get_chat_target_forms(situation_id)
    enriched: list[dict] = []
    for f in forms:
        spanish = f.get("spanish") or ""
        pronoun = f.get("pronoun") or ""
        enriched.append({
            **f,
            "id": f.get("id") or f"form:{spanish}:{pronoun}",
        })
    return enriched


def _make_learner_context(
    user: User,
    situation: Situation,
    conversation: Conversation,
    *,
    vocab_level: int,
    grammar_level: float,
    completed_chip_ids: list[str] | None = None,
    target_word_objects: list[Word] | None = None,
) -> LearnerContext:
    """Assemble a LearnerContext for prompt building.

    For grammar chat lessons (`*_chat`) we read chips off
    `conversation.chat_target_forms_json` (snapshotted at creation).
    For vocab encounters we project `target_word_ids` into chips so the
    target-steering block has something to render either way.

    `completed_chip_ids` defaults to `used_spoken_word_ids` for vocab
    encounters and `[]` for grammar chats. Callers that already ran
    `check_chat_chip_completion` should pass the returned list to keep
    the prompt's "what's done" view consistent with chip-tick state.
    """
    chips: list[ChipTarget] = []
    chat_forms = conversation.chat_target_forms_json or []

    if chat_forms:
        for form in chat_forms:
            chips.append(ChipTarget(
                id=form.get("id") or f"form:{form.get('spanish', '')}:{form.get('pronoun', '')}",
                spanish=form.get("spanish") or "",
                english=form.get("english") or "",
                verb=form.get("verb"),
                pronoun=form.get("pronoun"),
            ))
        if completed_chip_ids is None:
            completed_chip_ids = []
    else:
        words = target_word_objects or []
        for word in words:
            chips.append(ChipTarget(
                id=word.id,
                spanish=word.spanish,
                english=word.english,
            ))
        if completed_chip_ids is None:
            completed_chip_ids = list(conversation.used_spoken_word_ids or [])

    return LearnerContext(
        spanish_level=user.q0_spanish_level,
        vocab_level=vocab_level,
        grammar_level=grammar_level,
        goal=situation.goal,
        target_chips=chips,
        completed_chip_ids=completed_chip_ids,
        consecutive_no_progress_turns=conversation.consecutive_no_progress_turns or 0,
    )


def _pending_chips_for_validation(
    db: Session, conversation: Conversation,
) -> list[ChipTarget]:
    """Build the pending-chip list `validate_assistant_reply` needs.

    Cheaper than `_make_learner_context` because it skips Situation /
    User / level lookups — the validator only needs each chip's Spanish
    form and the (verb, pronoun) pair (to detect grammar chips). For
    grammar chats we read straight off `chat_target_forms_json`; for
    vocab encounters we project `target_word_ids` into chips. Either
    way we filter by `completed_chip_ids` (chats) or `used_spoken_word_ids`
    (vocab) so the leak check only fires on chips the student can still
    earn.
    """
    chat_forms = conversation.chat_target_forms_json or []
    if chat_forms:
        completed = set(conversation.completed_chip_ids or [])
        chips: list[ChipTarget] = []
        for form in chat_forms:
            chip_id = form.get("id") or (
                f"form:{form.get('spanish', '')}:{form.get('pronoun', '')}"
            )
            if chip_id in completed:
                continue
            chips.append(ChipTarget(
                id=chip_id,
                spanish=form.get("spanish") or "",
                english=form.get("english") or "",
                verb=form.get("verb"),
                pronoun=form.get("pronoun"),
            ))
        return chips

    target_ids = conversation.target_word_ids or []
    if not target_ids:
        return []
    used = set(conversation.used_spoken_word_ids or [])
    pending_ids = [wid for wid in target_ids if wid not in used]
    if not pending_ids:
        return []
    words = db.query(Word).filter(Word.id.in_(pending_ids)).all()
    return [
        ChipTarget(id=w.id, spanish=w.spanish, english=w.english)
        for w in words
    ]


# Cache for initial message TTS audio URLs — avoids re-synthesizing the same audio
# Key: (situation_id, alt_language) → R2/local URL
_initial_tts_cache: dict[tuple[str, str | None], str] = {}

# OpenAI TTS voice + instructions per situation — keyed by animation_type
_ACCENT = "Speak with a Mexican Spanish accent."
_ALT_ACCENTS = {
    "catalan": "Speak with a Catalan accent.",
    "swedish": "Speak with a Swedish accent.",
}
SITUATION_VOICE_CONFIG = {
    "police": {
        "voice": "alloy",
        "instructions": f"{_ACCENT} Use an authoritative female voice, firm but professional.",
    },
    "banking": {
        "voice": "shimmer",
        "instructions": f"{_ACCENT} Use a professional, composed female voice with a warm undertone.",
    },
    "airport": {
        "voice": "shimmer",
        "instructions": f"{_ACCENT} Use a professional, clear female voice.",
    },
    "clothing": {
        "voice": "coral",
        "instructions": f"{_ACCENT} Use a casual, charming female voice.",
    },
    "small_talk": {
        "voice": "shimmer",
        "instructions": f"{_ACCENT} Use a warm, older female voice with a friendly, neighborly tone.",
    },
    "internet": {
        "voice": "coral",
        "instructions": f"{_ACCENT} Use a young, energetic female voice.",
    },
    "restaurant": {
        "voice": "ash",
        "instructions": f"{_ACCENT} Use a suave, charming male voice.",
    },
    "mechanic": {
        "voice": "ash",
        "instructions": f"{_ACCENT} Use a deep male voice.",
    },
    "groceries": {
        "voice": "ash",
        "instructions": f"{_ACCENT} Use a casual, charming male voice.",
    },
    "contractor": {
        "voice": "ash",
        "instructions": f"{_ACCENT} Use a deep, husky baritone male voice.",
    },
    "core": {
        "voice": "ash",
        "instructions": f"{_ACCENT} Use a casual, friendly male voice.",
    },
    "grammar": {
        "voice": "ash",
        "instructions": f"{_ACCENT} Use a casual, friendly male voice.",
    },
}


def get_tts_instructions(
    animation_type: str,
    alt_language: str | None = None,
    situation_id: str | None = None,
) -> tuple[str, str | None]:
    """Return (voice, instructions) for TTS, adjusted for alt language mode.

    Grammar lessons all carry animation_type='grammar', but each chat lesson
    is mapped to a specific scene/character in GRAMMAR_SCENE_MAP (small_talk
    neighbor, restaurant waiter, contractor, etc.). When a situation_id is
    supplied for a grammar lesson, defer to the mapped scene's voice config
    so the audio matches the visual character — without this, every grammar
    chat speaks in the male `ash` core voice regardless of who's on screen.
    """
    key = animation_type
    if animation_type == "grammar" and situation_id:
        from app.data.situation_roles import GRAMMAR_SCENE_MAP
        mapped = GRAMMAR_SCENE_MAP.get(situation_id)
        if mapped:
            key = mapped
    cfg = SITUATION_VOICE_CONFIG.get(key, {})
    voice = cfg.get("voice", "alloy")
    instructions = cfg.get("instructions")
    if alt_language and instructions and alt_language in _ALT_ACCENTS:
        instructions = instructions.replace(_ACCENT, _ALT_ACCENTS[alt_language])
    return voice, instructions


@router.post("", response_model=CreateConversationResponse)
async def create_conversation(
    request: CreateConversationRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new conversation"""
    import logging
    logger = logging.getLogger(__name__)
    logger.info(f"🔍 POST /v1/conversations - User: {current_user.id}, Situation: {request.situation_id}, Mode: {request.mode}")
    situation = db.query(Situation).filter(Situation.id == request.situation_id).first()
    if not situation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Situation not found"
        )
    
    # Voice mode only - reuse words from existing conversation created by startSituation
    # startSituation creates a "text" mode conversation as the source of truth for words
    existing_conv = db.query(Conversation).filter(
        Conversation.user_id == current_user.id,
        Conversation.situation_id == request.situation_id,
        Conversation.mode == "text"
    ).order_by(Conversation.created_at.desc()).with_for_update().first()
    
    if existing_conv and existing_conv.target_word_ids:
        # Reuse existing conversation's words
        target_word_ids = existing_conv.target_word_ids
        words = get_words_by_ids(db, target_word_ids)
        final_words = sort_words_encounter_first(words, request.situation_id, db, target_word_ids)
        
        # Create or get voice conversation with same words
        voice_conv = db.query(Conversation).filter(
            Conversation.user_id == current_user.id,
            Conversation.situation_id == request.situation_id,
            Conversation.mode == "voice",
            Conversation.status == "active"
        ).order_by(Conversation.created_at.desc()).with_for_update().first()

        # Snapshot the FE's chip list onto the conversation for grammar chat
        # lessons. `_enriched_chat_target_forms` returns [] for vocab/non-chat
        # situations — we leave `chat_target_forms_json` NULL there so the
        # legacy infinitive-completion path keeps running unchanged.
        chat_forms_for_db = _enriched_chat_target_forms(situation.id)

        if voice_conv:
            # Reset spoken words so backend + frontend start from same empty state.
            # Without this, reused conversations carry stale used_spoken_word_ids
            # which causes completion to fire before all word chips show checkmarks.
            # Also clear `completed_chip_ids`: `chat_target_forms_json` gets
            # re-sampled here (8 chips picked at random from the pool), so any
            # ticks from a prior session reference a different chip sample and
            # would falsely inflate this session's chips_done count.
            voice_conv.used_spoken_word_ids = []
            voice_conv.completed_chip_ids = []
            voice_conv.consecutive_no_progress_turns = 0
            voice_conv.chat_target_forms_json = chat_forms_for_db or None
            # Steering state was anchored to the prior sample; reset alongside
            # the chip list so the new session rolls a fresh target.
            voice_conv.steering_target_id = None
            voice_conv.steering_target_age = 0
            db.commit()

        if not voice_conv:
            voice_conv = Conversation(
                user_id=current_user.id,
                situation_id=request.situation_id,
                mode="voice",
                target_word_ids=target_word_ids,
                used_typed_word_ids=[],
                used_spoken_word_ids=[],
                chat_target_forms_json=chat_forms_for_db or None,
            )
            db.add(voice_conv)
            db.commit()
            db.refresh(voice_conv)

        vocab_level = get_vocab_level(db, current_user.id)
        grammar_level = get_grammar_level(db, current_user.id)
        language_mode = get_language_mode(situation.encounter_number, vocab_level, grammar_level)
        initial_message = get_initial_message_for_encounter(situation.id, situation.title, language_mode, alt_language=current_user.alt_language)

        # Alt language mode: swap words + adjust language_mode
        final_words = apply_alt_language(final_words, current_user.alt_language, db)
        if current_user.alt_language and language_mode in ("spanish_text", "spanish_audio"):
            language_mode = language_mode.replace("spanish_", f"{current_user.alt_language}_")

        # Use pre-generated R2 audio for initial message (no TTS call needed).
        # Audio files are uploaded by scripts/pregenerate_initial_audio.py with
        # deterministic filenames: initial_msg_{situation_id}.mp3
        from app.config import settings as _cfg
        initial_audio_url = f"{_cfg.r2_public_url}/initial_msg_{situation.id}.mp3" if _cfg.r2_public_url else None

        learner_ctx = _make_learner_context(
            current_user, situation, voice_conv,
            vocab_level=vocab_level, grammar_level=grammar_level,
            target_word_objects=final_words,
        )
        system_prompt = build_system_prompt(
            situation.animation_type, situation.id, language_mode,
            alt_language=current_user.alt_language,
            learner_ctx=learner_ctx,
        )
        from app.schemas import ChatTargetForm
        chat_target_forms = [
            ChatTargetForm(**f) for f in chat_forms_for_db
        ]
        scene = situation.animation_type
        if situation.animation_type == "grammar":
            from app.data.situation_roles import GRAMMAR_SCENE_MAP
            scene = GRAMMAR_SCENE_MAP.get(situation.id, "core")
        return CreateConversationResponse(
            conversation_id=voice_conv.id,
            words=[WordSchema(id=w.id, spanish=w.spanish, english=w.english, notes=w.notes) for w in final_words],
            chat_target_forms=chat_target_forms,
            scene=scene,
            initial_message=initial_message,
            initial_audio_url=initial_audio_url,
            language_mode=language_mode,
            vocab_level=vocab_level,
            system_prompt=system_prompt,
        )
    else:
        # No existing conversation - this shouldn't happen if startSituation was called first
        # But create one anyway as fallback
        encounter_word_ids, high_freq_word_ids = select_words_for_situation(
            db, current_user.id, request.situation_id,
            vocab_level=get_vocab_level(db, current_user.id),
            spanish_level=current_user.q0_spanish_level,
        )
        target_word_ids = encounter_word_ids + high_freq_word_ids
        all_words = db.query(Word).filter(Word.id.in_(target_word_ids)).all()
        final_words = sort_words_encounter_first(all_words, request.situation_id, db, target_word_ids)

        chat_forms_for_db = _enriched_chat_target_forms(situation.id)

        conversation = Conversation(
            user_id=current_user.id,
            situation_id=request.situation_id,
            mode=request.mode,
            target_word_ids=target_word_ids,
            used_typed_word_ids=[],
            used_spoken_word_ids=[],
            chat_target_forms_json=chat_forms_for_db or None,
        )
        db.add(conversation)
        db.commit()
        db.refresh(conversation)

        vocab_level = get_vocab_level(db, current_user.id)
        grammar_level = get_grammar_level(db, current_user.id)
        language_mode = get_language_mode(situation.encounter_number, vocab_level, grammar_level)
        initial_message = get_initial_message_for_encounter(situation.id, situation.title, language_mode, alt_language=current_user.alt_language)

        # Alt language mode: swap words + adjust language_mode
        final_words = apply_alt_language(final_words, current_user.alt_language, db)
        if current_user.alt_language and language_mode in ("spanish_text", "spanish_audio"):
            language_mode = language_mode.replace("spanish_", f"{current_user.alt_language}_")

        # Use pre-generated R2 audio for initial message
        from app.config import settings as _cfg2
        initial_audio_url = f"{_cfg2.r2_public_url}/initial_msg_{situation.id}.mp3" if _cfg2.r2_public_url else None

        learner_ctx = _make_learner_context(
            current_user, situation, conversation,
            vocab_level=vocab_level, grammar_level=grammar_level,
            target_word_objects=final_words,
        )
        system_prompt = build_system_prompt(
            situation.animation_type, situation.id, language_mode,
            alt_language=current_user.alt_language,
            learner_ctx=learner_ctx,
        )
        from app.schemas import ChatTargetForm
        chat_target_forms = [
            ChatTargetForm(**f) for f in chat_forms_for_db
        ]
        scene = situation.animation_type
        if situation.animation_type == "grammar":
            from app.data.situation_roles import GRAMMAR_SCENE_MAP
            scene = GRAMMAR_SCENE_MAP.get(situation.id, "core")
        return CreateConversationResponse(
            conversation_id=conversation.id,
            words=[WordSchema(id=w.id, spanish=w.spanish, english=w.english) for w in final_words],
            chat_target_forms=chat_target_forms,
            scene=scene,
            initial_message=initial_message,
            initial_audio_url=initial_audio_url,
            language_mode=language_mode,
            vocab_level=vocab_level,
            system_prompt=system_prompt,
        )


# Text chat endpoints removed - only voice chat is used now

@router.post("/check-pronunciation")
async def check_pronunciation(
    audio: UploadFile = File(...),
    expected_word: str = Form(...),
    current_user: User = Depends(get_current_user),
):
    """Lightweight pronunciation check: STT + string match. No LLM, no TTS."""
    import logging
    import re
    import unicodedata
    logger = logging.getLogger(__name__)

    audio_bytes = await audio.read()
    logger.info(f"[PronCheck] Checking pronunciation: expected='{expected_word}', audio={len(audio_bytes)} bytes")

    transcript = await gateway_transcribe_audio(
        audio_bytes=audio_bytes,
        filename=audio.filename or "audio.mp3",
        prompt=f"The user is saying a {get_target_language_name(current_user.alt_language)} word or phrase: {expected_word}. Transcribe exactly what they say.",
        language=None,
        request_id=str(current_user.id),
        user_id=str(current_user.id),
    )

    # Normalize for comparison: lowercase, strip accents, remove punctuation
    def normalize(s: str) -> str:
        s = s.lower().strip()
        s = unicodedata.normalize('NFD', s)
        s = re.sub(r'[\u0300-\u036f]', '', s)  # Remove accent marks
        s = s.replace('ñ', 'n')
        s = re.sub(r'[.,!?;:\'"¿¡]', '', s)
        s = re.sub(r'\s+', ' ', s).strip()
        return s

    norm_transcript = normalize(transcript)
    norm_expected = normalize(expected_word)
    is_correct = norm_transcript == norm_expected

    logger.info(f"[PronCheck] transcript='{transcript}' norm='{norm_transcript}' expected_norm='{norm_expected}' correct={is_correct}")

    return {"transcript": transcript, "is_correct": is_correct}


def _normalize_word_id(word_id: str) -> str:
    """Map synthetic frontend chip ids to their persisted base word_id.

    Grammar conjugation chips are synthesized client-side as `conj_<verb>_<pronoun>`
    (e.g. `conj_vivir_nosotros`) and never exist in the `words` table. Mastery
    tracking for grammar situations lives on the infinitive (`grammar_<verb>`),
    so we collapse the conjugation back to the base before any DB write.
    """
    if word_id.startswith("conj_"):
        parts = word_id.split("_")
        if len(parts) >= 3:
            return f"grammar_{parts[1]}"
    return word_id


@router.post("/{conversation_id}/mark-word")
async def mark_word_detected(
    conversation_id: str,
    word_id: str = Form(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Manually mark a word as detected (user override for STT failures)."""
    import logging
    logger = logging.getLogger(__name__)

    conversation = db.query(Conversation).filter(
        Conversation.id == conversation_id,
        Conversation.user_id == current_user.id,
    ).first()
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    normalized_word_id = _normalize_word_id(word_id)

    was_empty = len(conversation.used_spoken_word_ids or []) == 0
    current_used = set(conversation.used_spoken_word_ids or [])
    current_used.add(normalized_word_id)
    conversation.used_spoken_word_ids = list(current_used)

    from app.services.conversation_service import update_user_word_stats, check_conversation_complete, get_missing_word_ids
    update_user_word_stats(db, str(current_user.id), [normalized_word_id], "voice")

    if was_empty and conversation.conversation_type == "lesson":
        target_set = set(conversation.target_word_ids or [])
        if normalized_word_id in target_set:
            db.execute(
                pg_insert(UserMilestoneEvent)
                .values(
                    user_id=current_user.id,
                    milestone_key="first_word",
                    situation_id=conversation.situation_id,
                    conversation_id=conversation.id,
                )
                .on_conflict_do_nothing(constraint="uq_user_milestone_situation")
            )

    conversation_complete = check_conversation_complete(conversation, "voice")
    if conversation_complete:
        conversation.status = "complete"
        conversation.completed_at = datetime.now(timezone.utc)

    db.commit()
    missing_word_ids = get_missing_word_ids(conversation, "voice")
    logger.info(f"[MarkWord] User {current_user.id} marked word {word_id} (normalized={normalized_word_id}) in conversation {conversation_id}")

    return {
        "word_id": normalized_word_id,
        "missing_word_ids": missing_word_ids,
        "conversation_complete": conversation_complete,
    }


def _sync_tts(text, output_path, voice, instructions, request_id, user_id, db, learning_phase):
    """Synchronous TTS wrapper for use with run_in_executor."""
    import asyncio
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(gateway_synthesize_speech(
            text=text, output_path=output_path,
            voice=voice, instructions=instructions,
            request_id=request_id, user_id=user_id,
            db=db, learning_phase=learning_phase,
        ))
    finally:
        loop.close()


@router.get("/debug/stream-test")
async def stream_test():
    """Diagnostic: test if NDJSON streaming actually flushes through middleware.
    Yields two events 3s apart. If the client receives them 3s apart, streaming works.
    If both arrive together after 3s, middleware is buffering."""
    import asyncio
    async def generate():
        yield json_module.dumps({"type": "ping", "time": "t=0s", "message": "If you see this immediately, streaming works"}) + "\n"
        await asyncio.sleep(3)
        yield json_module.dumps({"type": "pong", "time": "t=3s", "message": "This should arrive 3s after ping"}) + "\n"
    return StreamingResponse(generate(), media_type="application/x-ndjson")


@router.post("/{conversation_id}/voice-turn")
async def voice_turn_transcribe(
    conversation_id: str,
    request: Request,
    audio: UploadFile = File(...),
    messages_json: Optional[str] = Form(None),
    # When set, the FE knows exactly what sentence the user is being asked
    # to produce (drill phase). Bias STT toward that exact sentence the same
    # way /check-pronunciation does — without the bias Whisper free-runs and
    # routinely garbles short target sentences (e.g. "nuestras familias"
    # transcribed as "¿Cómo estás, Daniel?").
    expected_text: Optional[str] = Form(None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Step 1: STT → word detection → DB update. Returns transcript immediately.
    Frontend then calls /voice-turn/respond with the transcript for LLM+TTS."""
    import time
    import logging
    logger = logging.getLogger(__name__)
    start_time = time.time()
    request_id = getattr(request.state, "request_id", "unknown")
    learning_phase = request.headers.get("X-Learning-Phase", "2")
    request.state.user_id = current_user.id

    conversation = db.query(Conversation).filter(
        Conversation.id == conversation_id,
        Conversation.user_id == current_user.id
    ).first()
    if not conversation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")
    if conversation.mode != "voice":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This endpoint is for voice mode only")

    audio_bytes = await audio.read()
    words = get_words_by_ids(db, conversation.target_word_ids)
    situation = db.query(Situation).filter(Situation.id == conversation.situation_id).first()

    alt_language = current_user.alt_language
    words = apply_alt_language(words, alt_language, db)

    if expected_text:
        # Drill mode — bias STT to the exact sentence so a near-miss doesn't
        # come back as a wildly off transcript. Phrasing mirrors the
        # benchmarked /check-pronunciation prompt (see line 653) exactly,
        # only swapping "word or phrase" for "sentence".
        transcription_prompt = (
            f"The user is saying a {get_target_language_name(alt_language)} sentence: "
            f"{expected_text}. Transcribe exactly what they say."
        )
    else:
        transcription_prompt = build_transcription_prompt(
            situation.title if situation else "a situation", words, alt_language=alt_language,
        )

    stt_start = time.time()
    user_transcript = await gateway_transcribe_audio(
        audio_bytes=audio_bytes, filename=audio.filename or "audio.mp3",
        prompt=transcription_prompt, language=None,
        request_id=request_id, user_id=str(current_user.id),
        db=db, learning_phase=learning_phase,
    )
    stt_time = time.time() - stt_start
    logger.info(f"[Voice Turn] STT: {stt_time:.2f}s, transcript: '{user_transcript}'")
    if stt_time > 2.0:
        logger.warning(f"[Voice Turn] STT exceeded 2s threshold: {stt_time:.2f}s")

    # Shared with /realtime-turn: detects words (grammar-aware when applicable),
    # extends used_spoken_word_ids, upserts user_words counters, records the
    # first_word milestone, and increments turn_count.
    _, detected_word_ids = persist_turn(
        db=db,
        conversation=conversation,
        user_id=current_user.id,
        user_transcript=user_transcript,
        assistant_text="",
        alt_language=alt_language,
    )
    missing_word_ids = get_missing_word_ids(conversation, "voice")
    db.commit()

    total = time.time() - start_time
    logger.info(f"[Voice Turn] Transcribe total: {total:.2f}s (stt: {stt_time:.2f}s)")

    return {
        "user_transcript": user_transcript,
        "detected_word_ids": detected_word_ids,
        "missing_word_ids": missing_word_ids,
    }


from pydantic import BaseModel as _BaseModel

class _RespondRequest(_BaseModel):
    user_transcript: str
    messages_json: Optional[str] = None


@router.post("/{conversation_id}/voice-turn/respond")
async def voice_turn_respond(
    conversation_id: str,
    body: _RespondRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Step 2: LLM → TTS → R2 upload. Returns AI response + audio URL."""
    import time
    import logging
    logger = logging.getLogger(__name__)
    start_time = time.time()
    request_id = getattr(request.state, "request_id", "unknown")
    learning_phase = request.headers.get("X-Learning-Phase", "2")
    request.state.user_id = current_user.id

    conversation = db.query(Conversation).filter(
        Conversation.id == conversation_id,
        Conversation.user_id == current_user.id
    ).first()
    if not conversation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")

    words = get_words_by_ids(db, conversation.target_word_ids)
    situation = db.query(Situation).filter(Situation.id == conversation.situation_id).first()
    alt_language = current_user.alt_language
    words = apply_alt_language(words, alt_language, db)

    user_transcript = body.user_transcript

    # Parse frontend messages
    frontend_messages = None
    if body.messages_json:
        try:
            frontend_messages = json_module.loads(body.messages_json)
        except (json_module.JSONDecodeError, TypeError):
            pass

    vocab_level = get_vocab_level(db, current_user.id)
    grammar_level = get_grammar_level(db, current_user.id)
    language_mode = get_language_mode(situation.encounter_number, vocab_level, grammar_level)
    if alt_language and language_mode in ("spanish_text", "spanish_audio"):
        language_mode = language_mode.replace("spanish_", f"{alt_language}_")

    # `persist_turn` from step 1 (`POST /voice-turn`) already updated the
    # cumulative chip set on the conversation row, so we just read it here.
    # Refresh first so we see what step 1 wrote in this same request cycle.
    db.refresh(conversation)
    completed_chip_ids = list(conversation.completed_chip_ids or [])
    target_chip_ids = {
        f.get("id") for f in (conversation.chat_target_forms_json or []) if f.get("id")
    }
    chips_total = len(target_chip_ids)
    # Only count ticks for chip ids that are actually in this session's chip
    # sample. Without this filter, ticks from a prior session (different
    # sample) inflate the count and the closer fires early.
    chip_complete = chips_total > 0 and target_chip_ids.issubset(set(completed_chip_ids))

    # The v3 prompt is level-aware, target-anchored, and reads chip state
    # straight off the conversation. No more side-band injection of
    # English "thinking" messages — targeting lives entirely in the
    # system prompt now.
    learner_ctx = _make_learner_context(
        current_user, situation, conversation,
        vocab_level=vocab_level, grammar_level=grammar_level,
        completed_chip_ids=completed_chip_ids if conversation.chat_target_forms_json else None,
        target_word_objects=words,
    )

    grammar_config_for_prompt = get_grammar_config(conversation.situation_id)
    if grammar_config_for_prompt:
        system_prompt = build_grammar_system_prompt(
            conversation.situation_id,
            language_mode=language_mode,
            alt_language=alt_language,
            learner_ctx=learner_ctx,
        )
    else:
        system_prompt = get_conversation_system_prompt(
            language_mode, alt_language=alt_language,
            animation_type=situation.animation_type if situation else "",
            situation_id=conversation.situation_id,
            learner_ctx=learner_ctx,
        )

    if frontend_messages:
        llm_messages = [{"role": "system", "content": system_prompt}]
        for msg in frontend_messages:
            if msg["role"] != "system":
                llm_messages.append(msg)
        llm_messages.append({"role": "user", "content": user_transcript})
    else:
        # Cold-start: no FE history. Pair the v3 system prompt with a
        # minimal user-prompt that surfaces the latest transcript and the
        # situation context. The legacy `build_grammar_user_prompt` /
        # `build_conversation_prompt` helpers still do the heavy lifting
        # for the non-history case so we don't duplicate that copy here.
        if grammar_config_for_prompt:
            user_prompt = build_grammar_user_prompt(
                situation.title, conversation.used_spoken_word_ids or [],
                user_transcript, grammar_config_for_prompt,
            )
        else:
            user_prompt = build_conversation_prompt(
                situation.title, words, conversation.used_spoken_word_ids or [],
                user_transcript, alt_language=alt_language,
            )
        llm_messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

    # ── Closing-turn bypass ──────────────────────────────────────────
    # When the student's transcript already ticked the LAST chip (or
    # achieved full vocab coverage in legacy non-chat encounters), the
    # encounter is functionally over but the v3 prompt's TURN-CLOSING
    # RULE still forces a `?` on the avatar's reply, so the student
    # gets one more question with nothing useful to answer. The bypass
    # swaps `llm_messages` for a "TTS engine, read this verbatim"
    # prompt + a canned closing line picked from
    # `app/data/closing_messages.py`. The Realtime API still streams
    # text + audio in the avatar's voice, so the FE flow is unchanged.
    if conversation.chat_target_forms_json:
        would_be_complete = chip_complete
    else:
        would_be_complete, _ = check_completion(conversation)
    if would_be_complete:
        closing_text = pick_closing_message(
            situation.animation_type if situation else "",
            alt_language=alt_language,
            seed_key=conversation.situation_id,
        )
        llm_messages = [
            {
                "role": "system",
                "content": (
                    "You are a TTS engine. Read aloud EXACTLY the user's "
                    "message, word-for-word, with natural prosody. Do not "
                    "greet, acknowledge, paraphrase, expand, summarize, "
                    "translate, or add ANY words before or after. If you "
                    "add 'Claro', 'Okay', '¡Hola!', or any other "
                    "acknowledgment you have failed."
                ),
            },
            {"role": "user", "content": closing_text},
        ]
        logger.info(
            f"[Voice Turn] Closing bypass: anim="
            f"{situation.animation_type if situation else ''}, "
            f"text={closing_text!r}"
        )

    # TTS voice config
    tts_voice, tts_instructions = get_tts_instructions(
        situation.animation_type if situation else "",
        alt_language=alt_language,
        situation_id=situation.id if situation else None,
    )

    # Log full messages object for debugging
    logger.info(f"[Voice Turn] Realtime messages for {conversation.situation_id} (voice={tts_voice}):\n"
                 + json_module.dumps(llm_messages, indent=2, ensure_ascii=False))

    # ── Realtime API: stream LLM + TTS as NDJSON ──
    # Audio chunks arrive at ~0.8s. Frontend plays PCM16 via Web Audio API.
    from app.services.realtime_service import stream_realtime
    import base64 as _base64

    async def generate_stream():
        assistant_text = ""
        try:
            async for event in stream_realtime(
                messages=llm_messages,
                voice=tts_voice,
                tts_instructions=tts_instructions,
                request_id=request_id,
            ):
                if event["type"] == "audio":
                    yield json_module.dumps({
                        "type": "audio",
                        "data": _base64.b64encode(event["data"]).decode(),
                    }) + "\n"

                elif event["type"] == "text":
                    assistant_text = event["text"]
                    yield json_module.dumps({
                        "type": "text",
                        "text": assistant_text,
                    }) + "\n"

                elif event["type"] == "done":
                    # Refresh conversation from DB to ensure we have latest
                    # used_spoken_word_ids and the stuck counter persist_turn
                    # just bumped.
                    db.refresh(conversation)
                    # Run the v3-rule validator against the assistant text we
                    # just streamed. Audio is already playing on the client so
                    # we can't regenerate, but we capture the violation in
                    # `avatar_dead_end_turns` and surface a flag in the `done`
                    # payload for the FE to render a soft nudge.
                    pending_chips_for_validation = learner_ctx.pending_chips()
                    flagged, leaked_ids, dead_end_reasons = validate_assistant_reply(
                        assistant_text, pending_chips_for_validation,
                    )
                    if flagged:
                        conversation.avatar_dead_end_turns = (
                            conversation.avatar_dead_end_turns or 0
                        ) + 1
                        logger.warning(
                            f"[Voice Turn] Avatar dead-end detected: "
                            f"reasons={dead_end_reasons}, "
                            f"text={assistant_text!r}"
                        )
                    # Grammar chats with a chip snapshot complete only when
                    # every chip ticks; vocab/non-chat grammar fall back to
                    # the legacy infinitive-coverage check.
                    if conversation.chat_target_forms_json:
                        conv_complete = chip_complete or (
                            conversation.turn_count or 0
                        ) >= EXCHANGE_HARD_LIMIT
                    else:
                        conv_complete, _ = check_completion(conversation)
                    logger.info(
                        f"[Voice Turn] Completion check: target={conversation.target_word_ids}, "
                        f"spoken={conversation.used_spoken_word_ids}, "
                        f"chips_done={len(completed_chip_ids)}/"
                        f"{len(conversation.chat_target_forms_json or [])}, "
                        f"no_progress={conversation.consecutive_no_progress_turns}, "
                        f"dead_ends={conversation.avatar_dead_end_turns}, "
                        f"turns={conversation.turn_count}, complete={conv_complete}"
                    )
                    if conv_complete:
                        conversation.status = "complete"
                        conversation.completed_at = datetime.now(timezone.utc)
                    db.commit()

                    total = time.time() - start_time
                    logger.info(f"[Voice Turn] Realtime stream: {total:.2f}s, text='{assistant_text[:60]}'")

                    yield json_module.dumps({
                        "type": "done",
                        "conversation_complete": conv_complete,
                        "completed_chip_ids": completed_chip_ids,
                        "consecutive_no_progress_turns": conversation.consecutive_no_progress_turns or 0,
                        "avatar_dead_end": flagged,
                    }) + "\n"

        except Exception as e:
            logger.error(f"[Voice Turn] Realtime stream failed: {e}")
            yield json_module.dumps({"type": "error", "message": str(e)}) + "\n"

    return StreamingResponse(generate_stream(), media_type="application/x-ndjson")


@router.post(
    "/{conversation_id}/realtime-turn",
    response_model=RealtimeTurnResponse,
)
async def realtime_turn(
    conversation_id: str,
    body: RealtimeTurnRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Ingest one completed realtime-voice turn.

    The browser streams audio directly to OpenAI over WebRTC (see
    `POST /v1/realtime/sessions`), so the backend doesn't see the audio or
    control endpointing. After each turn the FE POSTs the finalized
    transcripts here so we can:
      - run deterministic word detection against the conversation's targets,
      - extend `used_spoken_word_ids` and bump mastery counters,
      - increment `turn_count` and enforce the 30-turn hard limit,
      - record the `first_word` milestone for new lesson conversations,
      - report back the current state so the FE can update chips,
        countdowns, and close the peer connection on completion.

    Parity note: the word detection, persistence, and completion logic are
    the same helpers `/voice-turn` calls — splitting by flow would be a
    parity bug waiting to happen.
    """
    request.state.user_id = current_user.id

    conversation = db.query(Conversation).filter(
        Conversation.id == conversation_id,
        Conversation.user_id == current_user.id,
    ).first()
    if not conversation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found"
        )
    if conversation.mode != "voice":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This endpoint is for voice mode only",
        )

    _, detected_word_ids = persist_turn(
        db=db,
        conversation=conversation,
        user_id=current_user.id,
        user_transcript=body.user_transcript,
        assistant_text=body.assistant_text,
        alt_language=current_user.alt_language,
    )

    # v3-rule validation against the assistant's reply. WebRTC audio has
    # already played client-side so we can't regenerate, but we still
    # tally violations for telemetry and surface a flag for the FE.
    pending_chips = _pending_chips_for_validation(db, conversation)
    avatar_flagged, _leaked, dead_end_reasons = validate_assistant_reply(
        body.assistant_text or "", pending_chips,
    )
    if avatar_flagged:
        conversation.avatar_dead_end_turns = (
            conversation.avatar_dead_end_turns or 0
        ) + 1
        import logging as _logging
        _logging.getLogger(__name__).warning(
            f"[Realtime Turn] Avatar dead-end detected: "
            f"reasons={dead_end_reasons}, text={body.assistant_text!r}"
        )

    # Grammar chats with a chip snapshot complete only when every chip ticks;
    # vocab/non-chat grammar fall back to the legacy infinitive-coverage check.
    if conversation.chat_target_forms_json:
        target_chip_ids_rt = {
            f.get("id") for f in conversation.chat_target_forms_json if f.get("id")
        }
        completed_set_rt = set(conversation.completed_chip_ids or [])
        chip_complete = bool(target_chip_ids_rt) and target_chip_ids_rt.issubset(completed_set_rt)
        _, turns_remaining = check_completion(conversation)
        complete = chip_complete or (conversation.turn_count or 0) >= EXCHANGE_HARD_LIMIT
    else:
        complete, turns_remaining = check_completion(conversation)
    if complete and conversation.status != "complete":
        conversation.status = "complete"
        conversation.completed_at = datetime.now(timezone.utc)

    # Realtime steering: pick the chip the FE should ask the model to elicit
    # next, with 2-turn stickiness. Skipped on completion — the FE plays the
    # closer instead. If the user just landed the active steering target, we
    # reset the stickiness state before picking so the next turn rolls fresh.
    response_instructions: Optional[str] = None
    steering_target_id: Optional[str] = None
    if not complete:
        from app.services import realtime_steering

        realtime_steering.reset_steering_if_landed(conversation)
        target_id, target_form = realtime_steering.pick_next_target(db, conversation)
        if target_id and target_form:
            response_instructions = realtime_steering.build_response_instructions(target_form)
            steering_target_id = target_id

    db.commit()
    missing_word_ids = get_missing_word_ids(conversation, "voice")

    return RealtimeTurnResponse(
        detected_word_ids=detected_word_ids,
        missing_word_ids=missing_word_ids,
        conversation_complete=complete,
        turns_remaining=turns_remaining,
        completed_chip_ids=list(conversation.completed_chip_ids or []),
        consecutive_no_progress_turns=conversation.consecutive_no_progress_turns or 0,
        avatar_dead_end=avatar_flagged,
        # `steering_text` is deprecated by `response_instructions`; kept as
        # an explicit None so the FE upgrade can land independently.
        steering_text=None,
        steering_target_id=steering_target_id,
        response_instructions=response_instructions,
    )


# ── "Need help?" sentence hint ────────────────────────────────────────
# Avatar-side button on /voice-chat. Pulls the conversation's pending
# items (vocab `word_*` or grammar `conj_<verb>_<pronoun>` candidates),
# asks the LLM for ONE sentence the user could say next, TTS'es it with
# the character voice, and audits the result. Capped per conversation
# to keep cost predictable. Does NOT touch turn_count or
# used_spoken_word_ids — see issue ericlaycock/SpanishForExpats_BE#12.

class _SentenceHintRequest(_BaseModel):
    # Optional: FE may pass the recent message log (same shape it uses
    # for /voice-turn/respond) so the suggestion matches the live thread.
    # When absent we fall back to "no prior turns" in the prompt.
    messages_json: Optional[str] = None


@router.post(
    "/{conversation_id}/sentence-hint",
    response_model=SentenceHintResponse,
)
async def sentence_hint(
    conversation_id: str,
    body: _SentenceHintRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Generate one short Spanish sentence the learner could say next."""
    import logging as _logging
    from app.services.sentence_hint_service import (
        compute_pending_items,
        generate_sentence_hint,
        persist_hint_audit,
    )
    from app.core.logger import log_event

    logger = _logging.getLogger(__name__)
    request_id = getattr(request.state, "request_id", "unknown")
    # Stringify so the request_logging middleware's JSON encoder doesn't
    # choke when an HTTPException bubbles up before the success path.
    request.state.user_id = str(current_user.id)

    conversation = (
        db.query(Conversation)
        .filter(
            Conversation.id == conversation_id,
            Conversation.user_id == current_user.id,
        )
        .with_for_update()
        .first()
    )
    if not conversation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found"
        )
    if conversation.mode != "voice":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This endpoint is for voice mode only",
        )
    if conversation.status == "complete":
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="NO_PENDING_ITEMS"
        )

    used = conversation.sentence_hints_used or 0
    # No cap on hint requests — keep the counter for telemetry, never block.

    alt_language = current_user.alt_language
    pending_items = compute_pending_items(db, conversation, alt_language)
    if not pending_items:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="NO_PENDING_ITEMS"
        )

    recent_messages = None
    if body.messages_json:
        try:
            recent_messages = json_module.loads(body.messages_json)
            if not isinstance(recent_messages, list):
                recent_messages = None
        except (json_module.JSONDecodeError, TypeError):
            recent_messages = None

    english_text, llm_request_id = await generate_sentence_hint(
        db,
        user_id=str(current_user.id),
        request_id=request_id,
        pending_items=pending_items,
        recent_messages=recent_messages,
    )

    # Increment + audit + commit. The cap check above already locked the
    # conversation row via with_for_update so two parallel hint requests
    # serialize through the increment cleanly.
    conversation.sentence_hints_used = used + 1
    persist_hint_audit(
        db,
        conversation=conversation,
        user_id=current_user.id,
        english_gloss=english_text,
        pending_count=len(pending_items),
        llm_request_id=llm_request_id,
    )
    db.commit()

    log_event(
        level="info",
        event="sentence_hint_used",
        message=f"Sentence hint generated for conversation {conversation_id}",
        request_id=request_id,
        user_id=str(current_user.id),
        extra={
            "conversation_id": str(conversation.id),
            "situation_id": conversation.situation_id,
            "pending_count": len(pending_items),
            "hints_used": conversation.sentence_hints_used,
        },
    )

    # FE still expects a non-zero `hints_remaining`. Stuff a high sentinel
    # so the disabled-rate-limit branch never fires.
    return SentenceHintResponse(
        english_gloss=english_text,
        hints_remaining=999,
    )
