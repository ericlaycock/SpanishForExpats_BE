"""Audit tests for ENCOUNTER_MESSAGES opener strings.

Run: python3.11 -m pytest tests/test_encounter_messages.py --noconftest -v

Each entry in `app/services/encounter_messages_generated.py` is the
opener line the avatar speaks at the start of a vocab encounter (and
the audio of which is pregenerated and uploaded to R2). When the
opener is a statement that closes the floor — e.g. "El embarque
comenzará en breve." — the student is left with nothing to respond
to and the lesson dead-ends before the LLM can recover.

The same TURN-CLOSING RULE the v3 system prompt enforces on the LLM
(`tests/test_prompts.py`) applies to the seed openers too: every
opener must end with a question mark.

This test sweeps the dictionary topic-by-topic. As each topic gets
audited and rewritten, add its prefix to `AUDITED_TOPIC_PREFIXES`
to lock it in. Topics not yet audited are skipped — the test still
fails loudly for any audited topic that drifts.
"""
from __future__ import annotations

import pytest

from app.services.encounter_messages_generated import ENCOUNTER_MESSAGES


# Topics whose `es` openers have been audited and rewritten as
# questions. Add a prefix here once the corresponding sweep PR
# lands. Order doesn't matter.
AUDITED_TOPIC_PREFIXES: frozenset[str] = frozenset({
    "air",
    "bank",
    "cloth",
    "contr",
    "groc",
    "inet",
    "mech",
    "pol",
    "rest",
    "talk",
})

# Topics intentionally excluded from the question-mark requirement.
# Grammar lesson openers are long narrative scene-setters ("Imagina
# que estás en un mercado vibrante…"), not conversational openers —
# they end on `!` or `.` by design and the student starts the
# conversation themselves after the intro.
EXEMPT_TOPIC_PREFIXES: frozenset[str] = frozenset({
    "grammar",
})


def _topic_prefix(situation_id: str) -> str:
    """Return the topic prefix `<topic>_` portion of a situation id.

    Examples: `air_12` → `air`, `grammar_pronouns` → `grammar`,
    `bank_3` → `bank`. Returns the full id when there's no `_`.
    """
    return situation_id.split("_", 1)[0]


@pytest.mark.parametrize(
    "situation_id",
    [
        sid for sid in sorted(ENCOUNTER_MESSAGES)
        if _topic_prefix(sid) in AUDITED_TOPIC_PREFIXES
        and _topic_prefix(sid) not in EXEMPT_TOPIC_PREFIXES
    ],
)
def test_audited_es_opener_ends_with_question_mark(situation_id: str):
    """Every audited topic's `es` opener must end with `?`.

    Locks the audit in: once a topic is added to
    `AUDITED_TOPIC_PREFIXES`, regressions break the test.
    """
    es = (ENCOUNTER_MESSAGES[situation_id].get("es") or "").rstrip()
    assert es, f"{situation_id} has empty `es` opener"
    assert es.endswith(("?", "？")), (
        f"{situation_id} `es` opener is not a question: {es!r}\n"
        f"Convert to a question that invites a response — "
        f"see PR description for examples."
    )


def test_unaudited_topics_are_known():
    """Sanity check: list which non-grammar topics still need audit.

    This test always passes — its purpose is to surface the remaining
    topics in pytest's verbose output so the team can plan follow-up
    sweeps. Exempt topics (grammar) are excluded.
    """
    unaudited: dict[str, int] = {}
    for sid in ENCOUNTER_MESSAGES:
        topic = _topic_prefix(sid)
        if topic in AUDITED_TOPIC_PREFIXES or topic in EXEMPT_TOPIC_PREFIXES:
            continue
        es = (ENCOUNTER_MESSAGES[sid].get("es") or "").rstrip()
        if es and not es.endswith(("?", "？")):
            unaudited[topic] = unaudited.get(topic, 0) + 1

    if unaudited:
        # Print for visibility — pytest -v will show this in the
        # captured output of a passing test.
        print("\nUnaudited topics with non-question `es` openers:")
        for topic, count in sorted(unaudited.items()):
            print(f"  {topic}: {count} dead-end opener(s)")
