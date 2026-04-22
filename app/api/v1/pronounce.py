"""Pronunciation trainer endpoints.

Issues 10-minute Azure Speech tokens and tracks daily usage (500s/user/day).
Also provides espeak-ng IPA transcription and wav2vec2 phoneme recognition.
Only users with plan 'pronounce' or 'app_pronounce' (subscription.tier) can access.
"""
import uuid
import logging
import subprocess
import tempfile
import os
import time
from datetime import date
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from sqlalchemy import text
import httpx
from app.auth import get_current_user
from app.database import get_db
from app.models import User, Subscription
from app.config import settings

# Lazy-loaded wav2vec2 model singleton
_wav2vec2_processor = None
_wav2vec2_model = None

logger = logging.getLogger(__name__)
router = APIRouter()

DAILY_LIMIT = 500
MAX_RECORDING = 20
PRONOUNCE_PLANS = {"pronounce", "app_pronounce"}


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
        # espeak-ng outputs one line per word; join into flat space-separated stream
        ipa = " ".join(line.strip() for line in result.stdout.strip().splitlines() if line.strip())
        return {"ipa": ipa}
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="espeak-ng not available on this server")
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="espeak-ng timed out")


def _load_wav2vec2():
    global _wav2vec2_processor, _wav2vec2_model
    if _wav2vec2_model is None:
        import torch
        from transformers import AutoProcessor, Wav2Vec2ForCTC
        MODEL_ID = "facebook/wav2vec2-lv-60-espeak-cv-ft"
        logger.info(f"[Pronounce] Loading {MODEL_ID}...")
        t0 = time.perf_counter()
        _wav2vec2_processor = AutoProcessor.from_pretrained(MODEL_ID)
        t1 = time.perf_counter()
        logger.info(f"[Pronounce] Processor loaded in {t1-t0:.2f}s")
        _wav2vec2_model = Wav2Vec2ForCTC.from_pretrained(MODEL_ID)
        t2 = time.perf_counter()
        logger.info(f"[Pronounce] Model loaded in {t2-t1:.2f}s (total {t2-t0:.2f}s)")
        _wav2vec2_model.eval()
        logger.info("[Pronounce] wav2vec2 model ready.")
    return _wav2vec2_processor, _wav2vec2_model


@router.post("/phones")
async def recognize_phones(
    audio: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Accept an audio file, return IPA phoneme string of what was spoken."""
    _require_pronounce(current_user, db)

    import torch
    import numpy as np

    t_start = time.perf_counter()
    raw = await audio.read()
    if not raw:
        raise HTTPException(status_code=400, detail="Empty audio file")

    logger.info(f"[Phones] audio read: {len(raw)} bytes")

    # Write to temp file so ffmpeg can detect container format
    suffix = "." + (audio.filename.rsplit(".", 1)[-1] if audio.filename and "." in audio.filename else "webm")
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as f:
            f.write(raw)
            tmp_path = f.name

        t_ffmpeg = time.perf_counter()
        # Decode to mono float32 @ 16 kHz (same as sfe_pron/phones.py)
        ffmpeg_result = subprocess.run(
            [
                "ffmpeg", "-nostdin", "-loglevel", "error",
                "-i", tmp_path,
                "-ac", "1", "-ar", "16000",
                "-f", "f32le", "pipe:1",
            ],
            capture_output=True,
        )
        logger.info(f"[Phones] ffmpeg decode: {time.perf_counter()-t_ffmpeg:.2f}s")
        if ffmpeg_result.returncode != 0:
            raise HTTPException(status_code=400, detail="Audio decode failed")

        pcm = np.frombuffer(ffmpeg_result.stdout, dtype=np.float32).copy()
        logger.info(f"[Phones] pcm samples: {pcm.size} ({pcm.size/16000:.2f}s of audio)")
        if pcm.size < 1600:  # < 0.1s
            return {"ipa": ""}

        t_load = time.perf_counter()
        processor, model = _load_wav2vec2()
        logger.info(f"[Phones] model ready in {time.perf_counter()-t_load:.2f}s (0 if cached)")

        t_infer = time.perf_counter()
        inputs = processor(pcm, sampling_rate=16000, return_tensors="pt")
        with torch.no_grad():
            logits = model(inputs.input_values).logits
        pred = torch.argmax(logits, dim=-1)
        ipa = processor.batch_decode(pred)[0].strip()
        logger.info(f"[Phones] inference: {time.perf_counter()-t_infer:.2f}s | total: {time.perf_counter()-t_start:.2f}s | ipa: {ipa!r}")
        return {"ipa": ipa}

    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.unlink(tmp_path)
