"""OpenAI Media Gateway for STT and TTS with logging"""
from typing import Optional, Dict, Any, Tuple
import base64
import hashlib
import time
import uuid
import io
import logging
from openai import OpenAI
from sqlalchemy.orm import Session
from app.models import STTRequest, TTSRequest
from app.core.logger import log_event
from app.config import settings

PROVIDER = "openai"
STT_MODEL = "whisper-1"
TTS_MODEL = "gpt-4o-mini-tts"

# Lazy initialization
_client = None

def get_client() -> OpenAI:
    """Get or create OpenAI client"""
    global _client
    if _client is None:
        _client = OpenAI(api_key=settings.openai_api_key)
    return _client


def sha256_hash(data: bytes) -> str:
    """Calculate SHA256 hash of data"""
    return hashlib.sha256(data).hexdigest()


async def transcribe_audio(
    audio_bytes: bytes,
    filename: str,
    prompt: Optional[str] = None,
    language: Optional[str] = None,
    request_id: str = None,
    user_id: Optional[str] = None,
    db: Session = None,
    learning_phase: Optional[str] = None
) -> str:
    """
    Transcribe audio using OpenAI STT with full logging.
    
    Args:
        audio_bytes: Raw audio data
        filename: Original filename (for format detection)
        prompt: Optional prompt for better transcription
        language: Optional language hint (e.g., "es", "en")
        request_id: Correlation ID
        user_id: Optional user ID
        db: Database session
    
    Returns:
        Transcribed text
    """
    start_time = time.time()
    stt_request_id = uuid.uuid4()
    
    # Detect audio format from filename
    audio_format = filename.split(".")[-1].lower() if "." in filename else "mp3"
    
    # Calculate hash
    audio_sha256 = sha256_hash(audio_bytes)
    
    # Convert user_id to UUID if string
    user_id_uuid = None
    if user_id:
        if isinstance(user_id, str):
            user_id_uuid = uuid.UUID(user_id)
        else:
            user_id_uuid = user_id
    
    # Insert initial record (success=false)
    stt_record = None
    if db:
        stt_record = STTRequest(
            id=stt_request_id,
            request_id=request_id or "unknown",
            user_id=user_id_uuid,
            provider=PROVIDER,
            model=STT_MODEL,
            audio_sha256=audio_sha256,
            audio_bytes=len(audio_bytes),
            audio_format=audio_format,
            language=language,
            success=False
        )
        db.add(stt_record)
        db.commit()
        db.refresh(stt_record)
    
    # Log start event
    extra = {
        "provider": PROVIDER,
        "model": STT_MODEL,
        "audio_format": audio_format,
        "audio_bytes": len(audio_bytes),
        "language": language,
    }
    if learning_phase:
        extra["learning_phase"] = learning_phase
    log_event(
        level="info",
        event="stt_start",
        message=f"STT request started: {len(audio_bytes)} bytes",
        request_id=request_id or "unknown",
        user_id=str(user_id) if user_id else None,
        extra=extra
    )
    
    try:
        # Call OpenAI STT
        client = get_client()
        audio_file = io.BytesIO(audio_bytes)
        audio_file.name = filename
        
        params = {
            "model": STT_MODEL,
            "file": audio_file,
        }
        
        if language:
            params["language"] = language
        if prompt:
            params["prompt"] = prompt
        
        transcript_response = client.audio.transcriptions.create(**params)
        transcript_text = transcript_response.text
        
        # Calculate latency
        latency_ms = int((time.time() - start_time) * 1000)
        
        # Estimate cost (Whisper: $0.006 per minute)
        # Rough estimate: assume 1 minute per 1MB of audio
        estimated_cost = None
        if len(audio_bytes) > 0:
            # Very rough estimate - actual duration would require audio analysis
            estimated_minutes = len(audio_bytes) / (1024 * 1024)  # Assume 1MB = 1 minute
            estimated_cost = estimated_minutes * 0.006
        
        # Update record with success
        if db and stt_record:
            stt_record.success = True
            stt_record.transcript_text = transcript_text
            stt_record.output_json = {"text": transcript_text}
            stt_record.latency_ms = latency_ms
            stt_record.estimated_cost = estimated_cost
            db.commit()
        
        # Log success event
        extra_success = {
            "provider": PROVIDER,
            "model": STT_MODEL,
            "latency_ms": latency_ms,
            "audio_seconds": None,  # Would need audio analysis
            "output_chars": len(transcript_text),
            "estimated_cost": estimated_cost,
            "success": True,
        }
        if learning_phase:
            extra_success["learning_phase"] = learning_phase
        log_event(
            level="info",
            event="stt_success",
            message=f"STT completed: {latency_ms}ms, {len(transcript_text)} chars",
            request_id=request_id or "unknown",
            user_id=str(user_id) if user_id else None,
            extra=extra_success
        )
        
        return transcript_text
        
    except Exception as e:
        # Calculate latency even on error
        latency_ms = int((time.time() - start_time) * 1000)
        
        # Determine error code
        error_code = type(e).__name__
        error_message = str(e)
        
        # Update record with failure
        if db and stt_record:
            stt_record.success = False
            stt_record.latency_ms = latency_ms
            stt_record.error_code = error_code
            stt_record.error_message = error_message
            db.commit()
        
        # Log failure event
        extra_failure = {
            "provider": PROVIDER,
            "model": STT_MODEL,
            "latency_ms": latency_ms,
            "error_code": error_code,
            "error_message": error_message,
            "success": False,
        }
        if learning_phase:
            extra_failure["learning_phase"] = learning_phase
        log_event(
            level="error",
            event="stt_failure",
            message=f"STT failed: {error_code} - {error_message}",
            request_id=request_id or "unknown",
            user_id=str(user_id) if user_id else None,
            extra=extra_failure
        )
        
        # Re-raise exception
        raise


