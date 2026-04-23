"""HTTP-level tests for POST /v1/realtime/sessions.

Covers:
- Happy path: 201 + well-shaped body, passes through client_secret metadata.
- Ownership: 403 FORBIDDEN when the conversation belongs to another user.
- Not found: 404 for a random UUID.
- Paywall: 403 {error: "PAYWALL"} when the free tier is exhausted.
- Rate limit: 429 on a second mint within the window.
- OpenAI upstream errors: 502 for both 5xx and transport failures.

All tests mock `httpx.AsyncClient` used inside `realtime_session_service`, so
no network calls. DB work (Conversation, Situation, Subscription rows) runs
against the test Postgres via tests/conftest.py — SQLite is not compatible
with the JSONB/UUID columns per CLAUDE.md.
"""
import uuid

import pytest

from app.models import Conversation, Situation, Subscription, UserSituation
from app.services.realtime_session_service import (
    _reset_rate_limit_state_for_tests,
)
from tests.conftest import register_user


# ── Helpers ───────────────────────────────────────────────────────────────────


def _get_auth_user_id(headers):
    from jose import jwt
    token = headers["Authorization"].split()[1]
    payload = jwt.get_unverified_claims(token)
    return uuid.UUID(payload["sub"])


def _seed_banking_situation(db):
    sit = Situation(
        id="bank_open_rt",
        title="Open Bank Account",
        animation_type="banking",
        encounter_number=1,
        order_index=1,
        is_free=True,
    )
    db.add(sit)
    db.flush()
    return sit


def _make_voice_conversation(db, user_id, situation_id="bank_open_rt"):
    conv = Conversation(
        id=uuid.uuid4(),
        user_id=user_id,
        situation_id=situation_id,
        mode="voice",
        target_word_ids=[],
        used_typed_word_ids=[],
        used_spoken_word_ids=[],
        status="active",
    )
    db.add(conv)
    db.flush()
    return conv


class _FakeResponse:
    """httpx.Response-alike with just the bits realtime_session_service uses."""

    def __init__(self, *, status_code=200, body=None):
        self.status_code = status_code
        self.text = ""
        self._body = body or {}

    def raise_for_status(self):
        if self.status_code >= 400:
            import httpx
            req = httpx.Request("POST", "https://example.test")
            raise httpx.HTTPStatusError(
                f"{self.status_code}", request=req, response=self  # type: ignore[arg-type]
            )

    def json(self):
        return self._body


def _fake_openai_response(
    *,
    status_code: int = 200,
    client_secret_value: str = "ek_test_abc123",
    expires_at: int = 1776900000,
    model: str = "gpt-realtime-mini",
    voice: str = "shimmer",
    body_override: dict | None = None,
):
    """Build a fake httpx.Response-alike matching OpenAI's shape."""
    if body_override is not None:
        body = body_override
    else:
        body = {
            "id": "sess_test",
            "object": "realtime.session",
            "model": model,
            "voice": voice,
            "client_secret": {"value": client_secret_value, "expires_at": expires_at},
        }
    return _FakeResponse(status_code=status_code, body=body)


class _FakeAsyncClient:
    """Context-managed stand-in for httpx.AsyncClient used in the service.

    Captures the last call's args so tests can assert we posted the right
    session config to OpenAI.
    """

    _response = None  # class-level; reset per test via monkeypatch
    _raise_on_post = None
    last_call = {}

    def __init__(self, *args, **kwargs):
        self.init_kwargs = kwargs

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return False

    async def post(self, url, *, headers=None, json=None, **_):
        _FakeAsyncClient.last_call = {"url": url, "headers": headers, "json": json}
        if _FakeAsyncClient._raise_on_post is not None:
            raise _FakeAsyncClient._raise_on_post
        return _FakeAsyncClient._response


@pytest.fixture
def fake_httpx(monkeypatch):
    """Install _FakeAsyncClient in place of httpx.AsyncClient for the service.

    Yields a controller with `.set_response(...)` and `.raise_on_post(exc)`
    helpers so each test can dictate OpenAI's response.
    """
    _reset_rate_limit_state_for_tests()
    _FakeAsyncClient._response = _fake_openai_response()
    _FakeAsyncClient._raise_on_post = None
    _FakeAsyncClient.last_call = {}

    monkeypatch.setattr(
        "app.services.realtime_session_service.httpx.AsyncClient",
        _FakeAsyncClient,
    )

    class _Controller:
        def set_response(self, resp):
            _FakeAsyncClient._response = resp

        def raise_on_post(self, exc):
            _FakeAsyncClient._raise_on_post = exc

        @property
        def last_call(self):
            return _FakeAsyncClient.last_call

    yield _Controller()

    _reset_rate_limit_state_for_tests()


