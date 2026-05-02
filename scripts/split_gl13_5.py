"""Split GL 13.5 (Imperatives) into 2 sub-blocks of 2 verbs each.

Sub-blocks:
  - hablar + comer (regular tú/usted/nosotros affirmative imperatives)
  - tener + venir (irregular tú short-forms: ten, ven; plus full usted/nosotros)

Output: scripts/_gl13_5_output.py — replaces grammar_imperatives_{1,2}{,_chat}.

Imperative pronoun set: tú, usted, nosotros, ustedes. Pipe-encoding: regular
imperatives split between stem and ending; irregular tú short forms get a
leading pipe.
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
    CONCURRENCY,
    author_sentences, fmt_sentence_lit,
)

OUTPUT = ROOT / "scripts" / "_gl13_5_output.py"

# Imperative answers — pronoun set is {tú, usted, nosotros, ustedes}.
# Regular: stem|ending. Irregulars (tú): leading pipe (suppletive shortcuts).
ANSWERS = {
    "hablar": {"tú": "habl|a", "usted": "habl|e", "nosotros": "habl|emos", "ustedes": "habl|en"},
    "comer": {"tú": "com|e", "usted": "com|a", "nosotros": "com|amos", "ustedes": "com|an"},
    # Irregular tú: ten, ven (short forms). usted/nosotros/ustedes use the subjunctive stem.
    "tener": {"tú": "|ten", "usted": "ten|ga", "nosotros": "ten|gamos", "ustedes": "ten|gan"},
    "venir": {"tú": "|ven", "usted": "ven|ga", "nosotros": "ven|gamos", "ustedes": "ven|gan"},
}

VERB_GLOSS_EN = {
    "hablar": "to speak", "comer": "to eat",
    "tener": "to have", "venir": "to come",
}

IMP_PRONOUNS = ["tú", "usted", "nosotros", "ustedes"]
# Diverse pronoun rotations within imperative pronoun set
IMP_DIVERSE = ["tú", "usted", "nosotros", "ustedes",
               "tú", "usted", "tú", "usted", "nosotros", "ustedes"]
IMP_DIVERSE_2 = ["usted", "tú", "ustedes", "nosotros",
                 "usted", "tú", "ustedes", "tú", "usted", "nosotros"]

SUBBLOCKS = [
    {
        "key": "hablar_comer",
        "verbs": ["hablar", "comer"],
        "lesson_numbers": [1, 2, 2.5],
        "title_short": "hablar + comer (regular tú)",
        "intro_const": "IMPERATIVES_HABLAR_COMER_INTRO",
        "intro_pitch": "**Affirmative imperative** = command form. For regular -ar verbs, the **tú** command swaps -ar → -a (habla = speak!). For -er/-ir, swap to -e (come = eat!).",
        "intro_text2": "Other commands (usted, nosotros, ustedes) use the subjunctive stem: hable, hablemos, hablen. We'll cover those alongside tú so you see the whole picture.",
        "openers": [
            ("Speak slowly, please.", "Habla despacio, por favor."),
            ("Eat the bread now.", "Come el pan ahora."),
        ],
    },
    {
        "key": "tener_venir",
        "verbs": ["tener", "venir"],
        "lesson_numbers": [3, 4, 4.5],
        "title_short": "tener + venir (irregular tú)",
        "intro_const": "IMPERATIVES_TENER_VENIR_INTRO",
        "intro_pitch": "Eight common verbs have **short irregular tú commands**: di, haz, ve, pon, sal, sé, ten, ven. Here we drill **ten** (have!) and **ven** (come!).",
        "intro_text2": "Outside tú, these verbs use the regular subjunctive stem: tenga, tengamos, tengan / venga, vengamos, vengan. The yo-go pattern shows up here too (tengo → tenga).",
        "openers": [
            ("Have patience, please.", "Ten paciencia, por favor."),
            ("Come here right now.", "Ven aquí ahora mismo."),
        ],
    },
]


def emit_intro(sb: dict) -> str:
    v1, v2 = sb["verbs"]
    a1, a2 = ANSWERS[v1], ANSWERS[v2]

    def mt(verb: str, ans: dict, gloss: str) -> str:
        rows = [(p, p) for p in IMP_PRONOUNS]
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

    keys = IMP_PRONOUNS
    pairs1 = ", ".join(f'"{k}": "{a1[k]}"' for k in keys)
    pairs2 = ", ".join(f'"{k}": "{a2[k]}"' for k in keys)
    recall = f'''    "recall": [
        {{"verb": "{v1}", "answers": {{{pairs1}}}}},
        {{"verb": "{v2}", "answers": {{{pairs2}}}}},
    ],'''
    return f'''{sb["intro_const"]} = {{
    "kind": "cards",
    "title": "Imperatives — {sb["title_short"]}",
    "cards": [
        {{
            "kind": "text",
            "title": "{sb["title_short"]}",
            "body": "{sb["intro_pitch"]}",
        }},
        {{
            "kind": "text",
            "title": "Beyond tú",
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
    sid = f'grammar_imperatives_{sb["key"]}_{drill_idx}'
    a1, a2 = ANSWERS[v1], ANSWERS[v2]
    sentence_lit = fmt_sentence_lit(sentences)
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in drill_targets)
    intro_line = f'\n        "intro_chart": {sb["intro_const"]},' if with_intro else ""
    phases_0a = "True" if with_intro else "False"
    en_opener, es_opener = sb["openers"][drill_idx - 1]

    def fmt_ans(verb: str, ans: dict) -> str:
        items = [f'"{p}": "{ans[p]}"' for p in IMP_PRONOUNS]
        return f'                "{verb}": {{{", ".join(items)}}}'

    return f'''    "{sid}": {{
        "title": "Imperatives — {sb["title_short"]} ({drill_idx}/2)",
        "grammar_level": 13.5,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": None,
        "drill_type": "conjugation",
        "tense": "imperative",{intro_line}
        "rule_chart": IMPERATIVES_RULE,
        "drill_config": {{
            "answers": {{
{fmt_ans(v1, a1)},
{fmt_ans(v2, a2)},
            }},
        }},
        "phases": {{"0a": {phases_0a}, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False}},
        "phase_1c_config": {{"total_items": 5, "mode": "random_pronoun_verb"}},
        "drill_sentences": [
{chr(10).join(sentence_lit)}
        ],
        "drill_targets": [{target_lit}],
        "phase_2_config": {{
            "description": "Imperatives {sb["title_short"]} ({drill_idx}/2): {v1}, {v2}",
            "targets": [{target_lit}],
        }},
        "opener_en": "{en_opener}",
        "opener_es": "{es_opener}",
    }},'''


def emit_chat_lesson(sb: dict, lesson_number: float) -> str:
    v1, v2 = sb["verbs"]
    sid = f'grammar_imperatives_{sb["key"]}_chat'
    targets = []
    for i in range(5):
        targets.append((v1, IMP_DIVERSE[i]))
    for i in range(5):
        targets.append((v2, IMP_DIVERSE_2[i]))
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in targets)
    return f'''    "{sid}": {{
        "title": "Imperatives — {sb["title_short"]} Chat",
        "grammar_level": 13.5,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "imperative",
        "phases": {{"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False}},
        "drill_sentences": [],
        "phase_2_config": {{"description": "Imperatives {sb["title_short"]} chat: {v1}, {v2}", "targets": [{target_lit}]}},
    }},'''


def make_drill_spec_imp(verb: str, drill_idx: int) -> list[tuple[str, str, str]]:
    pronouns = IMP_DIVERSE if drill_idx == 1 else IMP_DIVERSE_2
    return [(verb, pronouns[i], "written" if i % 2 == 0 else "auditory") for i in range(5)]


async def main():
    client = AsyncOpenAI(api_key=settings.openai_api_key)
    sem = asyncio.Semaphore(CONCURRENCY)

    tasks = []
    task_meta = []
    for sb in SUBBLOCKS:
        v1, v2 = sb["verbs"]
        for drill_idx in [1, 2]:
            spec = make_drill_spec_imp(v1, drill_idx) + make_drill_spec_imp(v2, drill_idx)
            tasks.append(author_sentences(
                client, sem, [v1, v2], VERB_GLOSS_EN, spec,
                tense_label="affirmative imperative",
                tense_desc="Spanish affirmative imperative (command form). Pronouns are tú/usted/nosotros/ustedes — these mean 'you (informal)', 'you (formal)', 'let's', 'you all'. In English, render as imperative ('Speak Spanish', 'Eat now', 'Let's eat'). When pronoun=nosotros, the EN form is 'Let's [verb]'. When pronoun=ustedes, the EN form is '[Verb], you all' or just '[Verb]' (like 'Speak'). When pronoun=tú or usted, the EN is just '[Verb]' optionally with 'please'.",
            ))
            task_meta.append((sb, drill_idx, spec))

    print(f"Authoring {len(tasks)} drill batches...")
    results = await asyncio.gather(*tasks)

    out_lines = ['"""Auto-generated by scripts/split_gl13_5.py — splice into grammar_situations.py.', '"""', '', '']
    out_lines.append("# ── Retire keys: grammar_imperatives_{1,2}{,_chat}")
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
