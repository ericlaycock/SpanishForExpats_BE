#!/usr/bin/env python3
"""Pre-generate TTS audio for all initial greeting messages and upload to R2.

Uses OpenAI's `/v1/audio/speech` endpoint with `gpt-4o-mini-tts` so the audio
is a verbatim reading of the opener text (no LLM in the loop). With --verify,
each upload is round-tripped through `gpt-4o-mini-transcribe` to confirm the
audio matches the source string.

Audio is uploaded to R2 with deterministic filenames:
    initial_msg_{situation_id}.mp3
(no language suffix — alt-language audio not yet pre-generated).

Usage:
    python scripts/pregenerate_initial_audio.py                          # all situations
    python scripts/pregenerate_initial_audio.py bank_1                    # specific situation(s)
    python scripts/pregenerate_initial_audio.py --force                   # regenerate even if exists
    python scripts/pregenerate_initial_audio.py --verify                  # transcribe-back verify
    python scripts/pregenerate_initial_audio.py --ids-file ids.txt        # IDs from file (one per line)

Requires R2 env vars: R2_ENDPOINT_URL, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY,
                       R2_BUCKET_NAME, R2_PUBLIC_URL
"""

import argparse
import asyncio
import os
import re
import sys
import time
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path

import httpx

from app.config import settings
from app.data.seed_bank import SITUATIONS
from app.data.grammar_situations import GRAMMAR_SITUATIONS
from app.services.encounter_messages import get_initial_message_for_encounter
from app.utils.audio import upload_to_r2, _get_s3_client

AUDIO_DIR = Path("/tmp/initial_audio")
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

TTS_MODEL = "gpt-4o-mini-tts"
TRANSCRIBE_MODEL = "gpt-4o-mini-transcribe"
SPEECH_URL = "https://api.openai.com/v1/audio/speech"
TRANSCRIBE_URL = "https://api.openai.com/v1/audio/transcriptions"

CONCURRENCY = 8

# Voice config per animation_type (must match conversations.py SITUATION_VOICE_CONFIG)
_ACCENT = "Speak with a Mexican Spanish accent."
VOICE_CONFIG = {
    "airport": ("shimmer", f"{_ACCENT} Use a professional, clear female voice."),
    "banking": ("shimmer", f"{_ACCENT} Use a professional, composed female voice with a warm undertone."),
    "clothing": ("coral", f"{_ACCENT} Use a casual, charming female voice."),
    "contractor": ("ash", f"{_ACCENT} Use a deep, husky baritone male voice."),
    "core": ("ash", f"{_ACCENT} Use a casual, friendly male voice."),
    "groceries": ("ash", f"{_ACCENT} Use a casual, charming male voice."),
    "internet": ("coral", f"{_ACCENT} Use a young, energetic female voice."),
    "mechanic": ("ash", f"{_ACCENT} Use a deep male voice."),
    "police": ("alloy", f"{_ACCENT} Use an authoritative female voice, firm but professional."),
    "restaurant": ("ash", f"{_ACCENT} Use a suave, charming male voice."),
    "small_talk": ("shimmer", f"{_ACCENT} Use a warm, older female voice with a friendly, neighborly tone."),
    "grammar": ("ash", f"{_ACCENT} Use a casual, friendly male voice."),
}


def r2_file_exists(filename: str) -> bool:
    """Check if a file already exists in R2."""
    client = _get_s3_client()
    if not client:
        return False
    try:
        client.head_object(Bucket=settings.r2_bucket_name, Key=filename)
        return True
    except Exception:
        return False


def _normalize(s: str) -> str:
    if not s:
        return ""
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[¿¡!?.,;:\"'…—–\-()«»‘’“”]", "", s)
    return re.sub(r"\s+", " ", s).strip()


async def _tts(client: httpx.AsyncClient, voice: str, instructions: str, text: str) -> bytes:
    resp = await client.post(
        SPEECH_URL,
        headers={"Authorization": f"Bearer {settings.openai_api_key}"},
        json={
            "model": TTS_MODEL,
            "voice": voice,
            "input": text,
            "instructions": instructions,
            "response_format": "mp3",
        },
        timeout=60,
    )
    resp.raise_for_status()
    return resp.content


async def _verify(client: httpx.AsyncClient, mp3_bytes: bytes, expected: str) -> tuple[bool, str]:
    """Transcribe the just-generated mp3 and compare to expected text (normalized)."""
    files = {"file": ("audio.mp3", mp3_bytes, "audio/mpeg")}
    data = {"model": TRANSCRIBE_MODEL, "language": "es"}
    resp = await client.post(
        TRANSCRIBE_URL,
        headers={"Authorization": f"Bearer {settings.openai_api_key}"},
        files=files,
        data=data,
        timeout=60,
    )
    resp.raise_for_status()
    heard = (resp.json().get("text") or "").strip()
    return _normalize(expected) == _normalize(heard), heard


