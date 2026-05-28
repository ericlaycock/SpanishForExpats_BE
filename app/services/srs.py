"""Unified spaced-repetition engine — one Leitner system shared by every review
deck (Tense Quest verb cards + the main vocab deck).

There used to be two near-identical SRS implementations that drifted apart (the
vocab box CHECK constraint once lagged a ladder change and box-6 promotions
started throwing IntegrityErrors). This module is the single source of truth for
the box ladder and the per-review transition. Deck-specific concerns stay in the
callers: the vocab module→main promotion tier, the coin economy, deck ordering
for presentation, and which `response_mode` a card uses.

One ladder, indexed by box-1 (boxes are 1..MAX_BOX):

    box  1     2     3     4      5      6      7
    due  4h    1d    3d    1w     16d    35d    60d

Transition rules (`apply_review`), mode-aware on the slow ceiling:
  * correct & ≤ FAST_MS              → "great", box += 2 (cap MAX_BOX)
  * correct & ≤ slow ceiling         → "good",  box += 1 (cap MAX_BOX)
  * wrong, or correct but too slow   → "lapse", box -= LAPSE_DROP (floor 1),
                                       requeue in LAPSE_MINUTES
A lapse costs a couple of rungs of spacing, not all of it: a mature box-7 card
falls to box 5, not back to square one. A correct answer with no timing info
counts as "good" — a missing measurement is never punished as a lapse.

The slow ceiling is tighter for spoken answers (speaking is faster than typing,
so a slow spoken answer signals weaker recall). Keep SLOW_MS_* in sync with the
FE verdict constants in `components/tensequest/ReviewSession.tsx`.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Optional

# One ladder for every deck. Index 0 == box 1, in hours.
# 4h, 1d, 3d, 1w, 16d, 35d, 60d — tops out at ~2 months for a card nailed every time.
BOX_INTERVAL_HOURS = [4, 24, 72, 168, 384, 840, 1440]
MIN_BOX = 1
MAX_BOX = len(BOX_INTERVAL_HOURS)  # 7
# A lapse demotes by this many boxes (floored at MIN_BOX) instead of resetting
# to box 1, so one slip doesn't wipe out a card's whole spacing history.
LAPSE_DROP = 2
LAPSE_MINUTES = 10  # how soon a lapsed card re-enters the "due" pool

FAST_MS = 5_000
SLOW_MS_TYPED = 15_000
SLOW_MS_SPOKEN = 10_000

# Coins awarded per outcome — decks that pay review coins use this mapping.
COINS_FOR_RESULT = {"great": 2, "good": 1, "lapse": 0}


def coins_for_result(result: str) -> int:
    return COINS_FOR_RESULT.get(result, 0)


def _now(now: Optional[datetime]) -> datetime:
    return now or datetime.now(timezone.utc)


def _slow_ceiling(response_mode: str) -> int:
    return SLOW_MS_SPOKEN if response_mode == "speak" else SLOW_MS_TYPED


def classify(correct: bool, response_ms: Optional[int], response_mode: str = "type") -> str:
    """Grade one attempt → 'great' | 'good' | 'lapse'.

    `response_mode` is 'type' or 'speak'; anything else falls back to the longer
    typed ceiling (conservative for un-classifiable cards). A correct-but-slow
    answer is a silent lapse — recall was too weak even though the spelling
    matched. Missing/zero timing is treated as 'good', never 'great' or 'lapse'.
    """
    if not correct or (response_ms is not None and response_ms > _slow_ceiling(response_mode)):
        return "lapse"
    if response_ms is not None and 0 < response_ms <= FAST_MS:
        return "great"
    return "good"


def interval_for(box: int) -> timedelta:
    """How long until a card in `box` is next due."""
    box = max(MIN_BOX, min(MAX_BOX, box))
    return timedelta(hours=BOX_INTERVAL_HOURS[box - 1])


def apply_review(
    card,
    correct: bool,
    response_ms: Optional[int],
    response_mode: str = "type",
    now: Optional[datetime] = None,
) -> str:
    """Mutate `card.box` and `card.due_at` for one review outcome; return the
    grade ('great' | 'good' | 'lapse').

    `card` is any object exposing `box` and `due_at` (both deck models do). Extra
    bookkeeping fields are updated only when the card carries them, so the same
    engine serves the verb deck (reps/lapses/last_result) and the vocab deck
    (which tracks neither): `reps`, `last_result`, `last_response_ms` are set when
    present, and `lapses` is incremented on a lapse when present.
    """
    now = _now(now)
    result = classify(correct, response_ms, response_mode)
    box = card.box or MIN_BOX

    if result == "lapse":
        card.box = max(MIN_BOX, box - LAPSE_DROP)
        card.due_at = now + timedelta(minutes=LAPSE_MINUTES)
        if hasattr(card, "lapses"):
            card.lapses = (card.lapses or 0) + 1
    else:
        card.box = min(MAX_BOX, box + (2 if result == "great" else 1))
        card.due_at = now + interval_for(card.box)

    if hasattr(card, "reps"):
        card.reps = (card.reps or 0) + 1
    if hasattr(card, "last_result"):
        card.last_result = result
    if hasattr(card, "last_response_ms"):
        card.last_response_ms = response_ms
    return result


def order_cards(cards: list, now: Optional[datetime] = None) -> list:
    """Deck order: due cards first (overdue / due now), then the rest. Within
    each bucket, by deck_position then box. Newly-lapsed cards (due ~10 min out)
    drop back into the 'due' bucket quickly, which is how "surface the ones you
    got wrong more often" falls out. Cards without a deck_position sort at 0."""
    now = _now(now)

    def sort_key(c):
        due = c.due_at
        if due is not None and due.tzinfo is None:
            due = due.replace(tzinfo=timezone.utc)
        is_due = due is None or due <= now
        return (0 if is_due else 1, getattr(c, "deck_position", 0) or 0, c.box or 1, due or now)

    return sorted(cards, key=sort_key)
