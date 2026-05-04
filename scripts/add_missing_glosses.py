"""Add a `glosses` dict to every drill_sentence in app/data/grammar_situations.py
that lacks one. Calls gpt-4.1-mini in parallel via AsyncOpenAI.

Per the canonical drill-gloss rule (docs/learning-flow.md), glosses cover
ONLY nouns / adjectives / adverbs (bidirectional EN↔ES). Verb forms,
pronouns, articles, and pure-glue prepositions are NEVER glossed.

The script:
1. Parses grammar_situations.py via regex to find every drill_sentence dict.
2. Identifies sentences without `glosses` (or with `glosses: {}`).
3. Fires N concurrent LLM calls (default 30) to author glosses for each.
4. Patches the file by inserting `, "glosses": {<dict>}` before the closing
   brace of each affected sentence dict.

Idempotent: re-running on already-glossed sentences is a no-op.
"""
from __future__ import annotations
import asyncio
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.config import settings  # noqa: E402
from openai import AsyncOpenAI  # noqa: E402

TARGET = ROOT / "app" / "data" / "grammar_situations.py"
MODEL = "gpt-4.1-mini"
CONCURRENCY = 8  # gpt-4.1-mini TPM=200k, RPM=500 — keep concurrency modest
MAX_RETRIES = 6

SYSTEM_PROMPT = """You author `glosses` dicts for Spanish grammar drill sentences.

THE RULE (universal, no exceptions)
====================================
Glosses MUST contain entries for every noun, adjective, and adverb in the sentence.
Glosses MUST NOT contain entries for any of these:

  FORBIDDEN:
  - VERB FORMS in any tense or mood: am/is/are/was/were/be/been; soy/eres/es/somos/era/fue; speaks/spoke; habla/hablaba; eating/comiendo; to live/vivir; have/has/had; haber/he/has/ha/hemos/han; modal helpers (have to/tengo que, need to/necesito, going to/voy a)
  - PRONOUNS: I/you/he/she/we/they; yo/tú/él/ella/usted/nosotros/nosotras/ellos/ellas/ustedes; me/te/se/lo/la/le/nos/los/las/les
  - ARTICLES: the/a/an; el/la/los/las/un/una/unos/unas
  - PURE-GLUE PREPOSITIONS standing alone: to/of/in/with/for; a/de/en/con/por/para

  REQUIRED (every one of these in the sentence):
  - NOUNS: trucks/camiones, water/agua, book/libro, country/campo
  - ADJECTIVES: tall/alto, happy/feliz, important/importante
  - ADVERBS: fast/rápido, quickly/rápidamente, well/bien
  - MULTI-WORD NOUN/ADJ/ADV PHRASES that translate as a unit: "out loud"/"en voz alta", "a lot"/"mucho", "at home"/"en casa", "far away"/"lejos"

EVERY entry is BIDIRECTIONAL. If you include "X": "Y", you must also include "Y": "X".
If a sentence has zero noun/adjective/adverb content, return an empty object {}.

EXAMPLES
========

Sentence: en="The trucks move quickly", es="Los camiones mueven rápidamente"
Glosses: {"trucks": "camiones", "quickly": "rápidamente", "camiones": "trucks", "rápidamente": "quickly"}

Sentence: en="I love eating cheese", es="Yo amo comer queso"
Glosses: {"cheese": "queso", "queso": "cheese"}

Sentence: en="He is important", es="Él es importante"
Glosses: {"important": "importante", "importante": "important"}

Sentence: en="We are going to study", es="Vamos a estudiar"
Glosses: {}

Sentence: en="She lives far away", es="Ella vive lejos"
Glosses: {"far away": "lejos", "lejos": "far away"}

Sentence: en="They eat a lot at home", es="Ellos comen mucho en casa"
Glosses: {"a lot": "mucho", "at home": "en casa", "mucho": "a lot", "en casa": "at home"}

OUTPUT FORMAT
=============
Reply with ONLY a JSON object: {"glosses": {<bidirectional dict>}}.
No commentary, no code fences."""

USER_TMPL = """Sentence:
- en: {en}
- es: {es}

Author the glosses dict per the rule. JSON only."""


