"""Split GL 4 (Irregular Present I) into 3 sub-blocks of 2 verbs each.

Sub-blocks (each = 2 drills + 1 chat):
  - ser + estar (identity vs state)
  - ir + dar (both yo→-oy, both 2-letter infinitives)
  - tener + venir (both yo→-go + e→ie stem change)

Strategy:
  1. Pull existing pipe-encoded answers from build_grammar_lessons.py-style
     hardcoded dicts (the present-tense irregulars are well-known).
  2. Use gpt-4.1-mini in parallel to author 10 drill sentences per drill
     lesson with strict-rule glosses.
  3. Build intro_chart constants programmatically (text cards + mini_tables
     + recall on first verb).
  4. Write output to scripts/_gl4_output.py for inspection, then splice
     into grammar_situations.py replacing the 6 retired GL 4 keys.

Output is reviewable before splice.
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
OUTPUT = ROOT / "scripts" / "_gl4_output.py"
MODEL = "gpt-4.1-mini"
CONCURRENCY = 6
MAX_RETRIES = 6

# ── Pipe-encoded present-tense conjugations for GL 4 verbs ──────────────────

ANSWERS = {
    "ser": {"yo": "|soy", "tú": "|eres", "él": "|es", "ella": "|es", "usted": "|es",
            "nosotros": "|somos", "nosotras": "|somos",
            "ellos": "|son", "ellas": "|son", "ustedes": "|son"},
    "estar": {"yo": "est|oy", "tú": "est|ás", "él": "est|á", "ella": "est|á", "usted": "est|á",
              "nosotros": "est|amos", "nosotras": "est|amos",
              "ellos": "est|án", "ellas": "est|án", "ustedes": "est|án"},
    "ir": {"yo": "|voy", "tú": "|vas", "él": "|va", "ella": "|va", "usted": "|va",
           "nosotros": "|vamos", "nosotras": "|vamos",
           "ellos": "|van", "ellas": "|van", "ustedes": "|van"},
    "dar": {"yo": "d|oy", "tú": "d|as", "él": "d|a", "ella": "d|a", "usted": "d|a",
            "nosotros": "d|amos", "nosotras": "d|amos",
            "ellos": "d|an", "ellas": "d|an", "ustedes": "d|an"},
    "tener": {"yo": "ten|go", "tú": "t|ienes", "él": "t|iene", "ella": "t|iene", "usted": "t|iene",
              "nosotros": "ten|emos", "nosotras": "ten|emos",
              "ellos": "t|ienen", "ellas": "t|ienen", "ustedes": "t|ienen"},
    "venir": {"yo": "ven|go", "tú": "v|ienes", "él": "v|iene", "ella": "v|iene", "usted": "v|iene",
              "nosotros": "ven|imos", "nosotras": "ven|imos",
              "ellos": "v|ienen", "ellas": "v|ienen", "ustedes": "v|ienen"},
}

VERB_GLOSS_EN = {
    "ser": "to be (identity)", "estar": "to be (state)",
    "ir": "to go", "dar": "to give",
    "tener": "to have", "venir": "to come",
}

# ── Sub-block specs ─────────────────────────────────────────────────────────

SUBBLOCKS = [
    {
        "key": "ser_estar",
        "verbs": ["ser", "estar"],
        "lesson_numbers": [1, 2, 2.5],  # drill_1, drill_2, chat
        "title_short": "ser + estar",
        "intro_const": "IRREGULAR_PRESENT_SER_ESTAR_INTRO",
        "intro_pitch": "**ser** and **estar** both translate as 'to be,' but Spanish splits them: **ser** is permanent identity (*soy americano*), **estar** is location and state (*estoy cansado*).",
        "intro_text2": "Both are deeply irregular — yo soy / yo estoy share nothing with their infinitives. Memorize them whole.",
        "openers": [
            ("Where are you from?", "¿De dónde eres?"),
            ("How are you today?", "¿Cómo estás hoy?"),
        ],
    },
    {
        "key": "ir_dar",
        "verbs": ["ir", "dar"],
        "lesson_numbers": [3, 4, 4.5],
        "title_short": "ir + dar",
        "intro_const": "IRREGULAR_PRESENT_IR_DAR_INTRO",
        "intro_pitch": "**ir** (to go) and **dar** (to give) are short, suppletive verbs. Both end in **-oy** in yo (voy / doy) and follow a similar pattern.",
        "intro_text2": "ir is the workhorse for the *ir + a + infinitive* future construction (you'll meet it again in GL 9). dar is essential for any 'give' or 'pass' construction.",
        "openers": [
            ("Where are you going?", "¿Adónde vas?"),
            ("Do you give classes?", "¿Das clases?"),
        ],
    },
    {
        "key": "tener_venir",
        "verbs": ["tener", "venir"],
        "lesson_numbers": [5, 6, 6.5],
        "title_short": "tener + venir",
        "intro_const": "IRREGULAR_PRESENT_TENER_VENIR_INTRO",
        "intro_pitch": "**tener** (to have) and **venir** (to come) share two irregularities: yo ends in **-go** (tengo, vengo), and the e→ie stem change appears in tú / él / ellos (tienes, viene, vienen).",
        "intro_text2": "tener is also used for ages and obligations: *tengo 30 años*, *tengo que trabajar*. venir works for arrivals and origins.",
        "openers": [
            ("Do you have time?", "¿Tienes tiempo?"),
            ("When are you coming?", "¿Cuándo vienes?"),
        ],
    },
]

# Distribute drill targets across 5 collapsed pronouns (yo / tú / él-ella-usted / nosotros-nosotras / ellos-ellas-ustedes)
# DIVERSE_PRONOUNS for variety honoring "include feminine/formal" memory rule
DIVERSE_PRONOUNS = ["yo", "tú", "ella", "nosotras", "ustedes",
                    "él", "ella", "usted", "nosotros", "ellos"]
DIVERSE_PRONOUNS_2 = ["tú", "yo", "él", "nosotros", "ellas",
                      "usted", "ellos", "ella", "nosotras", "ustedes"]


# ── LLM: drill sentence authoring ─────────────────────────────────────────

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
  "I have a brother" / "Yo tengo un hermano" → {"brother":"hermano","hermano":"brother"}

PRODUCTION RULES:
- Short, natural A1/A2 sentences (3-7 words English).
- Use the target verb in the conjugation indicated for each sentence.
- Mix subjects diversely: include ella/ellas/nosotras/usted/ustedes — NOT just masculine.
- When ES uses nosotras/ellas, EN must say "We (f)" / "They (f)".
- Type alternates "written" / "auditory" — caller specifies.
- Spanish must be natural, register-appropriate, no awkward word-for-word.

OUTPUT: JSON only, format {"sentences": [{"en":"...", "es":"...", "type":"...", "glosses":{...}}, ...]}.
No commentary, no code fences."""

