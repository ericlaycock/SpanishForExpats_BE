"""Split GL 7 (Stem-changers e→ie) into 3 sub-blocks of 2 verbs each.

Sub-blocks:
  - querer + pensar
  - cerrar + empezar
  - entender + preferir

Output: scripts/_gl7_output.py — replaces grammar_present_e_ie_{1,2,3}{,_chat}.
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

OUTPUT = ROOT / "scripts" / "_gl7_output.py"

ANSWERS = {
    "querer": {"yo": "qu|iero", "tú": "qu|ieres", "él": "qu|iere", "ella": "qu|iere", "usted": "qu|iere",
               "nosotros": "quer|emos", "nosotras": "quer|emos",
               "ellos": "qu|ieren", "ellas": "qu|ieren", "ustedes": "qu|ieren"},
    "pensar": {"yo": "p|ienso", "tú": "p|iensas", "él": "p|iensa", "ella": "p|iensa", "usted": "p|iensa",
               "nosotros": "pens|amos", "nosotras": "pens|amos",
               "ellos": "p|iensan", "ellas": "p|iensan", "ustedes": "p|iensan"},
    "cerrar": {"yo": "c|ierro", "tú": "c|ierras", "él": "c|ierra", "ella": "c|ierra", "usted": "c|ierra",
               "nosotros": "cerr|amos", "nosotras": "cerr|amos",
               "ellos": "c|ierran", "ellas": "c|ierran", "ustedes": "c|ierran"},
    "empezar": {"yo": "emp|iezo", "tú": "emp|iezas", "él": "emp|ieza", "ella": "emp|ieza", "usted": "emp|ieza",
                "nosotros": "empez|amos", "nosotras": "empez|amos",
                "ellos": "emp|iezan", "ellas": "emp|iezan", "ustedes": "emp|iezan"},
    "entender": {"yo": "ent|iendo", "tú": "ent|iendes", "él": "ent|iende", "ella": "ent|iende", "usted": "ent|iende",
                 "nosotros": "entend|emos", "nosotras": "entend|emos",
                 "ellos": "ent|ienden", "ellas": "ent|ienden", "ustedes": "ent|ienden"},
    "preferir": {"yo": "pref|iero", "tú": "pref|ieres", "él": "pref|iere", "ella": "pref|iere", "usted": "pref|iere",
                 "nosotros": "prefer|imos", "nosotras": "prefer|imos",
                 "ellos": "pref|ieren", "ellas": "pref|ieren", "ustedes": "pref|ieren"},
}

VERB_GLOSS_EN = {
    "querer": "to want", "pensar": "to think",
    "cerrar": "to close", "empezar": "to begin",
    "entender": "to understand", "preferir": "to prefer",
}

SUBBLOCKS = [
    {
        "key": "querer_pensar",
        "verbs": ["querer", "pensar"],
        "lesson_numbers": [1, 2, 2.5],
        "title_short": "querer + pensar",
        "intro_const": "PRESENT_E_IE_QUERER_PENSAR_INTRO",
        "intro_pitch": "**e → ie** in stressed syllables: qu**ie**ro, p**ie**nso. Nosotros / nosotras stay regular (queremos, pensamos).",
        "intro_text2": "**querer** is 'to want' (and 'to love' with people). **pensar** is 'to think' or 'to plan' (pienso ir = I plan to go).",
        "openers": [
            ("What do you want?", "¿Qué quieres?"),
            ("What are you thinking?", "¿Qué piensas?"),
        ],
    },
    {
        "key": "cerrar_empezar",
        "verbs": ["cerrar", "empezar"],
        "lesson_numbers": [3, 4, 4.5],
        "title_short": "cerrar + empezar",
        "intro_const": "PRESENT_E_IE_CERRAR_EMPEZAR_INTRO",
        "intro_pitch": "Same e → ie pattern: c**ie**rro, emp**ie**zo. The **z** in empezar / empiezo is part of the stem; no spelling change needed in present tense.",
        "intro_text2": "**cerrar** is 'to close' (a door, a deal). **empezar** is 'to begin'; followed by *a + infinitive* (empiezo a trabajar = I'm starting to work).",
        "openers": [
            ("Do you close the windows?", "¿Cierras las ventanas?"),
            ("When do you start work?", "¿Cuándo empiezas a trabajar?"),
        ],
    },
    {
        "key": "entender_preferir",
        "verbs": ["entender", "preferir"],
        "lesson_numbers": [5, 6, 6.5],
        "title_short": "entender + preferir",
        "intro_const": "PRESENT_E_IE_ENTENDER_PREFERIR_INTRO",
        "intro_pitch": "Same e → ie pattern: ent**ie**ndo, pref**ie**ro. **preferir** is one of the few -ir verbs in this group; it shares the change with sentir, mentir.",
        "intro_text2": "**entender** is 'to understand' (synonym: comprender). **preferir** takes a noun or an infinitive: prefiero el café, prefiero salir.",
        "openers": [
            ("Do you understand me?", "¿Me entiendes?"),
            ("What do you prefer?", "¿Qué prefieres?"),
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
    "title": "Stem e→ie — {sb["title_short"]}",
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
    sid = f'grammar_present_e_ie_{sb["key"]}_{drill_idx}'
    a1, a2 = ANSWERS[v1], ANSWERS[v2]
    sentence_lit = fmt_sentence_lit(sentences)
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in drill_targets)
    intro_line = f'\n        "intro_chart": {sb["intro_const"]},' if with_intro else ""
    phases_0a = "True" if with_intro else "False"
    en_opener, es_opener = sb["openers"][drill_idx - 1]

    return f'''    "{sid}": {{
        "title": "Stem e→ie — {sb["title_short"]} ({drill_idx}/2)",
        "grammar_level": 7,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": "rk0AwBA9PEa",
        "drill_type": "conjugation",
        "tense": "present",{intro_line}
        "rule_chart": PRESENT_E_IE_RULE,
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
            "description": "Stem e→ie {sb["title_short"]} ({drill_idx}/2): {v1}, {v2}",
            "targets": [{target_lit}],
        }},
        "opener_en": "{en_opener}",
        "opener_es": "{es_opener}",
    }},'''


def emit_chat_lesson(sb: dict, lesson_number: float) -> str:
    v1, v2 = sb["verbs"]
    sid = f'grammar_present_e_ie_{sb["key"]}_chat'
    targets = []
    for i in range(5):
        targets.append((v1, DIVERSE_PRONOUNS[i]))
    for i in range(5):
        targets.append((v2, DIVERSE_PRONOUNS_2[i]))
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in targets)
    return f'''    "{sid}": {{
        "title": "Stem e→ie — {sb["title_short"]} Chat",
        "grammar_level": 7,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {{"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False}},
        "drill_sentences": [],
        "phase_2_config": {{"description": "Stem e→ie {sb["title_short"]} chat: {v1}, {v2}", "targets": [{target_lit}]}},
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
                tense_desc="Spanish simple present with e→ie stem change",
            ))
            task_meta.append((sb, drill_idx, spec))

    print(f"Authoring {len(tasks)} drill batches...")
    results = await asyncio.gather(*tasks)

    out_lines = ['"""Auto-generated by scripts/split_gl7.py — splice into grammar_situations.py.', '"""', '', '']
    out_lines.append("# ── Retire keys: grammar_present_e_ie_{1,2,3}{,_chat}")
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