# Match a single-line drill_sentence dict that has no glosses key.
# We look for `{"en": ..., "es": ..., "noun_id": ..., "type": "..."}` ending
# right before a `}` that's not preceded by glosses.
SENTENCE_RE = re.compile(
    r'\{"en":\s*"([^"]+)",\s*"es":\s*"([^"]+)",\s*"noun_id":\s*(?:None|"[^"]*"),\s*"type":\s*"(?:written|auditory)"(\s*,\s*"glosses":\s*\{[^{}]*\})?\}',
    re.DOTALL,
)


def find_missing_glosses(src: str):
    """Yield (match_obj, en, es) for drill sentences with no glosses or empty glosses."""
    for m in SENTENCE_RE.finditer(src):
        en, es, glosses_part = m.group(1), m.group(2), m.group(3)
        if glosses_part is None:
            yield m, en, es
            continue
        # Has a glosses part — check if empty
        inner = re.search(r"\{([^{}]*)\}", glosses_part).group(1)
        if not inner.strip():
            yield m, en, es


async def author_glosses(client: AsyncOpenAI, sem: asyncio.Semaphore, en: str, es: str):
    async with sem:
        for attempt in range(MAX_RETRIES):
            try:
                resp = await client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": USER_TMPL.format(en=en, es=es)},
                    ],
                    temperature=0,
                    response_format={"type": "json_object"},
                )
                content = resp.choices[0].message.content or "{}"
                parsed = json.loads(content)
                g = parsed.get("glosses", {})
                # Bidirectional sanity
                for k, v in list(g.items()):
                    if v not in g:
                        g[v] = k
                return g
            except Exception as e:
                msg = str(e)
                if "429" in msg or "rate_limit" in msg.lower():
                    delay = (2 ** attempt) + 0.5
                    await asyncio.sleep(delay)
                    continue
                return {"__ERROR__": msg}
        return {"__ERROR__": "max retries exceeded"}


def fmt_glosses(d: dict[str, str]) -> str:
    return ", ".join(f'"{k}": "{v}"' for k, v in d.items())


async def main(limit: int | None = None) -> int:
    client = AsyncOpenAI(api_key=settings.openai_api_key)
    src = TARGET.read_text()

    targets = list(find_missing_glosses(src))
    print(f"Drill sentences missing glosses: {len(targets)}")
    if limit is not None:
        targets = targets[:limit]
        print(f"(limited to first {len(targets)})")

    sem = asyncio.Semaphore(CONCURRENCY)

    # Wrap each task with index so we can show progress + maintain order via gather.
    progress = {"done": 0, "total": len(targets)}

    async def _one(idx: int, en: str, es: str):
        result = await author_glosses(client, sem, en, es)
        progress["done"] += 1
        if progress["done"] % 25 == 0 or progress["done"] == progress["total"]:
            print(f"  ... {progress['done']}/{progress['total']}")
        return result

    results = await asyncio.gather(*[_one(i, en, es) for i, (_, en, es) in enumerate(targets)])

    # Apply patches in reverse offset order so earlier offsets stay valid.
    edits = []
    failed = []
    empty = 0
    authored = 0
    for (m, en, es), gl in zip(targets, results):
        if "__ERROR__" in gl:
            failed.append((en, gl["__ERROR__"]))
            continue
        if not gl:
            empty += 1
        else:
            authored += 1
        # Patch: replace the entire matched sentence with one that has glosses.
        original = m.group(0)
        if m.group(3) is None:
            # No glosses key — insert one before the closing brace
            new_text = original[:-1] + f', "glosses": {{{fmt_glosses(gl)}}}}}'
        else:
            # Has empty glosses key — replace it
            new_text = re.sub(
                r',\s*"glosses":\s*\{[^{}]*\}',
                f', "glosses": {{{fmt_glosses(gl)}}}',
                original,
            )
        edits.append((m.start(), m.end(), new_text))

    out = src
    for start, end, new_text in reversed(edits):
        out = out[:start] + new_text + out[end:]
    TARGET.write_text(out)

    print()
    print(f"Authored: {authored}")
    print(f"Empty (legitimate, no nouns/adj/adv): {empty}")
    print(f"Failed: {len(failed)}")
    if failed:
        print("Sample failures:")
        for en, err in failed[:5]:
            print(f"  - {en!r}: {err}")
    return 0


if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else None
    raise SystemExit(asyncio.run(main(limit)))
