"""Shared clean-word filter for vocab module generation.

The HF corpus (app/data/hf_words.py) was bulk-appended from an OpenSubtitles
frequency list, so past rank ~989 it is heavily polluted with:

  * proper names        — "mary", "steve", "jimmy"  (subtitle character names)
  * conjugated verbs    — "estarás", "perdí", "hagan", "oí"
  * interjections/slang — "nena", "diablo"

Vocab modules must only ever teach citation forms: nouns, adjectives, adverbs,
and *infinitive* verbs. This module is the single source of truth for that
judgement so the generator and its tests agree.

The English gloss is a far stronger signal than Spanish morphology alone —
"ama" is ambiguous (noun "mistress" vs. verb "he/she loves") but its gloss
"he/she loves" is not. So every rule below leans on the gloss first.
"""

from __future__ import annotations

import re
import unicodedata

# ---------------------------------------------------------------- categories

POS_NOUN = "noun"
POS_ADJECTIVE = "adjective"
POS_ADVERB = "adverb"
POS_VERB = "verb"  # infinitive only — never a conjugated form

# Reasons a candidate is rejected. Surfaced in the generator's audit report so a
# human can eyeball *why* the corpus shrank, rather than trusting a bare count.
REJECT_PROPER_NAME = "proper_name"
REJECT_CONJUGATED = "conjugated_verb"
REJECT_FUNCTION_WORD = "function_word"
REJECT_INTERJECTION = "interjection"
REJECT_MULTIWORD = "multiword"
REJECT_TOO_SHORT = "too_short"
REJECT_NO_GLOSS = "no_gloss"

# ------------------------------------------------------------------ patterns

# A gloss that opens with a subject pronoun is a finite verb, not a lemma.
# "he/she loves", "I lost", "you carry", "it will last", "they do".
_FINITE_GLOSS = re.compile(
    r"^(i|you|he|she|it|we|they|he/she|s?he)\b"
    r"|^(i'm|you're|he's|she's|it's|we're|they're)\b",
    re.I,
)

# Imperatives and subjunctives that the gloss renders without a pronoun.
_IMPERATIVE_GLOSS = re.compile(
    r"^(let's|help me|give me|tell me|come on|look|listen|wait)\b", re.I
)

# A bare English command, used to confirm an enclitic-imperative reading.
# Morphology alone cannot do this: "déjalo" and "película" are both
# stress-shifted words ending in a clitic-shaped syllable, and so are
# "miércoles", "artículo", "célula". The gloss is what separates them.
_COMMAND_GLOSS = re.compile(
    r"^(leave|help|tell|give|take|call|bring|put|let|do|make|come|go|say|show"
    r"|send|buy|find|stop|wait|look|listen|forgive|excuse|hold|keep|move|open"
    r"|close|follow|watch|remember|forget|try|use|write|read|eat|drink|calm|hurry|relax|sit|stand|hold on|shut|get)\b",
    re.I,
)

# An infinitive gloss: "to speak", "to be (essence)".
_INFINITIVE_GLOSS = re.compile(r"^to\s+\w", re.I)

# Conditional / imperfect glosses that carry no subject pronoun and so slip past
# _FINITE_GLOSS: "podría"->"could", "había"->"there was", "tenía"->"had".
# These matter because -ía had to be dropped from the morphology list to save
# the -ería noun family (ferretería, panadería, sequía).
_PAST_MODAL_GLOSS = re.compile(
    r"^(could|would|should|might|must|had|has been|was|were|there (was|were|is|are))\b",
    re.I,
)

# Abbreviations ("sr.", "dr.", "ud.") are corpus artefacts, not vocabulary.
_ABBREVIATION = re.compile(r"\.")

# Spanish infinitive surface form.
# Accented stems (oír, reír, freír) are infinitives too.
_INFINITIVE_ES = re.compile(r"[aeiáéí]r$")

