"""Split GL 8 (Stem-changers e→i) into 3 sub-blocks of 2 verbs each.

Sub-blocks:
  - pedir + servir
  - repetir + seguir
  - vestir + elegir

Output: scripts/_gl8_output.py — replaces grammar_present_e_i_{1,2,3}{,_chat}.
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

OUTPUT = ROOT / "scripts" / "_gl8_output.py"

ANSWERS = {
    "pedir": {"yo": "p|ido", "tú": "p|ides", "él": "p|ide", "ella": "p|ide", "usted": "p|ide",
              "nosotros": "ped|imos", "nosotras": "ped|imos",
              "ellos": "p|iden", "ellas": "p|iden", "ustedes": "p|iden"},
    "servir": {"yo": "s|irvo", "tú": "s|irves", "él": "s|irve", "ella": "s|irve", "usted": "s|irve",
               "nosotros": "serv|imos", "nosotras": "serv|imos",
               "ellos": "s|irven", "ellas": "s|irven", "ustedes": "s|irven"},
    "repetir": {"yo": "rep|ito", "tú": "rep|ites", "él": "rep|ite", "ella": "rep|ite", "usted": "rep|ite",
                "nosotros": "repet|imos", "nosotras": "repet|imos",
                "ellos": "rep|iten", "ellas": "rep|iten", "ustedes": "rep|iten"},
    "seguir": {"yo": "s|igo", "tú": "s|igues", "él": "s|igue", "ella": "s|igue", "usted": "s|igue",
               "nosotros": "segu|imos", "nosotras": "segu|imos",
               "ellos": "s|iguen", "ellas": "s|iguen", "ustedes": "s|iguen"},
    "vestir": {"yo": "v|isto", "tú": "v|istes", "él": "v|iste", "ella": "v|iste", "usted": "v|iste",
               "nosotros": "vest|imos", "nosotras": "vest|imos",
               "ellos": "v|isten", "ellas": "v|isten", "ustedes": "v|isten"},
    "elegir": {"yo": "el|ijo", "tú": "el|iges", "él": "el|ige", "ella": "el|ige", "usted": "el|ige",
               "nosotros": "eleg|imos", "nosotras": "eleg|imos",
               "ellos": "el|igen", "ellas": "el|igen", "ustedes": "el|igen"},
}

VERB_GLOSS_EN = {
    "pedir": "to ask for/request", "servir": "to serve",
    "repetir": "to repeat", "seguir": "to follow",
    "vestir": "to dress", "elegir": "to choose",
}

SUBBLOCKS = [
    {
        "key": "pedir_servir",
        "verbs": ["pedir", "servir"],
        "lesson_numbers": [1, 2, 2.5],
        "title_short": "pedir + servir",
        "intro_const": "PRESENT_E_I_PEDIR_SERVIR_INTRO",
        "intro_pitch": "**e → i** in stressed syllables (only -ir verbs do this): p**i**do, s**i**rvo. Nosotros / nosotras stay regular (pedimos, servimos).",
        "intro_text2": "**pedir** is 'to ask for' — used for ordering food, requesting things. **servir** is 'to serve' (food, a purpose).",
        "openers": [
            ("What do you order?", "¿Qué pides?"),
            ("Do they serve breakfast?", "¿Sirven desayuno?"),
        ],
    },
    {
        "key": "repetir_seguir",
        "verbs": ["repetir", "seguir"],
        "lesson_numbers": [3, 4, 4.5],
        "title_short": "repetir + seguir",
        "intro_const": "PRESENT_E_I_REPETIR_SEGUIR_INTRO",
        "intro_pitch": "Same e → i pattern: rep**i**to, s**i**go. **seguir** drops the **u** before -o/-a (yo sigo, not 'siguo') — same spelling rule we saw with conseguir.",
        "intro_text2": "**repetir** is 'to repeat' (a word, an action). **seguir** is 'to follow' or 'to keep doing': sigo trabajando = I keep working.",
        "openers": [
            ("Can you repeat that?", "¿Puedes repetir?"),
            ("Do you follow me?", "¿Me sigues?"),
        ],
    },
    {
        "key": "vestir_elegir",
        "verbs": ["vestir", "elegir"],
        "lesson_numbers": [5, 6, 6.5],
        "title_short": "vestir + elegir",
        "intro_const": "PRESENT_E_I_VESTIR_ELEGIR_INTRO",
        "intro_pitch": "Same e → i pattern: v**i**sto, el**i**jo. **elegir** changes **g → j** before -o (spelling-only): yo el**ijo**.",
        "intro_text2": "**vestir** is 'to dress' (often reflexive: vestirse = to get dressed). **elegir** is 'to choose'.",
        "openers": [
            ("How do you dress for work?", "¿Cómo te vistes para el trabajo?"),
            ("Which one do you choose?", "¿Cuál eliges?"),
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
    "title": "Stem e→i — {sb["title_short"]}",
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
    sid = f'grammar_present_e_i_{sb["key"]}_{drill_idx}'
    a1, a2 = ANSWERS[v1], ANSWERS[v2]
    sentence_lit = fmt_sentence_lit(sentences)
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in drill_targets)
    intro_line = f'\n        "intro_chart": {sb["intro_const"]},' if with_intro else ""
    phases_0a = "True" if with_intro else "False"
    en_opener, es_opener = sb["openers"][drill_idx - 1]

    return f'''    "{sid}": {{
        "title": "Stem e→i — {sb["title_short"]} ({drill_idx}/2)",
        "grammar_level": 8,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": "L8M2P3RDsfx",
        "drill_type": "conjugation",
        "tense": "present",{intro_line}
        "rule_chart": PRESENT_E_I_RULE,
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
            "description": "Stem e→i {sb["title_short"]} ({drill_idx}/2): {v1}, {v2}",
            "targets": [{target_lit}],
        }},
        "opener_en": "{en_opener}",
        "opener_es": "{es_opener}",
    }},'''


def emit_chat_lesson(sb: dict, lesson_number: float) -> str:
    v1, v2 = sb["verbs"]
    sid = f'grammar_present_e_i_{sb["key"]}_chat'
    targets = []
    for i in range(5):
        targets.append((v1, DIVERSE_PRONOUNS[i]))
    for i in range(5):
        targets.append((v2, DIVERSE_PRONOUNS_2[i]))
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in targets)
    return f'''    "{sid}": {{
        "title": "Stem e→i — {sb["title_short"]} Chat",
        "grammar_level": 8,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {{"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False}},
        "drill_sentences": [],
        "phase_2_config": {{"description": "Stem e→i {sb["title_short"]} chat: {v1}, {v2}", "targets": [{target_lit}]}},
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
                tense_desc="Spanish simple present with e→i stem change",
            ))
            task_meta.append((sb, drill_idx, spec))

    print(f"Authoring {len(tasks)} drill batches...")
    results = await asyncio.gather(*tasks)

    out_lines = ['"""Auto-generated by scripts/split_gl8.py — splice into grammar_situations.py.', '"""', '', '']
    out_lines.append("# ── Retire keys: grammar_present_e_i_{1,2,3}{,_chat}")
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
