"""Memorize utility endpoints.

- `POST /v1/memorize/connect` → gpt-5-mini mnemonic decomposition
- `POST /v1/memorize/complete` → records a confirmed memorisation and
  awards +1 sun (rolls into `_user_points()` for the header HUD).
"""
import logging
import time
import uuid
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, Request
from openai import OpenAI
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.config import settings
from app.database import get_db
from app.models import MemorizeCompletion, User

logger = logging.getLogger(__name__)
router = APIRouter()

TRANSLATE_MODEL = "gpt-4.1"

TRANSLATE_SYSTEM_PROMPTS: dict[str, str] = {
    "es_to_en": (
        "Translate the given Spanish word or phrase to its most natural English "
        "equivalent. For verb conjugations, conjugate the English verb to match "
        "(e.g. 'habla' → 'he speaks', 'comimos' → 'we ate'). Respond with ONLY "
        "the translation — no quotes, no commentary, no list of alternatives."
    ),
    "en_to_es": (
        "Translate the given English word or phrase to its most natural Latin "
        "American Spanish equivalent. For verb conjugations, conjugate the "
        "Spanish verb to match (e.g. 'he speaks' → 'habla', 'we ate' → "
        "'comimos'). Respond with ONLY the translation — no quotes, no "
        "commentary, no list of alternatives."
    ),
}

# Stored prompt on OpenAI (Responses API). Model + system message live on
# the stored prompt — change them there, not here. The stored prompt
# template doesn't (currently) accept a user-supplied English meaning, so
# the model infers it from the Spanish input alone; some divergence from
# what the user typed in their English field is expected and acceptable.
CONNECT_PROMPT_ID = "pmpt_6a1310672d7c8190ae7e361783490e4106beea0a84d4b3df"
CONNECT_PROMPT_VERSION = "1"

# Lazy OpenAI client.
_client: OpenAI | None = None


def _get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(api_key=settings.openai_api_key)
    return _client


class ConnectRequest(BaseModel):
    word: str = Field(..., min_length=1, max_length=200)


class ConnectResponse(BaseModel):
    response: str


@router.post("/connect", response_model=ConnectResponse)
def memorize_connect(
    body: ConnectRequest,
    current_user: User = Depends(get_current_user),  # noqa: ARG001 — auth gate only
):
    """Return a mnemonic decomposition for the given Spanish word."""
    word = body.word.strip()
    if not word:
        raise HTTPException(status_code=400, detail="word must not be empty")

    start = time.time()
    try:
        client = _get_client()
        response = client.responses.create(
            prompt={
                "id": CONNECT_PROMPT_ID,
                "version": CONNECT_PROMPT_VERSION,
            },
            input=word,
        )
        content = (getattr(response, "output_text", "") or "").strip()
    except Exception as exc:
        logger.error("memorize/connect openai call failed: %s", exc)
        raise HTTPException(status_code=502, detail="Unable to reach the model. Try again.") from exc

    elapsed_ms = int((time.time() - start) * 1000)
    logger.info("memorize/connect ok word=%s len=%d ms=%d", word, len(content), elapsed_ms)

    if not content:
        content = "No connections available."

    return ConnectResponse(response=content)


class CompleteRequest(BaseModel):
    spanish: str = Field(..., min_length=1, max_length=500)
    english: str | None = Field(default=None, max_length=500)


class CompleteResponse(BaseModel):
    points: int  # user's new lifetime-earned sun total after this completion
    coins_earned: int  # always 1 today; future-proofed in case the reward shape changes


@router.post("/complete", response_model=CompleteResponse)
def memorize_complete(
    body: CompleteRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Record a confirmed memorisation, awarding +1 sun."""
    spanish = body.spanish.strip()
    if not spanish:
        raise HTTPException(status_code=400, detail="spanish must not be empty")
    english = (body.english or "").strip() or None

    row = MemorizeCompletion(
        id=uuid.uuid4(),
        user_id=current_user.id,
        spanish_phrase=spanish,
        english_phrase=english,
        coins_earned=1,
    )
    db.add(row)
    db.commit()

    # Read back the user's updated lifetime-earned total so the FE can
    # show the new sun count immediately without a second round-trip.
    from app.api.v1.tense_quest import _user_points
    points = _user_points(db, current_user.id)

    logger.info(
        "memorize/complete user=%s spanish=%r english=%r new_points=%d",
        current_user.id,
        spanish,
        english,
        points,
    )

    return CompleteResponse(points=points, coins_earned=1)


class TranslateRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=500)
    direction: Literal["es_to_en", "en_to_es"]


class TranslateResponse(BaseModel):
    translated: str


# Translate is public (the anonymous free trial calls it), so it carries a
# simple in-memory per-IP rate limit to cap LLM cost/abuse. NOTE: in-memory →
# resets on deploy and is per-process (not shared across instances); adequate as
# a basic guard, not a hard quota.
_TRANSLATE_RATE_LIMIT = 40        # max requests …
_TRANSLATE_RATE_WINDOW = 3600.0   # … per IP per hour
_translate_hits: dict[str, list[float]] = {}


def _client_ip(request: Request) -> str:
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


def _enforce_translate_rate_limit(request: Request) -> None:
    ip = _client_ip(request)
    now = time.time()
    hits = [t for t in _translate_hits.get(ip, []) if now - t < _TRANSLATE_RATE_WINDOW]
    if len(hits) >= _TRANSLATE_RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Too many translations right now. Please try again later.",
        )
    hits.append(now)
    _translate_hits[ip] = hits


@router.post("/translate", response_model=TranslateResponse)
def memorize_translate(body: TranslateRequest, request: Request):
    """Translate a Spanish word/phrase to English or vice versa via gpt-4.1.

    Public (no auth) so the anonymous free trial can use it; rate-limited per IP.
    """
    _enforce_translate_rate_limit(request)
    text = body.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="text must not be empty")

    system_prompt = TRANSLATE_SYSTEM_PROMPTS[body.direction]
    start = time.time()
    try:
        client = _get_client()
        completion = client.chat.completions.create(
            model=TRANSLATE_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text},
            ],
            temperature=0.1,
            max_tokens=300,
        )
        translated = (completion.choices[0].message.content or "").strip()
        # Strip surrounding quotes that some models add despite the system prompt.
        if (translated.startswith('"') and translated.endswith('"')) or (
            translated.startswith("'") and translated.endswith("'")
        ):
            translated = translated[1:-1].strip()
    except Exception as exc:
        logger.error("memorize/translate openai call failed: %s", exc)
        raise HTTPException(status_code=502, detail="Unable to reach the model. Try again.") from exc

    elapsed_ms = int((time.time() - start) * 1000)
    logger.info(
        "memorize/translate ok direction=%s in=%r out=%r ms=%d",
        body.direction, text, translated, elapsed_ms,
    )

    return TranslateResponse(translated=translated)
