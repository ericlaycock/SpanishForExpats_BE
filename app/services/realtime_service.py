"""OpenAI Realtime API service for combined LLM + TTS generation.

Uses WebSocket to get streamed text + audio in one call (~0.8s to first audio byte
vs ~5s with separate LLM + TTS).

Audio output is PCM16 24kHz mono, converted to MP3 via ffmpeg.
"""

import asyncio
import base64
import json
import logging
import struct
import subprocess
import time
import tempfile
from pathlib import Path
from typing import Optional

import websockets

from app.config import settings

logger = logging.getLogger(__name__)

REALTIME_MODEL = "gpt-4o-realtime-preview-2025-06-03"
REALTIME_URL = f"wss://api.openai.com/v1/realtime?model={REALTIME_MODEL}"


async def generate_with_realtime(
    messages: list,
    voice: str = "shimmer",
    tts_instructions: Optional[str] = None,
    request_id: str = "unknown",
) -> dict:
    """Generate LLM response + TTS audio via the Realtime API.

    Args:
        messages: Conversation history [{role, content}, ...]
        voice: TTS voice name
        tts_instructions: Voice style instructions (used as system prompt suffix)
        request_id: For logging

    Returns:
        {"text": str, "audio_bytes": bytes, "first_audio_ms": int, "total_ms": int}
    """
    headers = {
        "Authorization": f"Bearer {settings.openai_api_key}",
        "OpenAI-Beta": "realtime=v1",
    }

    t0 = time.time()
    first_audio_ms = None
    first_text_ms = None
    full_text = ""
    audio_chunks = []

    # Extract system prompt from messages
    system_content = ""
    conversation_items = []
    for msg in messages:
        if msg["role"] == "system":
            system_content = msg["content"]
        else:
            conversation_items.append(msg)

    # Append TTS style to system instructions if provided
    if tts_instructions:
        system_content += f"\n\n[Voice style: {tts_instructions}]"

    try:
        async with websockets.connect(REALTIME_URL, additional_headers=headers, close_timeout=5) as ws:
            connect_ms = int((time.time() - t0) * 1000)
            logger.info(f"[Realtime] Connected in {connect_ms}ms (request={request_id})")

            # Configure session
            await ws.send(json.dumps({
                "type": "session.update",
                "session": {
                    "modalities": ["text", "audio"],
                    "voice": voice,
                    "instructions": system_content,
                    "output_audio_format": "pcm16",
                    "turn_detection": None,
                }
            }))

            # Add conversation history
            for item in conversation_items:
                role = item["role"]
                content = item["content"]
                if role == "assistant":
                    await ws.send(json.dumps({
                        "type": "conversation.item.create",
                        "item": {
                            "type": "message",
                            "role": "assistant",
                            "content": [{"type": "text", "text": content}],
                        }
                    }))
                elif role == "user":
                    await ws.send(json.dumps({
                        "type": "conversation.item.create",
                        "item": {
                            "type": "message",
                            "role": "user",
                            "content": [{"type": "input_text", "text": content}],
                        }
                    }))

            # Request response
            await ws.send(json.dumps({"type": "response.create"}))

            # Collect events
            while True:
                msg = await asyncio.wait_for(ws.recv(), timeout=30)
                event = json.loads(msg)
                event_type = event.get("type", "")

                if event_type == "response.audio.delta":
                    chunk = base64.b64decode(event.get("delta", ""))
                    audio_chunks.append(chunk)
                    if first_audio_ms is None:
                        first_audio_ms = int((time.time() - t0) * 1000)

                elif event_type == "response.audio_transcript.delta":
                    full_text += event.get("delta", "")
                    if first_text_ms is None:
                        first_text_ms = int((time.time() - t0) * 1000)

                elif event_type == "response.done":
                    break

                elif event_type == "error":
                    error_msg = event.get("error", {}).get("message", str(event))
                    logger.error(f"[Realtime] Error: {error_msg}")
                    raise RuntimeError(f"Realtime API error: {error_msg}")

    except websockets.exceptions.ConnectionClosed as e:
        logger.error(f"[Realtime] WebSocket closed: {e}")
        raise
    except asyncio.TimeoutError:
        logger.error(f"[Realtime] Timeout waiting for response")
        raise

    total_ms = int((time.time() - t0) * 1000)
    audio_bytes = b"".join(audio_chunks)

    logger.info(
        f"[Realtime] Done: {total_ms}ms total, first_audio={first_audio_ms}ms, "
        f"first_text={first_text_ms}ms, text_len={len(full_text)}, "
        f"audio_bytes={len(audio_bytes)} (request={request_id})"
    )

    return {
        "text": full_text,
        "audio_bytes": audio_bytes,  # PCM16 24kHz mono
        "first_audio_ms": first_audio_ms or 0,
        "first_text_ms": first_text_ms or 0,
        "total_ms": total_ms,
    }


def pcm16_to_mp3(pcm_bytes: bytes, output_path: str, sample_rate: int = 24000):
    """Convert raw PCM16 audio to MP3 using ffmpeg."""
    result = subprocess.run(
        [
            "ffmpeg", "-y",
            "-f", "s16le",           # raw PCM16
            "-ar", str(sample_rate), # 24kHz
            "-ac", "1",              # mono
            "-i", "pipe:0",          # stdin
            "-codec:a", "libmp3lame",
            "-b:a", "64k",           # 64kbps (plenty for speech)
            output_path,
        ],
        input=pcm_bytes,
        capture_output=True,
        timeout=10,
    )
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg failed: {result.stderr.decode()[:200]}")
