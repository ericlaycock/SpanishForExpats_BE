"""Pure-Python tests for the Spanish-frame grammar elicitation helper.

Run with: python3.11 -m pytest tests/test_services/test_grammar_elicitation.py --noconftest -v
"""
from app.services.grammar_elicitation import (
    PRONOUN_ELICITATION_FRAMES,
    format_target_steering,
    is_student_asks_chip,
    _vocab_elicitation_hint,
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


class TestIsStudentAsksChip:
    def test_question_label_detected(self):
        assert is_student_asks_chip(
            ChipTarget(id="x", spanish="¿sale mañana?", english="does it leave tomorrow?")
        ) is True

    def test_label_with_trailing_whitespace(self):
        assert is_student_asks_chip(
            ChipTarget(id="x", spanish="?", english="does it leave today?  \n")
        ) is True

    def test_non_question_label(self):
        for label in ("departure", "arrival", "the (masc.)", "of/from", "that/which"):
            chip = ChipTarget(id="x", spanish="x", english=label)
            assert is_student_asks_chip(chip) is False, f"{label!r} flagged"

    def test_empty_label(self):
        assert is_student_asks_chip(
            ChipTarget(id="x", spanish="x", english="")
        ) is False


class TestStudentAsksAnnotation:
    def test_steering_block_tags_question_chips(self):
        chips = [
            ChipTarget(id="a", spanish="¿sale mañana?", english="does it leave tomorrow?"),
            ChipTarget(id="b", spanish="salida", english="departure"),
        ]
        out = format_target_steering(chips, [])
        # Question chip is tagged.
        question_line = next(l for l in out.splitlines() if "tomorrow" in l)
        assert "[STUDENT ASKS]" in question_line
        # Plain vocab chip is NOT tagged.
        plain_line = next(l for l in out.splitlines() if "departure" in l)
        assert "[STUDENT ASKS]" not in plain_line

    def test_grammar_chip_no_tag_even_with_question_mark_in_gloss(self):
        # Grammar conjugation chips never have `?` in their english label
        # ("you sing", "I dance", …), but the rendering still goes through
        # the same code path. Confirm the tag isn't accidentally appended
        # to a typical grammar chip.
        chip = ChipTarget(
            id="conj_cantar_tu", spanish="cantas", english="you sing",
            verb="cantar", pronoun="tú",
        )
        out = format_target_steering([chip], [])
        assert "[STUDENT ASKS]" not in out


class TestVocabElicitationHints:
    """Hints for grammatical-artifact vocab chips (reflexives, contractions).

    These chips come from the previous grammar lesson and the encounter
    is designed to immediately practice them. Without an elicitation
    hint the LLM defaults to asking generic questions (`¿cuál es su
    nombre?`) whose answers don't exercise the chip — see the airport
    screenshots in the avatar-dynamics thread.
    """

    def test_reflexive_pronoun_chip_emits_hint(self):
        chip = ChipTarget(id="hf_27", spanish="se", english="oneself (reflexive)")
        out = format_target_steering([chip], [])
        assert "Elicit with:" in out
        assert "reflexive" in out.lower()
        # Hint must NOT cause the LLM to leak the form itself.
        assert "Do NOT use the form yourself" in out

    def test_del_chip_emits_hint(self):
        chip = ChipTarget(id="hf_28", spanish="del", english="of the (de + el)")
        out = format_target_steering([chip], [])
        assert "Elicit with:" in out
        # hint references the contracted form
        assert "del" in out
        assert "masculine" in out.lower()

    def test_al_chip_emits_hint(self):
        chip = ChipTarget(id="hf_37", spanish="al", english="to the (a + el)")
        out = format_target_steering([chip], [])
        assert "Elicit with:" in out
        # 'al' appears in "natural" too — assert the hint mentions
        # contraction context rather than just the bare letters.
        assert "masculine" in out.lower()

    def test_plain_lexical_chip_has_no_hint(self):
        """Concrete nouns/verbs are self-elicitable — no hint needed."""
        for spanish, english in (
            ("botella", "bottle"),
            ("puerta", "gate"),
            ("pasaporte", "passport"),
        ):
            chip = ChipTarget(id="x", spanish=spanish, english=english)
            assert _vocab_elicitation_hint(chip) is None, (
                f"plain chip {english!r} should not get a hint"
            )

    def test_reflexive_infinitive_form_also_matches(self):
        """`(reflexive)` substring catches both pronouns AND infinitive
        forms like `quedarte`, so they all get the same elicitation
        guidance — sufficient because the underlying mechanic (set up
        a reflexive verb context) is identical."""
        chip = ChipTarget(
            id="hf_2014", spanish="quedarte", english="to stay (reflexive)",
        )
        assert _vocab_elicitation_hint(chip) is not None
