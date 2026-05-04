"""Split GL 18 (Gerund / Present Progressive) into 3 sub-blocks of 2 verbs each.

Sub-blocks:
  - hablar + caminar (-ar regulars)
  - comer + beber (-er regulars)
  - salir + inhibir (-ir regulars)

Output: scripts/_gl18_output.py — replaces grammar_gerund_{1,2,3,4}{,_chat}.

Construction: estar conjugated + gerund. The answer is the full progressive
("estoy hablando"). Pipe-encoding marks the changing portion: the estar form
gets a leading pipe; the gerund stays attached.

For a regular -ar verb: 'estoy habl|ando' would split inside the gerund. But
since estar is the part that flexes for the subject, the natural split is at
the start of the estar form. We encode the WHOLE thing with the boundary on
the irregular estar conjugation:
  estoy/estás/está/estamos/están are all suppletive → leading pipe.
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

OUTPUT = ROOT / "scripts" / "_gl18_output.py"

# estar forms (suppletive — leading pipe in the encoding)
ESTAR_FORMS = {
    "yo": "estoy", "tú": "estás", "él": "está", "ella": "está", "usted": "está",
    "nosotros": "estamos", "nosotras": "estamos",
    "ellos": "están", "ellas": "están", "ustedes": "están",
}

GERUND_FORMS = {
    "hablar": "hablando",
    "caminar": "caminando",
    "comer": "comiendo",
    "beber": "bebiendo",
    "salir": "saliendo",
    "inhibir": "inhibiendo",
}


def build_answers(infinitive: str) -> dict:
    g = GERUND_FORMS[infinitive]
    return {p: f"est|{form[3:]} {g}" if form.startswith("est") else f"|{form} {g}"
            for p, form in ESTAR_FORMS.items()}


# Cleaner version: estar splits between est and the suppletive ending
def build_answers_clean(infinitive: str) -> dict:
    g = GERUND_FORMS[infinitive]
    out = {}
    for p, est in ESTAR_FORMS.items():
        # estoy → est|oy ; estás → est|ás ; etc.
        out[p] = f"est|{est[3:]} {g}"
    return out


ANSWERS = {v: build_answers_clean(v) for v in GERUND_FORMS}

VERB_GLOSS_EN = {
    "hablar": "to speak", "caminar": "to walk",
    "comer": "to eat", "beber": "to drink",
    "salir": "to leave/go out", "inhibir": "to inhibit",
}

SUBBLOCKS = [
    {
        "key": "hablar_caminar",
        "verbs": ["hablar", "caminar"],
        "lesson_numbers": [1, 2, 2.5],
        "title_short": "hablar + caminar (-ar)",
        "intro_const": "GERUND_HABLAR_CAMINAR_INTRO",
        "intro_pitch": "**Present progressive** = estar + gerund: 'estoy hablando' (I am speaking). For -ar verbs, the gerund ending is **-ando**: hablando, caminando.",
        "intro_text2": "Spanish uses the progressive less often than English. Use it for actions happening *right now* or in a vivid moment, not for general habits.",
        "openers": [
            ("What are you saying?", "¿Qué estás hablando?"),
            ("Where are you walking?", "¿Por dónde estás caminando?"),
        ],
    },
    {
        "key": "comer_beber",
        "verbs": ["comer", "beber"],
        "lesson_numbers": [3, 4, 4.5],
        "title_short": "comer + beber (-er)",
        "intro_const": "GERUND_COMER_BEBER_INTRO",
        "intro_pitch": "For regular -er verbs, the gerund ending is **-iendo**: comiendo, bebiendo. estar still flexes for the subject (estoy comiendo, estás bebiendo).",
        "intro_text2": "The -iendo ending is shared with regular -ir verbs (next sub-block).",
        "openers": [
            ("What are you eating?", "¿Qué estás comiendo?"),
            ("What are you drinking?", "¿Qué estás bebiendo?"),
        ],
    },
    {
        "key": "salir_inhibir",
        "verbs": ["salir", "inhibir"],
        "lesson_numbers": [5, 6, 6.5],
        "title_short": "salir + inhibir (-ir)",
        "intro_const": "GERUND_SALIR_INHIBIR_INTRO",
        "intro_pitch": "Regular -ir verbs use the same **-iendo** ending: saliendo, inhibiendo.",
        "intro_text2": "Some -ir verbs have stem changes in the gerund (durmiendo, pidiendo, sintiendo) — but salir and inhibir are regular here.",
        "openers": [
            ("Who is leaving the building?", "¿Quién está saliendo del edificio?"),
            ("Are you holding back the urge?", "¿Estás inhibiendo el impulso?"),
        ],
    },
]


def emit_intro(sb: dict) -> str:
    v1, v2 = sb["verbs"]
    a1, a2 = ANSWERS[v1], ANSWERS[v2]

    def mt(verb: str, ans: dict, gloss: str) -> str:
        rows = [("yo", "yo"), ("tú", "tú"),
                ("él / ella / usted", "él"),
                ("nosotros / nosotras", "nosotros"),
                ("ellos / ellas / ustedes", "ellos")]
        rows_lit = ",\n            ".join(f'["{lbl}", "{ans[k]}"]' for lbl, k in rows)
        return f'''        {{
            "kind": "mini_table",
            "title": "{verb} ({gloss}) — present progressive",
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
    "title": "Gerund / Present Progressive — {sb["title_short"]}",
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
    sid = f'grammar_gerund_{sb["key"]}_{drill_idx}'
    a1, a2 = ANSWERS[v1], ANSWERS[v2]
    sentence_lit = fmt_sentence_lit(sentences)
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in drill_targets)
    intro_line = f'\n        "intro_chart": {sb["intro_const"]},' if with_intro else ""
    phases_0a = "True" if with_intro else "False"
    en_opener, es_opener = sb["openers"][drill_idx - 1]

    return f'''    "{sid}": {{
        "title": "Gerund — {sb["title_short"]} ({drill_idx}/2)",
        "grammar_level": 18,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": "Xpma6w0jy7m",
        "drill_type": "conjugation",
        "tense": "gerund",{intro_line}
        "rule_chart": GERUND_RULE,
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
            "description": "Gerund {sb["title_short"]} ({drill_idx}/2): {v1}, {v2}",
            "targets": [{target_lit}],
        }},
        "opener_en": "{en_opener}",
        "opener_es": "{es_opener}",
    }},'''


def emit_chat_lesson(sb: dict, lesson_number: float) -> str:
    v1, v2 = sb["verbs"]
    sid = f'grammar_gerund_{sb["key"]}_chat'
    targets = []
    for i in range(5):
        targets.append((v1, DIVERSE_PRONOUNS[i]))
    for i in range(5):
        targets.append((v2, DIVERSE_PRONOUNS_2[i]))
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in targets)
    return f'''    "{sid}": {{
        "title": "Gerund — {sb["title_short"]} Chat",
        "grammar_level": 18,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "gerund",
        "phases": {{"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False}},
        "drill_sentences": [],
        "phase_2_config": {{"description": "Gerund {sb["title_short"]} chat: {v1}, {v2}", "targets": [{target_lit}]}},
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
                tense_label="present progressive (estar + gerund)",
                tense_desc="Spanish present progressive: estar conjugated + gerund of the target verb. EN should use 'is/am/are -ing' present progressive ('I am speaking', 'You are walking', 'They are eating').",
            ))
            task_meta.append((sb, drill_idx, spec))

    print(f"Authoring {len(tasks)} drill batches...")
    results = await asyncio.gather(*tasks)

    out_lines = ['"""Auto-generated by scripts/split_gl18.py — splice into grammar_situations.py.', '"""', '', '']
    out_lines.append("# ── Retire keys: grammar_gerund_{1,2,3,4}{,_chat}")
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
