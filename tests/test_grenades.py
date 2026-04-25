"""Tests for the daily Grenade flow."""
import uuid
from datetime import datetime, timedelta, timezone

import pytest

from app.models import Grenade, Situation, SituationWord, User, UserWord, Word
from app.services import grenade_service
from app.services.refresh_service import set_initial_mastery


def _make_user(db):
    from app.auth import get_password_hash

    user = User(
        id=uuid.uuid4(),
        email=f"grenade_{uuid.uuid4().hex[:8]}@test.com",
        password_hash=get_password_hash("testpass123"),
    )
    db.add(user)
    db.flush()
    return user


def _make_word(db, word_id, spanish, word_type=None, category="high_frequency"):
    w = Word(
        id=word_id,
        spanish=spanish,
        english=spanish,
        word_category=category,
        word_type=word_type,
    )
    db.add(w)
    db.flush()
    return w


def _make_user_word(db, user, word, mastery_level=1, last_seen_form=None, updated_at=None):
    uw = UserWord(
        user_id=user.id,
        word_id=word.id,
        mastery_level=mastery_level,
        status="learning",
        last_seen_form=last_seen_form,
    )
    db.add(uw)
    db.flush()
    if updated_at is not None:
        uw.updated_at = updated_at
        db.flush()
    return uw


# ── Selection ────────────────────────────────────────────────────────────────


def test_no_grenade_when_no_words_learned_today(db):
    user = _make_user(db)
    result = grenade_service.get_or_pick_today(db, user.id)
    assert result is None


def test_picks_word_learned_today(db):
    user = _make_user(db)
    word = _make_word(db, f"gw_{uuid.uuid4().hex[:6]}", "aguacate")
    _make_user_word(db, user, word, mastery_level=1)

    grenade = grenade_service.get_or_pick_today(db, user.id)
    assert grenade is not None
    assert grenade.word_id == word.id
    assert grenade.target_form == "aguacate"
    assert grenade.assigned_date == datetime.now(timezone.utc).date()
    assert grenade.question_es is None  # not yet generated


def test_prefers_verb_when_available(db):
    user = _make_user(db)
    noun = _make_word(db, f"gn_{uuid.uuid4().hex[:6]}", "casa", word_type="noun")
    verb = _make_word(db, f"gv_{uuid.uuid4().hex[:6]}", "hablar", word_type="verb")
    _make_user_word(db, user, noun, last_seen_form="casa")
    _make_user_word(db, user, verb, last_seen_form="hablas")

    grenade = grenade_service.get_or_pick_today(db, user.id)
    assert grenade.word_id == verb.id
    assert grenade.target_form == "hablas"
    assert grenade.pos == "verb"


def test_skips_words_learned_yesterday(db):
    user = _make_user(db)
    word = _make_word(db, f"go_{uuid.uuid4().hex[:6]}", "viejo")
    yesterday = datetime.now(timezone.utc) - timedelta(days=1, hours=2)
    _make_user_word(db, user, word, mastery_level=1, updated_at=yesterday)

    grenade = grenade_service.get_or_pick_today(db, user.id)
    assert grenade is None


def test_idempotent_on_same_day(db):
    user = _make_user(db)
    word = _make_word(db, f"gi_{uuid.uuid4().hex[:6]}", "manzana")
    _make_user_word(db, user, word)

    g1 = grenade_service.get_or_pick_today(db, user.id)
    g2 = grenade_service.get_or_pick_today(db, user.id)
    assert g1.id == g2.id


# ── Recall ────────────────────────────────────────────────────────────────────


