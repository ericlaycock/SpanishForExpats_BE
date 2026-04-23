"""HTTP-level tests for POST /v1/conversations/{id}/realtime-turn.

The endpoint is the FE's post-turn ingestion hook for the realtime voice
flow. These tests go through the FastAPI test client and exercise the full
stack: ownership check, word detection (regular + grammar-aware), turn_count
enforcement, and response shape.

No network — the endpoint has no outbound calls (detection + persistence
are deterministic against the DB).
"""
import uuid

import pytest

from app.models import Conversation, Situation, User, Word
from app.services.voice_turn_service import (
    EXCHANGE_HARD_LIMIT,
    EXCHANGE_WARNING_THRESHOLD,
)
from tests.conftest import register_user


def _get_auth_user_id(headers):
    from jose import jwt
    token = headers["Authorization"].split()[1]
    payload = jwt.get_unverified_claims(token)
    return uuid.UUID(payload["sub"])


def _seed_banking(db):
    sit = Situation(
        id="bank_rt_turn",
        title="Test Banking",
        animation_type="banking",
        encounter_number=1,
        order_index=1,
        is_free=True,
    )
    db.add(sit)
    words = [
        Word(id="wr_cuenta", spanish="cuenta", english="account", word_category="encounter"),
        Word(id="wr_depositar", spanish="depositar", english="to deposit", word_category="encounter"),
        Word(id="wr_retirar", spanish="retirar", english="to withdraw", word_category="encounter"),
    ]
    for w in words:
        db.add(w)
    db.flush()
    return [w.id for w in words]


def _make_conversation(
    db, user_id, target_word_ids, *,
    used_spoken_word_ids=None, turn_count=0,
):
    conv = Conversation(
        id=uuid.uuid4(),
        user_id=user_id,
        situation_id="bank_rt_turn",
        mode="voice",
        target_word_ids=target_word_ids,
        used_typed_word_ids=[],
        used_spoken_word_ids=used_spoken_word_ids or [],
        status="active",
        turn_count=turn_count,
    )
    db.add(conv)
    db.flush()
    return conv


# ── Happy path ──────────────────────────────────────────────────────────────


def test_realtime_turn_happy_path(client, db, auth_user):
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    target_ids = _seed_banking(db)
    conv = _make_conversation(db, user_id, target_ids)

    resp = client.post(
        f"/v1/conversations/{conv.id}/realtime-turn",
        json={
            "user_transcript": "Quiero abrir una cuenta",
            "assistant_text": "Perfecto, vamos a abrirla.",
        },
        headers=headers,
    )
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["detected_word_ids"] == ["wr_cuenta"]
    assert set(body["missing_word_ids"]) == {"wr_depositar", "wr_retirar"}
    assert body["conversation_complete"] is False
    assert body["turns_remaining"] == EXCHANGE_WARNING_THRESHOLD - 1


def test_realtime_turn_empty_transcript_still_increments_turn(client, db, auth_user):
    """Empty transcript shouldn't 4xx — sometimes OpenAI returns no transcript
    (background noise, silence). We still count the turn to keep the hard
    limit honest."""
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    target_ids = _seed_banking(db)
    conv = _make_conversation(db, user_id, target_ids)

    resp = client.post(
        f"/v1/conversations/{conv.id}/realtime-turn",
        json={"user_transcript": "", "assistant_text": ""},
        headers=headers,
    )
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["detected_word_ids"] == []
    assert set(body["missing_word_ids"]) == set(target_ids)
    assert body["conversation_complete"] is False

    db.refresh(conv)
    assert conv.turn_count == 1


def test_realtime_turn_all_words_detected_triggers_completion(client, db, auth_user):
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    target_ids = _seed_banking(db)
    conv = _make_conversation(
        db, user_id, target_ids,
        used_spoken_word_ids=[target_ids[0], target_ids[1]],
    )

    resp = client.post(
        f"/v1/conversations/{conv.id}/realtime-turn",
        json={
            "user_transcript": "Ahora quiero retirar dinero",
            "assistant_text": "Por supuesto.",
        },
        headers=headers,
    )
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert "wr_retirar" in body["detected_word_ids"]
    assert body["missing_word_ids"] == []
    assert body["conversation_complete"] is True

    db.refresh(conv)
    assert conv.status == "complete"
    assert conv.completed_at is not None


def test_realtime_turn_hard_limit_forces_complete_regardless_of_words(
    client, db, auth_user
):
    """At turn 30 the conversation must complete even if the user hasn't
    spoken all target words. Matches EXCHANGE_HARD_LIMIT on the FE; the
    realtime flow relies on this because the backend can't pull the plug
    on an OpenAI session otherwise."""
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    target_ids = _seed_banking(db)
    # Conversation sits at turn_count=29; next ingestion brings it to 30.
    conv = _make_conversation(
        db, user_id, target_ids,
        turn_count=EXCHANGE_HARD_LIMIT - 1,
    )

    resp = client.post(
        f"/v1/conversations/{conv.id}/realtime-turn",
        json={
            "user_transcript": "just some filler with no target words",
            "assistant_text": "ok",
        },
        headers=headers,
    )
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["detected_word_ids"] == []
    # Targets still missing but completion fires via the hard limit.
    assert body["conversation_complete"] is True
    assert body["turns_remaining"] == 0

    db.refresh(conv)
    assert conv.turn_count == EXCHANGE_HARD_LIMIT
    assert conv.status == "complete"


