"""Tests for the Spaced Repetition System (SRS) refresh flow."""
import uuid
from datetime import datetime, timedelta, timezone

from app.models import User, UserWord, Conversation, Situation, Word, SituationWord, UserSituation
from app.services.refresh_service import (
    get_next_refresh_at,
    set_initial_mastery,
    get_pending_refreshes,
    get_due_word_ids,
    bump_mastery_after_refresh,
    SRS_INTERVALS,
)
from app.api.v1.situations import get_vocab_level
from tests.conftest import register_user


def _make_user(db):
    """Create a test user directly in the DB."""
    from app.auth import get_password_hash
    user = User(
        id=uuid.uuid4(),
        email=f"srs_{uuid.uuid4().hex[:8]}@test.com",
        password_hash=get_password_hash("testpass123"),
    )
    db.add(user)
    db.flush()
    return user


def _seed_situation_and_words(db):
    """Create a situation with 3 encounter words + 2 HF words."""
    sit = Situation(
        id=f"srs_sit_{uuid.uuid4().hex[:6]}",
        title="SRS Test Situation",
        animation_type="banking",
        encounter_number=1,
        order_index=9999,
        is_free=True,
    )
    db.add(sit)

    words = []
    for i in range(3):
        w = Word(id=f"srs_enc_{uuid.uuid4().hex[:6]}_{i}", spanish=f"palabra{i}", english=f"word{i}", word_category="encounter")
        db.add(w)
        db.add(SituationWord(situation_id=sit.id, word_id=w.id, position=i + 1))
        words.append(w)
    hf_words = []
    for i in range(2):
        w = Word(id=f"srs_hf_{uuid.uuid4().hex[:6]}_{i}", spanish=f"freq{i}", english=f"freq_en{i}", word_category="high_frequency", frequency_rank=100 + i)
        db.add(w)
        hf_words.append(w)

    db.flush()
    return sit, words, hf_words


def _create_user_words(db, user, words, mastery_level=0, next_refresh_at=None, source_situation_id=None):
    """Create UserWord entries at a given mastery level."""
    for w in words:
        uw = UserWord(
            user_id=user.id,
            word_id=w.id,
            mastery_level=mastery_level,
            status="learning" if mastery_level < 4 else "mastered",
            next_refresh_at=next_refresh_at,
            source_situation_id=source_situation_id,
        )
        db.add(uw)
    db.flush()


# --- Unit tests for refresh_service ---

def test_get_next_refresh_at_levels():
    """SRS intervals: level 1→24h, 2→7d, 3→30d, 4→None."""
    before = datetime.now(timezone.utc)
    assert get_next_refresh_at(1) is not None
    assert get_next_refresh_at(2) is not None
    assert get_next_refresh_at(3) is not None
    assert get_next_refresh_at(4) is None
    assert get_next_refresh_at(0) is None

    r1 = get_next_refresh_at(1)
    assert r1 - before >= timedelta(hours=23, minutes=59)

    r2 = get_next_refresh_at(2)
    assert r2 - before >= timedelta(days=6, hours=23)

    r3 = get_next_refresh_at(3)
    assert r3 - before >= timedelta(days=29, hours=23)


def test_pending_empty_for_new_user(db):
    """A new user with no words should have no pending refreshes."""
    user = _make_user(db)
    result = get_pending_refreshes(db, user.id)
    assert result == []


def test_complete_situation_sets_mastery_level_1(db):
    """set_initial_mastery should move words from level 0 → 1 and set next_refresh_at."""
    user = _make_user(db)
    sit, words, hf_words = _seed_situation_and_words(db)
    all_words = words + hf_words
    _create_user_words(db, user, all_words, mastery_level=0)

    word_ids = [w.id for w in all_words]
    set_initial_mastery(db, user.id, word_ids, sit.id)

    for w in all_words:
        uw = db.query(UserWord).filter(UserWord.user_id == user.id, UserWord.word_id == w.id).one()
        assert uw.mastery_level == 1
        assert uw.next_refresh_at is not None
        assert uw.source_situation_id == sit.id


def test_set_initial_mastery_skips_nonzero(db):
    """set_initial_mastery should not touch words already at level >= 1."""
    user = _make_user(db)
    sit, words, _ = _seed_situation_and_words(db)
    _create_user_words(db, user, words, mastery_level=2, source_situation_id=sit.id)

    word_ids = [w.id for w in words]
    set_initial_mastery(db, user.id, word_ids, sit.id)

    for w in words:
        uw = db.query(UserWord).filter(UserWord.user_id == user.id, UserWord.word_id == w.id).one()
        assert uw.mastery_level == 2  # unchanged


