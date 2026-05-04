"""Split GL 17 (Preterite Regular) into 3 sub-blocks of 2 verbs each.

Sub-blocks:
  - hablar + encontrar (-AR)
  - comer + beber (-ER)
  - salir + unir (-IR; -IR shares -ER endings in preterite)

Output: scripts/_gl17_output.py — replaces grammar_preterite_regular_{1,2,3}{,_chat}.

Pipe-encoding: regular preterite splits between the unchanged stem and the
inflected ending. -AR endings: -é, -aste, -ó, -amos, -aron. -ER/-IR endings:
-í, -iste, -ió, -imos, -ieron.
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

OUTPUT = ROOT / "scripts" / "_gl17_output.py"


def ar_pret(stem: str) -> dict:
    return {
        "yo": f"{stem}|é", "tú": f"{stem}|aste",
        "él": f"{stem}|ó", "ella": f"{stem}|ó", "usted": f"{stem}|ó",
        "nosotros": f"{stem}|amos", "nosotras": f"{stem}|amos",
        "ellos": f"{stem}|aron", "ellas": f"{stem}|aron", "ustedes": f"{stem}|aron",
    }


def er_ir_pret(stem: str) -> dict:
    return {
        "yo": f"{stem}|í", "tú": f"{stem}|iste",
        "él": f"{stem}|ió", "ella": f"{stem}|ió", "usted": f"{stem}|ió",
        "nosotros": f"{stem}|imos", "nosotras": f"{stem}|imos",
        "ellos": f"{stem}|ieron", "ellas": f"{stem}|ieron", "ustedes": f"{stem}|ieron",
    }


ANSWERS = {
    "hablar": ar_pret("habl"),
    "encontrar": ar_pret("encontr"),
    "comer": er_ir_pret("com"),
    "beber": er_ir_pret("beb"),
    "salir": er_ir_pret("sal"),
    "unir": er_ir_pret("un"),
}

VERB_GLOSS_EN = {
    "hablar": "to speak", "encontrar": "to find",
    "comer": "to eat", "beber": "to drink",
    "salir": "to leave/go out", "unir": "to unite/join",
}

SUBBLOCKS = [
    {
        "key": "hablar_encontrar",
        "verbs": ["hablar", "encontrar"],
        "lesson_numbers": [1, 2, 2.5],
        "title_short": "hablar + encontrar (-ar)",
        "intro_const": "PRETERITE_REGULAR_HABLAR_ENCONTRAR_INTRO",
        "intro_pitch": "**Preterite** is the simple past for completed actions: 'I spoke,' 'I found.' For -ar verbs, the endings are **-é, -aste, -ó, -amos, -aron**. Note the accents on the yo and él forms.",
        "intro_text2": "encontrar is normally an o→ue stem-changer in the present (encuentro), but in the preterite it stays regular: encontré, encontraste...",
        "openers": [
            ("What did you say yesterday?", "¿Qué hablaste ayer?"),
            ("Where did you find your keys?", "¿Dónde encontraste tus llaves?"),
        ],
    },
    {
        "key": "comer_beber",
        "verbs": ["comer", "beber"],
        "lesson_numbers": [3, 4, 4.5],
        "title_short": "comer + beber (-er)",
        "intro_const": "PRETERITE_REGULAR_COMER_BEBER_INTRO",
        "intro_pitch": "For regular -er verbs in the preterite, the endings are **-í, -iste, -ió, -imos, -ieron**. Like -ar, the yo and él forms carry an accent.",
        "intro_text2": "These same endings are shared by regular -ir verbs (you'll see in the next sub-block).",
        "openers": [
            ("What did you eat for lunch?", "¿Qué comiste para el almuerzo?"),
            ("What did you drink at the party?", "¿Qué bebiste en la fiesta?"),
        ],
    },
    {
        "key": "salir_unir",
        "verbs": ["salir", "unir"],
        "lesson_numbers": [5, 6, 6.5],
        "title_short": "salir + unir (-ir)",
        "intro_const": "PRETERITE_REGULAR_SALIR_UNIR_INTRO",
        "intro_pitch": "Regular -ir verbs use the **same preterite endings as -er**: -í, -iste, -ió, -imos, -ieron. salí, saliste, salió...",
        "intro_text2": "salir is yo-go in present (salgo) but completely regular in the preterite. unir is straightforward in both tenses.",
        "openers": [
            ("What time did you leave?", "¿A qué hora saliste?"),
            ("Did the team unite?", "¿Se unió el equipo?"),
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
    "title": "Preterite Regular — {sb["title_short"]}",
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
    sid = f'grammar_preterite_regular_{sb["key"]}_{drill_idx}'
    a1, a2 = ANSWERS[v1], ANSWERS[v2]
    sentence_lit = fmt_sentence_lit(sentences)
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in drill_targets)
    intro_line = f'\n        "intro_chart": {sb["intro_const"]},' if with_intro else ""
    phases_0a = "True" if with_intro else "False"
    en_opener, es_opener = sb["openers"][drill_idx - 1]

    return f'''    "{sid}": {{
        "title": "Preterite Regular — {sb["title_short"]} ({drill_idx}/2)",
        "grammar_level": 17,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": "uBOH6A3vO0U",
        "drill_type": "conjugation",
        "tense": "preterite",{intro_line}
        "rule_chart": PRETERITE_REGULAR_RULE,
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
            "description": "Preterite Regular {sb["title_short"]} ({drill_idx}/2): {v1}, {v2}",
            "targets": [{target_lit}],
        }},
        "opener_en": "{en_opener}",
        "opener_es": "{es_opener}",
    }},'''


def emit_chat_lesson(sb: dict, lesson_number: float) -> str:
    v1, v2 = sb["verbs"]
    sid = f'grammar_preterite_regular_{sb["key"]}_chat'
    targets = []
    for i in range(5):
        targets.append((v1, DIVERSE_PRONOUNS[i]))
    for i in range(5):
        targets.append((v2, DIVERSE_PRONOUNS_2[i]))
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in targets)
    return f'''    "{sid}": {{
        "title": "Preterite Regular — {sb["title_short"]} Chat",
        "grammar_level": 17,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite",
        "phases": {{"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False}},
        "drill_sentences": [],
        "phase_2_config": {{"description": "Preterite Regular {sb["title_short"]} chat: {v1}, {v2}", "targets": [{target_lit}]}},
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
                tense_label="preterite (simple past) conjugation",
                tense_desc="Spanish preterite — simple past tense for completed actions. EN should use simple past ('I spoke', 'You ate', 'They drank').",
            ))
            task_meta.append((sb, drill_idx, spec))

    print(f"Authoring {len(tasks)} drill batches...")
    results = await asyncio.gather(*tasks)

    out_lines = ['"""Auto-generated by scripts/split_gl17.py — splice into grammar_situations.py.', '"""', '', '']
    out_lines.append("# ── Retire keys: grammar_preterite_regular_{1,2,3}{,_chat}")
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
