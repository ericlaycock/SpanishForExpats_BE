"""HTTP-level tests for POST /v1/conversations/{id}/sentence-hint.

Covers:
- Happy path (vocab): 200 with spanish, english_gloss, audio_url, used_item_ids
  and hints_remaining decremented by 1.
- Grammar path: pending items walk drill_targets and the LLM is fed conjugated
  forms it can pick from.
- Cap: 5th hint succeeds, 6th returns 429 HINT_RATE_LIMIT.
- 409 NO_PENDING_ITEMS when every target word is already detected.
- 409 NO_PENDING_ITEMS when conversation status is already "complete".
- 404 when the conversation belongs to another user (or doesn't exist).
- turn_count is NOT incremented by hints — they are help, not progress.
- Audit row in `sentence_hints` carries the artefact text + pending_count.
- TTS failure: endpoint still returns the hint with audio_url=None.

All upstream calls (LLM, TTS, R2 upload) are monkeypatched. DB work runs
against the Postgres test instance via tests/conftest.py.
"""
import uuid

import pytest

from app.models import Conversation, SentenceHint, Situation, Word


# ── Helpers ───────────────────────────────────────────────────────────────


def _get_auth_user_id(headers):
    from jose import jwt
    token = headers["Authorization"].split()[1]
    payload = jwt.get_unverified_claims(token)
    return uuid.UUID(payload["sub"])


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
        Word(id="word_pasaporte", spanish="pasaporte", english="passport", word_category="high_frequency"),
    ])
    db.flush()
    return sit


def _seed_grammar_situation(db):
    """Use an existing grammar situation id from grammar_situations.py so
    `get_grammar_config` resolves and returns drill_targets.
    """
    sit = Situation(
        id="grammar_regular_present_1",
        title="Regular Present (1/3)",
        animation_type="grammar",
        encounter_number=300,
        order_index=1300,
        is_free=True,
        situation_type="grammar",
    )
    db.add(sit)
    db.add_all([
        Word(id="grammar_hablar", spanish="hablar", english="to speak", word_category="grammar"),
        Word(id="grammar_beber", spanish="beber", english="to drink", word_category="grammar"),
        Word(id="grammar_vivir", spanish="vivir", english="to live", word_category="grammar"),
    ])
    db.flush()
    return sit


def _make_voice_conv(db, user_id, situation_id, target_word_ids, used=None):
    conv = Conversation(
        id=uuid.uuid4(),
        user_id=user_id,
        situation_id=situation_id,
        mode="voice",
        target_word_ids=target_word_ids,
        used_typed_word_ids=[],
        used_spoken_word_ids=used or [],
        status="active",
    )
    db.add(conv)
    db.flush()
    return conv


def _stub_llm_and_tts(monkeypatch, *, spanish="Quiero abrir una cuenta.",
                      english_gloss="I want to open an account.",
                      used_item_ids=None,
                      audio_url="https://r2.example/hint_test.mp3"):
    """Wire the service to deterministic LLM/TTS responses.

    `llm_request_id` and `tts_request_id` are returned as None so tests
    don't need to seed those gateway tables — the audit row's FKs are
    nullable for exactly this reason. Production paths will populate them.
    """
    from app.services import sentence_hint_service as svc

    async def fake_generate_conversation(context, db):
        return {
            "content": {
                "spanish": spanish,
                "english_gloss": english_gloss,
                "used_item_ids": used_item_ids or [],
            },
            "tokens_in": 100,
            "tokens_out": 30,
            "latency_ms": 400,
            "estimated_cost": 0.0001,
            "llm_request_id": None,
        }

    async def fake_synthesize(db, *, text, voice, instructions, request_id, user_id):
        return audio_url, None

    monkeypatch.setattr(svc, "generate_conversation", fake_generate_conversation)
    monkeypatch.setattr(svc, "synthesize_hint_audio", fake_synthesize)


# ── Tests ─────────────────────────────────────────────────────────────────