async def synthesize_speech(
    text: str,
    output_path: str,
    voice: str = "alloy",
    instructions: Optional[str] = None,
    request_id: str = None,
    user_id: Optional[str] = None,
    db: Session = None,
    learning_phase: Optional[str] = None
) -> str:
    """
    Synthesize speech using OpenAI TTS with full logging.
    
    Args:
        text: Text to synthesize
        output_path: Path to save audio file
        voice: Voice to use (alloy, echo, fable, onyx, nova, shimmer)
        request_id: Correlation ID
        user_id: Optional user ID
        db: Database session
    
    Returns:
        Path to generated audio file
    """
    start_time = time.time()
    tts_request_id = uuid.uuid4()
    
    # Calculate hash of input text
    input_text_sha256 = sha256_hash(text.encode('utf-8'))
    input_chars = len(text)
    
    # Detect output format from path
    output_format = output_path.split(".")[-1].lower() if "." in output_path else "mp3"
    
    # Convert user_id to UUID if string
    user_id_uuid = None
    if user_id:
        if isinstance(user_id, str):
            user_id_uuid = uuid.UUID(user_id)
        else:
            user_id_uuid = user_id
    
    # Insert initial record (success=false)
    tts_record = None
    if db:
        tts_record = TTSRequest(
            id=tts_request_id,
            request_id=request_id or "unknown",
            user_id=user_id_uuid,
            provider=PROVIDER,
            model=TTS_MODEL,
            voice=voice,
            input_text_sha256=input_text_sha256,
            input_chars=input_chars,
            output_format=output_format,
            success=False
        )
        db.add(tts_record)
        db.commit()
        db.refresh(tts_record)
    
    # Log start event
    extra_tts_start = {
        "provider": PROVIDER,
        "model": TTS_MODEL,
        "voice": voice,
        "input_chars": input_chars,
        "output_format": output_format,
    }
    if learning_phase:
        extra_tts_start["learning_phase"] = learning_phase
    log_event(
        level="info",
        event="tts_start",
        message=f"TTS request started: {input_chars} chars",
        request_id=request_id or "unknown",
        user_id=str(user_id) if user_id else None,
        extra=extra_tts_start
    )
    
    try:
        # Call OpenAI TTS
        client = get_client()
        tts_kwargs = dict(model=TTS_MODEL, voice=voice, input=text)
        if instructions:
            tts_kwargs["instructions"] = instructions
        response = client.audio.speech.create(**tts_kwargs)
        
        # Save to file and get size
        audio_bytes_written = 0
        with open(output_path, "wb") as f:
            for chunk in response.iter_bytes():
                f.write(chunk)
                audio_bytes_written += len(chunk)
        
        # Calculate latency
        latency_ms = int((time.time() - start_time) * 1000)
        
        # Estimate cost (TTS: $15 per 1M characters)
        estimated_cost = (input_chars / 1_000_000) * 15
        
        # Update record with success
        if db and tts_record:
            tts_record.success = True
            tts_record.audio_bytes = audio_bytes_written
            tts_record.audio_path = output_path
            tts_record.latency_ms = latency_ms
            tts_record.estimated_cost = estimated_cost
            db.commit()
        
        # Log success event
        extra_tts_success = {
            "provider": PROVIDER,
            "model": TTS_MODEL,
            "latency_ms": latency_ms,
            "audio_bytes": audio_bytes_written,
            "estimated_cost": estimated_cost,
            "success": True,
        }
        if learning_phase:
            extra_tts_success["learning_phase"] = learning_phase
        log_event(
            level="info",
            event="tts_success",
            message=f"TTS completed: {latency_ms}ms, {audio_bytes_written} bytes",
            request_id=request_id or "unknown",
            user_id=str(user_id) if user_id else None,
            extra=extra_tts_success
        )
        
        return output_path
        
    except Exception as e:
        # Calculate latency even on error
        latency_ms = int((time.time() - start_time) * 1000)
        
        # Determine error code
        error_code = type(e).__name__
        error_message = str(e)
        
        # Update record with failure
        if db and tts_record:
            tts_record.success = False
            tts_record.latency_ms = latency_ms
            tts_record.error_code = error_code
            tts_record.error_message = error_message
            db.commit()
        
        # Log failure event
        extra_tts_failure = {
            "provider": PROVIDER,
            "model": TTS_MODEL,
            "latency_ms": latency_ms,
            "error_code": error_code,
            "error_message": error_message,
            "success": False,
        }
        if learning_phase:
            extra_tts_failure["learning_phase"] = learning_phase
        log_event(
            level="error",
            event="tts_failure",
            message=f"TTS failed: {error_code} - {error_message}",
            request_id=request_id or "unknown",
            user_id=str(user_id) if user_id else None,
            extra=extra_tts_failure
        )

        # Re-raise exception
        raise


