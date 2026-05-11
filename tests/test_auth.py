from datetime import datetime, timezone

from app.models import (
    Conversation,
    User,
    UserMilestoneEvent,
    UserSituation,
    UserWord,
)
from tests.conftest import register_user


def test_register_success(client):
    resp = client.post("/v1/auth/register", json={
        "email": "new@example.com",
        "password": "testpassword123",
        "confirm_password": "testpassword123",
    })
    assert resp.status_code == 200
    data = resp.json()
    assert "access_token" in data
    assert "user_id" in data


def test_register_duplicate_email(client):
    register_user(client, email="dup@example.com")
    resp = client.post("/v1/auth/register", json={
        "email": "dup@example.com",
        "password": "testpassword123",
        "confirm_password": "testpassword123",
    })
    assert resp.status_code == 400
    assert "already registered" in resp.json()["detail"].lower()


def test_login_success(client):
    register_user(client, email="login@example.com")
    resp = client.post("/v1/auth/login", json={
        "email": "login@example.com",
        "password": "testpassword123",
    })
    assert resp.status_code == 200
    assert "access_token" in resp.json()


def test_login_wrong_password(client):
    register_user(client, email="wrong@example.com")
    resp = client.post("/v1/auth/login", json={
        "email": "wrong@example.com",
        "password": "wrongpassword123",
    })
    assert resp.status_code == 401


def test_reset_progress_requires_admin(client):
    _, headers = register_user(client, email="notadmin@example.com")
    resp = client.post("/v1/auth/reset-progress", headers=headers)
    assert resp.status_code == 403


def test_reset_progress_clears_progress_including_milestone_events(client, db, seed_data):
    """Reset must also drop user_milestone_events — they hold a non-cascading FK
    to conversations, so leaving them makes the conversation delete fail with a
    foreign-key violation (the bug this test guards against)."""
    data, headers = register_user(client, email="resetme@example.com")
    user = db.query(User).filter(User.id == data["user_id"]).first()
    user.is_admin = True
    db.flush()

    now = datetime.now(timezone.utc)
    conv = Conversation(
        user_id=user.id, situation_id="bank_open_1", mode="voice", target_word_ids=[],
    )
    db.add(conv)
    db.flush()
    db.add(UserWord(user_id=user.id, word_id="hf_1", mastery_level=1))
    db.add(UserSituation(user_id=user.id, situation_id="bank_open_1", completed_at=now))
    db.add(UserMilestoneEvent(
        user_id=user.id, milestone_key="phase_drill",
        situation_id="bank_open_1", conversation_id=conv.id,
    ))
    db.flush()

    resp = client.post("/v1/auth/reset-progress", headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["reset"] is True
    assert body["deleted_words"] == 1
    assert body["deleted_situations"] == 1
    assert body["deleted_conversations"] == 1

    assert db.query(UserWord).filter(UserWord.user_id == user.id).count() == 0
    assert db.query(UserSituation).filter(UserSituation.user_id == user.id).count() == 0
    assert db.query(Conversation).filter(Conversation.user_id == user.id).count() == 0
    assert db.query(UserMilestoneEvent).filter(UserMilestoneEvent.user_id == user.id).count() == 0
    # Account itself survives.
    assert db.query(User).filter(User.id == user.id).count() == 1
