"""Tests for the /v1/auth/explainers first-time flag store."""
from app.models import User
from tests.conftest import register_user


def test_explainers_empty_for_new_user(client):
    _, headers = register_user(client, email="exp_a@test.com")
    resp = client.get("/v1/auth/explainers", headers=headers)
    assert resp.status_code == 200
    assert resp.json() == {"keys": []}


def test_mark_explainer_seen_round_trips(client, db):
    data, headers = register_user(client, email="exp_b@test.com")

    resp = client.post(
        "/v1/auth/explainers/seen",
        json={"key": "vocab_word_cards"},
        headers=headers,
    )
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert "vocab_word_cards" in body["keys"]

    # Persisted on the user row
    db.expire_all()
    user = db.query(User).filter(User.email == data["email"]).one()
    assert user.seen_explainers.get("vocab_word_cards") is True

    # Round-trips through GET
    resp = client.get("/v1/auth/explainers", headers=headers)
    assert resp.status_code == 200
    assert "vocab_word_cards" in resp.json()["keys"]


def test_mark_explainer_seen_idempotent(client, db):
    data, headers = register_user(client, email="exp_c@test.com")

    for _ in range(3):
        resp = client.post(
            "/v1/auth/explainers/seen",
            json={"key": "verb_voice_chat"},
            headers=headers,
        )
        assert resp.status_code == 200

    db.expire_all()
    user = db.query(User).filter(User.email == data["email"]).one()
    assert user.seen_explainers == {"verb_voice_chat": True}


def test_mark_explainer_rejects_unknown_key(client):
    _, headers = register_user(client, email="exp_d@test.com")
    resp = client.post(
        "/v1/auth/explainers/seen",
        json={"key": "not_a_real_explainer"},
        headers=headers,
    )
    assert resp.status_code == 422  # Pydantic literal rejection


def test_multiple_explainers_accumulate(client, db):
    data, headers = register_user(client, email="exp_e@test.com")

    for key in ("vocab_word_cards", "verb_lesson", "verb_voice_chat"):
        client.post("/v1/auth/explainers/seen", json={"key": key}, headers=headers)

    resp = client.get("/v1/auth/explainers", headers=headers)
    assert resp.status_code == 200
    assert set(resp.json()["keys"]) == {"vocab_word_cards", "verb_lesson", "verb_voice_chat"}


def test_dashboard_tour_explainer_accepted(client, db):
    """The dashboard_tour key was added when the first-visit dashboard tour
    shipped — confirm the BE whitelist accepts it (regression guard)."""
    _, headers = register_user(client, email="exp_dash@test.com")
    resp = client.post(
        "/v1/auth/explainers/seen",
        json={"key": "dashboard_tour"},
        headers=headers,
    )
    assert resp.status_code == 200
    assert "dashboard_tour" in resp.json()["keys"]
