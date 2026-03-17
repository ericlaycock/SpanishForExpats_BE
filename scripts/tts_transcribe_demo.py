"""
TTS → gpt-4o-mini-transcribe demo: test timestamp support.

Usage:
    cd SpanishForExpats_BE && .venv/bin/python scripts/tts_transcribe_demo.py
"""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from openai import OpenAI

CATALAN_TEXT = (
    "Barcelona és una ciutat meravellosa situada a la costa mediterrània. "
    "La seva arquitectura modernista, dissenyada per Antoni Gaudí, atrau milions "
    "de visitants cada any. Els carrers del Barri Gòtic són plens d'història "
    "i cultura catalana."
)

OUTPUT_MP3 = Path(__file__).resolve().parent / "tts_demo_output.mp3"


def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not set.")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    # --- Generate TTS (reuse existing file if present) ---
    if not OUTPUT_MP3.exists():
        print("Generating TTS...")
        response = client.audio.speech.create(model="tts-1", voice="alloy", input=CATALAN_TEXT)
        with open(OUTPUT_MP3, "wb") as f:
            for chunk in response.iter_bytes():
                f.write(chunk)
        print(f"Saved {OUTPUT_MP3} ({OUTPUT_MP3.stat().st_size} bytes)\n")
    else:
        print(f"Reusing existing {OUTPUT_MP3}\n")

    # --- Test matrix ---
    tests = [
        ("gpt-4o-mini-transcribe", "json", ["word"]),
        ("gpt-4o-mini-transcribe", "json", ["segment"]),
        ("gpt-4o-mini-transcribe", "verbose_json", ["word"]),
        ("gpt-4o-mini-transcribe", "verbose_json", ["segment"]),
        ("gpt-4o-mini-transcribe", "text", None),
        ("whisper-1", "verbose_json", ["word"]),
        ("whisper-1", "verbose_json", ["segment"]),
    ]

    for model, fmt, granularities in tests:
        label = f"{model} | format={fmt} | granularities={granularities}"
        print(f"\n{'='*60}")
        print(f"TEST: {label}")
        print(f"{'='*60}")

        try:
            params = {
                "model": model,
                "file": open(OUTPUT_MP3, "rb"),
                "language": "ca",
                "response_format": fmt,
            }
            if granularities:
                params["timestamp_granularities"] = granularities

            transcript = client.audio.transcriptions.create(**params)

            # For text format, result is just a string
            if fmt == "text":
                print(f"Text: {transcript}")
                continue

            print(f"Text: {getattr(transcript, 'text', 'N/A')}")

            # Check for words
            words = getattr(transcript, "words", None)
            if words:
                print(f"Words ({len(words)} total):")
                for w in words[:5]:
                    s = getattr(w, "start", "?")
                    e = getattr(w, "end", "?")
                    t = getattr(w, "word", "?")
                    print(f"  [{s:.2f} - {e:.2f}] {t}")
                if len(words) > 5:
                    print(f"  ... and {len(words)-5} more")
            else:
                print("Words: None")

            # Check for segments
            segments = getattr(transcript, "segments", None)
            if segments:
                print(f"Segments ({len(segments)} total):")
                for seg in segments[:3]:
                    s = getattr(seg, "start", "?")
                    e = getattr(seg, "end", "?")
                    t = getattr(seg, "text", "?")
                    print(f"  [{s:.2f} - {e:.2f}] {t}")
            else:
                print("Segments: None")

            # Print any other attrs
            known = {"text", "words", "segments", "language", "duration", "task", "logprobs", "usage"}
            for attr in dir(transcript):
                if not attr.startswith("_") and attr not in known and not callable(getattr(transcript, attr)):
                    print(f"  Extra attr: {attr} = {getattr(transcript, attr)}")

        except Exception as e:
            print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