def test_pending_recall_only_for_crafted_prior_grenades(db):
    user = _make_user(db)
    word = _make_word(db, f"gr_{uuid.uuid4().hex[:6]}", "ayer")

    # A prior-day grenade with no question crafted should NOT surface as pending.
    not_crafted = Grenade(
        id=uuid.uuid4(),
        user_id=user.id,
        word_id=word.id,
        target_form="ayer",
        assigned_date=(datetime.now(timezone.utc) - timedelta(days=1)).date(),
    )
    db.add(not_crafted)
    db.flush()

    pending = grenade_service.find_pending_recall(db, user.id)
    assert pending is None

    # Once crafted, it surfaces.
    not_crafted.question_es = "¿Sabes qué hicimos ayer?"
    not_crafted.question_en = "Do you know what we did yesterday?"
    not_crafted.audience = "friend"
    db.flush()

    pending = grenade_service.find_pending_recall(db, user.id)
    assert pending is not None
    assert pending.id == not_crafted.id


def test_record_recall_marks_used(db):
    user = _make_user(db)
    word = _make_word(db, f"gu_{uuid.uuid4().hex[:6]}", "leche")
    grenade = Grenade(
        id=uuid.uuid4(),
        user_id=user.id,
        word_id=word.id,
        target_form="leche",
        assigned_date=(datetime.now(timezone.utc) - timedelta(days=1)).date(),
        question_es="¿Tienen leche?",
        question_en="Do you have milk?",
        audience="merchant",
    )
    db.add(grenade)
    db.flush()

    grenade_service.record_recall(db, user.id, grenade.id, used=True)
    refreshed = db.query(Grenade).filter(Grenade.id == grenade.id).one()
    assert refreshed.used is True
    assert refreshed.answered_at is not None


# ── Strip ────────────────────────────────────────────────────────────────────


def test_strip_has_14_days(db):
    user = _make_user(db)
    cells = grenade_service.build_strip(db, user.id)
    assert len(cells) == 14
    assert all(c.state == "none" for c in cells)


def test_strip_reflects_used_missed_pending(db):
    user = _make_user(db)
    word = _make_word(db, f"gs_{uuid.uuid4().hex[:6]}", "café")
    today = datetime.now(timezone.utc).date()

    # 3 days ago: deployed
    db.add(Grenade(
        id=uuid.uuid4(), user_id=user.id, word_id=word.id, target_form="café",
        assigned_date=today - timedelta(days=3), used=True,
        question_es="q", question_en="q", audience="friend",
    ))
    # 2 days ago: missed
    db.add(Grenade(
        id=uuid.uuid4(), user_id=user.id, word_id=word.id, target_form="café",
        assigned_date=today - timedelta(days=2), used=False,
        question_es="q", question_en="q", audience="friend",
    ))
    # today: crafted but unanswered
    db.add(Grenade(
        id=uuid.uuid4(), user_id=user.id, word_id=word.id, target_form="café",
        assigned_date=today, used=None,
        question_es="q", question_en="q", audience="friend",
    ))
    db.flush()

    cells = grenade_service.build_strip(db, user.id)
    states = {c.date: c.state for c in cells}
    assert states[(today - timedelta(days=3)).isoformat()] == "used"
    assert states[(today - timedelta(days=2)).isoformat()] == "missed"
    assert states[today.isoformat()] == "pending"
    # Other days remain 'none'
    assert states[(today - timedelta(days=5)).isoformat()] == "none"


# ── last_seen_form integration ────────────────────────────────────────────────


def test_set_initial_mastery_seeds_lemma_for_non_verbs(db):
    user = _make_user(db)
    sit = Situation(
        id=f"sit_{uuid.uuid4().hex[:6]}",
        title="Test",
        animation_type="banking",
        encounter_number=1,
        order_index=999,
    )
    db.add(sit)
    word = _make_word(db, f"gx_{uuid.uuid4().hex[:6]}", "panadería", word_type="noun", category="encounter")
    db.add(SituationWord(situation_id=sit.id, word_id=word.id, position=1))
    db.add(UserWord(user_id=user.id, word_id=word.id, mastery_level=0, status="learning"))
    db.flush()

    set_initial_mastery(db, user.id, [word.id], sit.id)
    db.flush()

    uw = db.query(UserWord).filter(UserWord.user_id == user.id, UserWord.word_id == word.id).one()
    assert uw.mastery_level == 1
    assert uw.last_seen_form == "panadería"