# Finite endings consulted ONLY when the gloss is inconclusive. This list is
# deliberately conservative: many Spanish noun/adjective endings collide with
# verb endings, and a false reject silently starves a deck. Excluded on purpose:
#   -ía   → sequía, cirugía, tubería, ferretería, lejía, encía   (noun -ería)
#   -ara  → lámpara, cuchara, cámara
#   -án   → huracán, alemán, capitán
#   -én   → almacén, andén
#   -ás/-és/-ís → interés, país, inglés, francés, además
#   -é/-í → café, bebé, colibrí
# Those are all caught by the gloss rules above when they really are verbs.
#   -ería/-aría → ferretería, panadería, secretaría (vs. conditional "comería")
#   -amos/-emos/-imos → primos, ramos, amos      (vs. "vivimos")
# Conditionals and 1st-person plurals are always caught by the gloss rules, so
# dropping them here costs nothing and saves a pile of real nouns.
_FINITE_ES = re.compile(
    r"(ó|aré|eré|iré|ará|erá|irá|aba|abas|ábamos|aban"
    r"|íamos|ían|aron|ieron|aste|iste|ase|iese|áis|éis)$"
)

_GERUND_ES = re.compile(r"(ando|iendo|yendo)$")

# Past participles share their ending with plenty of ordinary nouns
# ("abogado", "comida"), so -ado/-ido alone proves nothing. The tell is a bare
# "-ed" gloss: "matado" -> "killed". A handful of participles have fully
# lexicalised into everyday adjectives, and those we do want to teach.
_PARTICIPLE_ES = re.compile(r"(ado|ido|ada|ida|aído|eído)$")
_PARTICIPLE_GLOSS = re.compile(r"^\w+ed$", re.I)

# English past participles that do not end in -ed, so _PARTICIPLE_GLOSS misses
# them: "traído"->"brought", "ganado"->"won", "tomado"->"taken".
_IRREGULAR_PARTICIPLE_GLOSS = {
    "brought", "taken", "won", "given", "seen", "done", "made", "said", "gone",
    "come", "put", "found", "left", "kept", "held", "told", "sent", "met",
    "paid", "lost", "built", "sold", "bought", "caught", "taught", "thought",
    "written", "driven", "eaten", "fallen", "forgotten", "gotten", "known",
    "shown", "spoken", "broken", "chosen", "frozen", "stolen", "worn", "run",
    "read", "heard", "understood", "become", "begun", "drunk", "sung", "swum",
}

_PARTICIPIAL_ADJECTIVES = {
    "cansado", "cansada", "casado", "casada", "ocupado", "ocupada",
    "enojado", "enojada", "perdido", "perdida", "aburrido", "aburrida",
    "preocupado", "preocupada", "sentado", "sentada", "acostado", "acostada",
    "dormido", "dormida", "callado", "callada", "mojado", "mojada",
    "helado", "helada", "pasado", "pasada", "querido", "querida",
    "prohibido", "prohibida", "complicado", "complicada", "equivocado",
    "equivocada", "emocionado", "emocionada", "asustado", "asustada",
}

# Closed-class words. Useful for grammar drills, dead weight in a vocab deck —
# a learner does not "study" `de` as a flashcard.
_FUNCTION_WORDS = {
    "de", "que", "y", "a", "en", "el", "la", "los", "las", "un", "una", "unos",
    "unas", "lo", "al", "del", "se", "su", "sus", "mi", "mis", "tu", "tus",
    "me", "te", "nos", "le", "les", "por", "para", "con", "sin", "o", "u",
    "e", "ni", "pero", "sino", "si", "no", "sí", "es", "son", "era", "fue",
    "ha", "he", "han", "has", "hay", "más", "menos", "muy", "ya", "también",
    "porque", "como", "cuando", "donde", "quien", "cual", "cuyo", "este",
    "esta", "estos", "estas", "ese", "esa", "esos", "esas", "aquel", "aquella",
    "yo", "tú", "él", "ella", "usted", "ustedes", "ellos", "ellas", "nosotros",
    "nosotras",
}

# Subtitle-corpus noise: interjections, vocatives, profanity, filler.
_INTERJECTIONS = {
    "nena", "nene", "diablo", "diablos", "carajo", "joder", "mierda", "coño",
    "vaya", "oye", "eh", "ah", "oh", "uh", "mmm", "wow", "guau", "ay", "uy",
    "hola", "adiós", "bueno", "pues", "vale", "okay", "ok", "sí", "no",
    "jesús", "dios", "cielos", "vamos", "anda", "venga",
    # transcription filler that the subtitle corpus preserves verbatim
    "um", "uhm", "ehm", "mm", "hmm", "aja", "ajá", "eeh", "este",
}

