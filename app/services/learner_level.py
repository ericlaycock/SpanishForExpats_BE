"""Shared level-aware prompt rules keyed on `User.q0_spanish_level`.

The onboarding V2 quiz answer (`a`/`b`/`c`/`d`) maps to a learner-level
band that we surface to the LLM as a short rule string. Two consumers:

- `sentence_hint_service` — needs a sentence-budget rule (one sentence,
  word count, allowable subordinates) so the hint stays speakable.
- The conversation/grammar agents (prompts.json v3) — need a cadence rule
  governing the AI's own turns (sentence length, complexity, idiom use).

These are deliberately different prompts: a hint is one sentence the
learner produces; a conversation rule governs the AI's pacing across
many turns. Sharing a level lookup but separate copy keeps both honest.

Null/unknown levels fall back to `c` (intermediate) — safe middle ground
for legacy users who never went through V2 onboarding.
"""
from __future__ import annotations

from typing import Optional


_DEFAULT_LEVEL = "c"


def _normalize(spanish_level: Optional[str]) -> str:
    return (spanish_level or _DEFAULT_LEVEL).lower()


def level_rules_for_hint(spanish_level: Optional[str]) -> str:
    """Sentence-budget rule for `/sentence-hint` generation.

    Returns a single bullet line ready to drop into the hint system
    prompt. Tighter limits at lower levels because a 14-word hint is
    unspeakable for an absolute beginner.
    """
    level = _normalize(spanish_level)
    if level == "a":
        return (
            "- LEARNER LEVEL: absolute beginner. The sentence MUST be 5–7 words "
            "and use EXACTLY ONE pending item. No subordinate clauses, no "
            "compound sentences, no embedded questions. Keep it as simple as "
            "physically possible to say out loud."
        )
    if level == "b":
        return (
            "- LEARNER LEVEL: novice. The sentence MUST be 7–9 words and use 1 "
            "pending item (a second only if it fits naturally). No complex "
            "subordinates."
        )
    if level == "d":
        return (
            "- LEARNER LEVEL: advanced. Sentence may be up to ~14 words and "
            "use 1 or 2 pending items with natural complexity."
        )
    return (
        "- LEARNER LEVEL: intermediate. The sentence MUST be 9–12 words and "
        "use 1 or 2 pending items. Simple subordinates allowed."
    )


def level_rules_for_conversation(spanish_level: Optional[str]) -> str:
    """Cadence rule for the conversation/grammar agent's own turns.

    Governs how the AI speaks back: sentence length, complexity, idiom
    tolerance, speed cues. Separate from `level_rules_for_hint` because
    the AI is producing many turns in roleplay, not a single sentence
    the learner must repeat.
    """
    level = _normalize(spanish_level)
    if level == "a":
        return (
            "- LEARNER LEVEL: absolute beginner. Speak slowly. 4–6 word "
            "sentences. One idea per turn. No subordinate clauses, no idioms, "
            "no slang. Stick to present tense verbs the learner has seen."
        )
    if level == "b":
        return (
            "- LEARNER LEVEL: novice. 6–9 word sentences. Avoid compound "
            "clauses. No idioms or regional slang. Repeat key nouns rather "
            "than using pronouns the learner may not catch."
        )
    if level == "d":
        return (
            "- LEARNER LEVEL: advanced. Speak normally but clearly. Natural "
            "sentence length is fine; idioms and varied tenses welcome. "
            "Push the learner with follow-ups."
        )
    return (
        "- LEARNER LEVEL: intermediate. Natural sentences but no idioms or "
        "optional subjunctive. Keep clauses short — one subordinate max."
    )
