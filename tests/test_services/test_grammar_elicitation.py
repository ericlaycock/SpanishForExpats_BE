"""Pure-Python tests for the Spanish-frame grammar elicitation helper.

Run with: python3.11 -m pytest tests/test_services/test_grammar_elicitation.py --noconftest -v
"""
from app.services.grammar_elicitation import (
    PRONOUN_ELICITATION_FRAMES,
    format_target_steering,
)
from app.services.learner_context import ChipTarget


class TestFrames:
    def test_all_pronouns_covered(self):
        expected = {
            "yo", "tú", "él", "ella", "usted",
            "nosotros", "nosotras", "ellos", "ellas", "ustedes",
        }
        assert set(PRONOUN_ELICITATION_FRAMES.keys()) == expected

    def test_frames_are_spanish(self):
        """Frames lead with Spanish copy, not English."""
        for pronoun, frame in PRONOUN_ELICITATION_FRAMES.items():
            # Each frame contains a Spanish question or sentence-stem;
            # English appears only inside the [bare_lemma in X form] slot.
            stripped = frame.split("[")[0].strip()
            # Spanish anchors: "Yo", "Cuéntame", "Y tu", "Tus", etc.
            assert any(stripped.startswith(p) for p in (
                "Yo", "Cuéntame", "Y", "Tus",
            )), f"{pronoun} frame doesn't start with Spanish copy: {frame!r}"


class TestFormatTargetSteering:
    def test_empty_chips_returns_empty_string(self):
        assert format_target_steering([], []) == ""

    def test_all_completed_returns_empty_string(self):
        chips = [ChipTarget(id="x", spanish="hola", english="hi")]
        assert format_target_steering(chips, ["x"]) == ""

    def test_pending_only(self):
        chips = [
            ChipTarget(id="a", spanish="agua", english="water"),
            ChipTarget(id="b", spanish="pan", english="bread"),
        ]
        out = format_target_steering(chips, ["a"])
        assert "agua" not in out
        assert "pan" in out

    def test_grammar_chip_has_elicitation_frame(self):
        chip = ChipTarget(
            id="conj_hablar_yo",
            spanish="hablo",
            english="I speak",
            verb="hablar",
            pronoun="yo",
        )
        out = format_target_steering([chip], [])
        assert "hablo" in out
        assert "Elicit with:" in out
        # Frame should reference the target form for "yo"
        assert "1st person" in out

    def test_vocab_chip_has_no_elicitation_frame(self):
        chip = ChipTarget(id="word_botella", spanish="botella", english="bottle")
        out = format_target_steering([chip], [])
        assert "botella" in out
        assert "Elicit with:" not in out

    def test_unknown_pronoun_falls_back_to_generic_frame(self):
        chip = ChipTarget(
            id="x", spanish="forma", english="form",
            verb="hablar", pronoun="vos",  # not in PRONOUN_ELICITATION_FRAMES
        )
        out = format_target_steering([chip], [])
        assert "forma" in out
        # Generic fallback uses the bare lemma + pronoun template.
        assert "speak" in out.lower() or "vos" in out