USER_TMPL = """Author 10 drill sentences for a Spanish present-tense conjugation drill.

Verbs to drill: {verbs}
Verb glosses (do not include in sentence glosses): {verb_glosses}

For each sentence, I'll specify the (verb, pronoun, type) tuple. Distribute as listed:

{spec}

Return JSON: {{"sentences": [...]}} in the order I listed."""


def make_user_prompt(verbs: list[str], spec_rows: list[tuple[str, str, str]]) -> str:
    lines = []
    for i, (verb, pronoun, t) in enumerate(spec_rows, 1):
        lines.append(f'  {i}. verb={verb}, pronoun={pronoun}, type={t}')
    return USER_TMPL.format(
        verbs=", ".join(verbs),
        verb_glosses=", ".join(f"{v}={VERB_GLOSS_EN[v]}" for v in verbs),
        spec=chr(10).join(lines),
    )


async def author_sentences(client: AsyncOpenAI, sem: asyncio.Semaphore,
                            verbs: list[str], spec_rows: list[tuple[str, str, str]]):
    async with sem:
        for attempt in range(MAX_RETRIES):
            try:
                resp = await client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {"role": "system", "content": SENTENCE_SYSTEM},
                        {"role": "user", "content": make_user_prompt(verbs, spec_rows)},
                    ],
                    temperature=0.5,
                    response_format={"type": "json_object"},
                )
                content = resp.choices[0].message.content or "{}"
                parsed = json.loads(content)
                sents = parsed.get("sentences", [])
                # Bidirectional glosses sanity
                for s in sents:
                    g = s.get("glosses", {})
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


