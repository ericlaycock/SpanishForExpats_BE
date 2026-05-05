"""Pure-Python tests for realtime per-turn steering instructions.

Covers the two regimes of `build_response_instructions`:

- Grammar chips (with pronoun + verb): pronoun-flip template lookup.
- Vocab chips (no pronoun): VOCAB_ELICITATION_HINTS reuse for
  grammatical artifacts (reflexives, contractions, gendered articles)
  and the generic fallback for plain lexical chips.

Run: python3.11 -m pytest tests/test_services/test_realtime_steering.py --noconftest -v
"""
from __future__ import annotations

from app.services.realtime_steering import (
    _build_vocab_response_instructions,
    build_response_instructions,
)


class TestBuildResponseInstructionsGrammar:
    def test_yo_target_renders_tu_question_template(self):
        out = build_response_instructions({
            "id": "conj_comer_yo",
            "spanish": "como",
            "english": "I eat",
            "pronoun": "yo",
            "verb": "comer",
        })
        assert out is not None
        # The yo→tú flip uses a "Ask the user a question" template.
        assert "Ask the user" in out
        # Conjugated tú-form is substituted in.
        assert "comes" in out

    def test_unknown_pronoun_returns_none(self):
        out = build_response_instructions({
            "id": "x",
            "spanish": "cantamos",
            "english": "we sing",
            "pronoun": "vos",  # not in _PRONOUN_INSTRUCTIONS
            "verb": "cantar",
        })
        assert out is None


class TestBuildResponseInstructionsVocab:
    def test_plain_lexical_chip_uses_generic_fallback(self):
        out = build_response_instructions({
            "id": "w_gate_number",
            "spanish": "número de puerta",
            "english": "gate number",
        })
        assert out is not None
        # Generic fallback names both forms verbatim and forbids leak.
        assert "número de puerta" in out
        assert "gate number" in out
        assert "Do NOT say" in out
        # Brevity tag is appended.
        assert "2 short sentences" in out

    def test_masc_plural_article_chip_uses_hint(self):
        out = build_response_instructions({
            "id": "hf_26",
            "spanish": "los",
            "english": "the (masc. pl.)",
        })
        assert out is not None
        # Comes from VOCAB_ELICITATION_HINTS: instructs an answer with
        # masc.-plural article + noun.
        assert "masc." in out
        assert "plural" in out.lower()
        # Brevity tag still appended on the hint path.
        assert "2 short sentences" in out

    def test_a_el_contraction_chip_uses_hint(self):
        out = build_response_instructions({
            "id": "hf_37",
            "spanish": "al",
            "english": "to the (a + el)",
        })
        assert out is not None
        assert "masculine" in out.lower()
        assert "Do NOT say" in out

    def test_reflexive_chip_uses_hint(self):
        out = build_response_instructions({
            "id": "hf_27",
            "spanish": "se",
            "english": "oneself (reflexive)",
        })
        assert out is not None
        assert "reflexive" in out.lower()

    def test_missing_spanish_returns_none(self):
        assert build_response_instructions({
            "id": "x",
            "spanish": "",
            "english": "gate",
        }) is None

    def test_helper_called_directly_for_vocab(self):
        # The vocab helper is the path used by realtime turns whenever
        # the target lacks pronoun/verb metadata. Confirm it works
        # without going through the dispatcher.
        out = _build_vocab_response_instructions({
            "id": "w_gate",
            "spanish": "puerta",
            "english": "gate",
        })
        assert out is not None
        assert "puerta" in out
        assert "gate" in out
