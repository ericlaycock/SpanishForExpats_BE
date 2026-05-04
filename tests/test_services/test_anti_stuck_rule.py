"""Tests for the ANTI-STUCK rule renderer.

Run: python3.11 -m pytest tests/test_services/test_anti_stuck_rule.py --noconftest -v

The renderer escalates scaffolding as the learner skips the target
chip across consecutive turns. Three behaviours to lock in:

1. n=0 returns an empty string — no scaffolding pollution on the very
   first turn of every conversation.
2. 1 ≤ n < TRANSLATE returns the tactics menu (synonym / define /
   contrast / fill-in-blank / embedded yes/no) so the LLM rotates
   strategies instead of repeating one elicitation pattern.
3. n ≥ TRANSLATE returns the last-resort English-parenthetical
   instruction.

Lowering the nudge threshold from 2 → 1 was a behavioural choice for
native-English-speaking learners; locking it in here so a future
"performance" tweak doesn't silently push it back without test churn.
"""
from __future__ import annotations

from app.services.voice_turn_service import (
    _render_anti_stuck_rule,
    _STUCK_THRESHOLD_NUDGE,
    _STUCK_THRESHOLD_TRANSLATE,
)


class TestThresholds:
    def test_nudge_fires_after_one_no_progress_turn(self):
        """Native-English learners need scaffolding fast. Nudge starts at n=1."""
        assert _STUCK_THRESHOLD_NUDGE == 1

    def test_translate_threshold_unchanged(self):
        """Last-resort English glossing still requires 3 stuck turns."""
        assert _STUCK_THRESHOLD_TRANSLATE == 3


class TestRenderedText:
    def test_zero_returns_empty(self):
        assert _render_anti_stuck_rule(0) == ""

    def test_negative_treated_as_zero(self):
        assert _render_anti_stuck_rule(-1) == ""

    def test_none_treated_as_zero(self):
        # The renderer accepts the legacy None coming out of older
        # learner_ctx call-sites (defaults to 0).
        assert _render_anti_stuck_rule(None) == ""  # type: ignore[arg-type]

    def test_nudge_level_lists_all_five_tactics(self):
        """The menu must surface every alternative tactic so the LLM
        actually rotates instead of looping on one pattern."""
        out = _render_anti_stuck_rule(1)
        assert "ANTI-STUCK" in out
        for tactic in ("Synonym", "Define", "Contrast",
                       "Fill-in-blank", "Embedded yes/no"):
            assert tactic in out, f"tactic {tactic!r} missing from menu"

    def test_nudge_level_uses_spanish_examples(self):
        """Examples should be in the target language, not English —
        the LLM tends to mirror the language of its examples."""
        out = _render_anti_stuck_rule(1)
        # Sample Spanish anchor phrases from the menu's examples.
        for sample in ("demorado", "no sale a tiempo", "está a tiempo"):
            assert sample in out, f"Spanish example {sample!r} missing"

    def test_translate_level_kicks_in_at_threshold(self):
        out = _render_anti_stuck_rule(_STUCK_THRESHOLD_TRANSLATE)
        assert "translate" in out.lower()
        # The menu tactics should NOT also appear at translate level —
        # we want the prompt to commit to one behaviour, not show both.
        assert "Synonym" not in out
        assert "Embedded yes/no" not in out

    def test_intermediate_levels_still_show_menu(self):
        """n=1 and n=2 both show the menu (translate threshold = 3)."""
        out_1 = _render_anti_stuck_rule(1)
        out_2 = _render_anti_stuck_rule(2)
        assert "Synonym" in out_1 and "Synonym" in out_2

    def test_count_appears_in_message(self):
        """The count is interpolated so the LLM knows how stuck the
        learner has been (helps it pick a more direct tactic)."""
        out_2 = _render_anti_stuck_rule(2)
        assert "2 turn" in out_2