# ── Code-emit helpers ──────────────────────────────────────────────────────

def emit_intro(sb: dict) -> str:
    """Produce the intro_chart constant Python literal."""
    v1, v2 = sb["verbs"]
    a1, a2 = ANSWERS[v1], ANSWERS[v2]

    def mini_table(verb: str, ans: dict) -> str:
        rows_lit = ",\n            ".join(
            f'["{label}", "{ans[key]}"]'
            for label, key in [("yo", "yo"), ("tú", "tú"),
                               ("él / ella / usted", "él"),
                               ("nosotros / nosotras", "nosotros"),
                               ("ellos / ellas / ustedes", "ellos")]
        )
        return f'''        {{
            "kind": "mini_table",
            "title": "{verb} ({VERB_GLOSS_EN[verb]})",
            "rows": [
            {rows_lit},
            ],
        }}'''

    recall = a1
    recall_lit = ", ".join(
        f'"{p}": "{recall[p]}"' for p in ["yo", "tú", "él", "nosotros", "ellos"]
    )

    return f'''{sb["intro_const"]} = {{
    "kind": "cards",
    "title": "Irregular Present — {sb["title_short"]}",
    "cards": [
        {{
            "kind": "text",
            "title": "{sb["title_short"]}: high-frequency, hand-memorize",
            "body": "{sb["intro_pitch"]}",
        }},
        {{
            "kind": "text",
            "title": "Why these two together",
            "body": "{sb["intro_text2"]}",
        }},
{mini_table(v1, a1)},
{mini_table(v2, a2)},
    ],
    "recall": {{
        "verb": "{v1}",
        "answers": {{{recall_lit}}},
    }},
}}'''


def emit_drill_lesson(sb: dict, drill_idx: int, sentences: list[dict],
                      lesson_number: float, drill_targets: list[tuple[str, str]],
                      with_intro: bool) -> str:
    v1, v2 = sb["verbs"]
    sid = f'grammar_irregular_present_{sb["key"]}_{drill_idx}'
    a1, a2 = ANSWERS[v1], ANSWERS[v2]

    def fmt_answers(verb: str, ans: dict) -> str:
        items = [f'"{p}": "{ans[p]}"' for p in
                 ["yo", "tú", "él", "ella", "usted",
                  "nosotros", "nosotras", "ellos", "ellas", "ustedes"]]
        return f'                "{verb}": {{{", ".join(items)}}}'

    sentence_lit = []
    for s in sentences:
        glosses = s.get("glosses", {})
        gloss_pairs = ", ".join(f'"{k}": "{v}"' for k, v in glosses.items())
        sentence_lit.append(
            '            {{"en": "{en}", "es": "{es}", "noun_id": None, '
            '"type": "{t}", "glosses": {{{g}}}}},'.format(
                en=s["en"].replace('"', '\\"'),
                es=s["es"].replace('"', '\\"'),
                t=s.get("type", "written"),
                g=gloss_pairs,
            )
        )

    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in drill_targets)

    intro_line = f'\n        "intro_chart": {sb["intro_const"]},' if with_intro else ""
    phases_0a = "True" if with_intro else "False"

    en_opener, es_opener = sb["openers"][drill_idx - 1]

    return f'''    "{sid}": {{
        "title": "Irregular Present — {sb["title_short"]} ({drill_idx}/2)",
        "grammar_level": 4,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": "6jpCj97AHMN",
        "drill_type": "conjugation",
        "tense": "present",{intro_line}
        "rule_chart": IRREGULAR_PRESENT_RULE,
        "drill_config": {{
            "answers": {{
{fmt_answers(v1, a1)},
{fmt_answers(v2, a2)},
            }},
        }},
        "phases": {{"0a": {phases_0a}, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False}},
        "phase_1c_config": {{"total_items": 5, "mode": "random_pronoun_verb"}},
        "drill_sentences": [
{chr(10).join(sentence_lit)}
        ],
        "drill_targets": [{target_lit}],
        "phase_2_config": {{
            "description": "Irregular Present {sb["title_short"]} ({drill_idx}/2): {v1}, {v2}",
            "targets": [{target_lit}],
        }},
        "opener_en": "{en_opener}",
        "opener_es": "{es_opener}",
    }},'''


