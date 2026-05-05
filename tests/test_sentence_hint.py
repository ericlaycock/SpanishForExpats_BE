"""HTTP-level tests for POST /v1/conversations/{id}/sentence-hint.

After the TTS/R2 strip the contract is:
    request:  { messages_json?: stringified [{role, content}] }
    response: { english_gloss: str, hints_remaining: int }

Covers happy path + cap-removed sentinel + the two 409 cases. The
per-conversation cap was removed in commit e4e0f19; the BE now returns
a fixed `hints_remaining=999` sentinel so the FE keeps rendering its
counter without a special case. Upstream LLM call is monkeypatched. No
TTS, no R2.
"""
import uuid

from app.models import Conversation, Situation, Word


def _seed_vocab_situation(db):
    sit = Situation(
        id="bank_hint",
        title="Open a Bank Account",
        animation_type="banking",
        encounter_number=1,
        order_index=1,
        is_free=True,
    )
    db.add(sit)
    db.add_all([
        Word(id="word_cuenta", spanish="cuenta", english="account", word_category="encounter"),
        Word(id="word_depositar", spanish="depositar", english="to deposit", word_category="encounter"),
    ])
    db.flush()
    return sit


def _make_voice_conv(db, user_id, situation_id, target_word_ids, used=None, status="active"):
    conv = Conversation(
        id=uuid.uuid4(),
        user_id=user_id,
        situation_id=situation_id,
        mode="voice",
        target_word_ids=target_word_ids,
        used_typed_word_ids=[],
        used_spoken_word_ids=used or [],
        status=status,
    )
    db.add(conv)
    db.flush()
    return conv


def _stub_llm(monkeypatch, *, content="Could you open an **account** for me?"):
    """Patch the LLM call to return a deterministic English string."""
    from app.services import sentence_hint_service as svc

    async def fake_generate_conversation(context, db):
        return {
            "content": content,
            "tokens_in": 80,
            "tokens_out": 20,
            "latency_ms": 300,
            "estimated_cost": 0.00005,
            "llm_request_id": None,
        }

    monkeypatch.setattr(svc, "generate_conversation", fake_generate_conversation)


def test_sentence_hint_happy_path(client, db, auth_user, monkeypatch):
    _, headers = auth_user
    sit = _seed_vocab_situation(db)
    conv = _make_voice_conv(
        db,
        user_id=_jwt_user_id(headers),
        situation_id=sit.id,
        target_word_ids=["word_cuenta", "word_depositar"],
    )
    db.commit()

    _stub_llm(monkeypatch, content="Could you open an **account** for me?")

    r = client.post(
        f"/v1/conversations/{conv.id}/sentence-hint",
        headers=headers,
        json={},
    )
    assert r.status_code == 200, r.text
    body = r.json()
    # `hints_remaining` is a fixed sentinel post-cap-removal (e4e0f19) —
    # the FE counter keeps rendering, but there is no per-conversation
    # ceiling enforced server-side.
    assert body == {
        "english_gloss": "Could you open an **account** for me?",
        "hints_remaining": 999,
    }


def test_sentence_hint_no_per_conversation_cap(client, db, auth_user, monkeypatch):
    """The per-conversation hint cap was removed in commit e4e0f19. Pin
    that callers can keep requesting hints without hitting a 429 — the
    sentinel `hints_remaining` stays positive across many calls.
    """
    _, headers = auth_user
    sit = _seed_vocab_situation(db)
    conv = _make_voice_conv(
        db,
        user_id=_jwt_user_id(headers),
        situation_id=sit.id,
        target_word_ids=["word_cuenta", "word_depositar"],
    )
    db.commit()

    _stub_llm(monkeypatch)

    # Six calls — would have tripped the old 5-cap; should all succeed now.
    for _ in range(6):
        r = client.post(
            f"/v1/conversations/{conv.id}/sentence-hint",
            headers=headers,
            json={},
        )
        assert r.status_code == 200, r.text
        assert r.json()["hints_remaining"] > 0


def test_sentence_hint_409_when_all_words_detected(client, db, auth_user, monkeypatch):
    _, headers = auth_user
    sit = _seed_vocab_situation(db)
    conv = _make_voice_conv(
        db,
        user_id=_jwt_user_id(headers),
        situation_id=sit.id,
        target_word_ids=["word_cuenta", "word_depositar"],
        used=["word_cuenta", "word_depositar"],
    )
    db.commit()

    _stub_llm(monkeypatch)

    r = client.post(
        f"/v1/conversations/{conv.id}/sentence-hint",
        headers=headers,
        json={},
    )
    assert r.status_code == 409
    assert r.json()["detail"] == "NO_PENDING_ITEMS"


def test_sentence_hint_409_when_conversation_complete(client, db, auth_user, monkeypatch):
    _, headers = auth_user
    sit = _seed_vocab_situation(db)
    conv = _make_voice_conv(
        db,
        user_id=_jwt_user_id(headers),
        situation_id=sit.id,
        target_word_ids=["word_cuenta"],
        status="complete",
    )
    db.commit()

    _stub_llm(monkeypatch)

    r = client.post(
        f"/v1/conversations/{conv.id}/sentence-hint",
        headers=headers,
        json={},
    )
    assert r.status_code == 409
    assert r.json()["detail"] == "NO_PENDING_ITEMS"


def _jwt_user_id(headers):
    """Decode the Bearer JWT to get the user UUID. We need this on the BE
    side because the conversation row needs the same user_id the JWT is
    minted for."""
    from jose import jwt
    token = headers["Authorization"].split()[1]
    payload = jwt.get_unverified_claims(token)
    return uuid.UUID(payload["sub"])
