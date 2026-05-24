"""Memorize utility endpoints.

Currently exposes one endpoint, `/v1/memorize/connect`, which sends a
Spanish word/phrase to gpt-5-mini and returns a short decomposition that
helps the user build a mnemonic bridge to the meaning.
"""
import logging
import time

from fastapi import APIRouter, Depends, HTTPException
from openai import OpenAI
from pydantic import BaseModel, Field

from app.auth import get_current_user
from app.config import settings
from app.models import User

logger = logging.getLogger(__name__)
router = APIRouter()

CONNECT_MODEL = "gpt-5-mini"

CONNECT_SYSTEM_PROMPT = (
    "You first decompose the given Spanish word into 3-5 similar sounding "
    "English words or English words that overlap in sound, and then "
    "(second) you consider each for any semantic links to the English "
    "meaning. For example, if given \"llave\", you first decompose this "
    "into \"llama\", \"wave\", \"Ave Maria\". For \"llama\", there is no "
    "semantic path to \"key\". For \"wave\", you could say \"a musical "
    "key is composed of sound waves, so llave->wave->key\". For \"Ave "
    "Maria\", you could say \"Ave Maria is a song sung in the key of B "
    "flat, so llave->Ave Maria->key, although it's a weaker connection\". "
    "For verb conjugations, or any you fail to find, just return \"No "
    "connections available.\". Do not return shitty connections."
)

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
        completion = client.chat.completions.create(
            model=CONNECT_MODEL,
            messages=[
                {"role": "system", "content": CONNECT_SYSTEM_PROMPT},
                {"role": "user", "content": word},
            ],
        )
        content = (completion.choices[0].message.content or "").strip()
    except Exception as exc:
        logger.error("memorize/connect openai call failed: %s", exc)
        raise HTTPException(status_code=502, detail="Unable to reach the model. Try again.") from exc

    elapsed_ms = int((time.time() - start) * 1000)
    logger.info("memorize/connect ok word=%s len=%d ms=%d", word, len(content), elapsed_ms)

    if not content:
        content = "No connections available."

    return ConnectResponse(response=content)