def emit_chat_lesson(sb: dict, lesson_number: float) -> str:
    v1, v2 = sb["verbs"]
    sid = f'grammar_irregular_present_{sb["key"]}_chat'
    targets = []
    for i in range(5):
        targets.append((v1, DIVERSE_PRONOUNS[i]))
    for i in range(5):
        targets.append((v2, DIVERSE_PRONOUNS_2[i]))
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in targets)
    return f'''    "{sid}": {{
        "title": "Irregular Present — {sb["title_short"]} Chat",
        "grammar_level": 4,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {{"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False}},
        "drill_sentences": [],
        "phase_2_config": {{"description": "Irregular Present {sb["title_short"]} chat: {v1}, {v2}", "targets": [{target_lit}]}},
    }},'''


# ── Drill target distribution (10 per drill: 5 v1 + 5 v2 with diverse pronouns) ─

def make_drill_spec(verb: str, drill_idx: int) -> list[tuple[str, str, str]]:
    """Return (verb, pronoun, type) for 5 sentences using verb."""
    pronouns = DIVERSE_PRONOUNS if drill_idx == 1 else DIVERSE_PRONOUNS_2
    return [(verb, pronouns[i], "written" if i % 2 == 0 else "auditory") for i in range(5)]


async def main():
    client = AsyncOpenAI(api_key=settings.openai_api_key)
    sem = asyncio.Semaphore(CONCURRENCY)

    # 6 LLM calls total: 3 sub-blocks × 2 drills, each generating 10 sentences
    tasks = []
    task_meta = []
    for sb in SUBBLOCKS:
        v1, v2 = sb["verbs"]
        for drill_idx in [1, 2]:
            spec = make_drill_spec(v1, drill_idx) + make_drill_spec(v2, drill_idx)
            tasks.append(author_sentences(client, sem, [v1, v2], spec))
            task_meta.append((sb, drill_idx, spec))

    print(f"Authoring {len(tasks)} drill batches of 10 sentences each...")
    results = await asyncio.gather(*tasks)

    # Build the output Python module
    out_lines = ['"""Auto-generated by scripts/split_gl4.py — splice into grammar_situations.py.', '"""', '', '']
    out_lines.append("# ── New intro constants ──────────────────────────────────────────────────")
    out_lines.append("")
    for sb in SUBBLOCKS:
        out_lines.append(emit_intro(sb))
        out_lines.append("")

    out_lines.append("# ── New lesson dicts (paste into GRAMMAR_SITUATIONS) ─────────────────────")
    out_lines.append("")
    for (sb, drill_idx, spec), sents in zip(task_meta, results):
        if sents and "__ERROR__" in sents[0]:
            print(f"  FAIL {sb['key']} drill {drill_idx}: {sents[0]['__ERROR__']}")
            continue
        # Drill targets matches the sentences' pronouns
        targets = [(spec[i][0], spec[i][1]) for i in range(len(spec))]
        out_lines.append(emit_drill_lesson(
            sb, drill_idx, sents,
            lesson_number=sb["lesson_numbers"][drill_idx - 1],
            drill_targets=targets,
            with_intro=(drill_idx == 1),
        ))
        out_lines.append("")

    for sb in SUBBLOCKS:
        out_lines.append(emit_chat_lesson(sb, sb["lesson_numbers"][2]))
        out_lines.append("")

    OUTPUT.write_text("\n".join(out_lines))
    print(f"Wrote {OUTPUT}")
    print(f"Lines: {len(out_lines)}")


if __name__ == "__main__":
    asyncio.run(main())
