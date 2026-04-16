"""Unit tests for conversation_service.update_user_word_stats.

Covers the defensive FK-safety filter that prevents synthetic or bogus
word_ids from throwing ForeignKeyViolation on the user_words table.
"""
import uuid

import pytest

from app.auth import get_password_hash
from app.models import User, UserWord, Word
from app.services.conversation_service import update_user_word_stats


def _make_user(db):
    user = User(
        id=uuid.uuid4(),
        email=f"uws_{uuid.uuid4().hex[:8]}@test.com",
        password_hash=get_password_hash("testpass123"),
    )
    db.add(user)
    db.flush()
    return user


def _make_grammar_word(db, word_id: str, spanish: str = "testverb") -> Word:
    w = Word(
        id=word_id,
        spanish=spanish,
        english="to test",
        word_category="grammar",
    )
    db.add(w)
    db.flush()
    return w


def test_update_user_word_stats_known_id(db):
    """Baseline: known word_id is upserted normally."""
    user = _make_user(db)
    _make_grammar_word(db, "grammar_vivir", "vivir")

    update_user_word_stats(db, str(user.id), ["grammar_vivir"], "voice")

    row = db.query(UserWord).filter_by(user_id=user.id, word_id="grammar_vivir").first()
    assert row is not None
    assert row.spoken_correct_count == 1


def test_update_user_word_stats_unknown_id_is_skipped(db, caplog):
    """Unknown word_id does NOT raise — it's logged and silently skipped.

    This is the defensive layer protecting against FK violations from any
    caller (mark-word, voice-turn, future drill types) that might pass a
    synthetic id not seeded in the `words` table.
    """
    user = _make_user(db)

    with caplog.at_level("WARNING", logger="app.services.conversation_service"):
        # Should not raise despite no row for 'bogus_xyz' in words table
        update_user_word_stats(db, str(user.id), ["bogus_xyz"], "voice")

    # No user_words row should have been written
    rows = db.query(UserWord).filter_by(user_id=user.id).all()
    assert rows == []

    # The warning should mention the unknown id for observability
    assert any(
        "skipping unknown word_ids" in r.message and "bogus_xyz" in r.message
        for r in caplog.records
    ), f"Expected warning about unknown word_id, got: {[r.message for r in caplog.records]}"


def test_update_user_word_stats_mixed_known_and_unknown(db, caplog):
    """Known ids are still upserted when mixed with unknown ones."""
    user = _make_user(db)
    _make_grammar_word(db, "grammar_hablar", "hablar")

    with caplog.at_level("WARNING", logger="app.services.conversation_service"):
        update_user_word_stats(
            db, str(user.id),
            ["grammar_hablar", "conj_hablar_yo", "some_other_bogus"],
            "voice",
        )

    known_row = db.query(UserWord).filter_by(user_id=user.id, word_id="grammar_hablar").first()
    assert known_row is not None
    assert known_row.spoken_correct_count == 1

    assert db.query(UserWord).filter_by(word_id="conj_hablar_yo").first() is None
    assert db.query(UserWord).filter_by(word_id="some_other_bogus").first() is None


def test_update_user_word_stats_empty_list(db):
    """Empty word_ids list is a no-op; no errors."""
    user = _make_user(db)
    update_user_word_stats(db, str(user.id), [], "voice")
    assert db.query(UserWord).filter_by(user_id=user.id).all() == []


def test_update_user_word_stats_text_mode_also_filters(db):
    """Text mode (typed) also benefits from the defensive filter."""
    user = _make_user(db)
    _make_grammar_word(db, "grammar_comer", "comer")

    # Must not raise
    update_user_word_stats(
        db, str(user.id),
        ["grammar_comer", "conj_comer_yo"],
        "text",
    )

    row = db.query(UserWord).filter_by(user_id=user.id, word_id="grammar_comer").first()
    assert row is not None
    assert row.typed_correct_count == 1
    assert db.query(UserWord).filter_by(word_id="conj_comer_yo").first() is None
