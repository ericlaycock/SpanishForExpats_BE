"""Grammar categories — the bucketing the dashboard / TQ map uses for the
per-category diagnostic gate.

A new user lands on the map with these seven categories *locked*. Tapping a
locked category routes to its diagnostic; passing the diagnostic unlocks
that category. Existing users are grandfathered to fully-unlocked at
migration time (see `migrations/versions/044_user_category_progress.py`,
and `046_dragon_and_avatars.py` for the subjunctive 1→3 split).

Each grammar_level maps to exactly one of:

- ``"present"``, ``"past"``, ``"future"``, ``"modals"``,
  ``"subjunctive_triggers"``, ``"present_subjunctive"``,
  ``"imperfect_subjunctive"`` — the seven lockable categories.
- ``None`` — foundation lessons (pronouns, gender, possessive adjectives,
  gustar, object pronouns) that don't belong to any tense category. These
  stay open by default; locking them would block every new user from doing
  anything.

If you add a new grammar_level to ``GRAMMAR_SITUATIONS``, also add it here.
The :func:`gl_to_category` lookup falls through to ``None`` for unknown GLs,
matching the foundation behavior — failing closed (locked) would surprise a
content author shipping a new lesson.
"""

from __future__ import annotations

# Public list of the lockable categories, in the order they should render on
# the TQ map. The FE imports this list verbatim.
CATEGORIES: list[str] = [
    "present",
    "past",
    "future",
    "modals",
    "subjunctive_triggers",
    "present_subjunctive",
    "imperfect_subjunctive",
]

# Display labels — kept here so the FE and BE never disagree on capitalization.
CATEGORY_LABELS: dict[str, str] = {
    "present": "Present",
    "past": "Past",
    "future": "Future & Conditional",
    "modals": "Modals & Commands",
    "subjunctive_triggers": "Subjunctive Triggers",
    "present_subjunctive": "Present Subjunctive",
    "imperfect_subjunctive": "Imperfect Subjunctive",
}

# grammar_level → category mapping. Foundations explicitly map to None.
_GL_TO_CATEGORY: dict[float, str | None] = {
    # Foundations — always open.
    1: None,        # Pronouns
    1.5: None,      # Possessive Adjectives
    2: None,        # Grammatical Gender
    10: None,       # Gustar 1
    10.3: None,     # Gustar 2
    10.6: None,     # Gustar 3
    19: None,       # Direct + Indirect Object Pronouns

    # Present family — regular, irregular, spelling changes, stem changes,
    # reflexive. (Gerund used to live here but moved into Modals & Commands
    # in 2026-05 per user direction — it pairs naturally with "estar +
    # gerund" which is more of a periphrasis than a present-tense form.)
    3: "present",   # Regular Present
    4: "present",   # Irregular Present
    4.1: "present", # Ser vs Estar
    4.2: "present", # Por vs Para
    4.3: "present", # Demonstratives
    4.4: "present", # Possessive Pronouns
    4.5: "present", # Irregular Present II
    5: "present",   # Spelling Changes
    5.5: "present", # Saber vs Conocer
    6: "present",   # O→UE
    7: "present",   # E→IE
    8: "present",   # E→I
    13: "present",  # Reflexive

    # Modals & Commands — verb constructions that take an infinitive,
    # commands, and the gerund (which is itself a periphrasis: estar + -ndo).
    9: "modals",    # Ir A + Infinitive
    11: "modals",   # Tengo que / Me toca / Necesito
    13.5: "modals", # Imperatives (commands)
    18: "modals",   # Gerund (-ing)

    # Past — imperfect, preterite (regular + every irregular variant),
    # pret-vs-imperfect, perfect tenses.
    12: "past",     # Imperfect
    16: "past",     # Preterite vs Imperfect
    17: "past",     # Preterite Regular
    17.1: "past",   # Preterite Highly Irregular
    17.2: "past",   # Preterite Weird Spelling Changes
    17.3: "past",   # Preterite Stem Changers
    17.4: "past",   # Preterite DUCIR
    17.5: "past",   # Preterite e-to-i Irregular
    18.5: "past",   # Perfect Tenses

    # Future & Conditional — future simple + conditional.
    14: "future",   # Future Simple
    15: "future",   # Conditional

    # Subjunctive — split into THREE lockable buckets so learners progress
    # from rule recognition → present conjugation → past conjugation.
    19.5: "subjunctive_triggers",   # WEIRDO trigger phrases
    20: "present_subjunctive",       # hablar → hable, comer → coma…
    20.5: "imperfect_subjunctive",   # hablar → hablara, si tuviera…
}


def gl_to_category(gl: float) -> str | None:
    """Return the lockable category for a grammar_level, or None if the level
    is a foundation (always-open) or unknown (treated as foundation to avoid
    accidentally locking new content the author hasn't classified yet)."""
    return _GL_TO_CATEGORY.get(gl)


def is_foundation(gl: float) -> bool:
    """True when the grammar_level is not behind any category gate."""
    return gl_to_category(gl) is None
