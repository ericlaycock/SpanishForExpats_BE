"""Tests for `pick_closing_message`.

Run: python3.11 -m pytest tests/test_services/test_closing_message_service.py --noconftest -v
"""
from __future__ import annotations

from app.data.closing_messages import (
    CLOSING_MESSAGES_ES,
    CLOSING_MESSAGES_CA,
    CLOSING_MESSAGES_SV,
)
from app.services.closing_message_service import pick_closing_message


class TestKnownAnimationTypes:
    def test_returns_a_known_es_line(self):
        line = pick_closing_message("airport")
        assert line in CLOSING_MESSAGES_ES["airport"]

    def test_returns_a_known_catalan_line(self):
        line = pick_closing_message("airport", alt_language="catalan")
        assert line in CLOSING_MESSAGES_CA["airport"]

    def test_returns_a_known_swedish_line(self):
        line = pick_closing_message("airport", alt_language="swedish")
        assert line in CLOSING_MESSAGES_SV["airport"]

    def test_explicit_spanish_string_resolves_to_es(self):
        # Some callers may pass "spanish" instead of None — both routes
        # should land on the Spanish bank.
        line = pick_closing_message("banking", alt_language="spanish")
        assert line in CLOSING_MESSAGES_ES["banking"]


class TestUnknownAnimationType:
    def test_unknown_anim_type_falls_back_to_generic(self):
        # A rare anim_type that isn't in any bank → still returns a
        # non-empty closing rather than raising.
        line = pick_closing_message("__not_a_real_anim_type__")
        assert isinstance(line, str)
        assert line.strip()

    def test_unknown_alt_language_falls_back_to_spanish_bank(self):
        # If the locale isn't supported yet but the anim_type IS in
        # Spanish, we'd rather speak Spanish than nothing.
        line = pick_closing_message("airport", alt_language="basque")
        assert line in CLOSING_MESSAGES_ES["airport"]


class TestDeterministicSeed:
    """`seed_key` controls the variant index. The same key must
    always produce the same closing — that's what lets the FE retry
    a transient failure without flapping the closing copy."""

    def test_same_seed_picks_same_line_repeatedly(self):
        line_a = pick_closing_message("airport", seed_key="air_15")
        line_b = pick_closing_message("airport", seed_key="air_15")
        line_c = pick_closing_message("airport", seed_key="air_15")
        assert line_a == line_b == line_c

    def test_different_seeds_can_pick_different_lines(self):
        # Sweep ~50 distinct seeds; given >= 5 variants in the airport
        # bank, the picker MUST land on more than one line. If it
        # returns the same line every time, crc32 mod is broken.
        seen = {
            pick_closing_message("airport", seed_key=f"sid_{i}")
            for i in range(50)
        }
        assert len(seen) >= 2, (
            "seed-based rotation collapsed to a single line — picker bug"
        )

    def test_no_seed_returns_first_variant(self):
        # `seed_key=None` → deterministic first-variant pick. Used by
        # tests and any caller that doesn't have a stable id.
        line = pick_closing_message("airport", seed_key=None)
        assert line == CLOSING_MESSAGES_ES["airport"][0]


class TestNeverReturnsEmpty:
    """Belt-and-suspenders: even pathological inputs return a usable
    string. The bypass route streams whatever this function returns
    straight into the Realtime API, so an empty string would mean
    silent audio."""

    def test_empty_animation_type(self):
        line = pick_closing_message("")
        assert line.strip()

    def test_empty_alt_language(self):
        line = pick_closing_message("airport", alt_language="")
        assert line.strip()

    def test_empty_seed_key_string(self):
        # Empty string seed isn't None — it goes through crc32, which
        # is fine (returns 0). Should NOT crash.
        line = pick_closing_message("airport", seed_key="")
        assert line in CLOSING_MESSAGES_ES["airport"]
