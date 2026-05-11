"""Tense Quest spaced-repetition transitions.

Simple Leitner-style schedule (boxes 1..5). Inputs from the FE per review:
`correct` (did the spelling match) and `response_ms` (time the player took).

Rules baked into `apply_review`:
  * wrong  → lapse: box back to 1, surfaces again soon (~10 min).
  * correct but slow (> SLOW_MS) → still a *lapse* — the player isn't shown this
    fail state (the FE shows the green "correct!"), but internally the card is
    treated as not-known so it keeps surfacing.
  * correct and quick → box up by 1 ('good').
  * correct and very quick (≤ FAST_MS) → box up by 2 ('great').

`due_at` for non-lapses follows BOX_INTERVAL_HOURS; a fresh lapse comes back in
LAPSE_MINUTES so it re-enters the "due" pool within the same session.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Optional

FAST_MS = 5_000
SLOW_MS = 10_000
LAPSE_MINUTES = 10
MAX_BOX = 5

# Roughly: 4h, 1d, 3d, 1w, 16d.
BOX_INTERVAL_HOURS = {1: 4, 2: 24, 3: 72, 4: 168, 5: 384}


def _now(now: Optional[datetime]) -> datetime:
    return now or datetime.now(timezone.utc)


def apply_review(card, correct: bool, response_ms: Optional[int], now: Optional[datetime] = None) -> str:
    """Mutate `card` (a TenseQuestCard) for one review outcome. Returns the
    result label: 'great' | 'good' | 'lapse'."""
    now = _now(now)
    too_slow = response_ms is not None and response_ms > SLOW_MS
    very_fast = response_ms is not None and response_ms <= FAST_MS

    if not correct or too_slow:
        card.box = 1
        card.lapses = (card.lapses or 0) + 1
        result = "lapse"
    elif very_fast:
        card.box = min(MAX_BOX, (card.box or 1) + 2)
        result = "great"
    else:
        card.box = min(MAX_BOX, (card.box or 1) + 1)
        result = "good"

    card.reps = (card.reps or 0) + 1
    card.last_result = result
    card.last_response_ms = response_ms

    if result == "lapse":
        card.due_at = now + timedelta(minutes=LAPSE_MINUTES)
    else:
        card.due_at = now + timedelta(hours=BOX_INTERVAL_HOURS.get(card.box, 24))
    return result


def order_cards(cards: list, now: Optional[datetime] = None) -> list:
    """Deck order: due cards first (overdue / due now), then the rest. Within
    each bucket, by deck_position then box. Newly-lapsed cards (due ~10 min out,
    box 1) drop into the 'due' bucket again quickly, which is how the SRS
    'surface the ones you got wrong more often' behaviour falls out."""
    now = _now(now)

    def sort_key(c):
        due = c.due_at
        if due is not None and due.tzinfo is None:
            due = due.replace(tzinfo=timezone.utc)
        is_due = due is None or due <= now
        return (0 if is_due else 1, c.deck_position or 0, c.box or 1, due or now)

    return sorted(cards, key=sort_key)
