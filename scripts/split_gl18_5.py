"""Split GL 18.5 (Perfect Tenses) into 2 sub-blocks of 2 verbs each.

Sub-blocks:
  - present perfect: hablar + comer (haber-present + participle)
  - pluperfect: hablar + vivir (haber-imperfect + participle)

Output: scripts/_gl18_5_output.py — replaces grammar_perfect_tenses_drill_{1,2}{,_chat}.

Construction: haber + past participle. Pipe-encoding: haber forms get a leading
pipe (suppletive); the participle stays attached.
"""
from __future__ import annotations
import asyncio
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from openai import AsyncOpenAI  # noqa: E402
from app.config import settings  # noqa: E402
from scripts._split_common import (  # noqa: E402
    CONCURRENCY, DIVERSE_PRONOUNS, DIVERSE_PRONOUNS_2,
    author_sentences, fmt_answers_block, fmt_sentence_lit, make_drill_spec,
)

OUTPUT = ROOT / "scripts" / "_gl18_5_output.py"

# haber present
HABER_PRES = {
    "yo": "he", "tú": "has", "él": "ha", "ella": "ha", "usted": "ha",
    "nosotros": "hemos", "nosotras": "hemos",
    "ellos": "han", "ellas": "han", "ustedes": "han",
}
HABER_IMPF = {
    "yo": "había", "tú": "habías", "él": "había", "ella": "había", "usted": "había",
    "nosotros": "habíamos", "nosotras": "habíamos",
    "ellos": "habían", "ellas": "habían", "ustedes": "habían",
}

PARTICIPLES = {
    "hablar": "hablado",
    "comer": "comido",
    "vivir": "vivido",
}


def build_pres_perfect(verb: str) -> dict:
    p = PARTICIPLES[verb]
    return {pn: f"|{h} {p}" for pn, h in HABER_PRES.items()}


def build_pluperfect(verb: str) -> dict:
    p = PARTICIPLES[verb]
    return {pn: f"|{h} {p}" for pn, h in HABER_IMPF.items()}


VERB_GLOSS_EN = {
    "hablar": "to speak", "comer": "to eat", "vivir": "to live",
}

SUBBLOCKS = [
    {
        "key": "present_perfect",
        "verbs": ["hablar", "comer"],
        "lesson_numbers": [1, 2, 2.5],
        "title_short": "present perfect (hablar + comer)",
        "intro_const": "PERFECT_TENSES_PRESENT_INTRO",
        "intro_pitch": "**Present perfect** = haber-present + past participle: 'he hablado' (I have spoken). The endings of haber are: he, has, ha, hemos, han.",
        "intro_text2": "Past participles for regular verbs: -ar → -ado (hablado), -er/-ir → -ido (comido, vivido). They never agree in gender or number when used with haber.",
        "openers": [
            ("Have you spoken with him?", "¿Has hablado con él?"),
            ("Have you eaten lunch?", "¿Has comido el almuerzo?"),
        ],
        "build": build_pres_perfect,
    },
    {
        "key": "pluperfect",
        "verbs": ["hablar", "vivir"],
        "lesson_numbers": [3, 4, 4.5],
        "title_short": "pluperfect (hablar + vivir)",
        "intro_const": "PERFECT_TENSES_PLUPERFECT_INTRO",
        "intro_pitch": "**Pluperfect** = haber-imperfect + past participle: 'había hablado' (I had spoken). The endings: había, habías, había, habíamos, habían.",
        "intro_text2": "Use the pluperfect for actions that happened *before* another past action: 'cuando llegué, ya había comido' (when I arrived, I had already eaten).",
        "openers": [
            ("Had you spoken to her before?", "¿Le habías hablado antes?"),
            ("Had you lived there before?", "¿Habías vivido allí antes?"),
        ],
        "build": build_pluperfect,
    },
]

# Pre-compute ANSWERS dict for both sub-blocks (verb -> {pronoun: form})
ANSWERS = {}
for sb in SUBBLOCKS:
    for v in sb["verbs"]:
        ANSWERS[(sb["key"], v)] = sb["build"](v)


def emit_intro(sb: dict) -> str:
    v1, v2 = sb["verbs"]
    a1 = sb["build"](v1)
    a2 = sb["build"](v2)

    def mt(verb: str, ans: dict, gloss: str) -> str:
        rows = [("yo", "yo"), ("tú", "tú"),
                ("él / ella / usted", "él"),
                ("nosotros / nosotras", "nosotros"),
                ("ellos / ellas / ustedes", "ellos")]
        rows_lit = ",\n            ".join(f'["{lbl}", "{ans[k]}"]' for lbl, k in rows)
        return f'''        {{
            "kind": "mini_table",
            "title": "{verb} ({gloss})",
            "rows": [
            {rows_lit},
            ],
        }}'''

    mt1 = mt(v1, a1, VERB_GLOSS_EN[v1])
    mt2 = mt(v2, a2, VERB_GLOSS_EN[v2])
    keys = ["yo", "tú", "él", "nosotros", "ellos"]
    pairs1 = ", ".join(f'"{k}": "{a1[k]}"' for k in keys)
    pairs2 = ", ".join(f'"{k}": "{a2[k]}"' for k in keys)
    recall = f'''    "recall": [
        {{"verb": "{v1}", "answers": {{{pairs1}}}}},
        {{"verb": "{v2}", "answers": {{{pairs2}}}}},
    ],'''
    return f'''{sb["intro_const"]} = {{
    "kind": "cards",
    "title": "Perfect Tenses — {sb["title_short"]}",
    "cards": [
        {{
            "kind": "text",
            "title": "{sb["title_short"]}",
            "body": "{sb["intro_pitch"]}",
        }},
        {{
            "kind": "text",
            "title": "Notes",
            "body": "{sb["intro_text2"]}",
        }},
{mt1},
{mt2},
    ],
{recall}
}}'''