# ── Happy path ────────────────────────────────────────────────────────────────


def test_create_session_happy_path(client, db, auth_user, fake_httpx):
    """201 + all four fields present, and the session config posted to OpenAI
    carries the expected model + voice for this situation."""
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_banking_situation(db)
    conv = _make_voice_conversation(db, user_id)

    resp = client.post(
        "/v1/realtime/sessions",
        json={"conversation_id": str(conv.id)},
        headers=headers,
    )

    assert resp.status_code == 201, resp.text
    body = resp.json()
    assert body["client_secret"] == "ek_test_abc123"
    assert body["expires_at"] == 1776900000
    assert body["model"] == "gpt-realtime-mini"
    assert body["voice"] == "shimmer"

    # Verify we posted the right session config to OpenAI.
    posted = fake_httpx.last_call["json"]
    assert posted["model"] == "gpt-realtime-mini"
    assert posted["voice"] == "shimmer"  # banking situation
    assert posted["turn_detection"] == {
        "type": "server_vad",
        "threshold": 0.5,
        "silence_duration_ms": 500,
    }
    assert posted["input_audio_transcription"] == {"model": "whisper-1"}
    assert fake_httpx.last_call["url"] == (
        "https://api.openai.com/v1/realtime/sessions"
    )
    assert fake_httpx.last_call["headers"]["OpenAI-Beta"] == "realtime=v1"


# ── Validation / missing conversation ─────────────────────────────────────────


def test_create_session_conversation_not_found(client, auth_user, fake_httpx):
    _, headers = auth_user
    resp = client.post(
        "/v1/realtime/sessions",
        json={"conversation_id": str(uuid.uuid4())},
        headers=headers,
    )
    assert resp.status_code == 404, resp.text


def test_create_session_malformed_uuid_422(client, auth_user, fake_httpx):
    """Pydantic should reject a non-UUID body before the service runs."""
    _, headers = auth_user
    resp = client.post(
        "/v1/realtime/sessions",
        json={"conversation_id": "not-a-uuid"},
        headers=headers,
    )
    assert resp.status_code == 422


# ── Ownership ────────────────────────────────────────────────────────────────


def test_create_session_rejects_foreign_conversation(client, db, auth_user, fake_httpx):
    """User A asking for a client_secret on User B's conversation → 403 FORBIDDEN,
    not 404 (404 would leak which ids exist)."""
    _, headers_a = auth_user

    # Create user B + their own conversation
    _, headers_b = register_user(client, email="other@example.com")
    user_b_id = _get_auth_user_id(headers_b)
    _seed_banking_situation(db)
    conv_b = _make_voice_conversation(db, user_b_id)

    resp = client.post(
        "/v1/realtime/sessions",
        json={"conversation_id": str(conv_b.id)},
        headers=headers_a,
    )
    assert resp.status_code == 403, resp.text
    assert resp.json()["detail"] == {"error": "FORBIDDEN"}


# ── Paywall ───────────────────────────────────────────────────────────────────


def test_create_session_paywall_blocks_exhausted_free_user(
    client, db, auth_user, fake_httpx
):
    """Free user who has completed the free-tier limit on non-grammar
    encounters → 403 {error: 'PAYWALL'}."""
    from app.services.subscription_service import FREE_ENCOUNTERS_LIMIT

    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_banking_situation(db)
    conv = _make_voice_conversation(db, user_id)

    # Give the user an inactive subscription (default) and N completed
    # non-grammar encounters to trip the gate.
    db.add(Subscription(user_id=user_id, active=False))
    for i in range(FREE_ENCOUNTERS_LIMIT):
        sit = Situation(
            id=f"bank_paywall_{i}",
            title=f"Paywall seed {i}",
            animation_type="banking",
            encounter_number=i + 2,
            order_index=100 + i,
            is_free=True,
        )
        db.add(sit)
        db.flush()
        db.add(UserSituation(
            user_id=user_id,
            situation_id=sit.id,
            completed_at=__import__("datetime").datetime.now(
                __import__("datetime").timezone.utc
            ),
        ))
    db.flush()

    resp = client.post(
        "/v1/realtime/sessions",
        json={"conversation_id": str(conv.id)},
        headers=headers,
    )
    assert resp.status_code == 403, resp.text
    assert resp.json()["detail"] == {"error": "PAYWALL"}


