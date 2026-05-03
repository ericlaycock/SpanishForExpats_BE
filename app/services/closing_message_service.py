"""Pick a canned closing for an encounter that's just been completed.

Bypasses the v3 LLM prompt on the wrap-up turn so the avatar doesn't
generate a new question on top of an already-completed lesson. Without
the bypass the TURN-CLOSING RULE forces a `?`, leaving the student
with nothing useful to say after they ticked the last chip.

Selection is deterministic per `(situation_id, completed_chip_count)`
so the FE can replay the same conversation (e.g. retry on transient
audio failure) and get the same closing line — flapping is jarring
when the user already heard one variant. Across separate encounters
the variant rotates naturally because `situation_id` differs.
"""
from __future__ import annotations

import zlib
from typing import Optional

from app.data.closing_messages import CLOSING_BANKS, GENERIC_CLOSING_ES


def _resolve_bank(animation_type: str, alt_language: Optional[str]) -> list[str]:
    """Return the per-language bank for `animation_type`, falling back
    to Spanish then to `GENERIC_CLOSING_ES` if the entry is missing.

    `alt_language=None` and `alt_language="spanish"` both resolve to
    the Spanish bank — the BE elsewhere uses None for the default
    Spanish path, but accepting "spanish" too keeps callers honest.
    """
    lang_key = (alt_language or "es").lower()
    if lang_key in ("spanish", "es"):
        lang_key = "es"
    bank_for_lang = CLOSING_BANKS.get(lang_key)
    # Unknown alt_language → fall back to Spanish.
    if bank_for_lang is None:
        bank_for_lang = CLOSING_BANKS["es"]
    bank = bank_for_lang.get(animation_type)
    if bank:
        return bank
    # Some langs only cover the canonical animation_types — fall back
    # to Spanish for that anim_type before hitting the generic bag.
    bank = CLOSING_BANKS["es"].get(animation_type)
    return bank or GENERIC_CLOSING_ES


def pick_closing_message(
    animation_type: str,
    alt_language: Optional[str] = None,
    seed_key: Optional[str] = None,
) -> str:
    """Return a closing line for the given scene.

    `seed_key` is hashed into the variant index. Pass the
    `situation_id` (or any stable string) to keep the choice stable
    across replays of the same encounter; pass `None` to get the
    first variant deterministically (used by tests).

    Always returns a non-empty string — the underlying bank is
    audited at import time by `tests/test_closing_messages.py`.
    """
    bank = _resolve_bank(animation_type, alt_language)
    if not bank:
        # _resolve_bank already guarantees this can't happen, but the
        # belt-and-suspenders branch keeps mypy happy and protects
        # against an empty list slipping into a future bank update.
        return "¡Buen trabajo! Hasta pronto."
    if seed_key is None:
        return bank[0]
    # crc32 → stable across runs and Python versions; mod into the
    # bank length to pick a variant.
    idx = zlib.crc32(seed_key.encode("utf-8")) % len(bank)
    return bank[idx]
