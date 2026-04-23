"""Mint short-lived OpenAI Realtime session tokens for the browser.

The browser connects directly to OpenAI's Realtime API over WebRTC to run a
voice conversation — we never relay audio through our backend. To do that the
browser needs a `client_secret` (ephemeral token) scoped to a specific session
config. This module owns the mint flow:

  1. Load the Conversation and verify the caller owns it.
  2. Run the paywall check so free-tier users past their quota can't spin up
     a realtime session.
  3. Rate-limit mints at (user_id, conversation_id) granularity — prevents
     refresh-spam from burning OpenAI quota when the FE reconnects in a loop.
  4. Build the ephemeral session config via `build_session_config(..., mode=
     "ephemeral")` so the minted token already carries the right system prompt,
     voice, VAD, and transcription settings.
  5. POST to OpenAI's `/v1/realtime/sessions` and return the client_secret +
     metadata straight through.

Tokens have a short TTL (typically ~60s); the FE re-mints before expiry. If
this module's OpenAI call fails we surface a 502 — the FE should not treat
that as a conversation-level error and should fall back to the legacy
`/voice-turn` flow behind its feature flag.
"""
import logging
import time
from typing import Tuple
from uuid import UUID

import httpx
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.config import settings
from app.models import Conversation, User
from app.services.realtime_config import build_session_config
from app.services.subscription_service import check_paywall

logger = logging.getLogger(__name__)

OPENAI_REALTIME_SESSIONS_URL = "https://api.openai.com/v1/realtime/sessions"
OPENAI_REQUEST_TIMEOUT_SECONDS = 10

# Rate limit: one mint per (user_id, conversation_id) per this window.
# v1 uses a process-local dict — fine for single-worker QA and acceptable on
# Railway where workers are typically ≤2. If we scale out, move to Redis so
# the limit holds across workers; rate-limit bypass only costs OpenAI cents.
RATE_LIMIT_WINDOW_SECONDS = 30
_rate_limit_state: dict[Tuple[str, str], float] = {}


def _reset_rate_limit_state_for_tests() -> None:
    """Clear the process-local rate limit dict. Tests call this in setup so
    one test's mints don't bleed into the next."""
    _rate_limit_state.clear()


def _check_rate_limit(user_id: str, conversation_id: str) -> None:
    """Raise 429 if this (user, conversation) minted within the window."""
    key = (user_id, conversation_id)
    now = time.monotonic()
    last = _rate_limit_state.get(key)
    if last is not None and (now - last) < RATE_LIMIT_WINDOW_SECONDS:
        retry_after = max(1, int(RATE_LIMIT_WINDOW_SECONDS - (now - last)))
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail={
                "error": "RATE_LIMITED",
                "retry_after_seconds": retry_after,
            },
        )
    _rate_limit_state[key] = now


async def mint_ephemeral_session(
    conversation_id: UUID,
    current_user: User,
    db: Session,
    phase: str,
) -> dict:
    """Validate, build config, and mint an OpenAI Realtime client_secret.

    Returns a plain dict matching `RealtimeSessionResponse`'s shape. Raises
    `HTTPException` for every failure mode; the router just returns the dict.

    Ordering note: ownership check fires before paywall so a user probing
    someone else's conversation_id always sees 403 FORBIDDEN, never
    PAYWALL — that would leak which ids map to free-tier-exhausted accounts.
    """
    # Lazy imports to avoid circulars at module import time.
    from app.api.v1.situations import get_grammar_level, get_vocab_level

    conv = (
        db.query(Conversation)
        .filter(Conversation.id == conversation_id)
        .first()
    )
    if conv is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found",
        )

    if conv.user_id != current_user.id:
        # Don't leak existence — 403 with a generic error, not 404.
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"error": "FORBIDDEN"},
        )

    # Paywall check — admins bypass, matching the /voice-turn pattern.
    if not current_user.is_admin:
        allowed, error = check_paywall(db, str(current_user.id), conv.situation_id)
        if not allowed:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"error": error},
            )

    _check_rate_limit(str(current_user.id), str(conv.id))

    vocab_level = get_vocab_level(db, current_user.id)
    grammar_level = get_grammar_level(db, current_user.id)
    session_config = build_session_config(
        conv,
        phase=phase,
        db=db,
        alt_language=current_user.alt_language,
        vocab_level=vocab_level,
        grammar_level=grammar_level,
        mode="ephemeral",
    )

    try:
        async with httpx.AsyncClient(timeout=OPENAI_REQUEST_TIMEOUT_SECONDS) as client:
            r = await client.post(
                OPENAI_REALTIME_SESSIONS_URL,
                headers={
                    "Authorization": f"Bearer {settings.openai_api_key}",
                    "Content-Type": "application/json",
                    "OpenAI-Beta": "realtime=v1",
                },
                json=session_config,
            )
        r.raise_for_status()
    except httpx.HTTPStatusError as e:
        logger.error(
            "[Realtime Session] OpenAI returned %s: %s",
            e.response.status_code,
            e.response.text[:200],
        )
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Realtime session provider returned an error",
        )
    except httpx.RequestError as e:
        logger.error("[Realtime Session] OpenAI unreachable: %s", e)
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Realtime session provider unreachable",
        )

    body = r.json()
    client_secret_obj = body.get("client_secret") or {}
    if not client_secret_obj.get("value") or not client_secret_obj.get("expires_at"):
        # OpenAI 200'd but didn't return what we need — treat as upstream failure
        # rather than returning a malformed response that the FE can't act on.
        logger.error(
            "[Realtime Session] OpenAI response missing client_secret fields: %s",
            str(body)[:200],
        )
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Realtime session provider returned an incomplete response",
        )

    return {
        "client_secret": client_secret_obj["value"],
        "expires_at": client_secret_obj["expires_at"],
        # Fall back to the config we sent if OpenAI doesn't echo these.
        "model": body.get("model") or session_config["model"],
        "voice": body.get("voice") or session_config["voice"],
    }
