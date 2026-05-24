"""Memorize utility endpoints.

- `POST /v1/memorize/connect` → gpt-5-mini mnemonic decomposition
- `POST /v1/memorize/complete` → records a confirmed memorisation and
  awards +1 sun (rolls into `_user_points()` for the header HUD).
"""
import logging
import time
import uuid

from fastapi import APIRouter, Depends, HTTPException
from openai import OpenAI
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.config import settings
from app.database import get_db
from app.models import MemorizeCompletion, User

logger = logging.getLogger(__name__)
router = APIRouter()

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
