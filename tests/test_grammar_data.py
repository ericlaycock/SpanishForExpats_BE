"""Structural guards on grammar_situations.py.

Ensures every grammar situation has the drill data its drill type requires.
This catches the class of bug where a new situation is added without
populating its drill_config, which would surface to users as
"No drill data available" in the FE.
"""
import pytest

from app.data.grammar_situations import GRAMMAR_SITUATIONS


DRILL_TYPES_REQUIRING_ANSWERS = {"conjugation", "ir_a_inf"}


def _ids_by_drill_type(drill_type: str):
    return [
        sid for sid, cfg in GRAMMAR_SITUATIONS.items()
        if cfg.get("drill_type") == drill_type
    ]


@pytest.mark.parametrize("sid", _ids_by_drill_type("conjugation"))
def test_conjugation_drill_has_populated_answers(sid):
    """Every conjugation drill must have a non-empty answers table for every
    verb in its word_workload, and each verb must have at least one pronoun form."""
    cfg = GRAMMAR_SITUATIONS[sid]
    drill_config = cfg.get("drill_config")
    assert drill_config is not None, f"{sid}: drill_config missing"
    answers = drill_config.get("answers")
    assert answers, f"{sid}: drill_config.answers missing or empty"

    # Imperatives don't have a 'yo' form — you don't command yourself.
    required_pronouns = ("tú", "nosotros") if cfg.get("tense") == "imperative" else ("yo", "tú", "nosotros")

    for verb in cfg.get("word_workload", []):
        assert verb in answers, f"{sid}: missing answers for verb '{verb}'"
        forms = answers[verb]
        assert isinstance(forms, dict) and forms, (
            f"{sid}: empty or non-dict answers for verb '{verb}'"
        )
        for pronoun in required_pronouns:
            assert pronoun in forms, (
                f"{sid}: missing {pronoun!r} form for verb {verb!r}"
            )
            assert forms[pronoun], (
                f"{sid}: blank {pronoun!r} form for verb {verb!r}"
            )


@pytest.mark.parametrize("sid", _ids_by_drill_type("ir_a_inf"))
def test_ir_a_inf_drill_has_populated_answers(sid):
    cfg = GRAMMAR_SITUATIONS[sid]
    drill_config = cfg.get("drill_config")
    assert drill_config is not None, f"{sid}: drill_config missing"
    answers = drill_config.get("answers")
    assert answers, f"{sid}: drill_config.answers missing or empty"


@pytest.mark.parametrize("sid", _ids_by_drill_type("article_matching"))
def test_article_matching_drill_has_nouns(sid):
    cfg = GRAMMAR_SITUATIONS[sid]
    drill_config = cfg.get("drill_config")
    assert drill_config is not None, f"{sid}: drill_config missing"
    nouns = drill_config.get("curated_nouns") or drill_config.get("nouns") or drill_config.get("items")
    assert nouns, f"{sid}: article_matching drill missing curated_nouns/items"


@pytest.mark.parametrize("sid", _ids_by_drill_type("gustar") + _ids_by_drill_type("gustar_prefix"))
def test_gustar_drill_has_items(sid):
    cfg = GRAMMAR_SITUATIONS[sid]
    drill_config = cfg.get("drill_config")
    assert drill_config is not None, f"{sid}: drill_config missing"
    items = drill_config.get("items")
    assert items, f"{sid}: gustar drill missing items"


def test_every_grammar_situation_has_drill_type():
    """No grammar situation should be missing a drill_type field."""
    missing = [sid for sid, cfg in GRAMMAR_SITUATIONS.items() if not cfg.get("drill_type")]
    assert not missing, f"Grammar situations missing drill_type: {missing}"


def test_no_unexpected_drill_types():
    """Drill types must be one of the known set the FE knows how to render.

    If a new drill type is added, update this list AND the FE DrillPhase
    renderer. Otherwise users see 'No drill data available'.
    """
    known = {
        "skip", "conjugation", "article_matching",
        "ir_a_inf", "gustar", "gustar_prefix", "rule",
    }
    actual = {cfg.get("drill_type") for cfg in GRAMMAR_SITUATIONS.values()}
    unknown = actual - known
    assert not unknown, (
        f"Unknown drill_types present: {unknown}. "
        f"Add a renderer in DrillPhase.tsx and update this test."
    )
