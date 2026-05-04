"""Split GL 4.5 (Irregular Present II) into 4 sub-blocks of 2 verbs each.

Sub-blocks:
  - hacer + poner (yo-go pure)
  - salir + decir (yo-go + e→i in decir)
  - oír + caer (i→y in 3rd persons + yo-igo)
  - traer + valer (yo-igo + yo-go)

Output: scripts/_gl4_5_output.py — splice into grammar_situations.py replacing
the 8 retired keys: grammar_irregular_present_ii_{1,2,3,4}{,_chat}.
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

OUTPUT = ROOT / "scripts" / "_gl4_5_output.py"

# ── Pipe-encoded present-tense conjugations ──────────────────────────────────

ANSWERS = {
    "hacer": {"yo": "ha|go", "tú": "hac|es", "él": "hac|e", "ella": "hac|e", "usted": "hac|e",
              "nosotros": "hac|emos", "nosotras": "hac|emos",
              "ellos": "hac|en", "ellas": "hac|en", "ustedes": "hac|en"},
    "poner": {"yo": "pon|go", "tú": "pon|es", "él": "pon|e", "ella": "pon|e", "usted": "pon|e",
              "nosotros": "pon|emos", "nosotras": "pon|emos",
              "ellos": "pon|en", "ellas": "pon|en", "ustedes": "pon|en"},
    "salir": {"yo": "sal|go", "tú": "sal|es", "él": "sal|e", "ella": "sal|e", "usted": "sal|e",
              "nosotros": "sal|imos", "nosotras": "sal|imos",
              "ellos": "sal|en", "ellas": "sal|en", "ustedes": "sal|en"},
    "decir": {"yo": "di|go", "tú": "d|ices", "él": "d|ice", "ella": "d|ice", "usted": "d|ice",
              "nosotros": "dec|imos", "nosotras": "dec|imos",
              "ellos": "d|icen", "ellas": "d|icen", "ustedes": "d|icen"},
    "oír": {"yo": "o|igo", "tú": "o|yes", "él": "o|ye", "ella": "o|ye", "usted": "o|ye",
            "nosotros": "o|ímos", "nosotras": "o|ímos",
            "ellos": "o|yen", "ellas": "o|yen", "ustedes": "o|yen"},
    "caer": {"yo": "ca|igo", "tú": "ca|es", "él": "ca|e", "ella": "ca|e", "usted": "ca|e",
             "nosotros": "ca|emos", "nosotras": "ca|emos",
             "ellos": "ca|en", "ellas": "ca|en", "ustedes": "ca|en"},
    "traer": {"yo": "tra|igo", "tú": "tra|es", "él": "tra|e", "ella": "tra|e", "usted": "tra|e",
              "nosotros": "tra|emos", "nosotras": "tra|emos",
              "ellos": "tra|en", "ellas": "tra|en", "ustedes": "tra|en"},
    "valer": {"yo": "val|go", "tú": "val|es", "él": "val|e", "ella": "val|e", "usted": "val|e",
              "nosotros": "val|emos", "nosotras": "val|emos",
              "ellos": "val|en", "ellas": "val|en", "ustedes": "val|en"},
}

VERB_GLOSS_EN = {
    "hacer": "to do/make", "poner": "to put",
    "salir": "to leave/go out", "decir": "to say",
    "oír": "to hear", "caer": "to fall",
    "traer": "to bring", "valer": "to be worth",
}

SUBBLOCKS = [
    {
        "key": "hacer_poner",
        "verbs": ["hacer", "poner"],
        "lesson_numbers": [1, 2, 2.5],
        "title_short": "hacer + poner",
        "intro_const": "IRREGULAR_PRESENT_II_HACER_PONER_INTRO",
        "intro_pitch": "**hacer** (to do/make) and **poner** (to put) both have a yo-form that ends in **-go** (hago, pongo). Outside of yo, they conjugate like regular -er verbs.",
        "intro_text2": "This 'yo-go' pattern is one of the most common irregularities in Spanish. Once you spot it, you can predict yo for many verbs.",
        "openers": [
            ("What do you do for work?", "¿Qué haces de trabajo?"),
            ("Where do you put your keys?", "¿Dónde pones las llaves?"),
        ],
    },
    {
        "key": "salir_decir",
        "verbs": ["salir", "decir"],
        "lesson_numbers": [3, 4, 4.5],
        "title_short": "salir + decir",
        "intro_const": "IRREGULAR_PRESENT_II_SALIR_DECIR_INTRO",
        "intro_pitch": "**salir** (to leave/go out) is yo-go (salgo) and otherwise regular. **decir** (to say) is yo-go *plus* an e→i stem change (digo, dices, dice, dicen).",
        "intro_text2": "decir is unusually irregular and very high-frequency — drill it until it's automatic.",
        "openers": [
            ("What time do you leave?", "¿A qué hora sales?"),
            ("What do you say in Spanish?", "¿Qué dices en español?"),
        ],
    },
    {
        "key": "oir_caer",
        "verbs": ["oír", "caer"],
        "lesson_numbers": [5, 6, 6.5],
        "title_short": "oír + caer",
        "intro_const": "IRREGULAR_PRESENT_II_OIR_CAER_INTRO",
        "intro_pitch": "**oír** (to hear) and **caer** (to fall) both take **-igo** in yo (oigo, caigo). oír also inserts a **y** in tú/él/ellos (oyes, oye, oyen).",
        "intro_text2": "The y-insertion in oír makes the vowel cluster pronounceable. Watch for the same trick in construir / huir later (GL 5).",
        "openers": [
            ("Do you hear the music?", "¿Oyes la música?"),
            ("Do you fall a lot here?", "¿Te caes mucho aquí?"),
        ],
    },
    {
        "key": "traer_valer",
        "verbs": ["traer", "valer"],
        "lesson_numbers": [7, 8, 8.5],
        "title_short": "traer + valer",
        "intro_const": "IRREGULAR_PRESENT_II_TRAER_VALER_INTRO",
        "intro_pitch": "**traer** (to bring) takes **-igo** in yo (traigo). **valer** (to be worth) takes **-go** in yo (valgo). Outside yo, both behave like regular -er verbs.",
        "intro_text2": "valer shows up in fixed phrases like *vale la pena* (it's worth it) and *¿cuánto vale?* (how much is it?).",
        "openers": [
            ("What are you bringing?", "¿Qué traes?"),
            ("How much is this worth?", "¿Cuánto vale esto?"),
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
    "title": "Irregular Present II — {sb["title_short"]}",
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
    sid = f'grammar_irregular_present_ii_{sb["key"]}_{drill_idx}'
    a1, a2 = ANSWERS[v1], ANSWERS[v2]
    sentence_lit = fmt_sentence_lit(sentences)
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in drill_targets)
    intro_line = f'\n        "intro_chart": {sb["intro_const"]},' if with_intro else ""
    phases_0a = "True" if with_intro else "False"
    en_opener, es_opener = sb["openers"][drill_idx - 1]

    return f'''    "{sid}": {{
        "title": "Irregular Present II — {sb["title_short"]} ({drill_idx}/2)",
        "grammar_level": 4.5,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": "Bg9XcrNn3LL",
        "drill_type": "conjugation",
        "tense": "present",{intro_line}
        "rule_chart": IRREGULAR_PRESENT_II_RULE,
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
            "description": "Irregular Present II {sb["title_short"]} ({drill_idx}/2): {v1}, {v2}",
            "targets": [{target_lit}],
        }},
        "opener_en": "{en_opener}",
        "opener_es": "{es_opener}",
    }},'''


def emit_chat_lesson(sb: dict, lesson_number: float) -> str:
    v1, v2 = sb["verbs"]
    sid = f'grammar_irregular_present_ii_{sb["key"]}_chat'
    targets = []
    for i in range(5):
        targets.append((v1, DIVERSE_PRONOUNS[i]))
    for i in range(5):
        targets.append((v2, DIVERSE_PRONOUNS_2[i]))
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in targets)
    return f'''    "{sid}": {{
        "title": "Irregular Present II — {sb["title_short"]} Chat",
        "grammar_level": 4.5,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {{"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False}},
        "drill_sentences": [],
        "phase_2_config": {{"description": "Irregular Present II {sb["title_short"]} chat: {v1}, {v2}", "targets": [{target_lit}]}},
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
                tense_desc="Spanish simple present (irregular)",
            ))
            task_meta.append((sb, drill_idx, spec))

    print(f"Authoring {len(tasks)} drill batches of 10 sentences each...")
    results = await asyncio.gather(*tasks)

    out_lines = ['"""Auto-generated by scripts/split_gl4_5.py — splice into grammar_situations.py.', '"""', '', '']
    out_lines.append("# ── Retire these keys when splicing ────────────────────────────────────")
    out_lines.append("# grammar_irregular_present_ii_1, grammar_irregular_present_ii_2,")
    out_lines.append("# grammar_irregular_present_ii_3, grammar_irregular_present_ii_4,")
    out_lines.append("# and their _chat companions.")
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
    print(f"Lines: {len(out_lines)}")


if __name__ == "__main__":
    asyncio.run(main())
