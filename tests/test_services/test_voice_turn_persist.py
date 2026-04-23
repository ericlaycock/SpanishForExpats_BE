"""Unit tests for the Phase 2/3 voice-turn helpers.

Covers `detect_words`, `persist_turn`, and `check_completion` in
`app/services/voice_turn_service.py`. These run against the test Postgres
(via tests/conftest.py) — they don't go through the HTTP layer, so they
exercise edge cases that would be awkward to trigger from an endpoint test
(e.g. constructing a conversation at turn_count=29).
"""
import uuid
from datetime import datetime, timezone

import pytest

from app.auth import get_password_hash
from app.models import Conversation, Situation, User, UserWord, Word
from app.services.voice_turn_service import (
    EXCHANGE_HARD_LIMIT,
    EXCHANGE_WARNING_THRESHOLD,
    check_completion,
    detect_words,
    persist_turn,
)


# ── Fixtures ──────────────────────────────────────────────────────────────────


def _make_user(db, *, email_suffix=None) -> User:
    user = User(
        id=uuid.uuid4(),
        email=f"vt_{email_suffix or uuid.uuid4().hex[:8]}@test.com",
        password_hash=get_password_hash("testpass123"),
    )
    db.add(user)
    db.flush()
    return user


def _make_situation(db, *, sid="bank_open_vt", animation_type="banking") -> Situation:
    sit = Situation(
        id=sid,
        title="Test Banking",
        animation_type=animation_type,
        encounter_number=1,
        order_index=1,
        is_free=True,
    )
    db.add(sit)
    db.flush()
    return sit


def _seed_words(db):
    words = [
        Word(id="w_cuenta", spanish="cuenta", english="account", word_category="encounter"),
        Word(id="w_depositar", spanish="depositar", english="to deposit", word_category="encounter"),
        Word(id="w_retirar", spanish="retirar", english="to withdraw", word_category="encounter"),
    ]
    for w in words:
        db.add(w)
    db.flush()
    return [w.id for w in words]


def _make_conversation(
    db,
    user_id,
    *,
    situation_id="bank_open_vt",
    target_word_ids=None,
    used_spoken_word_ids=None,
    turn_count=0,
    conversation_type="lesson",
):
    conv = Conversation(
        id=uuid.uuid4(),
        user_id=user_id,
        situation_id=situation_id,
        mode="voice",
        conversation_type=conversation_type,
        target_word_ids=target_word_ids or [],
        used_typed_word_ids=[],
        used_spoken_word_ids=used_spoken_word_ids or [],
        status="active",
        turn_count=turn_count,
    )
    db.add(conv)
    db.flush()
    return conv


# ── detect_words ──────────────────────────────────────────────────────────────


def test_detect_words_matches_target_words_in_transcript(db):
    user = _make_user(db)
    _make_situation(db)
    target_ids = _seed_words(db)
    conv = _make_conversation(db, user.id, target_word_ids=target_ids)

    detected = detect_words(db, conv, "Quiero abrir una cuenta para depositar dinero.")
    assert set(detected) == {"w_cuenta", "w_depositar"}


def test_detect_words_empty_transcript_returns_empty(db):
    user = _make_user(db)
    _make_situation(db)
    target_ids = _seed_words(db)
    conv = _make_conversation(db, user.id, target_word_ids=target_ids)

    assert detect_words(db, conv, "") == []
    assert detect_words(db, conv, None) == []


def test_detect_words_no_overlap_returns_empty(db):
    user = _make_user(db)
    _make_situation(db)
    target_ids = _seed_words(db)
    conv = _make_conversation(db, user.id, target_word_ids=target_ids)

    assert detect_words(db, conv, "Hello how are you today friend") == []


# ── persist_turn ──────────────────────────────────────────────────────────────


def test_persist_turn_appends_detected_words_and_increments_turn_count(db):
    user = _make_user(db)
    _make_situation(db)
    target_ids = _seed_words(db)
    conv = _make_conversation(db, user.id, target_word_ids=target_ids)

    _, detected = persist_turn(
        db=db,
        conversation=conv,
        user_id=user.id,
        user_transcript="quiero abrir una cuenta",
        assistant_text="claro, con gusto",
    )

    db.flush()
    assert detected == ["w_cuenta"]
    assert conv.used_spoken_word_ids == ["w_cuenta"]
    assert conv.turn_count == 1

    # user_words counter got incremented for the detected word.
    uw = db.query(UserWord).filter_by(user_id=user.id, word_id="w_cuenta").first()
    assert uw is not None
    assert uw.spoken_correct_count == 1