def test_sentence_hint_vocab_happy_path(client, db, auth_user, monkeypatch):
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_vocab_situation(db)
    conv = _make_voice_conv(
        db, user_id, "bank_hint",
        target_word_ids=["word_cuenta", "word_depositar", "word_pasaporte"],
    )
    db.commit()

    _stub_llm_and_tts(
        monkeypatch,
        spanish="Quiero abrir una cuenta.",
        english_gloss="I want to open an account.",
        used_item_ids=["word_cuenta"],
    )

    resp = client.post(
        f"/v1/conversations/{conv.id}/sentence-hint",
        json={},
        headers=headers,
    )

    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["spanish"] == "Quiero abrir una cuenta."
    assert body["english_gloss"] == "I want to open an account."
    assert body["audio_url"] == "https://r2.example/hint_test.mp3"
    assert body["used_item_ids"] == ["word_cuenta"]
    assert body["hints_remaining"] == 4

    db.refresh(conv)
    assert conv.sentence_hints_used == 1
    assert conv.turn_count == 0  # hints don't advance turns

    # Audit row persisted with the same artefacts
    audit = db.query(SentenceHint).filter_by(conversation_id=conv.id).one()
    assert audit.spanish == "Quiero abrir una cuenta."
    assert audit.english_gloss == "I want to open an account."
    assert audit.audio_url == "https://r2.example/hint_test.mp3"
    assert audit.used_item_ids == ["word_cuenta"]
    assert audit.pending_count == 3
    assert audit.user_id == user_id
    assert audit.situation_id == "bank_hint"


def test_sentence_hint_grammar_emits_conjugation_candidates(
    client, db, auth_user, monkeypatch
):
    """For a grammar conversation, the LLM should be fed conj_<verb>_<pronoun>
    candidates pulled from drill_targets + drill_config.answers.
    """
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_grammar_situation(db)
    conv = _make_voice_conv(
        db, user_id, "grammar_regular_present_1",
        target_word_ids=["grammar_hablar", "grammar_beber", "grammar_vivir"],
    )
    db.commit()

    captured = {}
    from app.services import sentence_hint_service as svc

    real_build = svc.build_hint_messages

    def spy_build(pending_items, recent_messages, situation_title, alt_language, spanish_level=None):
        captured["items"] = list(pending_items)
        return real_build(
            pending_items, recent_messages, situation_title, alt_language,
            spanish_level=spanish_level,
        )

    monkeypatch.setattr(svc, "build_hint_messages", spy_build)
    _stub_llm_and_tts(
        monkeypatch,
        spanish="Yo hablo inglés.",
        english_gloss="I speak English.",
        used_item_ids=["conj_hablar_yo"],
    )

    resp = client.post(
        f"/v1/conversations/{conv.id}/sentence-hint",
        json={},
        headers=headers,
    )
    assert resp.status_code == 200, resp.text

    items = captured["items"]
    assert items, "Expected pending items for a grammar conversation"
    assert all(it.kind == "grammar" for it in items)
    # Conjugated forms come from drill_config.answers — sanity-check one.
    pairs = {(it.verb, it.pronoun): it.conjugated for it in items}
    assert pairs.get(("hablar", "yo")) == "hablo"
    assert all(
        it.id == f"conj_{it.verb}_{it.pronoun}" for it in items
    )


def test_sentence_hint_cap_blocks_sixth(client, db, auth_user, monkeypatch):
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_vocab_situation(db)
    conv = _make_voice_conv(
        db, user_id, "bank_hint",
        target_word_ids=["word_cuenta", "word_depositar"],
    )
    conv.sentence_hints_used = 5
    db.commit()

    _stub_llm_and_tts(monkeypatch)

    resp = client.post(
        f"/v1/conversations/{conv.id}/sentence-hint",
        json={},
        headers=headers,
    )
    assert resp.status_code == 429
    assert resp.json()["detail"] == "HINT_RATE_LIMIT"


def test_sentence_hint_409_when_all_words_detected(
    client, db, auth_user, monkeypatch
):
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_vocab_situation(db)
    conv = _make_voice_conv(
        db, user_id, "bank_hint",
        target_word_ids=["word_cuenta", "word_depositar"],
        used=["word_cuenta", "word_depositar"],
    )
    db.commit()
    _stub_llm_and_tts(monkeypatch)

    resp = client.post(
        f"/v1/conversations/{conv.id}/sentence-hint",
        json={},
        headers=headers,
    )
    assert resp.status_code == 409
    assert resp.json()["detail"] == "NO_PENDING_ITEMS"


def test_sentence_hint_409_when_conversation_complete(
    client, db, auth_user, monkeypatch
):
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_vocab_situation(db)
    conv = _make_voice_conv(
        db, user_id, "bank_hint",
        target_word_ids=["word_cuenta"],
    )
    conv.status = "complete"
    db.commit()
    _stub_llm_and_tts(monkeypatch)

    resp = client.post(
        f"/v1/conversations/{conv.id}/sentence-hint",
        json={},
        headers=headers,
    )
    assert resp.status_code == 409
    assert resp.json()["detail"] == "NO_PENDING_ITEMS"