# Imperative + enclitic pronoun: "déjalo", "ayúdame", "dímelo", "cuéntame".
# Spanish only writes an accent on these because attaching the clitic pushed the
# stress back, so "written accent + trailing clitic" is a reliable tell that the
# word is a command rather than a lemma.
_CLITIC_IMPERATIVE = re.compile(
    r"[áéíóú]\w*(me|te|se|lo|la|le|nos|los|las|les)(lo|la|le|los|las)?$"
)

# Insults and slurs. The corpus is subtitle-derived, so it is full of them, and
# "imbécil" surfacing on a flashcard for a paying learner is not acceptable.
_OFFENSIVE = {
    "imbécil", "idiota", "estúpido", "estúpida", "tonto", "tonta", "maldito",
    "maldita", "bastardo", "perra", "puta", "puto", "cabrón", "pendejo",
    "gilipollas", "capullo", "cretino", "asqueroso", "asquerosa", "basura",
    "infierno", "demonio", "matar", "muerte", "muerto", "muerta", "asesino",
    "asesinato", "arma", "pistola", "disparar", "sangre", "borracho",
}

# LATAM-only: the peninsular vosotros paradigm must never reach a learner.
# `-ís` is deliberately absent — it would swallow "país", and the verb forms it
# would catch ("vivís") are already rejected by their pronoun-led gloss.
_VOSOTROS = re.compile(r"(áis|éis)$|^os$|aos$")


def _strip_accents(text: str) -> str:
    decomposed = unicodedata.normalize("NFD", text)
    return "".join(c for c in decomposed if unicodedata.category(c) != "Mn")


# English capitalises these categories, but they are ordinary Spanish words and
# must survive the single-capitalised-gloss rule below.
_CAPITALISED_IN_ENGLISH_ONLY = {
    # days
    "lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo",
    # months
    "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
    "septiembre", "setiembre", "octubre", "noviembre", "diciembre",
    # languages / nationalities
    "español", "española", "inglés", "inglesa", "francés", "francesa",
    "alemán", "alemana", "italiano", "italiana", "portugués", "portuguesa",
    "chino", "china", "japonés", "japonesa", "americano", "americana",
    "colombiano", "colombiana", "mexicano", "mexicana", "argentino",
    "argentina", "peruano", "peruana", "chileno", "chilena", "brasileño",
    "brasileña", "europeo", "europea", "latino", "latina",
    # religion / holidays that gloss as capitalised nouns
    "navidad", "pascua", "católico", "cristiano",
}


def _looks_like_proper_name(spanish: str, english: str) -> bool:
    """Detect subtitle character and place names.

    The corpus is film dialogue, so it is dense with them: "mary" -> "Mary
    (name)", "londres" -> "London". Any single capitalised English gloss is
    treated as a proper noun unless the Spanish word belongs to a category that
    English capitalises but Spanish does not (weekdays, months, nationalities).
    """
    if "(name)" in english.lower():
        return True
    gloss = english.strip()
    if not gloss or " " in gloss or not gloss[0].isupper():
        return False
    if spanish.strip().lower() in _CAPITALISED_IN_ENGLISH_ONLY:
        return False
    # A capitalised one-word gloss on a lowercase Spanish entry: "London",
    # "Piper", "Steve". Acronyms the learner really does need (PIN, SSID) are
    # spelled uppercase in Spanish too, so they are exempt.
    return not spanish.isupper()


