"""Tests for daily grenade selection, recall, and 14-day strip."""
import uuid
from datetime import datetime, timedelta, timezone, date

from app.models import (
    DailyEncounterLog,
    DailyGrenade,
    Situation,
    User,
    UserWord,
    Word,
)
from app.services import grenade_service


def _make_user(db):
    from app.auth import get_password_hash
    u = User(
        id=uuid.uuid4(),
        email=f"gren_{uuid.uuid4().hex[:8]}@test.com",
        password_hash=get_password_hash("x" * 12),
    )
    db.add(u)
    db.flush()
    return u


def _seed_word(db, wid, spanish, word_type=None):
    w = Word(id=wid, spanish=spanish, english=spanish + "_en", word_type=word_type)
    db.add(w)
    db.flush()
    return w


def _learned_today(db, user, word, last_seen=None):
    uw = UserWord(
        user_id=user.id,
        word_id=word.id,
        mastery_level=1,
        status="learning",
        last_seen_form=last_seen,
    )
    db.add(uw)
    db.flush()
    return uw


def _seed_lesson_done(db, user):
    sit = Situation(
        id=f"gren_sit_{uuid.uuid4().hex[:6]}",
        title="t",
        animation_type="banking",
        encounter_number=1,
        order_index=9999,
        is_free=True,
    )
    db.add(sit)
    db.flush()
    db.add(DailyEncounterLog(user_id=user.id, situation_id=sit.id))
    db.flush()


def test_no_eligible_word_returns_none(db):
    user = _make_user(db)
    assert grenade_service.pick_or_get_todays_grenade(db, user.id) is None


def test_picks_verb_over_noun(db):
    user = _make_user(db)
    noun = _seed_word(db, f"n_{uuid.uuid4().hex[:6]}", "aguacate", word_type="noun")
    verb = _seed_word(db, f"v_{uuid.uuid4().hex[:6]}", "hacer", word_type="verb")
    _learned_today(db, user, noun)
    _learned_today(db, user, verb, last_seen="hará")
    g = grenade_service.pick_or_get_todays_grenade(db, user.id)
    assert g is not None
    assert g.word_id == verb.id
    assert g.surface_form == "hará"
    assert g.audience == "friend"


def test_noun_audience_is_merchant(db):
    user = _make_user(db)
    noun = _seed_word(db, f"n_{uuid.uuid4().hex[:6]}", "aguacate", word_type="noun")
    _learned_today(db, user, noun)
    g = grenade_service.pick_or_get_todays_grenade(db, user.id)
    assert g.audience == "merchant"
    assert g.surface_form == "aguacate"


def test_idempotent_same_day(db):
    user = _make_user(db)
    w = _seed_word(db, f"w_{uuid.uuid4().hex[:6]}", "café", word_type="noun")
    _learned_today(db, user, w)
    g1 = grenade_service.pick_or_get_todays_grenade(db, user.id)
    g2 = grenade_service.pick_or_get_todays_grenade(db, user.id)
    assert g1.id == g2.id


def test_record_recall(db):
    user = _make_user(db)
    w = _seed_word(db, f"w_{uuid.uuid4().hex[:6]}", "perro", word_type="noun")
    _learned_today(db, user, w)
    g = grenade_service.pick_or_get_todays_grenade(db, user.id)
    out = grenade_service.record_recall(db, user.id, g.id, used=True)
    assert out.used is True
    assert out.answered_at is not None


def test_recent_strip_fills_none_days(db):
    user = _make_user(db)
    today = date.today()
    # one used 3 days ago, one missed 1 day ago
    g1 = DailyGrenade(
        id=uuid.uuid4(), user_id=user.id, grenade_date=today - timedelta(days=3),
        user_word_id="x", word_id="x", surface_form="x", audience="friend", used=True,
    )
    g2 = DailyGrenade(
        id=uuid.uuid4(), user_id=user.id, grenade_date=today - timedelta(days=1),
        user_word_id="x", word_id="x", surface_form="x", audience="friend", used=False,
    )
    # need a real Word for the FK; insert one
    _seed_word(db, "x", "x", word_type="noun")
    db.add_all([g1, g2])
    db.flush()
    strip = grenade_service.get_recent_grenades(db, user.id, days=14)
    assert len(strip) == 14
    statuses = [s["status"] for s in strip]
    assert statuses.count("used") == 1
    assert statuses.count("missed") == 1
    assert statuses.count("none") == 12


def test_first_lesson_done_today(db):
    user = _make_user(db)
    assert grenade_service.first_lesson_done_today(db, user.id) is False
    _seed_lesson_done(db, user)
    assert grenade_service.first_lesson_done_today(db, user.id) is True


def test_prior_unanswered(db):
    user = _make_user(db)
    _seed_word(db, "y", "y", word_type="noun")
    yesterday = date.today() - timedelta(days=1)
    g = DailyGrenade(
        id=uuid.uuid4(), user_id=user.id, grenade_date=yesterday,
        user_word_id="y", word_id="y", surface_form="y", audience="friend",
        sentence_es="¿Quieres y?", sentence_en="Want y?",
    )
    db.add(g)
    db.flush()
    out = grenade_service.get_prior_unanswered(db, user.id)
    assert out is not None
    assert out.id == g.id
