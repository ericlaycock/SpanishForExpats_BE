"""Realtime voice-chat endpoints.

Owns the ephemeral-token mint used by the FE WebRTC client. The browser trades
the minted `client_secret` for a direct OpenAI Realtime connection — no audio
flows through this backend. Word detection, exchange limits, and persistence
happen server-side via `POST /v1/conversations/{id}/realtime-turn` (Phase 2).

See `app/services/realtime_session_service.py` for the mint flow and backend
issue #10 for the full phased design.
"""
import logging

from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import User
from app.schemas import RealtimeSessionCreate, RealtimeSessionResponse
from app.services.realtime_session_service import mint_ephemeral_session

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post(
    "/sessions",
    response_model=RealtimeSessionResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_realtime_session(
    body: RealtimeSessionCreate,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Mint a short-lived OpenAI Realtime client_secret for one Conversation.

    The FE calls this once per conversation (and re-mints when the token is
    about to expire). The response is safe to embed in the browser — the token
    can only open a session scoped to the config we built here.

    Errors:
    - 404 if the conversation doesn't exist.
    - 403 {error: "FORBIDDEN"} if it belongs to someone else.
    - 403 {error: "PAYWALL"} if the caller is past the free-tier limit.
    - 429 if called again for the same conversation within the rate-limit
      window. Body carries `retry_after_seconds`.
    - 502 if OpenAI is unreachable or returns an error — the FE should fall
      back to the legacy `/voice-turn` flow behind its feature flag.
    """
    phase = request.headers.get("X-Learning-Phase", "2")
    request.state.user_id = current_user.id

    return await mint_ephemeral_session(
        conversation_id=body.conversation_id,
        current_user=current_user,
        db=db,
        phase=phase,
    )
