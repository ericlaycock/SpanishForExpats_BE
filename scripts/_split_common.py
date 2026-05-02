"""Shared helpers for split_glX.py scripts (Phase C.3).

Each split_glN script imports from this module to:
  - call gpt-4.1-mini in parallel to author 10 drill sentences per drill
  - emit intro/drill/chat lesson Python literals
  - apply strict gloss + (m)/(f) marking rules

Pipe-encoding for conjugations is supplied by each caller via ANSWERS dict.
"""
from __future__ import annotations
import asyncio
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.config import settings  # noqa: E402
from openai import AsyncOpenAI  # noqa: E402

MODEL = "gpt-4.1-mini"
CONCURRENCY = 6
MAX_RETRIES = 6

# Diverse pronoun lists honoring "include feminine/formal" memory
DIVERSE_PRONOUNS = ["yo", "tú", "ella", "nosotras", "ustedes",
                    "él", "ella", "usted", "nosotros", "ellos"]
DIVERSE_PRONOUNS_2 = ["tú", "yo", "él", "nosotros", "ellas",
                      "usted", "ellos", "ella", "nosotras", "ustedes"]

ALL_PRONOUNS = ["yo", "tú", "él", "ella", "usted",
                "nosotros", "nosotras", "ellos", "ellas", "ustedes"]


# ── LLM authoring ────────────────────────────────────────────────────────────

SENTENCE_SYSTEM = """You author Spanish A1/A2 drill sentence pairs (English + Spanish).

GLOSS RULE — strict, no exceptions:
- Each sentence's `glosses` dict contains ONLY nouns, adjectives, and adverbs.
- Verb forms (any tense, any verb in the sentence), pronouns (subject/object/reflexive), articles, and pure-glue prepositions are NEVER glossed.
- Glosses are bidirectional: if "X":"Y", then "Y":"X" too.
- If a sentence has no glossable noun/adj/adv content, return empty {} for that sentence's glosses.

Examples:
  "I am tall" / "Yo soy alto" → {"tall":"alto","alto":"tall"}
  "He is at home" / "Él está en casa" → {"home":"casa","casa":"home"}
  "We go to the store" / "Nosotros vamos a la tienda" → {"store":"tienda","tienda":"store"}

PRODUCTION RULES:
- Short, natural A1/A2 sentences (3-7 words English).
- Use the target verb in the conjugation indicated for each sentence (in the TARGET TENSE that the user specifies).
- Mix subjects diversely: include ella/ellas/nosotras/usted/ustedes — NOT just masculine.
- When ES uses Nosotros/Ellos, EN must say "We (m)" / "They (m)".
- When ES uses Nosotras/Ellas, EN must say "We (f)" / "They (f)".
- Type alternates "written" / "auditory" — caller specifies.
- Spanish must be natural, register-appropriate, no awkward word-for-word.

OUTPUT: JSON only, format {"sentences": [{"en":"...", "es":"...", "type":"...", "glosses":{...}}, ...]}.
No commentary, no code fences."""


USER_TMPL = """Author 10 drill sentences for a Spanish {tense_label} drill.

Verbs to drill: {verbs}
Verb glosses (do not include in sentence glosses): {verb_glosses}
Target tense / construction: {tense_desc}

For each sentence, I'll specify the (verb, pronoun, type) tuple. Distribute as listed:

{spec}

Return JSON: {{"sentences": [...]}} in the order I listed."""


def make_user_prompt(verbs: list[str], verb_gloss_en: dict,
                     spec_rows: list[tuple[str, str, str]],
                     tense_label: str, tense_desc: str) -> str:
    lines = []
    for i, (verb, pronoun, t) in enumerate(spec_rows, 1):
        lines.append(f'  {i}. verb={verb}, pronoun={pronoun}, type={t}')
    return USER_TMPL.format(
        tense_label=tense_label,
        tense_desc=tense_desc,
        verbs=", ".join(verbs),
        verb_glosses=", ".join(f"{v}={verb_gloss_en[v]}" for v in verbs),
        spec=chr(10).join(lines),
    )


