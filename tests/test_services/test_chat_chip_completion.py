"""Pure-Python tests for `check_chat_chip_completion`.

Uses a SimpleNamespace stand-in for the Conversation row so we don't
need a DB connection. The function only reads `chat_target_forms_json`
off the conversation, so a duck-typed object is enough.

Run with:
  python3.11 -m pytest tests/test_services/test_chat_chip_completion.py --noconftest -v
"""
from types import SimpleNamespace

from app.services.conversation_service import check_chat_chip_completion


def _conv(chips):
    return SimpleNamespace(chat_target_forms_json=chips)


def test_no_chips_returns_empty():
    complete, ids = check_chat_chip_completion(_conv(None), ["hola"])
    assert complete is False
    assert ids == []


def test_no_transcripts_returns_empty():
    chips = [{"id": "x", "spanish": "hablo"}]
    complete, ids = check_chat_chip_completion(_conv(chips), [])
    assert complete is False
    assert ids == []


def test_single_chip_ticked():
    chips = [{"id": "x", "spanish": "hablo", "pronoun": "yo"}]
    complete, ids = check_chat_chip_completion(
        _conv(chips), ["yo hablo todos los días"],
    )
    assert complete is True
    assert ids == ["x"]


def test_partial_completion_lists_only_ticked():
    chips = [
        {"id": "a", "spanish": "hablo", "pronoun": "yo"},
        {"id": "b", "spanish": "habla", "pronoun": "ella"},
        {"id": "c", "spanish": "hablan", "pronoun": "ellos"},
    ]
    complete, ids = check_chat_chip_completion(
        _conv(chips),
        ["yo hablo en casa.", "mi hermana habla mucho"],
    )
    assert complete is False
    assert set(ids) == {"a", "b"}


def test_word_boundary_prevents_false_positive():
    # "hablo" must not match "hablamos" — word-boundary check.
    chips = [{"id": "yo", "spanish": "hablo", "pronoun": "yo"}]
    complete, ids = check_chat_chip_completion(
        _conv(chips), ["nosotros hablamos español"],
    )
    assert complete is False
    assert ids == []


def test_accent_insensitive_match():
    chips = [{"id": "x", "spanish": "tú", "pronoun": "tú"}]
    complete, ids = check_chat_chip_completion(
        _conv(chips), ["tu hablas mucho"],
    )
    assert complete is True
    assert ids == ["x"]


def test_id_synthesized_when_missing():
    """Older rows without an `id` field still tick correctly via fallback."""
    chips = [{"spanish": "hablo", "pronoun": "yo"}]
    complete, ids = check_chat_chip_completion(_conv(chips), ["yo hablo"])
    assert complete is True
    assert ids == ["form:hablo:yo"]


def test_punctuation_stripped():
    chips = [{"id": "x", "spanish": "hablo", "pronoun": "yo"}]
    complete, ids = check_chat_chip_completion(
        _conv(chips), ["¡Hablo! ¿Tú?"],
    )
    assert complete is True
    assert ids == ["x"]
