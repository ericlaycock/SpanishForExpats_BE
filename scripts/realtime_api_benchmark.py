#!/usr/bin/env python3
"""Benchmark: Realtime API (combined LLM+TTS) vs current separate LLM+TTS.

Measures time-to-first-audio-byte and total time for both approaches.

Usage:
    python scripts/realtime_api_benchmark.py
"""

import os
import sys
import time
import json
import asyncio
import websockets

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=OPENAI_API_KEY)

# Test case: Banking first turn
SYSTEM_PROMPT = (
    "You are a 40 year old woman who works as a bank teller - poised, methodical, "
    "and quietly observant, speaking to a customer at the bank. the customer needs "
    "help with their bank account. You are assisting them at the counter.\n\n"
    "Speak mostly in English with occasional Spanish words. 1-2 sentences max."
)
ASSISTANT_OPENER = "Good morning -- how can I help you today?"
USER_MESSAGE = (
    "Hi, I need to check something on my account please.\n\n"
    "[HIDDEN INSTRUCTION — do not repeat this to the user. Gently guide the "
    "conversation in a way that will require me to use one of these words/phrases. "
    "Do not state these Spanish words yourself: banco, cajero, cliente, hola, chao]"
)

MESSAGES = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "assistant", "content": ASSISTANT_OPENER},
    {"role": "user", "content": USER_MESSAGE},
]


def test_current_approach():
    """Current: separate LLM (Responses API) + TTS."""
    print("\n=== CURRENT: Separate LLM + TTS ===")

    # LLM
    t0 = time.time()
    response = client.responses.create(
        model="gpt-5.4-mini",
        input=MESSAGES,
        reasoning={"effort": "low"},
    )
    llm_time = time.time() - t0
    text = response.output_text
    print(f"  LLM: {llm_time:.2f}s — \"{text}\"")

    # TTS
    t1 = time.time()
    tts_response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="shimmer",
        input=text,
        instructions="Speak with a Mexican Spanish accent, mixing English and Spanish words naturally. Use a professional, composed female voice with a warm undertone.",
    )
    audio_bytes = b""
    first_byte_time = None
    for chunk in tts_response.iter_bytes():
        if first_byte_time is None:
            first_byte_time = time.time() - t1
        audio_bytes += chunk
    tts_time = time.time() - t1
    total = time.time() - t0

    print(f"  TTS: {tts_time:.2f}s (first byte: {first_byte_time:.2f}s), {len(audio_bytes)} bytes")
    print(f"  TOTAL: {total:.2f}s")
    return total, text


async def test_realtime_api():
    """Realtime API: combined LLM+TTS in one WebSocket call."""
    print("\n=== REALTIME API: Combined LLM+TTS ===")

    url = "wss://api.openai.com/v1/realtime?model=gpt-4o-mini-realtime-preview"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "OpenAI-Beta": "realtime=v1",
    }

    t0 = time.time()
    first_audio_time = None
    first_text_time = None
    full_text = ""
    total_audio_bytes = 0
    import base64

    try:
        async with websockets.connect(url, additional_headers=headers) as ws:
            connect_time = time.time() - t0
            print(f"  WebSocket connected: {connect_time:.2f}s")

            # Configure session
            await ws.send(json.dumps({
                "type": "session.update",
                "session": {
                    "modalities": ["text", "audio"],
                    "voice": "shimmer",
                    "instructions": SYSTEM_PROMPT,
                    "input_audio_format": "pcm16",
                    "output_audio_format": "pcm16",
                    "turn_detection": None,
                }
            }))

            # Add conversation context
            # Add assistant opener
            await ws.send(json.dumps({
                "type": "conversation.item.create",
                "item": {
                    "type": "message",
                    "role": "assistant",
                    "content": [{"type": "text", "text": ASSISTANT_OPENER}],
                }
            }))

            # Add user message
            await ws.send(json.dumps({
                "type": "conversation.item.create",
                "item": {
                    "type": "message",
                    "role": "user",
                    "content": [{"type": "input_text", "text": USER_MESSAGE}],
                }
            }))

            # Request response
            await ws.send(json.dumps({
                "type": "response.create",
            }))

            # Read events until response is done
            while True:
                msg = await asyncio.wait_for(ws.recv(), timeout=30)
                event = json.loads(msg)
                event_type = event.get("type", "")

                if event_type == "response.audio.delta":
                    if first_audio_time is None:
                        first_audio_time = time.time() - t0
                    audio_data = base64.b64decode(event.get("delta", ""))
                    total_audio_bytes += len(audio_data)

                elif event_type == "response.audio_transcript.delta":
                    if first_text_time is None:
                        first_text_time = time.time() - t0
                    full_text += event.get("delta", "")

                elif event_type == "response.done":
                    break

                elif event_type == "error":
                    print(f"  ERROR: {event}")
                    break

    except Exception as e:
        print(f"  FAILED: {e}")
        return None, None

    total = time.time() - t0
    print(f"  First text: {first_text_time:.2f}s" if first_text_time else "  First text: N/A")
    print(f"  First audio byte: {first_audio_time:.2f}s" if first_audio_time else "  First audio: N/A")
    print(f"  Text: \"{full_text}\"")
    print(f"  Audio: {total_audio_bytes} bytes")
    print(f"  TOTAL: {total:.2f}s")
    return total, full_text


