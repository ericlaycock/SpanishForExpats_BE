"""Split GL 6 (Stem-changers o→ue) into 3 sub-blocks of 2 verbs each.

Sub-blocks:
  - poder + volver
  - dormir + morir
  - mover + almorzar

Output: scripts/_gl6_output.py — splice replacing
grammar_present_o_ue_{1,2,3}{,_chat}.
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
    emit_mini_table, emit_recall_list,
)

OUTPUT = ROOT / "scripts" / "_gl6_output.py"

ANSWERS = {
    "poder": {"yo": "p|uedo", "tú": "p|uedes", "él": "p|uede", "ella": "p|uede", "usted": "p|uede",
              "nosotros": "pod|emos", "nosotras": "pod|emos",
              "ellos": "p|ueden", "ellas": "p|ueden", "ustedes": "p|ueden"},
    "volver": {"yo": "v|uelvo", "tú": "v|uelves", "él": "v|uelve", "ella": "v|uelve", "usted": "v|uelve",
               "nosotros": "volv|emos", "nosotras": "volv|emos",
               "ellos": "v|uelven", "ellas": "v|uelven", "ustedes": "v|uelven"},
    "dormir": {"yo": "d|uermo", "tú": "d|uermes", "él": "d|uerme", "ella": "d|uerme", "usted": "d|uerme",
               "nosotros": "dorm|imos", "nosotras": "dorm|imos",
               "ellos": "d|uermen", "ellas": "d|uermen", "ustedes": "d|uermen"},
    "morir": {"yo": "m|uero", "tú": "m|ueres", "él": "m|uere", "ella": "m|uere", "usted": "m|uere",
              "nosotros": "mor|imos", "nosotras": "mor|imos",
              "ellos": "m|ueren", "ellas": "m|ueren", "ustedes": "m|ueren"},
    "mover": {"yo": "m|uevo", "tú": "m|ueves", "él": "m|ueve", "ella": "m|ueve", "usted": "m|ueve",
              "nosotros": "mov|emos", "nosotras": "mov|emos",
              "ellos": "m|ueven", "ellas": "m|ueven", "ustedes": "m|ueven"},
    "almorzar": {"yo": "alm|uerzo", "tú": "alm|uerzas", "él": "alm|uerza", "ella": "alm|uerza", "usted": "alm|uerza",
                 "nosotros": "almorz|amos", "nosotras": "almorz|amos",
                 "ellos": "alm|uerzan", "ellas": "alm|uerzan", "ustedes": "alm|uerzan"},
}

VERB_GLOSS_EN = {
    "poder": "to be able to", "volver": "to return",
    "dormir": "to sleep", "morir": "to die",
    "mover": "to move", "almorzar": "to have lunch",
}

SUBBLOCKS = [
    {
        "key": "poder_volver",
        "verbs": ["poder", "volver"],
        "lesson_numbers": [1, 2, 2.5],
        "title_short": "poder + volver",
        "intro_const": "PRESENT_O_UE_PODER_VOLVER_INTRO",
        "intro_pitch": "Stem-changing verbs change **o → ue** in the stressed syllable: p**ue**do, v**ue**lvo. The change skips nosotros / nosotras.",
        "intro_text2": "**poder** is the modal 'can/be able' (puedo ir = I can go). **volver** means 'to come back' or 'to return'. Both are workhorses in spoken Spanish.",
        "openers": [
            ("Can you help me?", "¿Puedes ayudarme?"),
            ("When do you come back?", "¿Cuándo vuelves?"),
        ],
    },
    {
        "key": "dormir_morir",
        "verbs": ["dormir", "morir"],
        "lesson_numbers": [3, 4, 4.5],
        "title_short": "dormir + morir",
        "intro_const": "PRESENT_O_UE_DORMIR_MORIR_INTRO",
        "intro_pitch": "**dormir** (to sleep) and **morir** (to die) are the only two -ir o→ue stem-changers. Pattern: d**ue**rmo, m**ue**ro; nosotros stays unchanged (dormimos, morimos).",
        "intro_text2": "Both share an extra quirk in the preterite (durmió, murió) — but in present they follow the standard o→ue pattern.",
        "openers": [
            ("Do you sleep well?", "¿Duermes bien?"),
            ("Are you dying of hunger?", "¿Te mueres de hambre?"),
        ],
    },
    {
        "key": "mover_almorzar",
        "verbs": ["mover", "almorzar"],
        "lesson_numbers": [5, 6, 6.5],
        "title_short": "mover + almorzar",
        "intro_const": "PRESENT_O_UE_MOVER_ALMORZAR_INTRO",
        "intro_pitch": "**mover** (to move) and **almorzar** (to have lunch) follow the standard o→ue pattern. m**ue**vo, alm**ue**rzo; nosotros forms (movemos, almorzamos) stay regular.",
        "intro_text2": "almorzar is built on **almuerzo** (the noun for 'lunch'). Many other -ar verbs follow this pattern: contar, encontrar, recordar.",
        "openers": [
            ("Do you move the chair?", "¿Mueves la silla?"),
            ("Where do you have lunch?", "¿Dónde almuerzas?"),
        ],
    },
]


def emit_intro(sb: dict) -> str:
    v1, v2 = sb["verbs"]
    a1, a2 = ANSWERS[v1], ANSWERS[v2]
    mt1 = emit_mini_table(v1, a1, VERB_GLOSS_EN[v1])
    mt2 = emit_mini_table(v2, a2, VERB_GLOSS_EN[v2])
    recall = emit_recall_list([v1, v2], ANSWERS)
    return f'''{sb["intro_const"]} = {{
    "kind": "cards",
    "title": "Stem o→ue — {sb["title_short"]}",
    "cards": [
        {{
            "kind": "text",
            "title": "{sb["title_short"]}",
            "body": "{sb["intro_pitch"]}",
        }},
        {{
            "kind": "text",
            "title": "Why these two together",
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
    sid = f'grammar_present_o_ue_{sb["key"]}_{drill_idx}'
    a1, a2 = ANSWERS[v1], ANSWERS[v2]
    sentence_lit = fmt_sentence_lit(sentences)
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in drill_targets)
    intro_line = f'\n        "intro_chart": {sb["intro_const"]},' if with_intro else ""
    phases_0a = "True" if with_intro else "False"
    en_opener, es_opener = sb["openers"][drill_idx - 1]

    return f'''    "{sid}": {{
        "title": "Stem o→ue — {sb["title_short"]} ({drill_idx}/2)",
        "grammar_level": 6,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": "9JFpAFFVQzc",
        "drill_type": "conjugation",
        "tense": "present",{intro_line}
        "rule_chart": PRESENT_O_UE_RULE,
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
            "description": "Stem o→ue {sb["title_short"]} ({drill_idx}/2): {v1}, {v2}",
            "targets": [{target_lit}],
        }},
        "opener_en": "{en_opener}",
        "opener_es": "{es_opener}",
    }},'''


def emit_chat_lesson(sb: dict, lesson_number: float) -> str:
    v1, v2 = sb["verbs"]
    sid = f'grammar_present_o_ue_{sb["key"]}_chat'
    targets = []
    for i in range(5):
        targets.append((v1, DIVERSE_PRONOUNS[i]))
    for i in range(5):
        targets.append((v2, DIVERSE_PRONOUNS_2[i]))
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in targets)
    return f'''    "{sid}": {{
        "title": "Stem o→ue — {sb["title_short"]} Chat",
        "grammar_level": 6,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {{"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False}},
        "drill_sentences": [],
        "phase_2_config": {{"description": "Stem o→ue {sb["title_short"]} chat: {v1}, {v2}", "targets": [{target_lit}]}},
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
                tense_label="present-tense conjugation",
                tense_desc="Spanish simple present with o→ue stem change",
            ))
            task_meta.append((sb, drill_idx, spec))

    print(f"Authoring {len(tasks)} drill batches...")
    results = await asyncio.gather(*tasks)

    out_lines = ['"""Auto-generated by scripts/split_gl6.py — splice into grammar_situations.py.', '"""', '', '']
    out_lines.append("# ── Retire keys: grammar_present_o_ue_{1,2,3}{,_chat}")
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
