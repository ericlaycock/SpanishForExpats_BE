"""Spanish-language elicitation frames for grammar chat targeting.

Replaces the previous English-hardcoded `_build_grammar_hint` dict
(370+ lines of `(verb, pronoun) → English question` overrides) with a
small set of Spanish frames keyed by pronoun and parameterised on the
verb's English lemma. The avatar speaks Spanish in roleplay, so its
"what should I ask next" hint should be in Spanish too — feeding it
English think-aloud caused the model to leak English into its reply
and made the elicitation feel mechanical.

These frames are not a rigid script. They go into the v3 system prompt
under the target-steering block as suggestions; the LLM adapts them to
the scene and the conversation history.
"""
from __future__ import annotations

from typing import List

from app.data.grammar_situations import GRAMMAR_WORD_TRANSLATIONS
from app.services.learner_context import ChipTarget


# Each frame sets up a question whose natural answer uses the target
# (verb, pronoun) form. The Spanish frame stays roleplay-natural; the
# `[verb in {pronoun}]` slot is left as an English directive so the LLM
# fills it with the contextually-appropriate Spanish form when it
# speaks. Frames are deliberately short — the LLM has freedom to
# decorate them with scene context (a restaurant waiter, a neighbour,
# etc.).
PRONOUN_ELICITATION_FRAMES: dict[str, str] = {
    "yo":       "Yo siempre [{bare_lemma} in 1st person]. ¿Y tú?",
    "tú":       "Cuéntame, ¿tú [{bare_lemma} in tú form]?",
    "él":       "Y tu hermano, ¿[{bare_lemma} in 3rd person sing.]?",
    "ella":     "Y tu hermana, ¿[{bare_lemma} in 3rd person sing.]?",
    "usted":    "Y usted, ¿[{bare_lemma} in usted form]?",
    "nosotros": "Tus amigos y tú, ¿[{bare_lemma} in nosotros form]?",
    "nosotras": "Tus hermanas y tú, ¿[{bare_lemma} in nosotras form]?",
    "ellos":    "Tus amigos, ¿[{bare_lemma} in ellos form]?",
    "ellas":    "Tus amigas, ¿[{bare_lemma} in ellas form]?",
    "ustedes":  "Y ustedes, ¿[{bare_lemma} in ustedes form]?",
}


def _strip_to(lemma_en: str) -> str:
    """Drop a leading 'to ' and return the bare verb."""
    base = lemma_en.lower().strip()
    if base.startswith("to "):
        base = base[3:]
    base = base.split("/")[0].strip()  # "drink/take" → "drink"
    base = base.split(" or ")[0].strip()
    base = base.split("(")[0].strip()
    return base


def _frame_for_chip(chip: ChipTarget) -> str:
    """Render the elicitation frame for one grammar chip.

    Falls back to a generic prompt if the pronoun isn't in the frame
    table — keeps the prompt usable for any future pronouns we add.
    """
    pronoun = chip.pronoun or "tú"
    verb = chip.verb or chip.spanish
    en_lemma_full = GRAMMAR_WORD_TRANSLATIONS.get(verb, verb)
    bare_lemma = _strip_to(en_lemma_full)

    template = PRONOUN_ELICITATION_FRAMES.get(
        pronoun,
        "Cuéntame, ¿[{bare_lemma} in {pronoun} form]?",
    )
    return template.format(bare_lemma=bare_lemma, pronoun=pronoun)