async def test_realtime_api_newer():
    """Try with newer gpt-realtime model if available."""
    print("\n=== REALTIME API (gpt-4o-realtime-preview-2025-06-03) ===")

    # Try different model endpoints
    for model in ["gpt-4o-realtime-preview-2025-06-03", "gpt-4o-mini-realtime-preview-2025-06-03"]:
        url = f"wss://api.openai.com/v1/realtime?model={model}"
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "OpenAI-Beta": "realtime=v1",
        }

        t0 = time.time()
        first_audio_time = None
        first_text_time = None
        full_text = ""
        total_audio_bytes = 0
        import base64

        try:
            async with websockets.connect(url, additional_headers=headers) as ws:
                connect_time = time.time() - t0
                print(f"\n  [{model}] Connected: {connect_time:.2f}s")

                await ws.send(json.dumps({
                    "type": "session.update",
                    "session": {
                        "modalities": ["text", "audio"],
                        "voice": "shimmer",
                        "instructions": SYSTEM_PROMPT,
                        "turn_detection": None,
                    }
                }))

                await ws.send(json.dumps({
                    "type": "conversation.item.create",
                    "item": {
                        "type": "message",
                        "role": "assistant",
                        "content": [{"type": "text", "text": ASSISTANT_OPENER}],
                    }
                }))

                await ws.send(json.dumps({
                    "type": "conversation.item.create",
                    "item": {
                        "type": "message",
                        "role": "user",
                        "content": [{"type": "input_text", "text": USER_MESSAGE}],
                    }
                }))

                await ws.send(json.dumps({"type": "response.create"}))

                while True:
                    msg = await asyncio.wait_for(ws.recv(), timeout=30)
                    event = json.loads(msg)
                    event_type = event.get("type", "")

                    if event_type == "response.audio.delta":
                        if first_audio_time is None:
                            first_audio_time = time.time() - t0
                        audio_data = base64.b64decode(event.get("delta", ""))
                        total_audio_bytes += len(audio_data)
                    elif event_type == "response.audio_transcript.delta":
                        if first_text_time is None:
                            first_text_time = time.time() - t0
                        full_text += event.get("delta", "")
                    elif event_type == "response.done":
                        break
                    elif event_type == "error":
                        print(f"  ERROR: {event}")
                        break

            total = time.time() - t0
            print(f"  First text: {first_text_time:.2f}s" if first_text_time else "  First text: N/A")
            print(f"  First audio: {first_audio_time:.2f}s" if first_audio_time else "  First audio: N/A")
            print(f"  Text: \"{full_text}\"")
            print(f"  Audio: {total_audio_bytes} bytes")
            print(f"  TOTAL: {total:.2f}s")

        except Exception as e:
            print(f"  [{model}] FAILED: {e}")


def main():
    print("=" * 70)
    print("LLM+TTS Benchmark: Current vs Realtime API")
    print("=" * 70)

    # Current approach
    current_total, current_text = test_current_approach()

    # Realtime API
    rt_total, rt_text = asyncio.run(test_realtime_api())

    # Try newer models
    asyncio.run(test_realtime_api_newer())

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  Current (LLM+TTS separate): {current_total:.2f}s")
    if rt_total:
        print(f"  Realtime API:               {rt_total:.2f}s")
        print(f"  Speedup:                    {current_total / rt_total:.1f}x")


if __name__ == "__main__":
    main()