async def author_sentences(client: AsyncOpenAI, sem: asyncio.Semaphore,
                            verbs: list[str], verb_gloss_en: dict,
                            spec_rows: list[tuple[str, str, str]],
                            tense_label: str, tense_desc: str):
    async with sem:
        for attempt in range(MAX_RETRIES):
            try:
                resp = await client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {"role": "system", "content": SENTENCE_SYSTEM},
                        {"role": "user", "content": make_user_prompt(
                            verbs, verb_gloss_en, spec_rows, tense_label, tense_desc)},
                    ],
                    temperature=0.5,
                    response_format={"type": "json_object"},
                )
                content = resp.choices[0].message.content or "{}"
                parsed = json.loads(content)
                sents = parsed.get("sentences", [])
                # Bidirectional gloss sanity
                for s in sents:
                    g = s.get("glosses", {}) or {}
                    for k, v in list(g.items()):
                        if v not in g:
                            g[v] = k
                    s["glosses"] = g
                return sents
            except Exception as e:
                msg = str(e)
                if "429" in msg or "rate_limit" in msg.lower():
                    await asyncio.sleep((2 ** attempt) + 0.5)
                    continue
                return [{"__ERROR__": msg}]
        return [{"__ERROR__": "max retries"}]


# ── Drill spec distribution ─────────────────────────────────────────────────

def make_drill_spec(verb: str, drill_idx: int) -> list[tuple[str, str, str]]:
    """Return (verb, pronoun, type) for 5 sentences using verb."""
    pronouns = DIVERSE_PRONOUNS if drill_idx == 1 else DIVERSE_PRONOUNS_2
    return [(verb, pronouns[i], "written" if i % 2 == 0 else "auditory") for i in range(5)]


# ── Code emit helpers ───────────────────────────────────────────────────────

def fmt_answers_block(verb: str, ans: dict, pronouns: list[str] | None = None) -> str:
    """Format full pronoun-keyed answer dict for drill_config.answers."""
    if pronouns is None:
        pronouns = ALL_PRONOUNS
    items = [f'"{p}": "{ans[p]}"' for p in pronouns if p in ans]
    return f'                "{verb}": {{{", ".join(items)}}}'


def fmt_sentence_lit(sentences: list[dict]) -> list[str]:
    out = []
    for s in sentences:
        glosses = s.get("glosses", {}) or {}
        gloss_pairs = ", ".join(f'"{k}": "{v}"' for k, v in glosses.items())
        out.append(
            '            {{"en": "{en}", "es": "{es}", "noun_id": None, '
            '"type": "{t}", "glosses": {{{g}}}}},'.format(
                en=s["en"].replace('"', '\\"'),
                es=s["es"].replace('"', '\\"'),
                t=s.get("type", "written"),
                g=gloss_pairs,
            )
        )
    return out


def emit_mini_table(verb: str, ans: dict, gloss_en: str,
                    pronoun_rows: list[tuple[str, str]] | None = None) -> str:
    """Render a mini_table card. pronoun_rows is list of (label, key) defaulting to 5-row collapsed."""
    if pronoun_rows is None:
        pronoun_rows = [
            ("yo", "yo"), ("tú", "tú"),
            ("él / ella / usted", "él"),
            ("nosotros / nosotras", "nosotros"),
            ("ellos / ellas / ustedes", "ellos"),
        ]
    rows_lit = ",\n            ".join(
        f'["{label}", "{ans[key]}"]' for label, key in pronoun_rows if key in ans
    )
    return f'''        {{
            "kind": "mini_table",
            "title": "{verb} ({gloss_en})",
            "rows": [
            {rows_lit},
            ],
        }}'''


def emit_recall_list(verbs: list[str], answers_by_verb: dict,
                     pronoun_keys: list[str] | None = None) -> str:
    """Emit the new list-form recall: [{"verb": v, "answers": {...}}, ...]."""
    if pronoun_keys is None:
        pronoun_keys = ["yo", "tú", "él", "nosotros", "ellos"]
    items = []
    for v in verbs:
        a = answers_by_verb[v]
        pairs = ", ".join(f'"{p}": "{a[p]}"' for p in pronoun_keys if p in a)
        items.append(f'        {{"verb": "{v}", "answers": {{{pairs}}}}}')
    return "    \"recall\": [\n" + ",\n".join(items) + ",\n    ],"
