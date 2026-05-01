"""Regression tests for app.core.logger.

The structured logger sits in the global exception handler path, so a
serialization crash here masks every 4xx/5xx the API ever returns and
surfaces an opaque 500 instead. The tests below pin the contract that
common non-JSON-native types (UUID, datetime) survive a `log_event`
call without raising.
"""
import json
import uuid
from datetime import datetime, timezone
from unittest.mock import patch

from app.core.logger import log_event


def _captured_stdout(monkeypatch_target_print):
    """Wrap `print` so we can assert what `log_event` emits."""
    captured = []

    def fake_print(payload, **_kwargs):
        captured.append(payload)

    return captured, fake_print


def test_log_event_serializes_uuid_user_id():
    """`request.state.user_id` is sometimes set to `current_user.id` (a UUID).
    The handler must not crash when that bubbles into `log_event`."""
    user_id = uuid.uuid4()
    captured = []

    with patch("app.core.logger.print", lambda payload, **_: captured.append(payload)):
        log_event(
            level="info",
            event="unit_test",
            message="m",
            request_id="req-1",
            user_id=user_id,  # type: ignore[arg-type]  — intentional: simulate UUID leak
        )

    assert captured, "log_event should have emitted exactly one line"
    parsed = json.loads(captured[0])
    assert parsed["user_id"] == str(user_id)


def test_log_event_serializes_uuid_in_extra():
    """UUIDs that ride along in `extra` (e.g. conversation_id) must also not
    crash dumps — the global handler injects `query_params` and similar."""
    conv_id = uuid.uuid4()
    captured = []

    with patch("app.core.logger.print", lambda payload, **_: captured.append(payload)):
        log_event(
            level="warning",
            event="unit_test",
            message="m",
            request_id="req-2",
            extra={"conversation_id": conv_id, "nested": {"id": conv_id}},
        )

    parsed = json.loads(captured[0])
    assert parsed["conversation_id"] == str(conv_id)
    assert parsed["nested"] == {"id": str(conv_id)}


def test_log_event_serializes_datetime_in_extra():
    """Same defense for datetime — Pydantic models hand these out routinely."""
    ts = datetime(2026, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
    captured = []

    with patch("app.core.logger.print", lambda payload, **_: captured.append(payload)):
        log_event(
            level="info",
            event="unit_test",
            message="m",
            request_id="req-3",
            extra={"created_at": ts},
        )

    parsed = json.loads(captured[0])
    # `default=str` calls str() on datetime, which yields ISO-ish output.
    assert "2026-01-02" in parsed["created_at"]