def classify(
    spanish: str, english: str, *, allow_multiword: bool = False
) -> tuple[str | None, str | None]:
    """Return ``(pos, reject_reason)`` — exactly one of the two is non-None.

    ``pos`` is one of POS_NOUN / POS_ADJECTIVE / POS_ADVERB / POS_VERB when the
    entry is safe to teach. Otherwise ``pos`` is None and ``reject_reason``
    explains the drop.

    ``allow_multiword`` admits noun phrases such as "número de reserva" or
    "fecha de vencimiento". Situation decks want these — they are the useful
    unit at a check-in counter. Frequency-band decks do not, because a rank is
    defined over single tokens. Full sentences and questions are rejected in
    either mode.
    """
    es = (spanish or "").strip()
    en = (english or "").strip()

    if not en:
        return None, REJECT_NO_GLOSS
    if not es or len(es) < 2:
        return None, REJECT_TOO_SHORT
    if _ABBREVIATION.search(es):
        return None, REJECT_TOO_SHORT
    if " " in es:
        # A question or a sentence is not a vocabulary item in any mode.
        is_sentence = es.startswith("¿") or es.endswith("?") or len(es.split()) > 4
        if not allow_multiword or is_sentence:
            return None, REJECT_MULTIWORD
        # Judge a noun phrase by its head word, which in Spanish comes first.
        head = es.split()[0].lower()
        if head in _FUNCTION_WORDS or head in _INTERJECTIONS:
            return None, REJECT_FUNCTION_WORD
        if _FINITE_GLOSS.match(en) or _IMPERATIVE_GLOSS.match(en):
            return None, REJECT_CONJUGATED
        return POS_NOUN, None

    lower = es.lower()

    if _looks_like_proper_name(es, en):
        return None, REJECT_PROPER_NAME
    if lower in _FUNCTION_WORDS:
        return None, REJECT_FUNCTION_WORD
    if lower in _INTERJECTIONS:
        return None, REJECT_INTERJECTION
    if lower in _OFFENSIVE:
        return None, REJECT_INTERJECTION
    if _VOSOTROS.search(lower):
        return None, REJECT_CONJUGATED
    # Only an imperative-shaped gloss confirms the enclitic reading; without
    # it "película" and "miércoles" would be dropped as commands.
    if _CLITIC_IMPERATIVE.search(lower) and _COMMAND_GLOSS.match(en):
        return None, REJECT_CONJUGATED

    # --- verbs -----------------------------------------------------------
    # An infinitive gloss + infinitive surface form is the only accepted verb.
    if _INFINITIVE_GLOSS.match(en):
        if _INFINITIVE_ES.search(lower):
            return POS_VERB, None
        # "to X" gloss on a non-infinitive surface form = conjugated ("durará").
        return None, REJECT_CONJUGATED

    # A pronoun-led, imperative, or conditional/imperfect gloss is a finite verb
    # regardless of spelling.
    if _FINITE_GLOSS.match(en) or _IMPERATIVE_GLOSS.match(en):
        return None, REJECT_CONJUGATED
    if _PAST_MODAL_GLOSS.match(en):
        return None, REJECT_CONJUGATED

    # Gloss was inconclusive — fall back to Spanish morphology.
    if _GERUND_ES.search(lower):
        return None, REJECT_CONJUGATED
    if _FINITE_ES.search(lower) and not _INFINITIVE_ES.search(lower):
        return None, REJECT_CONJUGATED
    # Past participle used as a verb form ("matado" -> "killed"), as opposed to
    # one that has lexicalised into an adjective ("cansado" -> "tired").
    if (
        _PARTICIPLE_ES.search(lower)
        and _PARTICIPLE_GLOSS.match(en)
        and lower not in _PARTICIPIAL_ADJECTIVES
    ):
        return None, REJECT_CONJUGATED
    # A gloss may carry several senses ("cattle; won"). Only the first one
    # decides, since that is the reading the learner is being taught.
    first_sense = re.split(r"[;,]", en)[0].strip().lower()
    if (
        first_sense in _IRREGULAR_PARTICIPLE_GLOSS
        and lower not in _PARTICIPIAL_ADJECTIVES
        and (_PARTICIPLE_ES.search(lower) or lower.endswith(("to", "cho")))
    ):
        return None, REJECT_CONJUGATED

    # --- non-verbs -------------------------------------------------------
    if lower.endswith("mente"):
        return POS_ADVERB, None
    # Adjective gloss heuristics: glosses that read as a bare quality.
    if re.match(r"^(very\s+)?\w+$", en) and lower.endswith(("oso", "osa", "able", "ible", "ivo", "iva")):
        return POS_ADJECTIVE, None

    return POS_NOUN, None


def is_clean(spanish: str, english: str) -> bool:
    pos, _ = classify(spanish, english)
    return pos is not None
