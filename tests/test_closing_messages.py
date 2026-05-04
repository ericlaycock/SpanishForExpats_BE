"""Coverage + integrity tests for the closing-message bank.

Run: python3.11 -m pytest tests/test_closing_messages.py --noconftest -v

The bank is consumed by `pick_closing_message` on the wrap-up turn
of a completed encounter. If a key is missing or a line ends with
`?`, the bypass either falls through to a generic message (silent
regression) or reintroduces the very dead-end question we removed.
"""
from __future__ import annotations

from app.data.closing_messages import (
    CLOSING_MESSAGES_ES,
    CLOSING_MESSAGES_CA,
    CLOSING_MESSAGES_SV,
    CLOSING_BANKS,
    GENERIC_CLOSING_ES,
)


# Keep this aligned with `SITUATION_ROLES` in app/data/situation_roles.py
# plus the synthetic `grammar` scene; if a new animation_type lands we
# want this test to fail loudly until the bank is filled in.
EXPECTED_ANIMATION_TYPES: frozenset[str] = frozenset({
    "airport", "banking", "clothing", "contractor", "core", "groceries",
    "internet", "mechanic", "police", "restaurant", "small_talk",
    "grammar",
})

MIN_VARIANTS_PER_ANIM_TYPE = 3


class TestSpanishBankCoverage:
    def test_every_animation_type_has_an_entry(self):
        missing = EXPECTED_ANIMATION_TYPES - set(CLOSING_MESSAGES_ES.keys())
        assert not missing, f"Spanish bank missing keys: {sorted(missing)}"

    def test_no_extra_animation_types(self):
        extra = set(CLOSING_MESSAGES_ES.keys()) - EXPECTED_ANIMATION_TYPES
        assert not extra, (
            f"Spanish bank has unexpected keys (was a scene removed?): "
            f"{sorted(extra)}"
        )

    def test_each_entry_has_minimum_variants(self):
        for anim, lines in CLOSING_MESSAGES_ES.items():
            assert len(lines) >= MIN_VARIANTS_PER_ANIM_TYPE, (
                f"Spanish bank {anim!r} has only {len(lines)} variant(s); "
                f"need >= {MIN_VARIANTS_PER_ANIM_TYPE} so consecutive "
                f"replays don't repeat."
            )


class TestNoDeadEndQuestions:
    """The whole point of the bypass is to STOP asking another
    question after the lesson is over. A `?` in any closing line
    would defeat that — even one would partially regress."""

    def _all_lines(self):
        for bank in (CLOSING_MESSAGES_ES, CLOSING_MESSAGES_CA, CLOSING_MESSAGES_SV):
            for anim, lines in bank.items():
                for line in lines:
                    yield (anim, line)
        for line in GENERIC_CLOSING_ES:
            yield ("generic", line)

    def test_no_line_ends_with_question_mark(self):
        for anim, line in self._all_lines():
            stripped = line.rstrip()
            assert not stripped.endswith(("?", "？", "¿")), (
                f"closing line for {anim!r} ends with question punctuation: "
                f"{line!r}"
            )

    def test_no_empty_lines(self):
        for anim, line in self._all_lines():
            assert line.strip(), f"{anim!r} bank has an empty/whitespace line"

    def test_lines_have_terminal_punctuation(self):
        for anim, line in self._all_lines():
            stripped = line.rstrip()
            assert stripped.endswith((".", "!", "！")), (
                f"closing line for {anim!r} should end with `.` or `!` "
                f"(closes the floor cleanly): {line!r}"
            )


class TestAltLanguageBanks:
    """Catalan + Swedish banks don't need to mirror Spanish line-for-line
    but every Spanish key MUST exist so the picker never falls through
    silently to GENERIC_CLOSING_ES (which is Spanish-only)."""

    def test_catalan_covers_every_animation_type(self):
        missing = set(CLOSING_MESSAGES_ES.keys()) - set(CLOSING_MESSAGES_CA.keys())
        assert not missing, f"Catalan bank missing keys: {sorted(missing)}"

    def test_swedish_covers_every_animation_type(self):
        missing = set(CLOSING_MESSAGES_ES.keys()) - set(CLOSING_MESSAGES_SV.keys())
        assert not missing, f"Swedish bank missing keys: {sorted(missing)}"

    def test_alt_banks_have_minimum_variants(self):
        # Lower bar than Spanish (translations are cheap to add over time)
        # but still > 1 so we have at least *some* rotation.
        for lang, bank in (("catalan", CLOSING_MESSAGES_CA),
                           ("swedish", CLOSING_MESSAGES_SV)):
            for anim, lines in bank.items():
                assert len(lines) >= 2, (
                    f"{lang} bank {anim!r}: needs >= 2 variants, got "
                    f"{len(lines)}"
                )


class TestClosingBanksDispatch:
    """`CLOSING_BANKS` is the language → bank dict consumed by the
    picker service; missing keys mean the picker falls back to ES."""

    def test_es_alias(self):
        assert CLOSING_BANKS["es"] is CLOSING_MESSAGES_ES

    def test_catalan_key(self):
        assert CLOSING_BANKS["catalan"] is CLOSING_MESSAGES_CA

    def test_swedish_key(self):
        assert CLOSING_BANKS["swedish"] is CLOSING_MESSAGES_SV

    def test_known_languages_only(self):
        # Reminds us to extend `alt_language_service.get_target_language_name`
        # whenever this set grows.
        assert set(CLOSING_BANKS.keys()) == {"es", "catalan", "swedish"}
