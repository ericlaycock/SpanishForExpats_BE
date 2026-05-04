"""Split GL 17.1 (Preterite Highly Irregular) into 4 sub-blocks of 2 verbs each.

Sub-blocks:
  - ser + ir (suppletive, identical fui-paradigm)
  - dar + ver
  - hacer + decir (strong stems)
  - traer + dormir (strong + e→i / o→u in 3rd persons)

Output: scripts/_gl17_1_output.py — replaces grammar_preterite_irregular_{1,2,3,4}{,_chat}.

Pipe-encoding: highly irregular preterite forms are mostly suppletive — leading
pipe on yo/tú/él/ellos forms; nosotros and ellos may share a partial stem.
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

OUTPUT = ROOT / "scripts" / "_gl17_1_output.py"

# Pipe-encoding: stem boundary before the irregular ending.
# fui/fuiste/fue/fuimos/fueron — fully suppletive, leading pipe.
ANSWERS = {
    "ser": {"yo": "|fui", "tú": "|fuiste", "él": "|fue", "ella": "|fue", "usted": "|fue",
            "nosotros": "|fuimos", "nosotras": "|fuimos",
            "ellos": "|fueron", "ellas": "|fueron", "ustedes": "|fueron"},
    "ir": {"yo": "|fui", "tú": "|fuiste", "él": "|fue", "ella": "|fue", "usted": "|fue",
           "nosotros": "|fuimos", "nosotras": "|fuimos",
           "ellos": "|fueron", "ellas": "|fueron", "ustedes": "|fueron"},
    # dar takes -er/-ir endings: di, diste, dio, dimos, dieron
    "dar": {"yo": "d|i", "tú": "d|iste", "él": "d|io", "ella": "d|io", "usted": "d|io",
            "nosotros": "d|imos", "nosotras": "d|imos",
            "ellos": "d|ieron", "ellas": "d|ieron", "ustedes": "d|ieron"},
    "ver": {"yo": "v|i", "tú": "v|iste", "él": "v|io", "ella": "v|io", "usted": "v|io",
            "nosotros": "v|imos", "nosotras": "v|imos",
            "ellos": "v|ieron", "ellas": "v|ieron", "ustedes": "v|ieron"},
    # Strong-stem: hic-/hiz-, dij-
    "hacer": {"yo": "hic|e", "tú": "hic|iste", "él": "hiz|o", "ella": "hiz|o", "usted": "hiz|o",
              "nosotros": "hic|imos", "nosotras": "hic|imos",
              "ellos": "hic|ieron", "ellas": "hic|ieron", "ustedes": "hic|ieron"},
    "decir": {"yo": "dij|e", "tú": "dij|iste", "él": "dij|o", "ella": "dij|o", "usted": "dij|o",
              "nosotros": "dij|imos", "nosotras": "dij|imos",
              "ellos": "dij|eron", "ellas": "dij|eron", "ustedes": "dij|eron"},
    # traer: traj- strong stem with -eron in 3rd plural
    "traer": {"yo": "traj|e", "tú": "traj|iste", "él": "traj|o", "ella": "traj|o", "usted": "traj|o",
              "nosotros": "traj|imos", "nosotras": "traj|imos",
              "ellos": "traj|eron", "ellas": "traj|eron", "ustedes": "traj|eron"},
    # dormir: regular except 3rd persons get o→u (durmió/durmieron)
    "dormir": {"yo": "dorm|í", "tú": "dorm|iste", "él": "d|urmió", "ella": "d|urmió", "usted": "d|urmió",
               "nosotros": "dorm|imos", "nosotras": "dorm|imos",
               "ellos": "d|urmieron", "ellas": "d|urmieron", "ustedes": "d|urmieron"},
}

VERB_GLOSS_EN = {
    "ser": "to be (identity)", "ir": "to go",
    "dar": "to give", "ver": "to see",
    "hacer": "to do/make", "decir": "to say",
    "traer": "to bring", "dormir": "to sleep",
}

SUBBLOCKS = [
    {
        "key": "ser_ir",
        "verbs": ["ser", "ir"],
        "lesson_numbers": [1, 2, 2.5],
        "title_short": "ser + ir (identical)",
        "intro_const": "PRETERITE_IRREGULAR_SER_IR_INTRO",
        "intro_pitch": "In the preterite, **ser** and **ir** share the **exact same forms**: fui, fuiste, fue, fuimos, fueron. Context tells you which one. *Fui médico* = I was a doctor. *Fui al mercado* = I went to the market.",
        "intro_text2": "These forms are the most common irregular preterites in Spanish — overlearn them.",
        "openers": [
            ("Where did you go yesterday?", "¿Adónde fuiste ayer?"),
            ("Were you a student?", "¿Fuiste estudiante?"),
        ],
    },
    {
        "key": "dar_ver",
        "verbs": ["dar", "ver"],
        "lesson_numbers": [3, 4, 4.5],
        "title_short": "dar + ver",
        "intro_const": "PRETERITE_IRREGULAR_DAR_VER_INTRO",
        "intro_pitch": "**dar** is -ar but takes the -er/-ir preterite endings, with no accents: di, diste, dio, dimos, dieron. **ver** is -er, also no accents: vi, viste, vio, vimos, vieron.",
        "intro_text2": "The accent-free yo and él forms (di, dio, vi, vio) are the giveaway here. Most other -ar / -er preterites carry accents (hablé, comí).",
        "openers": [
            ("What did you give him?", "¿Qué le diste?"),
            ("What did you see at the museum?", "¿Qué viste en el museo?"),
        ],
    },
    {
        "key": "hacer_decir",
        "verbs": ["hacer", "decir"],
        "lesson_numbers": [5, 6, 6.5],
        "title_short": "hacer + decir (strong stems)",
        "intro_const": "PRETERITE_IRREGULAR_HACER_DECIR_INTRO",
        "intro_pitch": "Strong-stem preterites: **hacer** uses **hic-** (hizo with z to keep the soft sound). **decir** uses **dij-** with a special 3rd-plural ending **-eron** (not -ieron): dijeron.",
        "intro_text2": "All strong-stem preterites share unaccented yo and él endings: -e, -iste, -o, -imos, -ieron / -eron. No accent on the yo!",
        "openers": [
            ("What did you do last weekend?", "¿Qué hiciste el fin de semana?"),
            ("What did she say?", "¿Qué dijo ella?"),
        ],
    },
    {
        "key": "traer_dormir",
        "verbs": ["traer", "dormir"],
        "lesson_numbers": [7, 8, 8.5],
        "title_short": "traer + dormir",
        "intro_const": "PRETERITE_IRREGULAR_TRAER_DORMIR_INTRO",
        "intro_pitch": "**traer** is strong-stem **traj-** with the special **-eron** ending in 3rd plural: trajeron. **dormir** is mostly regular but **o → u** in 3rd-person forms: durmió, durmieron.",
        "intro_text2": "The 3rd-person stem shift in dormir / morir mirrors what they do in the gerund (durmiendo, muriendo) — same trick.",
        "openers": [
            ("What did you bring to the party?", "¿Qué trajiste a la fiesta?"),
            ("How long did you sleep?", "¿Cuánto dormiste?"),
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
    "title": "Preterite Highly Irregular — {sb["title_short"]}",
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
    sid = f'grammar_preterite_irregular_{sb["key"]}_{drill_idx}'
    a1, a2 = ANSWERS[v1], ANSWERS[v2]
    sentence_lit = fmt_sentence_lit(sentences)
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in drill_targets)
    intro_line = f'\n        "intro_chart": {sb["intro_const"]},' if with_intro else ""
    phases_0a = "True" if with_intro else "False"
    en_opener, es_opener = sb["openers"][drill_idx - 1]

    return f'''    "{sid}": {{
        "title": "Preterite Highly Irregular — {sb["title_short"]} ({drill_idx}/2)",
        "grammar_level": 17.1,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": "Ib68zJ3q7i8",
        "drill_type": "conjugation",
        "tense": "preterite",{intro_line}
        "rule_chart": PRETERITE_IRREGULAR_RULE,
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
            "description": "Preterite Highly Irregular {sb["title_short"]} ({drill_idx}/2): {v1}, {v2}",
            "targets": [{target_lit}],
        }},
        "opener_en": "{en_opener}",
        "opener_es": "{es_opener}",
    }},'''


def emit_chat_lesson(sb: dict, lesson_number: float) -> str:
    v1, v2 = sb["verbs"]
    sid = f'grammar_preterite_irregular_{sb["key"]}_chat'
    targets = []
    for i in range(5):
        targets.append((v1, DIVERSE_PRONOUNS[i]))
    for i in range(5):
        targets.append((v2, DIVERSE_PRONOUNS_2[i]))
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in targets)
    return f'''    "{sid}": {{
        "title": "Preterite Highly Irregular — {sb["title_short"]} Chat",
        "grammar_level": 17.1,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite",
        "phases": {{"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False}},
        "drill_sentences": [],
        "phase_2_config": {{"description": "Preterite Highly Irregular {sb["title_short"]} chat: {v1}, {v2}", "targets": [{target_lit}]}},
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
                tense_label="preterite (simple past) conjugation, highly irregular",
                tense_desc="Spanish preterite — simple past for completed actions; these verbs are HIGHLY irregular. EN should use simple past ('I went', 'You did', 'They saw'). For ser+ir context disambiguates ('I was a doctor' vs 'I went to the store').",
            ))
            task_meta.append((sb, drill_idx, spec))

    print(f"Authoring {len(tasks)} drill batches...")
    results = await asyncio.gather(*tasks)

    out_lines = ['"""Auto-generated by scripts/split_gl17_1.py — splice into grammar_situations.py.', '"""', '', '']
    out_lines.append("# ── Retire keys: grammar_preterite_irregular_{1,2,3,4}{,_chat}")
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