# Vocab chips whose `english` label matches one of these patterns are
# grammatical artifacts (reflexive pronouns, contractions) rather than
# concrete lexical items. The avatar can't ask "what's the word for X?"
# to elicit them — it has to set up a question whose ANSWER naturally
# requires the form. Each entry maps a label substring to a hint the
# LLM can adapt.
#
# Why this matters: chips like `se`, `del`, `al` come from the previous
# grammar lesson and the encounter is supposed to immediately practice
# them. Without elicitation hints the LLM defaults to "¿cuál es su
# nombre?"-type questions whose answers don't exercise the chip — see
# the airport screenshots in the avatar-dynamics thread.
VOCAB_ELICITATION_HINTS: tuple[tuple[str, str], ...] = (
    (
        "(reflexive)",
        "ask a question whose natural answer uses a reflexive verb "
        "form so the student must say `me`/`te`/`se`/`nos` "
        "(e.g. '¿cómo se llama?', '¿a qué hora se levanta?', "
        "'¿quiere registrarse?'). Do NOT use the form yourself.",
    ),
    (
        "(de + el)",
        "ask a question whose answer requires `de` before a masculine "
        "noun so it contracts to `del` "
        "(e.g. '¿De qué país viene?' → 'vengo del…'; "
        "'¿De dónde sale el vuelo?' → 'sale del…'). "
        "Do NOT say `del` yourself.",
    ),
    (
        "(a + el)",
        "ask a question whose answer requires `a` before a masculine "
        "noun so it contracts to `al` "
        "(e.g. '¿Adónde va?' → 'voy al…'; "
        "'¿A qué lugar se dirige?' → 'al…'). "
        "Do NOT say `al` yourself.",
    ),
)


def _vocab_elicitation_hint(chip: ChipTarget) -> str | None:
    """Return an elicitation hint for grammatical-artifact vocab chips.

    Matches by substring on the `english` label so seed authors don't
    need to add metadata — `oneself (reflexive)`, `of the (de + el)`,
    and `to the (a + el)` are already the canonical glosses in
    `app/data/hf_words.py`. Returns `None` for ordinary lexical chips
    (`bottle`, `gate`, `passport`) — those are self-elicitable and the
    LLM can craft a natural question without help.
    """
    label = (chip.english or "").lower()
    for needle, hint in VOCAB_ELICITATION_HINTS:
        if needle in label:
            return hint
    return None


def is_student_asks_chip(chip: ChipTarget) -> bool:
    """Heuristic: chips whose English label is a question (ends with `?`)
    are ones the STUDENT must ask the avatar, not answer.

    Examples from real lessons:
      "does it leave tomorrow?" → student asks the avatar
      "how far does it go?"     → student asks the avatar
      "departure"               → student answers / mentions
      "the (masc.)"             → student uses in their reply

    The avatar's job for student-asks chips is opposite to its usual
    job: instead of asking a question whose answer is the chip, it
    must create a setup that *invites* the student to ask. Without
    this signal the LLM tends to ask the question itself, which both
    leaks the form and leaves the student with nothing to say.
    """
    label = (chip.english or "").rstrip()
    return label.endswith("?")


def format_target_steering(
    chips: List[ChipTarget],
    completed_chip_ids: List[str],
) -> str:
    """Render the target-steering block dropped into the v3 system prompt.

    Returns a multi-line string listing pending chips numbered 1..N with
    the EXACT Spanish form, English gloss, and (for grammar chips) a
    Spanish elicitation frame the LLM can adapt. Returns an empty
    string when there are no pending chips — the caller should omit the
    section entirely in that case.

    Question-shaped chips (English label ends with `?`) are tagged with
    `[STUDENT ASKS]` so the LLM knows to set up an opening rather than
    ask the question itself. See `is_student_asks_chip` for context.

    The block intentionally does NOT include already-completed chips —
    surfacing them invites the model to repeat words the learner has
    already mastered in this conversation.
    """
    completed = set(completed_chip_ids)
    pending = [c for c in chips if c.id not in completed]
    if not pending:
        return ""

    lines: List[str] = []
    for idx, chip in enumerate(pending, start=1):
        tag = " [STUDENT ASKS]" if is_student_asks_chip(chip) else ""
        if chip.is_grammar:
            frame = _frame_for_chip(chip)
            lines.append(
                f"{idx}.{tag} {chip.spanish} ({chip.english} — verb "
                f"'{chip.verb}' in {chip.pronoun}). "
                f"Elicit with: {frame}"
            )
        else:
            hint = _vocab_elicitation_hint(chip)
            if hint:
                lines.append(
                    f"{idx}.{tag} {chip.spanish} ({chip.english}). "
                    f"Elicit with: {hint}"
                )
            else:
                lines.append(f"{idx}.{tag} {chip.spanish} ({chip.english})")
    return "\n".join(lines)