def test_pending_after_24h(db):
    """Words at level 1 with next_refresh_at in the past should appear as pending."""
    user = _make_user(db)
    sit, words, _ = _seed_situation_and_words(db)
    past = datetime.now(timezone.utc) - timedelta(hours=25)
    _create_user_words(db, user, words, mastery_level=1, next_refresh_at=past, source_situation_id=sit.id)

    result = get_pending_refreshes(db, user.id)
    assert len(result) == 1
    assert result[0]["situation_id"] == sit.id
    assert result[0]["due_word_count"] == len(words)


def test_pending_not_due_yet(db):
    """Words with next_refresh_at in the future should NOT appear as pending."""
    user = _make_user(db)
    sit, words, _ = _seed_situation_and_words(db)
    future = datetime.now(timezone.utc) + timedelta(hours=12)
    _create_user_words(db, user, words, mastery_level=1, next_refresh_at=future, source_situation_id=sit.id)

    result = get_pending_refreshes(db, user.id)
    assert result == []


def test_start_refresh_creates_conversation(db):
    """get_due_word_ids should return the right word IDs."""
    user = _make_user(db)
    sit, words, _ = _seed_situation_and_words(db)
    past = datetime.now(timezone.utc) - timedelta(hours=25)
    _create_user_words(db, user, words, mastery_level=1, next_refresh_at=past, source_situation_id=sit.id)

    due_ids = get_due_word_ids(db, user.id, sit.id)
    assert set(due_ids) == {w.id for w in words}


def test_complete_refresh_bumps_to_level_2(db):
    """bump_mastery_after_refresh should move level 1 → 2."""
    user = _make_user(db)
    sit, words, _ = _seed_situation_and_words(db)
    past = datetime.now(timezone.utc) - timedelta(hours=25)
    _create_user_words(db, user, words, mastery_level=1, next_refresh_at=past, source_situation_id=sit.id)

    count, new_level = bump_mastery_after_refresh(db, user.id, sit.id)
    assert count == len(words)
    assert new_level == 2

    for w in words:
        uw = db.query(UserWord).filter(UserWord.user_id == user.id, UserWord.word_id == w.id).one()
        assert uw.mastery_level == 2
        assert uw.next_refresh_at is not None
        assert uw.status == "learning"


def test_full_srs_cycle_to_mastered(db):
    """Walk a word through the full SRS cycle: 1 → 2 → 3 → 4."""
    user = _make_user(db)
    sit, words, _ = _seed_situation_and_words(db)

    # Start at level 1, due now
    past = datetime.now(timezone.utc) - timedelta(hours=1)
    _create_user_words(db, user, words, mastery_level=1, next_refresh_at=past, source_situation_id=sit.id)

    # Refresh 1: 1 → 2
    count, lvl = bump_mastery_after_refresh(db, user.id, sit.id)
    assert lvl == 2
    for w in words:
        uw = db.query(UserWord).filter(UserWord.user_id == user.id, UserWord.word_id == w.id).one()
        assert uw.mastery_level == 2
        assert uw.next_refresh_at is not None
        # Simulate time passing
        uw.next_refresh_at = past
    db.flush()

    # Refresh 2: 2 → 3
    count, lvl = bump_mastery_after_refresh(db, user.id, sit.id)
    assert lvl == 3
    for w in words:
        uw = db.query(UserWord).filter(UserWord.user_id == user.id, UserWord.word_id == w.id).one()
        assert uw.mastery_level == 3
        assert uw.next_refresh_at is not None
        uw.next_refresh_at = past
    db.flush()

    # Refresh 3: 3 → 4 (mastered)
    count, lvl = bump_mastery_after_refresh(db, user.id, sit.id)
    assert lvl == 4
    for w in words:
        uw = db.query(UserWord).filter(UserWord.user_id == user.id, UserWord.word_id == w.id).one()
        assert uw.mastery_level == 4
        assert uw.next_refresh_at is None
        assert uw.status == "mastered"


def test_vocab_level_counts_from_mastery_1(db):
    """Vocab level should count HF words at mastery_level >= 1 (learned once)."""
    user = _make_user(db)
    sit, _, hf_words = _seed_situation_and_words(db)

    # At level 0 — should NOT count
    _create_user_words(db, user, hf_words, mastery_level=0, source_situation_id=sit.id)
    assert get_vocab_level(db, user.id) == 0

    # Bump to level 1 — should NOW count
    for w in hf_words:
        uw = db.query(UserWord).filter(UserWord.user_id == user.id, UserWord.word_id == w.id).one()
        uw.mastery_level = 1
    db.flush()
    assert get_vocab_level(db, user.id) == len(hf_words)
