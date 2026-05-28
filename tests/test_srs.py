"""Unified SRS engine (`app/services/srs.py`) — the single Leitner system shared
by the vocab and Tense Quest review decks. These are pure-function tests; the
deck endpoints that ride on the engine are covered in test_vocab.py /
test_tense_quest.py."""
from datetime import datetime, timedelta, timezone

from app.services import srs

# Fixed clock so due_at assertions are exact (no wall-clock flake).
NOW = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)


class _FakeCard:
    """A verb-deck-shaped card: carries the optional bookkeeping fields so we can
    assert the engine updates them when present."""
    def __init__(self, box=1, deck_position=0, due_at=None):
        self.box = box
        self.reps = 0
        self.lapses = 0
        self.last_result = None
        self.last_response_ms = None
        self.deck_position = deck_position
        self.due_at = due_at


class _MinimalCard:
    """A vocab-deck-shaped card: only box + due_at, no reps/lapses/last_result."""
    def __init__(self, box=1):
        self.box = box
        self.due_at = None


# ── classify ──────────────────────────────────────────────────────────────────

def test_classify_grades_by_speed_and_correctness():
    assert srs.classify(True, 1_000) == "great"                 # < FAST_MS
    assert srs.classify(True, srs.FAST_MS) == "great"           # exactly the fast bar
    assert srs.classify(True, srs.FAST_MS + 1) == "good"        # just over → medium
    assert srs.classify(True, 8_000) == "good"
    assert srs.classify(False, 1_000) == "lapse"                # wrong however fast
    assert srs.classify(True, srs.SLOW_MS_TYPED + 1) == "lapse"  # correct but too slow


def test_classify_slow_ceiling_is_mode_aware():
    # 12s is under the typed ceiling (15s) = good, but over the spoken one (10s) = lapse.
    assert srs.classify(True, 12_000, "type") == "good"
    assert srs.classify(True, 12_000, "speak") == "lapse"
    # An unrecognised mode falls back to the conservative (longer) typed ceiling.
    assert srs.classify(True, 12_000, "mystery") == "good"


def test_classify_missing_or_zero_timing_is_good():
    # A missing measurement must never be punished as a lapse nor rewarded as great.
    assert srs.classify(True, None) == "good"
    assert srs.classify(True, 0) == "good"
    assert srs.classify(False, None) == "lapse"


# ── ladder / interval_for ───────────────────────────────────────────────────────

def test_ladder_is_monotonic_and_clamps_out_of_range():
    hrs = srs.BOX_INTERVAL_HOURS
    assert hrs == sorted(hrs)                       # never schedules a higher box sooner
    assert srs.MAX_BOX == len(hrs)
    assert srs.interval_for(1) == timedelta(hours=4)
    assert srs.interval_for(srs.MAX_BOX) == timedelta(hours=hrs[-1])  # 60d at the top
    assert srs.interval_for(0) == srs.interval_for(1)                 # clamp low
    assert srs.interval_for(99) == srs.interval_for(srs.MAX_BOX)      # clamp high


# ── apply_review ────────────────────────────────────────────────────────────────

def test_great_double_bumps_and_schedules_by_new_box():
    c = _FakeCard(box=1)
    assert srs.apply_review(c, correct=True, response_ms=1_000, now=NOW) == "great"
    assert c.box == 3
    assert c.due_at == NOW + srs.interval_for(3)
    assert c.reps == 1 and c.last_result == "great" and c.last_response_ms == 1_000


def test_good_single_bumps():
    c = _FakeCard(box=2)
    assert srs.apply_review(c, correct=True, response_ms=8_000, now=NOW) == "good"
    assert c.box == 3
    assert c.due_at == NOW + srs.interval_for(3)


def test_bumps_cap_at_max_box():
    c = _FakeCard(box=srs.MAX_BOX)
    srs.apply_review(c, correct=True, response_ms=1_000, now=NOW)   # great (+2) can't overshoot
    assert c.box == srs.MAX_BOX
    c2 = _FakeCard(box=srs.MAX_BOX - 1)
    srs.apply_review(c2, correct=True, response_ms=1_000, now=NOW)  # +2 would pass the cap
    assert c2.box == srs.MAX_BOX


def test_lapse_demotes_by_two_not_to_one():
    c = _FakeCard(box=5)
    assert srs.apply_review(c, correct=False, response_ms=1_000, now=NOW) == "lapse"
    assert c.box == 3                               # 5 - LAPSE_DROP, not reset to 1
    assert c.lapses == 1
    assert c.due_at == NOW + timedelta(minutes=srs.LAPSE_MINUTES)


def test_lapse_floors_at_min_box():
    for start in (1, 2):
        c = _FakeCard(box=start)
        srs.apply_review(c, correct=False, response_ms=1_000, now=NOW)
        assert c.box == srs.MIN_BOX                 # max(1, start - 2)


def test_correct_but_slow_is_a_silent_lapse():
    c = _FakeCard(box=4)
    assert srs.apply_review(c, correct=True, response_ms=srs.SLOW_MS_TYPED + 1, now=NOW) == "lapse"
    assert c.box == 2
    assert c.lapses == 1


def test_engine_runs_on_a_card_without_bookkeeping_fields():
    # VocabCard exposes box + due_at but no reps/lapses/last_result; the engine
    # must skip attributes that aren't there rather than raise.
    c = _MinimalCard(box=3)
    assert srs.apply_review(c, correct=True, response_ms=1_000, now=NOW) == "great"
    assert c.box == 5
    assert c.due_at == NOW + srs.interval_for(5)


def test_full_climb_box1_to_top_then_holds():
    # Medium-correct every time → one rung per review, walking the whole ladder
    # and then sitting at the cap (60d spacing).
    c = _MinimalCard(box=1)
    seen = []
    for _ in range(srs.MAX_BOX + 2):
        srs.apply_review(c, correct=True, response_ms=8_000, now=NOW)
        seen.append(c.box)
    assert seen == [2, 3, 4, 5, 6, 7, 7, 7, 7]
    assert c.due_at == NOW + srs.interval_for(srs.MAX_BOX)


# ── coins ──────────────────────────────────────────────────────────────────────

def test_coins_for_result():
    assert srs.coins_for_result("great") == 2
    assert srs.coins_for_result("good") == 1
    assert srs.coins_for_result("lapse") == 0
    assert srs.coins_for_result("???") == 0


# ── order_cards ──────────────────────────────────────────────────────────────────

def test_order_cards_puts_due_first():
    now = datetime.now(timezone.utc)
    overdue = _FakeCard(box=1, deck_position=9, due_at=now - timedelta(hours=2))
    not_due = _FakeCard(box=5, deck_position=0, due_at=now + timedelta(days=3))
    due_now = _FakeCard(box=2, deck_position=5, due_at=now - timedelta(seconds=1))
    ordered = srs.order_cards([not_due, overdue, due_now], now=now)
    assert ordered[-1] is not_due                   # the only non-due card sorts last
    assert set(ordered[:2]) == {overdue, due_now}


def test_order_cards_treats_naive_due_at_as_utc():
    now = datetime.now(timezone.utc)
    naive_overdue = _FakeCard(box=1, due_at=datetime(2020, 1, 1))  # tz-naive
    future = _FakeCard(box=1, deck_position=1, due_at=now + timedelta(days=1))
    ordered = srs.order_cards([future, naive_overdue], now=now)
    assert ordered[0] is naive_overdue              # naive timestamp didn't crash the sort
