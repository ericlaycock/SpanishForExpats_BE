"""Unit tests for the avatar reply validator.

Pure-Python tests for the v3 prompt rule enforcement helpers in
`voice_turn_service`. No DB needed — they operate on plain
`ChipTarget` instances and strings.

Run: python3.11 -m pytest tests/test_services/test_avatar_validator.py --noconftest -v
"""
from __future__ import annotations

import pytest

from app.services.learner_context import ChipTarget
from app.services.voice_turn_service import (
    find_leaked_chips,
    is_dead_end_turn,
    validate_assistant_reply,
)


def _vocab_chip(spanish: str, *, chip_id: str | None = None) -> ChipTarget:
    return ChipTarget(
        id=chip_id or f"word:{spanish}",
        spanish=spanish,
        english="(gloss)",
    )


def _grammar_chip(spanish: str, *, verb: str = "cantar", pronoun: str = "tú") -> ChipTarget:
    return ChipTarget(
        id=f"conj_{verb}_{pronoun}",
        spanish=spanish,
        english="(gloss)",
        verb=verb,
        pronoun=pronoun,
    )


class TestIsDeadEndTurn:
    def test_question_mark_passes(self):
        assert is_dead_end_turn("¿A qué hora sale el vuelo?") is False

    def test_question_mark_with_trailing_whitespace_passes(self):
        assert is_dead_end_turn("¿Sale hoy?   \n") is False

    def test_period_is_dead_end(self):
        assert is_dead_end_turn("Déjame confirmar su hora de salida.") is True

    def test_ellipsis_is_dead_end(self):
        assert is_dead_end_turn("Un momento…") is True

    def test_exclamation_only_is_dead_end(self):
        assert is_dead_end_turn("¡Qué bien!") is True

    def test_full_width_question_mark_passes(self):
        assert is_dead_end_turn("¿Sale hoy？") is False

    def test_empty_text_is_not_flagged(self):
        # Empty replies are an upstream concern (no LLM output) — the
        # validator stays silent so the metric isn't polluted.
        assert is_dead_end_turn("") is False
        assert is_dead_end_turn("   \n  ") is False


class TestFindLeakedChips:
    def test_content_word_leak_detected(self):
        chips = [_vocab_chip("salida"), _vocab_chip("llegada")]
        leaked = find_leaked_chips(
            "Déjame confirmar su hora de salida.", chips,
        )
        assert leaked == ["word:salida"]

    def test_accent_insensitive(self):
        chips = [_vocab_chip("mañana")]
        # "manana" without tilde should still match — `normalize_text`
        # strips diacritics on both sides.
        leaked = find_leaked_chips("¿El vuelo sale manana?", chips)
        assert leaked == ["word:mañana"]

    def test_word_boundary_prevents_substring_false_positive(self):
        # "salida" should NOT match inside "salidas" (plural). The
        # validator uses a word-boundary regex for single-word chips.
        chips = [_vocab_chip("salida")]
        leaked = find_leaked_chips("Las salidas están atrasadas.", chips)
        assert leaked == []

    def test_function_word_chips_are_skipped(self):
        # `la`, `el`, `de`, `que` are function words — flagging them
        # would generate noise on every turn.
        chips = [
            _vocab_chip("la", chip_id="word:la"),
            _vocab_chip("el", chip_id="word:el"),
            _vocab_chip("de", chip_id="word:de"),
            _vocab_chip("que", chip_id="word:que"),
        ]
        leaked = find_leaked_chips(
            "El vuelo sale de la ciudad que está cerca.", chips,
        )
        assert leaked == []

    def test_grammar_chip_always_checked_even_if_short(self):
        # Conjugations like "voy" (3 chars) would be skipped by the
        # length heuristic alone — but grammar chips have a verb +
        # pronoun pair, so they get checked unconditionally.
        chips = [_grammar_chip("voy", verb="ir", pronoun="yo")]
        leaked = find_leaked_chips("Yo voy al aeropuerto.", chips)
        assert leaked == ["conj_ir_yo"]

    def test_multi_word_chip_substring_match(self):
        chips = [_vocab_chip("salida temprana")]
        leaked = find_leaked_chips(
            "Necesito una salida temprana mañana.", chips,
        )
        assert leaked == ["word:salida temprana"]

    def test_empty_inputs_return_empty(self):
        assert find_leaked_chips("", [_vocab_chip("salida")]) == []
        assert find_leaked_chips("Hola.", []) == []


class TestValidateAssistantReply:
    def test_clean_reply_passes(self):
        chips = [_vocab_chip("salida"), _vocab_chip("llegada")]
        flagged, leaked, reasons = validate_assistant_reply(
            "¿A qué hora quiere viajar?", chips,
        )
        assert flagged is False
        assert leaked == []
        assert reasons == []

    def test_dead_end_reply_flagged_with_no_question_reason(self):
        chips = [_vocab_chip("llegada")]
        flagged, leaked, reasons = validate_assistant_reply(
            "Voy a revisar.", chips,
        )
        assert flagged is True
        assert leaked == []
        assert reasons == ["no_question_mark"]

    def test_chip_leak_flagged(self):
        chips = [_vocab_chip("salida")]
        flagged, leaked, reasons = validate_assistant_reply(
            "¿Cuál es la salida?", chips,
        )
        assert flagged is True
        assert leaked == ["word:salida"]
        assert any(r.startswith("chip_leak:") for r in reasons)

    def test_both_violations_reported(self):
        # Statement that also leaks "salida" — both reasons should fire.
        chips = [_vocab_chip("salida")]
        flagged, leaked, reasons = validate_assistant_reply(
            "Déjame confirmar su hora de salida.", chips,
        )
        assert flagged is True
        assert leaked == ["word:salida"]
        assert "no_question_mark" in reasons
        assert any(r.startswith("chip_leak:") for r in reasons)

    def test_screenshot_2_regression(self):
        # Verbatim from the bug screenshot that motivated this work:
        # avatar leaked `salida` AND closed the floor without a question.
        chips = [
            _vocab_chip("salida", chip_id="word:departure"),
            _vocab_chip("llegada", chip_id="word:arrival"),
        ]
        flagged, leaked, reasons = validate_assistant_reply(
            "Déjame confirmar su hora de salida.", chips,
        )
        assert flagged is True
        assert leaked == ["word:departure"]
        assert "no_question_mark" in reasons