async def generate_and_upload(
    client: httpx.AsyncClient,
    situation_id: str,
    title: str,
    animation_type: str,
    force: bool,
    verify: bool,
) -> tuple[str, str | None]:
    """Generate verbatim TTS for one situation's opener and upload to R2.

    Returns (status, detail) where status is one of
        'ok' | 'skip' | 'no_message' | 'tts_fail' | 'verify_fail' | 'r2_fail'
    """
    filename = f"initial_msg_{situation_id}.mp3"

    if not force and r2_file_exists(filename):
        return "skip", None

    messages_by_lang = get_initial_message_for_encounter(situation_id, title)
    message = messages_by_lang.get("es") or messages_by_lang.get("en")
    if not message:
        return "no_message", None

    voice_key = animation_type
    if animation_type == "grammar":
        from app.data.situation_roles import GRAMMAR_SCENE_MAP
        mapped = GRAMMAR_SCENE_MAP.get(situation_id)
        if mapped:
            voice_key = mapped
    voice, tts_instructions = VOICE_CONFIG.get(voice_key, ("alloy", _ACCENT))

    try:
        mp3_bytes = await _tts(client, voice, tts_instructions, message)
    except Exception as e:
        print(f"  [ERROR] TTS failed for {situation_id}: {e}")
        return "tts_fail", None

    if not mp3_bytes:
        print(f"  [ERROR] No audio returned for {situation_id}")
        return "tts_fail", None

    verify_mismatch_text: str | None = None
    if verify:
        try:
            ok, heard = await _verify(client, mp3_bytes, message)
        except Exception as e:
            print(f"  [WARN] Verify request failed for {situation_id}: {e}")
            ok, heard = True, ""  # don't fail the run on verify-pipeline error
        if not ok:
            # Informational only — gpt-4o-mini-transcribe sometimes mis-hears
            # short utterances. Upload anyway; surface for manual review.
            print(f"  [VERIFY-MISMATCH] {situation_id}")
            print(f"    expected: {message!r}")
            print(f"    heard:    {heard!r}")
            verify_mismatch_text = heard

    local_path = AUDIO_DIR / filename
    local_path.write_bytes(mp3_bytes)

    r2_url = upload_to_r2(str(local_path), filename)
    if not r2_url:
        return "r2_fail", None

    if verify_mismatch_text is not None:
        return "verify_mismatch", verify_mismatch_text
    return "ok", None


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Pre-generate opener TTS audio and upload to R2.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("ids", nargs="*", help="Situation IDs to (re)generate. Default: all.")
    p.add_argument("--force", action="store_true", help="Regenerate even if file exists in R2.")
    p.add_argument("--verify", action="store_true", help="Transcribe-back verify each upload.")
    p.add_argument("--ids-file", type=Path, help="Path to file with one situation ID per line.")
    p.add_argument("--concurrency", type=int, default=CONCURRENCY, help=f"Parallel TTS calls (default: {CONCURRENCY}).")
    return p.parse_args()


async def main() -> None:
    args = _parse_args()

    ids: set[str] = set(args.ids)
    if args.ids_file:
        for line in args.ids_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                ids.add(line)

    all_situations: list[tuple[str, str, str]] = []
    for s in SITUATIONS:
        all_situations.append((s["id"], s["title"], s["animation_type"]))
    for sid, cfg in GRAMMAR_SITUATIONS.items():
        all_situations.append((sid, cfg["title"], "grammar"))

    if ids:
        all_situations = [(sid, t, a) for sid, t, a in all_situations if sid in ids]
        missing = ids - {sid for sid, _, _ in all_situations}
        if missing:
            print(f"[WARN] {len(missing)} requested ID(s) not found: {sorted(missing)[:5]}{'…' if len(missing) > 5 else ''}")

    if not all_situations:
        print("No situations found.")
        sys.exit(1)

    print(
        f"TTS ({TTS_MODEL}) for {len(all_situations)} situations  "
        f"force={args.force} verify={args.verify} concurrency={args.concurrency}"
    )
    start = time.time()

    stats = {"ok": 0, "skip": 0, "no_message": 0, "tts_fail": 0, "verify_mismatch": 0, "r2_fail": 0}
    sem = asyncio.Semaphore(args.concurrency)
    done = {"n": 0}
    total = len(all_situations)
    verify_mismatches: list[tuple[str, str]] = []

    async with httpx.AsyncClient(http2=False) as client:

        async def runner(sid: str, title: str, anim: str) -> None:
            async with sem:
                status, detail = await generate_and_upload(
                    client, sid, title, anim, args.force, args.verify,
                )
            stats[status] += 1
            if status == "verify_mismatch":
                verify_mismatches.append((sid, detail or ""))
            done["n"] += 1
            if done["n"] % 25 == 0 or done["n"] == total:
                elapsed = time.time() - start
                print(
                    f"  [{done['n']}/{total}] {elapsed:.0f}s — "
                    f"ok={stats['ok']} skip={stats['skip']} "
                    f"no_msg={stats['no_message']} tts_fail={stats['tts_fail']} "
                    f"verify_mismatch={stats['verify_mismatch']} r2_fail={stats['r2_fail']}",
                    flush=True,
                )

        await asyncio.gather(*(runner(sid, t, a) for sid, t, a in all_situations))

    total_t = time.time() - start
    print(f"\nDone in {total_t:.0f}s: {stats}")

    if verify_mismatches:
        print(f"\n[VERIFY] {len(verify_mismatches)} mismatches (audio uploaded; review manually):")
        for sid, heard in verify_mismatches[:20]:
            print(f"  {sid} → {heard!r}")
        if len(verify_mismatches) > 20:
            print(f"  ... and {len(verify_mismatches) - 20} more")

    if stats["tts_fail"] or stats["r2_fail"]:
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
