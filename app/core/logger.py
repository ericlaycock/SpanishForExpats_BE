"""Structured JSON logging system for Better Stack"""
import json
import sys
from datetime import datetime
from typing import Optional, Dict, Any
import os
from app.core.betterstack import schedule_ship_log


def log_event(
    level: str,
    event: str,
    message: str,
    request_id: str,
    user_id: Optional[str] = None,
    extra: Dict[str, Any] = {}
) -> None:
    """
    Emit structured JSON log event to stdout and optionally ship to Better Stack.
    
    Args:
        level: Log level (info, error, warn, debug)
        event: Event name (e.g., "api_request", "llm_success")
        message: Human-readable message
        request_id: Correlation ID for the request
        user_id: Optional user ID
        extra: Additional fields to include in log
    """
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "level": level,
        "event": event,
        "message": message,
        "request_id": request_id,
        "release": os.environ.get("RELEASE_SHA", "unknown"),
    }
    
    # Add optional fields if provided
    if user_id:
        log_entry["user_id"] = user_id
    
    # Merge extra fields
    log_entry.update(extra)
    
    # Always print JSON to stdout (Railway/Better Stack will capture).
    # `default=str` so UUIDs/datetimes/etc. coming through `user_id` or `extra`
    # don't crash the global exception handlers — endpoints set
    # `request.state.user_id = current_user.id` (a UUID) and we read that back
    # here when an HTTPException bubbles up. Without `default=str` the dumps
    # raises TypeError, which then re-enters the exception path and masks the
    # original 4xx/5xx with an opaque 500.
    print(json.dumps(log_entry, default=str), file=sys.stdout, flush=True)
    
    # Additionally ship to Better Stack asynchronously (fire-and-forget)
    schedule_ship_log(log_entry)

