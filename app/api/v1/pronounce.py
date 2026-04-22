"""Pronunciation trainer endpoints.

Issues 10-minute Azure Speech tokens and tracks daily usage (500s/user/day).
Also provides espeak-ng IPA transcription and HuggingFace wav2vec2 phoneme recognition.
Only users with plan 'pronounce' or 'app_pronounce' (subscription.tier) can access.
"""
import uuid
import logging
import subprocess
import struct
import time
import asyncio
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from sqlalchemy import text
import httpx
from app.auth import get_current_user
from app.database import get_db
from app.models import User, Subscription
from app.config import settings

logger = logging.getLogger(__name__)
router = APIRouter()

DAILY_LIMIT = 500
MAX_RECORDING = 20
PRONOUNCE_PLANS = {"pronounce", "app_pronounce"}
HF_MODEL_URL = "https://router.huggingface.co/hf-inference/models/facebook/wav2vec2-lv-60-espeak-cv-ft"

# Minimal 0.1s silence WAV (16kHz, 16-bit mono) for model warm-up
def _make_silence_wav() -> bytes:
    n = 1600  # 0.1s at 16kHz
    data = b'\x00' * (n * 2)
    hdr = struct.pack('<4sI4s4sIHHIIHH4sI',
        b'RIFF', 36 + len(data), b'WAVE', b'fmt ', 16,
        1, 1, 16000, 32000, 2, 16, b'data', len(data))
    return hdr + data

_SILENCE_WAV = _make_silence_wav()


def _require_pronounce(user: User, db: Session) -> Subscription:
    sub = db.query(Subscription).filter(Subscription.user_id == user.id).first()
    if not sub or sub.tier not in PRONOUNCE_PLANS:
        raise HTTPException(status_code=403, detail="Your account does not include pronunciation trainer access")
    return sub


def _get_seconds_used(db: Session, user_id: uuid.UUID) -> int:
    row = db.execute(
        text("SELECT seconds_used FROM pron_daily_usage WHERE user_id = :uid AND date = CURRENT_DATE"),
        {"uid": str(user_id)},
    ).first()
    return row.seconds_used if row else 0


@router.get("/token")
async def get_azure_token(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _require_pronounce(current_user, db)

    seconds_used = _get_seconds_used(db, current_user.id)
    if seconds_used >= DAILY_LIMIT:
        raise HTTPException(status_code=429, detail=f"Daily limit of {DAILY_LIMIT}s reached. Resets at midnight.")

    if not settings.speech_key or not settings.speech_region:
        raise HTTPException(status_code=503, detail="Azure Speech not configured on this server")

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(
                f"https://{settings.speech_region}.api.cognitive.microsoft.com/sts/v1.0/issueToken",
                headers={"Ocp-Apim-Subscription-Key": settings.speech_key},
            )
        r.raise_for_status()
    except httpx.HTTPStatusError as e:
        logger.error(f"[Pronounce] Azure token failed: {e.response.status_code}")
        raise HTTPException(status_code=502, detail="Azure Speech service unavailable")
    except httpx.RequestError as e:
        logger.error(f"[Pronounce] Azure token error: {e}")
        raise HTTPException(status_code=502, detail="Azure Speech service unreachable")

    return {
        "token": r.text,
        "region": settings.speech_region,
        "seconds_remaining": max(0, DAILY_LIMIT - seconds_used),
        "max_recording": MAX_RECORDING,
    }


@router.post("/usage")
def record_usage(
    body: dict,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _require_pronounce(current_user, db)

    seconds = min(int(body.get("seconds", 0)), MAX_RECORDING)
    if seconds <= 0:
        seconds_used = _get_seconds_used(db, current_user.id)
        return {"seconds_used": seconds_used, "seconds_remaining": max(0, DAILY_LIMIT - seconds_used)}

    db.execute(
        text("""
            INSERT INTO pron_daily_usage (id, user_id, date, seconds_used)
            VALUES (:id, :uid, CURRENT_DATE, :s)
            ON CONFLICT (user_id, date)
            DO UPDATE SET seconds_used = LEAST(pron_daily_usage.seconds_used + :s, :limit)
        """),
        {"id": str(uuid.uuid4()), "uid": str(current_user.id), "s": seconds, "limit": DAILY_LIMIT},
    )
    db.commit()

    seconds_used = _get_seconds_used(db, current_user.id)
    return {"seconds_used": seconds_used, "seconds_remaining": max(0, DAILY_LIMIT - seconds_used)}


@router.get("/usage")
def get_usage(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _require_pronounce(current_user, db)
    seconds_used = _get_seconds_used(db, current_user.id)
    return {"seconds_used": seconds_used, "seconds_remaining": max(0, DAILY_LIMIT - seconds_used), "limit": DAILY_LIMIT}


@router.get("/ipa")
def get_target_ipa(
    text: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Return espeak-ng IPA for the given Spanish text (target phonemes)."""
    _require_pronounce(current_user, db)
    try:
        result = subprocess.run(
            ["espeak-ng", "-v", "es", "-q", "--ipa", text],
            capture_output=True, text=True, timeout=10,
        )
        ipa = " ".join(line.strip() for line in result.stdout.strip().splitlines() if line.strip())
        return {"ipa": ipa}
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="espeak-ng not available on this server")
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="espeak-ng timed out")


async def _hf_infer(audio_bytes: bytes) -> str:
    """POST audio to HF Inference API, retry on 503 model-loading. Returns IPA string."""
    headers = {"Authorization": f"Bearer {settings.hf_token}"}
    async with httpx.AsyncClient(timeout=60) as client:
        for attempt in range(3):
            r = await client.post(HF_MODEL_URL, headers=headers, content=audio_bytes)
            if r.status_code == 503:
                ct = r.headers.get("content-type", "")
                body = r.json() if "json" in ct else {}
                wait = min(float(body.get("estimated_time", 20)), 40)
                logger.warning(f"[HF] model loading, waiting {wait:.0f}s (attempt {attempt+1})")
                await asyncio.sleep(wait)
                continue
            r.raise_for_status()
            return r.json().get("text", "")
    logger.error("[HF] model still loading after retries")
    return ""


@router.get("/warm")
async def warm_model(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Trigger HF model cold-start using silence. Call on page load; blocks until ready."""
    _require_pronounce(current_user, db)
    if not settings.hf_token:
        return {"status": "no_token"}
    try:
        t0 = time.perf_counter()
        await _hf_infer(_SILENCE_WAV)
        logger.info(f"[Warm] HF model ready in {time.perf_counter()-t0:.1f}s")
    except Exception as e:
        logger.warning(f"[Warm] HF warm-up failed: {e}")
    return {"status": "ready"}


@router.post("/phones")
async def recognize_phones(
    audio: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Accept an audio file, return IPA phoneme string via HuggingFace Inference API."""
    _require_pronounce(current_user, db)

    if not settings.hf_token:
        raise HTTPException(status_code=503, detail="HuggingFace token not configured")

    raw = await audio.read()
    if not raw:
        raise HTTPException(status_code=400, detail="Empty audio file")

    t_start = time.perf_counter()
    logger.info(f"[Phones] audio received: {len(raw)} bytes")

    try:
        ipa = await _hf_infer(raw)
        logger.info(f"[Phones] total: {time.perf_counter()-t_start:.2f}s | ipa: {ipa!r}")
        return {"ipa": ipa}
    except Exception as e:
        logger.error(f"[Phones] failed: {e}")
        return {"ipa": ""}