def emit_drill_lesson(sb: dict, drill_idx: int, sentences: list[dict],
                      lesson_number: float, drill_targets: list[tuple[str, str]],
                      with_intro: bool) -> str:
    v1, v2 = sb["verbs"]
    sid = f'grammar_perfect_tenses_{sb["key"]}_{drill_idx}'
    a1 = sb["build"](v1)
    a2 = sb["build"](v2)
    sentence_lit = fmt_sentence_lit(sentences)
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in drill_targets)
    intro_line = f'\n        "intro_chart": {sb["intro_const"]},' if with_intro else ""
    phases_0a = "True" if with_intro else "False"
    en_opener, es_opener = sb["openers"][drill_idx - 1]

    return f'''    "{sid}": {{
        "title": "Perfect Tenses — {sb["title_short"]} ({drill_idx}/2)",
        "grammar_level": 18.5,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": None,
        "drill_type": "conjugation",
        "tense": "perfect",{intro_line}
        "rule_chart": PERFECT_TENSES_RULE,
        "drill_config": {{
            "answers": {{
{fmt_answers_block(v1, a1)},
{fmt_answers_block(v2, a2)},
            }},
        }},
        "phases": {{"0a": {phases_0a}, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False}},
        "phase_1c_config": {{"total_items": 5, "mode": "random_pronoun_verb"}},
        "drill_sentences": [
{chr(10).join(sentence_lit)}
        ],
        "drill_targets": [{target_lit}],
        "phase_2_config": {{
            "description": "Perfect Tenses {sb["title_short"]} ({drill_idx}/2): {v1}, {v2}",
            "targets": [{target_lit}],
        }},
        "opener_en": "{en_opener}",
        "opener_es": "{es_opener}",
    }},'''


def emit_chat_lesson(sb: dict, lesson_number: float) -> str:
    v1, v2 = sb["verbs"]
    sid = f'grammar_perfect_tenses_{sb["key"]}_chat'
    targets = []
    for i in range(5):
        targets.append((v1, DIVERSE_PRONOUNS[i]))
    for i in range(5):
        targets.append((v2, DIVERSE_PRONOUNS_2[i]))
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in targets)
    return f'''    "{sid}": {{
        "title": "Perfect Tenses — {sb["title_short"]} Chat",
        "grammar_level": 18.5,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "perfect",
        "phases": {{"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False}},
        "drill_sentences": [],
        "phase_2_config": {{"description": "Perfect Tenses {sb["title_short"]} chat: {v1}, {v2}", "targets": [{target_lit}]}},
    }},'''


async def main():
    client = AsyncOpenAI(api_key=settings.openai_api_key)
    sem = asyncio.Semaphore(CONCURRENCY)

    tasks = []
    task_meta = []
    for sb in SUBBLOCKS:
        v1, v2 = sb["verbs"]
        for drill_idx in [1, 2]:
            spec = make_drill_spec(v1, drill_idx) + make_drill_spec(v2, drill_idx)
            if sb["key"] == "present_perfect":
                tense_desc = "Spanish present perfect: haber-present (he/has/ha/hemos/han) + past participle. EN should use 'have/has -ed' ('I have spoken', 'They have eaten')."
            else:
                tense_desc = "Spanish pluperfect: haber-imperfect (había/habías/había/habíamos/habían) + past participle. EN should use 'had -ed' ('I had spoken', 'They had lived')."
            tasks.append(author_sentences(
                client, sem, [v1, v2], VERB_GLOSS_EN, spec,
                tense_label=sb["title_short"],
                tense_desc=tense_desc,
            ))
            task_meta.append((sb, drill_idx, spec))

    print(f"Authoring {len(tasks)} drill batches...")
    results = await asyncio.gather(*tasks)

    out_lines = ['"""Auto-generated by scripts/split_gl18_5.py — splice into grammar_situations.py.', '"""', '', '']
    out_lines.append("# ── Retire keys: grammar_perfect_tenses_drill_{1,2}{,_chat}")
    out_lines.append("")
    out_lines.append("# ── New intro constants ──────────────────────────────────────────────────")
    out_lines.append("")
    for sb in SUBBLOCKS:
        out_lines.append(emit_intro(sb))
        out_lines.append("")

    out_lines.append("# ── New lesson dicts ────────────────────────────────────────────────────")
    out_lines.append("")
    for (sb, drill_idx, spec), sents in zip(task_meta, results):
        if sents and isinstance(sents[0], dict) and "__ERROR__" in sents[0]:
            print(f"  FAIL {sb['key']} drill {drill_idx}: {sents[0]['__ERROR__']}")
            continue
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
    print(f"Sections: {len(out_lines)}")


if __name__ == "__main__":
    asyncio.run(main())
