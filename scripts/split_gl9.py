"""Split GL 9 (ir + a + infinitive) into 3 sub-blocks of 2 verbs each.

Construction: ir conjugated + a + infinitive ("voy a hablar" = I'm going to speak).
Each sub-block pairs 2 different infinitives. The conjugated part is `ir`
(voy, vas, va, vamos, van) — that's the verb being tested across infinitives.

Sub-blocks:
  - hablar + comer (infinitives)
  - vivir + escribir (infinitives)
  - dormir + estudiar (infinitives)

Pipe-encoding: leading pipe on the whole `ir` form ("|voy a hablar"), since `ir`
is suppletive (no shared stem with infinitive).

Output: scripts/_gl9_output.py — replaces grammar_ir_a_inf_{1,2,3}{,_chat}.
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

OUTPUT = ROOT / "scripts" / "_gl9_output.py"

# Bare ir conjugation
IR_FORMS = {
    "yo": "voy", "tú": "vas", "él": "va", "ella": "va", "usted": "va",
    "nosotros": "vamos", "nosotras": "vamos",
    "ellos": "van", "ellas": "van", "ustedes": "van",
}


def build_answers_for(infinitive: str) -> dict:
    """Return pipe-encoded ir+a+infinitive for every pronoun."""
    return {p: f"|{form} a {infinitive}" for p, form in IR_FORMS.items()}


VERB_GLOSS_EN = {
    "hablar": "to speak", "comer": "to eat",
    "vivir": "to live", "escribir": "to write",
    "dormir": "to sleep", "estudiar": "to study",
}


SUBBLOCKS = [
    {
        "key": "hablar_comer",
        "verbs": ["hablar", "comer"],
        "lesson_numbers": [1, 2, 2.5],
        "title_short": "hablar + comer",
        "intro_const": "IR_A_INF_HABLAR_COMER_INTRO",
        "intro_pitch": "**ir + a + infinitive** is the everyday Spanish 'going-to' future. Conjugate **ir** (voy, vas, va, vamos, van), add **a**, then any infinitive. *Voy a hablar* = I'm going to speak.",
        "intro_text2": "This sub-block uses **hablar** (to speak) and **comer** (to eat) as the infinitives. The conjugated part — ir — is what you're learning to flex.",
        "openers": [
            ("What are you going to say?", "¿Qué vas a decir?"),
            ("What are you going to eat?", "¿Qué vas a comer?"),
        ],
    },
    {
        "key": "vivir_escribir",
        "verbs": ["vivir", "escribir"],
        "lesson_numbers": [3, 4, 4.5],
        "title_short": "vivir + escribir",
        "intro_const": "IR_A_INF_VIVIR_ESCRIBIR_INTRO",
        "intro_pitch": "Same construction: **ir + a + infinitive**. Today we use **vivir** (to live) and **escribir** (to write) as the infinitives.",
        "intro_text2": "Notice that the infinitive never changes — only **ir** flexes for the subject. The whole structure functions as a near-future tense.",
        "openers": [
            ("Where are you going to live?", "¿Dónde vas a vivir?"),
            ("What are you going to write?", "¿Qué vas a escribir?"),
        ],
    },
    {
        "key": "dormir_estudiar",
        "verbs": ["dormir", "estudiar"],
        "lesson_numbers": [5, 6, 6.5],
        "title_short": "dormir + estudiar",
        "intro_const": "IR_A_INF_DORMIR_ESTUDIAR_INTRO",
        "intro_pitch": "Same construction with **dormir** (to sleep) and **estudiar** (to study). Even stem-changers like dormir keep their plain infinitive shape here — only **ir** flexes.",
        "intro_text2": "ir + a + inf is more common in spoken Spanish than the simple future tense (hablaré). Drill it until it's automatic.",
        "openers": [
            ("When are you going to sleep?", "¿Cuándo vas a dormir?"),
            ("What are you going to study?", "¿Qué vas a estudiar?"),
        ],
    },
]


def emit_intro(sb: dict) -> str:
    v1, v2 = sb["verbs"]
    a1 = build_answers_for(v1)
    a2 = build_answers_for(v2)

    def mt(verb: str, ans: dict, gloss: str) -> str:
        rows = [("yo", "yo"), ("tú", "tú"),
                ("él / ella / usted", "él"),
                ("nosotros / nosotras", "nosotros"),
                ("ellos / ellas / ustedes", "ellos")]
        rows_lit = ",\n            ".join(f'["{lbl}", "{ans[k]}"]' for lbl, k in rows)
        return f'''        {{
            "kind": "mini_table",
            "title": "ir a + {verb} ({gloss})",
            "rows": [
            {rows_lit},
            ],
        }}'''

    mt1 = mt(v1, a1, VERB_GLOSS_EN[v1])
    mt2 = mt(v2, a2, VERB_GLOSS_EN[v2])
    # Recall: list-form, both infinitives, 5-pronoun condensed
    keys = ["yo", "tú", "él", "nosotros", "ellos"]
    pairs1 = ", ".join(f'"{k}": "{a1[k]}"' for k in keys)
    pairs2 = ", ".join(f'"{k}": "{a2[k]}"' for k in keys)
    recall = f'''    "recall": [
        {{"verb": "{v1}", "answers": {{{pairs1}}}}},
        {{"verb": "{v2}", "answers": {{{pairs2}}}}},
    ],'''
    return f'''{sb["intro_const"]} = {{
    "kind": "cards",
    "title": "ir a + Infinitive — {sb["title_short"]}",
    "cards": [
        {{
            "kind": "text",
            "title": "{sb["title_short"]}",
            "body": "{sb["intro_pitch"]}",
        }},
        {{
            "kind": "text",
            "title": "What changes, what stays",
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
    sid = f'grammar_ir_a_inf_{sb["key"]}_{drill_idx}'
    a1 = build_answers_for(v1)
    a2 = build_answers_for(v2)
    sentence_lit = fmt_sentence_lit(sentences)
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in drill_targets)
    intro_line = f'\n        "intro_chart": {sb["intro_const"]},' if with_intro else ""
    phases_0a = "True" if with_intro else "False"
    en_opener, es_opener = sb["openers"][drill_idx - 1]

    return f'''    "{sid}": {{
        "title": "ir a + Infinitive — {sb["title_short"]} ({drill_idx}/2)",
        "grammar_level": 9,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": "geHPDI9tMdH",
        "drill_type": "ir_a_inf",
        "tense": "ir_a_infinitive",{intro_line}
        "rule_chart": IR_A_INF_RULE,
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
            "description": "ir a + Infinitive {sb["title_short"]} ({drill_idx}/2): {v1}, {v2}",
            "targets": [{target_lit}],
        }},
        "opener_en": "{en_opener}",
        "opener_es": "{es_opener}",
    }},'''


def emit_chat_lesson(sb: dict, lesson_number: float) -> str:
    v1, v2 = sb["verbs"]
    sid = f'grammar_ir_a_inf_{sb["key"]}_chat'
    targets = []
    for i in range(5):
        targets.append((v1, DIVERSE_PRONOUNS[i]))
    for i in range(5):
        targets.append((v2, DIVERSE_PRONOUNS_2[i]))
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in targets)
    return f'''    "{sid}": {{
        "title": "ir a + Infinitive — {sb["title_short"]} Chat",
        "grammar_level": 9,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "ir_a_infinitive",
        "phases": {{"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False}},
        "drill_sentences": [],
        "phase_2_config": {{"description": "ir a + Infinitive {sb["title_short"]} chat: {v1}, {v2}", "targets": [{target_lit}]}},
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
            tasks.append(author_sentences(
                client, sem, [v1, v2], VERB_GLOSS_EN, spec,
                tense_label="ir + a + infinitive (going-to future)",
                tense_desc="Spanish 'ir + a + infinitive' near-future construction. The CONJUGATED VERB is `ir` (voy/vas/va/vamos/van), followed by `a` and the listed infinitive. So for verb=hablar, pronoun=yo, the form is 'voy a hablar'. The English equivalent is 'I'm going to speak' or 'I will speak'.",
            ))
            task_meta.append((sb, drill_idx, spec))

    print(f"Authoring {len(tasks)} drill batches...")
    results = await asyncio.gather(*tasks)

    out_lines = ['"""Auto-generated by scripts/split_gl9.py — splice into grammar_situations.py.', '"""', '', '']
    out_lines.append("# ── Retire keys: grammar_ir_a_inf_{1,2,3}{,_chat}")
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
