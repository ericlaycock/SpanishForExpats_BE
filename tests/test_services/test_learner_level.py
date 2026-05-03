"""Pure-Python tests for the level-aware prompt rule helpers.

Run with: python3.11 -m pytest tests/test_services/test_learner_level.py --noconftest -v
"""
from app.services.learner_level import (
    level_rules_for_conversation,
    level_rules_for_hint,
)


class TestLevelRulesForHint:
    def test_each_level_returns_distinct_string(self):
        seen = {
            level_rules_for_hint(level)
            for level in ("a", "b", "c", "d")
        }
        assert len(seen) == 4

    def test_null_falls_back_to_intermediate(self):
        assert level_rules_for_hint(None) == level_rules_for_hint("c")
        assert level_rules_for_hint("") == level_rules_for_hint("c")

    def test_unknown_level_falls_back_to_intermediate(self):
        assert level_rules_for_hint("zzz") == level_rules_for_hint("c")

    def test_a_is_strictest(self):
        a = level_rules_for_hint("a")
        d = level_rules_for_hint("d")
        assert "5–7 words" in a
        assert "14 words" in d


class TestLevelRulesForConversation:
    def test_each_level_returns_distinct_string(self):
        seen = {
            level_rules_for_conversation(level)
            for level in ("a", "b", "c", "d")
        }
        assert len(seen) == 4

    def test_null_falls_back_to_intermediate(self):
        assert level_rules_for_conversation(None) == level_rules_for_conversation("c")

    def test_a_is_slowest(self):
        a = level_rules_for_conversation("a")
        assert "Speak slowly" in a
        assert "4–6 word sentences" in a

    def test_d_is_natural(self):
        d = level_rules_for_conversation("d")
        assert "normally" in d.lower()


class TestSeparateRules:
    def test_hint_and_conversation_diverge(self):
        """Hint rule talks about a single sentence; conversation rule about cadence."""
        for level in ("a", "b", "c", "d"):
            assert level_rules_for_hint(level) != level_rules_for_conversation(level)
