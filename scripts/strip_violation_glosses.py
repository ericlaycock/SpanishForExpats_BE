"""Audit + rewrite every glosses dict in app/data/grammar_situations.py
to enforce the canonical drill-gloss rule:

  Glosses cover ONLY nouns, adjectives, and adverbs. Verb forms (any tense,
  including copulas/auxiliaries/gerunds/infinitives) and pronouns
  (subject/object/reflexive) are NEVER glossed. Articles and pure-glue
  prepositions are also excluded.

We use gpt-4.1-mini to classify each gloss entry against the sentence
context, since hand-coding a complete verb-form list is brittle (the file
spans every Spanish tense and irregular paradigm).

Idempotent: running again on already-clean data is a no-op.

Cost: ~140 calls × ~400 input + 100 output tokens ≈ $0.02 with gpt-4.1-mini.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.config import settings  # noqa: E402
from openai import OpenAI  # noqa: E402

TARGET = ROOT / "app" / "data" / "grammar_situations.py"
MODEL = "gpt-4.1-mini"

SYSTEM_PROMPT = """You audit `glosses` dicts in Spanish grammar drill sentences.

THE RULE
========
Glosses MUST contain entries for every noun, adjective, and adverb in the sentence.
Glosses MUST NOT contain entries whose key is one of these forbidden categories:

  FORBIDDEN — drop these from glosses:
  - VERB FORMS in any tense or mood: am/is/are/was/were/be/been; soy/eres/es/somos/son/era/fue; speaks/spoke; habla/hablaba; eating/comiendo; to live/vivir; have/has/had/haber/he/has/ha/hemos/han; modal helpers (have to/tengo que, need to/necesito, going to/voy a)
  - PRONOUNS: I/you/he/she/we/they; yo/tú/él/ella/usted/nosotros/nosotras/ellos/ellas/ustedes; me/te/se/lo/la/le/nos/los/las/les
  - ARTICLES: the/a/an; el/la/los/las/un/una/unos/unas
  - PURE-GLUE PREPOSITIONS standing alone: to/of/in/with/for; a/de/en/con/por/para

  KEEP — every entry whose key is one of these belongs in glosses:
  - NOUNS: trucks/camiones, water/agua, book/libro, country/campo, music/música, news/noticia, song/canción, message/mensaje, store/tienda
  - ADJECTIVES: tall/alto, happy/feliz, important/importante, elegant/elegante, sociable/social, professional/profesional, international/internacional, Latin/latina, Colombian/colombiana, sick/enfermo, ready/listo
  - ADVERBS: fast/rápido, quickly/rápidamente, well/bien, carefully/atentamente, loudly/alto, often/a menudo, far away/lejos, nearby/cerca, here/aquí, together/juntos
  - MULTI-WORD NOUN/ADJ/ADV PHRASES that translate as a unit: "out loud / en voz alta", "a lot / mucho", "at home / en casa"

EXAMPLES
========

Example 1 — adjective sentence
  en: "He is important", es: "Él es importante"
  current: {"is": "es", "important": "importante", "es": "is", "importante": "important"}
  corrected: {"important": "importante", "importante": "important"}
  reason: removed `is`/`es` (verb), kept `important`/`importante` (adjective)

Example 2 — copula + nationality adjective
  en: "We are Colombian", es: "Nosotros somos colombianos"
  current: {"are": "somos", "Colombian": "colombianos", "somos": "are", "colombianos": "Colombian"}
  corrected: {"Colombian": "colombianos", "colombianos": "Colombian"}

Example 3 — verb + noun + adverb
  en: "The trucks move quickly", es: "Los camiones mueven rápidamente"
  current: {"trucks": "camiones", "move": "mueven", "quickly": "rápidamente", "camiones": "trucks", "mueven": "move", "rápidamente": "quickly"}
  corrected: {"trucks": "camiones", "quickly": "rápidamente", "camiones": "trucks", "rápidamente": "quickly"}