def test_realtime_turn_turn_29_not_yet_complete(client, db, auth_user):
    """Turn 29 (one-before-hard-limit) should NOT flip complete on its own."""
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    target_ids = _seed_banking(db)
    conv = _make_conversation(
        db, user_id, target_ids,
        turn_count=EXCHANGE_HARD_LIMIT - 2,  # 28 → becomes 29 after this call
    )

    resp = client.post(
        f"/v1/conversations/{conv.id}/realtime-turn",
        json={
            "user_transcript": "nothing",
            "assistant_text": "",
        },
        headers=headers,
    )
    assert resp.status_code == 200, resp.text
    assert resp.json()["conversation_complete"] is False

    db.refresh(conv)
    assert conv.turn_count == EXCHANGE_HARD_LIMIT - 1
    assert conv.status == "active"


# ── Ownership / auth ─────────────────────────────────────────────────────────


def test_realtime_turn_rejects_foreign_conversation(client, db, auth_user):
    """Another user's conversation must 404 — same behavior as /voice-turn.
    Not a 403 here: /voice-turn uses a combined user+id filter that returns
    404 for non-ownership, and we mirror that rather than adding a new
    leak-shape at this endpoint."""
    _, headers_a = auth_user

    _, headers_b = register_user(client, email="rt_other@example.com")
    user_b_id = _get_auth_user_id(headers_b)
    target_ids = _seed_banking(db)
    conv_b = _make_conversation(db, user_b_id, target_ids)

    resp = client.post(
        f"/v1/conversations/{conv_b.id}/realtime-turn",
        json={"user_transcript": "x", "assistant_text": "y"},
        headers=headers_a,
    )
    assert resp.status_code == 404


def test_realtime_turn_conversation_not_found(client, auth_user, db):
    _, headers = auth_user
    resp = client.post(
        f"/v1/conversations/{uuid.uuid4()}/realtime-turn",
        json={"user_transcript": "x", "assistant_text": "y"},
        headers=headers,
    )
    assert resp.status_code == 404


def test_realtime_turn_rejects_text_mode_conversation(client, db, auth_user):
    """Conversations in 'text' mode shouldn't accept realtime-turn — the
    endpoint only makes sense for voice."""
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_banking(db)
    conv = Conversation(
        id=uuid.uuid4(),
        user_id=user_id,
        situation_id="bank_rt_turn",
        mode="text",
        target_word_ids=[],
        used_typed_word_ids=[],
        used_spoken_word_ids=[],
        status="active",
    )
    db.add(conv)
    db.flush()

    resp = client.post(
        f"/v1/conversations/{conv.id}/realtime-turn",
        json={"user_transcript": "x", "assistant_text": "y"},
        headers=headers,
    )
    assert resp.status_code == 400


def test_realtime_turn_requires_auth(client, db):
    resp = client.post(
        f"/v1/conversations/{uuid.uuid4()}/realtime-turn",
        json={"user_transcript": "x", "assistant_text": "y"},
    )
    assert resp.status_code in (401, 403)


# ── Grammar-aware detection ─────────────────────────────────────────────────


def test_realtime_turn_detects_grammar_verb_via_conjugated_form(client, db, auth_user):
    """Grammar situations match any conjugated form from drill_config.answers
    back to the infinitive's grammar_<verb> id. Mirrors FE behavior."""
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)

    # grammar_regular_present_1 is defined in app/data/grammar_situations.py
    # with drill_config.answers mapping verbs to all their conjugations.
    from app.data.grammar_situations import get_grammar_config
    config = get_grammar_config("grammar_regular_present_1")
    if not config or not config.get("drill_config", {}).get("answers"):
        pytest.skip("grammar_regular_present_1 drill config unavailable")
    answers = config["drill_config"]["answers"]
    # Pick the first verb/form deterministically.
    verb = next(iter(answers.keys()))
    conjugated = next(v for v in answers[verb].values() if v)

    # Seed minimal grammar situation + base word
    sit = Situation(
        id="grammar_regular_present_1",
        title="Regular Present 1",
        animation_type="grammar",
        encounter_number=300,
        order_index=1300,
        is_free=True,
        situation_type="grammar",
    )
    db.add(sit)
    word = Word(
        id=f"grammar_{verb}",
        spanish=verb,
        english="to x",
        word_category="grammar",
    )
    db.add(word)
    db.flush()

    conv = Conversation(
        id=uuid.uuid4(),
        user_id=user_id,
        situation_id="grammar_regular_present_1",
        mode="voice",
        target_word_ids=[f"grammar_{verb}"],
        used_typed_word_ids=[],
        used_spoken_word_ids=[],
        status="active",
    )
    db.add(conv)
    db.flush()

    resp = client.post(
        f"/v1/conversations/{conv.id}/realtime-turn",
        json={
            "user_transcript": f"Yo {conjugated} todos los días.",
            "assistant_text": "claro",
        },
        headers=headers,
    )
    assert resp.status_code == 200, resp.text
    assert resp.json()["detected_word_ids"] == [f"grammar_{verb}"]
