"""English renderings of a conjugated Spanish verb, for the Tense Quest
conjugation prompts ("nosotros + comer" → "We eat").

This is a deliberately small, pragmatic English conjugator — the bar is "clear
enough to translate *from*", not flawless grammar. It only handles the tenses
that actually appear as conjugation/ir-a-inf warmups in the grammar curriculum:
present, present progressive (gerund), near future (ir a + inf), simple past
(preterite), present perfect, and the imperative. Anything else → ``None``.

The English infinitive comes from ``GRAMMAR_WORD_TRANSLATIONS`` ("to eat"); a
small irregular table covers past / past-participle forms for the verbs in that
list. Multi-word glosses ("to ask for", "to have lunch") conjugate the first
word and keep the tail.
"""
from __future__ import annotations

import re
from typing import Optional

from app.data.grammar_situations import GRAMMAR_WORD_TRANSLATIONS

# Spanish subject pronoun → English subject (the (m)/(f) split is dropped).
_SUBJECT = {
    "yo": "I", "tú": "you", "él": "he", "ella": "she", "usted": "you",
    "nosotros": "we", "nosotras": "we", "ellos": "they", "ellas": "they",
    "ustedes": "you all",
}
# Pronouns that take English 3rd-person-singular verb agreement ("she eats").
# `usted` is grammatically 3rd-person in Spanish but maps to English "you" → "eat".
_THIRD_SG = {"él", "ella"}
# Pronouns that take "was" rather than "were" for the verb *to be*.
_BE_WAS = {"yo", "él", "ella"}

# base infinitive → (simple past, past participle). Anything not here is regular.
_IRREGULAR = {
    "be": ("was", "been"),  # `was`/`were` is fixed up per-pronoun below
    "begin": ("began", "begun"),
    "bring": ("brought", "brought"),
    "build": ("built", "built"),
    "choose": ("chose", "chosen"),
    "come": ("came", "come"),
    "do": ("did", "done"),
    "eat": ("ate", "eaten"),
    "fall": ("fell", "fallen"),
    "find": ("found", "found"),
    "get": ("got", "gotten"),
    "give": ("gave", "given"),
    "go": ("went", "gone"),
    "have": ("had", "had"),
    "hear": ("heard", "heard"),
    "know": ("knew", "known"),
    "leave": ("left", "left"),
    "put": ("put", "put"),
    "read": ("read", "read"),
    "say": ("said", "said"),
    "see": ("saw", "seen"),
    "sing": ("sang", "sung"),
    "sleep": ("slept", "slept"),
    "speak": ("spoke", "spoken"),
    "think": ("thought", "thought"),
    "understand": ("understood", "understood"),
    "write": ("wrote", "written"),
}
# Short verbs whose -ing / -ed forms double the final consonant.
_DOUBLERS = {"put", "get", "begin", "sit", "run", "stop", "plan", "set"}

_TENSES = {"present", "gerund", "ir_a_infinitive", "preterite", "perfect", "imperative"}


def _base(verb_es: str) -> Optional[str]:
    """English infinitive base for a Spanish infinitive: 'comer' → 'eat',
    'hacer' → 'do', 'almorzar' → 'have lunch'. None if unknown."""
    en = GRAMMAR_WORD_TRANSLATIONS.get(verb_es)
    if not en:
        return None
    en = en.strip()
    if en.lower().startswith("to "):
        en = en[3:]
    en = en.split("/")[0]  # 'do/make' → 'do'
    en = re.sub(r"\s*\([^)]*\)", "", en).strip()  # drop '(permanent)' etc.
    return en or None


def _split(base: str) -> tuple[str, str]:
    """First word + the rest ('have lunch' → ('have', ' lunch'))."""
    parts = base.split(" ", 1)
    return parts[0], (" " + parts[1] if len(parts) > 1 else "")


def _add_s(w: str) -> str:
    if w == "have":
        return "has"
    if w in ("go", "do"):
        return w + "es"
    if w.endswith(("s", "x", "z", "ch", "sh")):
        return w + "es"
    if len(w) > 1 and w.endswith("y") and w[-2] not in "aeiou":
        return w[:-1] + "ies"
    return w + "s"


def _gerund(w: str) -> str:
    if w == "be":
        return "being"
    if w.endswith("ie"):
        return w[:-2] + "ying"
    if w.endswith("ee"):
        return w + "ing"
    if w.endswith("e"):
        return w[:-1] + "ing"
    if w in _DOUBLERS:
        return w + w[-1] + "ing"
    return w + "ing"


def _regular_ed(w: str) -> str:
    if w.endswith("e"):
        return w + "d"
    if len(w) > 1 and w.endswith("y") and w[-2] not in "aeiou":
        return w[:-1] + "ied"
    if w in _DOUBLERS:
        return w + w[-1] + "ed"
    return w + "ed"


def _past(w: str, pronoun: str) -> str:
    if w == "be":
        return "was" if pronoun in _BE_WAS else "were"
    if w in _IRREGULAR:
        return _IRREGULAR[w][0]
    return _regular_ed(w)


def _participle(w: str) -> str:
    if w == "be":
        return "been"
    if w in _IRREGULAR:
        return _IRREGULAR[w][1]
    return _regular_ed(w)


def _be_present(pronoun: str) -> str:
    if pronoun == "yo":
        return "am"
    if pronoun in _THIRD_SG:
        return "is"
    return "are"


def _have_present(pronoun: str) -> str:
    return "has" if pronoun in _THIRD_SG else "have"


def _cap(s: str) -> str:
    return s[0].upper() + s[1:] if s else s


def english_for(verb_es: str, pronoun: str, tense: Optional[str]) -> Optional[str]:
    """A natural English rendering of `verb_es` conjugated for `pronoun` in
    `tense` — e.g. ('comer', 'nosotros', 'present') → 'We eat'. None if the verb
    or tense isn't covered."""
    if tense not in _TENSES:
        return None
    base = _base(verb_es)
    if not base:
        return None
    w0, tail = _split(base)
    third = pronoun in _THIRD_SG
    subj = _SUBJECT.get(pronoun, pronoun)

    if tense == "imperative":
        if pronoun in ("nosotros", "nosotras"):
            return _cap(f"let's {base}")
        return _cap(base) + "!"

    if tense == "present":
        if w0 == "be":
            return _cap(f"{subj} {_be_present(pronoun)}{tail}")
        head = _add_s(w0) if third else w0
        return _cap(f"{subj} {head}{tail}")

    if tense == "gerund":
        return _cap(f"{subj} {_be_present(pronoun)} {_gerund(w0)}{tail}")

    if tense == "ir_a_infinitive":
        return _cap(f"{subj} {_be_present(pronoun)} going to {base}")

    if tense == "preterite":
        return _cap(f"{subj} {_past(w0, pronoun)}{tail}")

    if tense == "perfect":
        return _cap(f"{subj} {_have_present(pronoun)} {_participle(w0)}{tail}")

    return None