V2V_MODEL = "gpt-4o-audio-preview"
_v2v_logger = logging.getLogger(__name__)


def _convert_to_wav(audio_bytes: bytes, source_format: str) -> bytes:
    """Convert audio from any format to WAV using ffmpeg via subprocess.
    gpt-4o-audio-preview only accepts 'wav' and 'mp3' input formats."""
    import subprocess
    import tempfile
    import os

    with tempfile.NamedTemporaryFile(suffix=f".{source_format}", delete=False) as src:
        src.write(audio_bytes)
        src_path = src.name

    dst_path = src_path.rsplit(".", 1)[0] + ".wav"

    try:
        subprocess.run(
            ["ffmpeg", "-i", src_path, "-ar", "16000", "-ac", "1", "-f", "wav", dst_path],
            capture_output=True, check=True, timeout=30,
        )
        with open(dst_path, "rb") as f:
            return f.read()
    finally:
        for p in (src_path, dst_path):
            try:
                os.unlink(p)
            except OSError:
                pass


def _run_v2v_sync(
    audio_b64: str,
    system_prompt: str,
    context_prompt: str,
    voice: str,
) -> Tuple[bytes, str]:
    """Synchronous V2V call — meant to run in a thread via asyncio.to_thread."""
    client = get_client()
    response = client.chat.completions.create(
        model=V2V_MODEL,
        modalities=["text", "audio"],
        audio={"voice": voice, "format": "mp3"},
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": [
                {"type": "input_audio", "input_audio": {"data": audio_b64, "format": "wav"}},
                {"type": "text", "text": context_prompt},
            ]},
        ],
    )
    audio_data = base64.b64decode(response.choices[0].message.audio.data)
    transcript = response.choices[0].message.audio.transcript
    return audio_data, transcript


async def voice_to_voice(
    audio_bytes: bytes,
    audio_format: str,
    system_prompt: str,
    context_prompt: str,
    voice: str = "nova",
    request_id: Optional[str] = None,
    user_id: Optional[str] = None,
) -> Tuple[bytes, str]:
    """Voice-to-voice: send user audio + context, get back (audio_bytes, transcript).

    Uses gpt-4o-audio-preview Chat Completions with audio modality.
    Converts input audio to WAV (the only formats accepted by the model are wav/mp3).
    Runs the blocking OpenAI SDK call in a thread for true async.
    """
    import asyncio
    start_time = time.time()
    _v2v_logger.info(f"[V2V] Starting voice-to-voice: audio={len(audio_bytes)} bytes, format={audio_format}, voice={voice}")

    # Convert to WAV if not already wav/mp3
    if audio_format not in ("wav", "mp3"):
        _v2v_logger.info(f"[V2V] Converting {audio_format} → wav")
        audio_bytes = _convert_to_wav(audio_bytes, audio_format)
        _v2v_logger.info(f"[V2V] Converted to WAV: {len(audio_bytes)} bytes")

    audio_b64 = base64.b64encode(audio_bytes).decode()

    try:
        audio_data, transcript = await asyncio.to_thread(
            _run_v2v_sync, audio_b64, system_prompt, context_prompt, voice
        )
    except Exception as e:
        latency_ms = int((time.time() - start_time) * 1000)
        # Log the full error including any response body
        error_body = ""
        if hasattr(e, "response"):
            try:
                error_body = e.response.text
            except Exception:
                error_body = str(e.response)
        _v2v_logger.error(f"[V2V] FAILED after {latency_ms}ms: {type(e).__name__}: {e}\nResponse body: {error_body}")
        raise

    latency_ms = int((time.time() - start_time) * 1000)
    _v2v_logger.info(f"[V2V] Complete: {latency_ms}ms, audio_out={len(audio_data)} bytes, transcript={transcript[:80]}...")

    return audio_data, transcript