def test_persist_turn_increments_turn_count_even_when_no_words_detected(db):
    """The hard-limit safety net depends on turn_count counting empty turns,
    otherwise a user who never says a target word can chat forever."""
    user = _make_user(db)
    _make_situation(db)
    target_ids = _seed_words(db)
    conv = _make_conversation(db, user.id, target_word_ids=target_ids, turn_count=5)

    _, detected = persist_turn(
        db=db,
        conversation=conv,
        user_id=user.id,
        user_transcript="no relevant words here friend",
        assistant_text="ok",
    )

    assert detected == []
    assert conv.used_spoken_word_ids == []
    assert conv.turn_count == 6


def test_persist_turn_dedupes_already_detected_words(db):
    """Saying a word twice shouldn't duplicate it in used_spoken_word_ids."""
    user = _make_user(db)
    _make_situation(db)
    target_ids = _seed_words(db)
    conv = _make_conversation(
        db, user.id,
        target_word_ids=target_ids,
        used_spoken_word_ids=["w_cuenta"],
    )

    _, detected = persist_turn(
        db=db,
        conversation=conv,
        user_id=user.id,
        user_transcript="cuenta otra vez",
        assistant_text="",
    )

    assert "w_cuenta" in detected
    assert conv.used_spoken_word_ids.count("w_cuenta") == 1


# ── check_completion ──────────────────────────────────────────────────────────


def test_check_completion_all_target_words_used(db):
    user = _make_user(db)
    _make_situation(db)
    target_ids = _seed_words(db)
    conv = _make_conversation(
        db, user.id,
        target_word_ids=target_ids,
        used_spoken_word_ids=target_ids,
        turn_count=3,
    )

    complete, turns_remaining = check_completion(conv)
    assert complete is True
    assert turns_remaining == EXCHANGE_WARNING_THRESHOLD - 3


def test_check_completion_missing_words_not_complete(db):
    user = _make_user(db)
    _make_situation(db)
    target_ids = _seed_words(db)
    conv = _make_conversation(
        db, user.id,
        target_word_ids=target_ids,
        used_spoken_word_ids=[target_ids[0]],
        turn_count=2,
    )

    complete, turns_remaining = check_completion(conv)
    assert complete is False
    assert turns_remaining == EXCHANGE_WARNING_THRESHOLD - 2


def test_check_completion_hard_limit_fires_regardless_of_words(db):
    """Turn 30 is the safety net — even with zero target words spoken, the
    conversation must flip to complete so the FE closes the peer connection."""
    assert EXCHANGE_HARD_LIMIT == 30

    user = _make_user(db)
    _make_situation(db)
    target_ids = _seed_words(db)

    # Turn 29 = not complete yet
    conv_29 = _make_conversation(
        db, user.id,
        target_word_ids=target_ids,
        used_spoken_word_ids=[],
        turn_count=29,
    )
    complete, turns_remaining = check_completion(conv_29)
    assert complete is False
    assert turns_remaining == 0  # past threshold, pinned at 0

    # Turn 30 = complete
    conv_30 = _make_conversation(
        db, _make_user(db, email_suffix="b").id,
        target_word_ids=target_ids,
        used_spoken_word_ids=[],
        turn_count=30,
    )
    complete, _ = check_completion(conv_30)
    assert complete is True

    # Turn 31 = still complete (idempotent past the limit)
    conv_31 = _make_conversation(
        db, _make_user(db, email_suffix="c").id,
        target_word_ids=target_ids,
        used_spoken_word_ids=[],
        turn_count=31,
    )
    complete, _ = check_completion(conv_31)
    assert complete is True


def test_check_completion_empty_targets_is_not_complete(db):
    """Sanity: a conversation with no target_word_ids shouldn't auto-complete
    on the word rule (empty set is trivially a subset). Hard limit still
    applies, but at turn 0 we expect not-complete."""
    user = _make_user(db)
    _make_situation(db)
    conv = _make_conversation(
        db, user.id,
        target_word_ids=[],
        used_spoken_word_ids=[],
        turn_count=0,
    )
    complete, turns_remaining = check_completion(conv)
    assert complete is False
    assert turns_remaining == EXCHANGE_WARNING_THRESHOLD