def test_sentence_hint_404_when_owned_by_other_user(
    client, db, auth_user, monkeypatch
):
    _, headers = auth_user
    _seed_vocab_situation(db)
    # Register a second real user so the conversations FK to users.id holds.
    from tests.conftest import register_user
    other_data, _ = register_user(client, email="other@example.com")
    other_user_id = uuid.UUID(other_data["user_id"])
    conv = _make_voice_conv(
        db, other_user_id, "bank_hint",
        target_word_ids=["word_cuenta"],
    )
    db.commit()
    _stub_llm_and_tts(monkeypatch)

    resp = client.post(
        f"/v1/conversations/{conv.id}/sentence-hint",
        json={},
        headers=headers,
    )
    assert resp.status_code == 404


def test_sentence_hint_audio_failure_returns_text_only(
    client, db, auth_user, monkeypatch
):
    """If TTS or the R2 upload fails, the endpoint still returns the hint
    with audio_url=None. The avatar bubble shows the text without the
    Listen affordance.
    """
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_vocab_situation(db)
    conv = _make_voice_conv(
        db, user_id, "bank_hint",
        target_word_ids=["word_cuenta"],
    )
    db.commit()

    _stub_llm_and_tts(
        monkeypatch,
        spanish="Quiero una cuenta.",
        english_gloss="I want an account.",
        used_item_ids=["word_cuenta"],
        audio_url=None,
    )

    resp = client.post(
        f"/v1/conversations/{conv.id}/sentence-hint",
        json={},
        headers=headers,
    )
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["spanish"] == "Quiero una cuenta."
    assert body["audio_url"] is None
    assert body["hints_remaining"] == 4

    db.refresh(conv)
    assert conv.sentence_hints_used == 1


def test_sentence_hint_falls_back_when_llm_returns_unparseable_json(
    client, db, auth_user, monkeypatch
):
    """gpt-5.4-mini's Responses API + reasoning + return_json sometimes
    returns an empty output_text, which makes `json.loads('')` raise.
    The endpoint must NOT 500 — it should fall back to a first-pending-
    item suggestion so the user keeps getting hints.
    """
    import json as _json

    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_vocab_situation(db)
    conv = _make_voice_conv(
        db, user_id, "bank_hint",
        target_word_ids=["word_cuenta", "word_depositar"],
    )
    db.commit()

    from app.services import sentence_hint_service as svc

    async def boom(context, db):
        raise _json.JSONDecodeError("Expecting value", "", 0)

    async def fake_synthesize(db, *, text, voice, instructions, request_id, user_id):
        return None, None

    monkeypatch.setattr(svc, "generate_conversation", boom)
    monkeypatch.setattr(svc, "synthesize_hint_audio", fake_synthesize)

    resp = client.post(
        f"/v1/conversations/{conv.id}/sentence-hint",
        json={},
        headers=headers,
    )
    assert resp.status_code == 200, resp.text
    body = resp.json()
    # Fallback uses the first pending item — it must surface a non-empty
    # spanish + english_gloss (no 500, no blank bubble).
    assert body["spanish"], "expected fallback spanish text, got empty"
    assert body["english_gloss"], "expected fallback gloss, got empty"
    assert body["used_item_ids"]  # at least one fallback id

    db.refresh(conv)
    # The cap counter still increments — a malformed model reply still
    # consumed the user's quota; we don't want to charge the user but
    # we also don't want to game the cap by returning empty hints.
    assert conv.sentence_hints_used == 1


def test_sentence_hint_does_not_change_turn_count(
    client, db, auth_user, monkeypatch
):
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_vocab_situation(db)
    conv = _make_voice_conv(
        db, user_id, "bank_hint",
        target_word_ids=["word_cuenta", "word_depositar"],
    )
    conv.turn_count = 7
    db.commit()
    _stub_llm_and_tts(monkeypatch)

    for _ in range(3):
        resp = client.post(
            f"/v1/conversations/{conv.id}/sentence-hint",
            json={},
            headers=headers,
        )
        assert resp.status_code == 200, resp.text

    db.refresh(conv)
    assert conv.turn_count == 7
    assert conv.sentence_hints_used == 3
