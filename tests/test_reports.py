import logging
from uuid import UUID

import pytest

from app.models import User, UserReport
from tests.conftest import register_user


@pytest.fixture
def admin_user(db):
    """Seed an is_admin=True user directly in the DB (no need to log them in)."""
    from app.auth import get_password_hash
    user = User(
        email="admin@example.com",
        password_hash=get_password_hash("adminpassword123"),
        is_admin=True,
    )
    db.add(user)
    db.flush()
    return user


def _scheduled_calls(background_scheduler):
    """Convenience: snapshot the list of scheduled background task callables."""
    return list(background_scheduler.calls)


class _FakeScheduler:
    """Captures BackgroundTasks scheduled calls without actually running them."""

    def __init__(self):
        self.calls = []

    def install(self, monkeypatch):
        from fastapi import BackgroundTasks

        real_add = BackgroundTasks.add_task

        def capture(self_bt, func, *args, **kwargs):
            _FakeScheduler._store.calls.append((func, args, kwargs))
            return real_add(self_bt, func, *args, **kwargs)

        _FakeScheduler._store = self
        monkeypatch.setattr(BackgroundTasks, "add_task", capture)


def _valid_body(**overrides):
    body = {
        "category": "platform",
        "description": "The start button on the lesson screen does nothing when I tap it.",
        "context": {"route": "/lesson/1", "situation_id": "bank_open_1"},
    }
    body.update(overrides)
    return body


def test_create_report_happy_path(client, db, auth_user, admin_user, monkeypatch):
    _, headers = auth_user

    scheduler = _FakeScheduler()
    scheduler.install(monkeypatch)
    # Prevent the captured background task from actually hitting SMTP.
    monkeypatch.setattr(
        "app.api.v1.reports.send_report_notification",
        lambda *args, **kwargs: True,
    )

    resp = client.post("/v1/reports", json=_valid_body(), headers=headers)

    assert resp.status_code == 201
    body = resp.json()
    assert body["category"] == "platform"
    assert body["status"] == "new"
    assert body["description"].startswith("The start button")
    report_id = UUID(body["id"])

    row = db.query(UserReport).filter(UserReport.id == report_id).one()
    assert row.category == "platform"
    assert row.context == {"route": "/lesson/1", "situation_id": "bank_open_1"}
    assert row.user_id is not None

    assert len(scheduler.calls) == 1
    _, args, _ = scheduler.calls[0]
    scheduled_report, scheduled_reporter_email, scheduled_recipients = args
    assert scheduled_report.id == report_id
    assert scheduled_reporter_email == "test@example.com"
    assert scheduled_recipients == ["admin@example.com"]


def test_create_report_description_too_short(client, auth_user):
    _, headers = auth_user
    resp = client.post(
        "/v1/reports",
        json=_valid_body(description="too short"),
        headers=headers,
    )
    assert resp.status_code == 422


def test_create_report_invalid_category(client, auth_user):
    _, headers = auth_user
    resp = client.post(
        "/v1/reports",
        json=_valid_body(category="not_a_real_category"),
        headers=headers,
    )
    assert resp.status_code == 422


def test_create_report_requires_auth_invalid_token(client):
    resp = client.post(
        "/v1/reports",
        json=_valid_body(),
        headers={"Authorization": "Bearer not-a-real-jwt"},
    )
    assert resp.status_code == 401


def test_create_report_no_admins_skips_scheduling(client, db, auth_user, monkeypatch, caplog):
    """With zero is_admin=True users, the background task must not be scheduled."""
    _, headers = auth_user

    scheduler = _FakeScheduler()
    scheduler.install(monkeypatch)

    with caplog.at_level(logging.WARNING, logger="app.api.v1.reports"):
        resp = client.post("/v1/reports", json=_valid_body(), headers=headers)

    assert resp.status_code == 201
    assert len(scheduler.calls) == 0
    assert any("No admin users configured" in rec.message for rec in caplog.records)


def test_create_report_notification_failure_does_not_fail_request(
    client, auth_user, admin_user, monkeypatch
):
    """If send_report_notification raises, the 201 response must still succeed."""
    _, headers = auth_user

    def boom(*args, **kwargs):
        raise RuntimeError("SMTP is on fire")

    monkeypatch.setattr("app.api.v1.reports.send_report_notification", boom)

    resp = client.post("/v1/reports", json=_valid_body(), headers=headers)
    # The background task runs AFTER the response is sent, so the status must
    # still be 201 regardless of what send_report_notification does.
    assert resp.status_code == 201