def test_create_session_admin_bypasses_paywall(client, db, auth_user, fake_httpx):
    """is_admin=True should bypass the paywall — matches /voice-turn's behavior."""
    from app.models import User
    from app.services.subscription_service import FREE_ENCOUNTERS_LIMIT

    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    db.query(User).filter(User.id == user_id).update({"is_admin": True})
    _seed_banking_situation(db)
    conv = _make_voice_conversation(db, user_id)

    # Seed enough completions that a non-admin would be paywalled.
    for i in range(FREE_ENCOUNTERS_LIMIT):
        sit = Situation(
            id=f"bank_admin_{i}",
            title=f"Admin seed {i}",
            animation_type="banking",
            encounter_number=i + 2,
            order_index=200 + i,
            is_free=True,
        )
        db.add(sit)
        db.flush()
        db.add(UserSituation(
            user_id=user_id,
            situation_id=sit.id,
            completed_at=__import__("datetime").datetime.now(
                __import__("datetime").timezone.utc
            ),
        ))
    db.flush()

    resp = client.post(
        "/v1/realtime/sessions",
        json={"conversation_id": str(conv.id)},
        headers=headers,
    )
    assert resp.status_code == 201, resp.text


# ── Rate limit ───────────────────────────────────────────────────────────────


def test_create_session_rate_limited_on_second_call(client, db, auth_user, fake_httpx):
    """Two mints for the same (user, conversation) within the window →
    first 201, second 429 with retry_after_seconds."""
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_banking_situation(db)
    conv = _make_voice_conversation(db, user_id)

    r1 = client.post(
        "/v1/realtime/sessions",
        json={"conversation_id": str(conv.id)},
        headers=headers,
    )
    assert r1.status_code == 201, r1.text

    r2 = client.post(
        "/v1/realtime/sessions",
        json={"conversation_id": str(conv.id)},
        headers=headers,
    )
    assert r2.status_code == 429, r2.text
    detail = r2.json()["detail"]
    assert detail["error"] == "RATE_LIMITED"
    assert isinstance(detail["retry_after_seconds"], int)
    assert detail["retry_after_seconds"] >= 1


def test_create_session_rate_limit_is_per_conversation(client, db, auth_user, fake_httpx):
    """Rate limit keys on (user, conversation) — a second conversation
    for the same user should still mint."""
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_banking_situation(db)
    conv1 = _make_voice_conversation(db, user_id)
    conv2 = _make_voice_conversation(db, user_id)

    r1 = client.post(
        "/v1/realtime/sessions",
        json={"conversation_id": str(conv1.id)},
        headers=headers,
    )
    r2 = client.post(
        "/v1/realtime/sessions",
        json={"conversation_id": str(conv2.id)},
        headers=headers,
    )
    assert r1.status_code == 201
    assert r2.status_code == 201


# ── OpenAI upstream failures ─────────────────────────────────────────────────


def test_create_session_openai_5xx_returns_502(client, db, auth_user, fake_httpx):
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_banking_situation(db)
    conv = _make_voice_conversation(db, user_id)

    fake_httpx.set_response(_fake_openai_response(status_code=503))

    resp = client.post(
        "/v1/realtime/sessions",
        json={"conversation_id": str(conv.id)},
        headers=headers,
    )
    assert resp.status_code == 502, resp.text


def test_create_session_openai_unreachable_returns_502(client, db, auth_user, fake_httpx):
    import httpx

    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_banking_situation(db)
    conv = _make_voice_conversation(db, user_id)

    fake_httpx.raise_on_post(httpx.ConnectError("boom"))

    resp = client.post(
        "/v1/realtime/sessions",
        json={"conversation_id": str(conv.id)},
        headers=headers,
    )
    assert resp.status_code == 502, resp.text


def test_create_session_openai_returns_incomplete_body_is_502(
    client, db, auth_user, fake_httpx
):
    """Guard: if OpenAI 200s but without client_secret.value, we must not
    return a malformed shape to the FE."""
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_banking_situation(db)
    conv = _make_voice_conversation(db, user_id)

    fake_httpx.set_response(
        _fake_openai_response(body_override={"id": "sess_x", "model": "gpt-realtime-mini"})
    )

    resp = client.post(
        "/v1/realtime/sessions",
        json={"conversation_id": str(conv.id)},
        headers=headers,
    )
    assert resp.status_code == 502, resp.text


# ── Auth ─────────────────────────────────────────────────────────────────────


def test_create_session_requires_auth(client, fake_httpx):
    resp = client.post(
        "/v1/realtime/sessions",
        json={"conversation_id": str(uuid.uuid4())},
    )
    # Matches other authed endpoints — 401/403 depending on get_current_user
    # implementation. Accept either so the test isn't brittle.
    assert resp.status_code in (401, 403)