Example 4 — only verbs and pronouns
  en: "We are going to study", es: "Vamos a estudiar"
  current: {"going": "vamos", "study": "estudiar"}
  corrected: {}
  reason: every word is verb/pronoun/article/preposition; glosses can be empty

Example 5 — already clean (idempotent)
  en: "I drink water", es: "Yo bebo agua"
  current: {"water": "agua", "agua": "water"}
  corrected: {"water": "agua", "agua": "water"}

OUTPUT FORMAT
=============
Return JSON only: {"glosses": {<corrected bidirectional dict>}}.
Bidirectional invariant: if you keep "X": "Y", you must also keep "Y": "X" (or add it).
If a key isn't clearly a noun/adjective/adverb in the sentence context, default to DROPPING it.
"""

USER_TMPL = """Sentence:
- en: {en}
- es: {es}

Current glosses (may contain violations):
{current}

Return the corrected glosses dict per the rule. JSON only."""


def find_drill_sentences(src: str):
    """Yield (start, end, en, es, glosses_inner_str) for every drill sentence
    that has a single-line `"glosses": {...}` block."""
    # Match a single-line drill_sentence dict literal.
    # This is brittle but the file uses a uniform single-line layout for
    # drill_sentences entries (one per line).
    pattern = re.compile(
        r'\{"en":\s*"([^"]+)",\s*"es":\s*"([^"]+)",[^}]*?"glosses":\s*\{([^{}]*)\}',
        re.DOTALL,
    )
    for m in pattern.finditer(src):
        yield m.start(3), m.end(3), m.group(1), m.group(2), m.group(3)


def fmt_glosses(d: dict[str, str]) -> str:
    return ", ".join(f'"{k}": "{v}"' for k, v in d.items())


def parse_glosses_inner(inner: str) -> dict[str, str]:
    pairs = re.findall(r'"([^"]+)":\s*"([^"]+)"', inner)
    return {k: v for k, v in pairs}


def audit_one(client: OpenAI, en: str, es: str, current: dict[str, str]) -> dict[str, str]:
    if not current:
        return {}
    user_prompt = USER_TMPL.format(en=en, es=es, current=json.dumps(current, ensure_ascii=False))
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0,
        response_format={"type": "json_object"},
    )
    content = resp.choices[0].message.content or "{}"
    parsed = json.loads(content)
    return parsed.get("glosses", {})


def main(limit: int | None = None) -> int:
    client = OpenAI(api_key=settings.openai_api_key)
    src = TARGET.read_text()

    matches = list(find_drill_sentences(src))
    print(f"Found {len(matches)} drill sentences with glosses")
    if limit is not None:
        matches = matches[:limit]
        print(f"(limited to first {len(matches)} for this run)")

    # Apply edits in reverse order so earlier offsets stay valid.
    edits: list[tuple[int, int, str]] = []
    changed = 0
    cleaned = 0
    skipped = 0

    for i, (start, end, en, es, inner) in enumerate(matches, 1):
        current = parse_glosses_inner(inner)
        if not current:
            skipped += 1
            continue
        try:
            corrected = audit_one(client, en, es, current)
        except Exception as e:
            print(f"  [{i}/{len(matches)}] FAIL en={en!r}: {e}")
            skipped += 1
            continue
        # Sanity: bidirectional check
        for k, v in list(corrected.items()):
            if v not in corrected:
                corrected[v] = k
        if corrected == current:
            cleaned += 1
            print(f"  [{i}/{len(matches)}] clean: {en}")
            continue
        new_inner = fmt_glosses(corrected)
        edits.append((start, end, new_inner))
        changed += 1
        removed = set(current) - set(corrected)
        print(f"  [{i}/{len(matches)}] FIX {en!r} — removed: {sorted(removed)}")

    # Apply edits in reverse order
    out = src
    for start, end, new_inner in reversed(edits):
        out = out[:start] + new_inner + out[end:]
    TARGET.write_text(out)

    print()
    print(f"Done. changed={changed}, already clean={cleaned}, skipped={skipped}")
    return 0


if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else None
    raise SystemExit(main(limit))
