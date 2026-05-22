"""Public anonymous funnel-tracking endpoint.

Records pre-signup wizard progression. Idempotent per (session_id, event_key)
via the unique constraint on the table — duplicate fires are no-ops.

This endpoint is intentionally unauthenticated. The only state it can mutate
is anonymous funnel rows; admin aggregation lives behind admin auth in
`app/api/v1/admin.py::get_webpageflow`.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert

from app.database import get_db
from app.models import AnonymousFunnelEvent
from app.schemas import FunnelTrackRequest, WEBPAGEFLOW_EVENT_KEYS

router = APIRouter()


@router.post("/track")
async def track_event(body: FunnelTrackRequest, db: Session = Depends(get_db)):
    if body.event_key not in WEBPAGEFLOW_EVENT_KEYS:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown event_key. Valid: {', '.join(WEBPAGEFLOW_EVENT_KEYS)}",
        )

    # Attribution is JSONB. Storing on every event row means we can recover
    # the source from any row for this session, not just the landing_view —
    # robust if landing_view ever fails to fire (e.g. ad-blocker on first hit
    # but not on the click).
    values = {"session_id": body.session_id, "event_key": body.event_key}
    if body.attribution:
        values["event_metadata"] = body.attribution

    stmt = (
        insert(AnonymousFunnelEvent)
        .values(**values)
        .on_conflict_do_nothing(constraint="uq_funnel_session_event")
    )
    db.execute(stmt)
    db.commit()
    return {"status": "ok"}
