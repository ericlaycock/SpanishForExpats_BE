"""Split GL 5 (Spelling Changes) into 4 sub-blocks of 2 verbs each.

Sub-blocks:
  - conocer + producir (zc)
  - construir + conseguir (i→y / e→i)
  - recoger + dirigir (g→j)
  - convencer + continuar (c→z / accent shift)

Output: scripts/_gl5_output.py — splice replacing
grammar_spelling_changes_{1,2,3,4}{,_chat}.
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

OUTPUT = ROOT / "scripts" / "_gl5_output.py"

ANSWERS = {
    "conocer": {"yo": "conoz|co", "tú": "conoc|es", "él": "conoc|e", "ella": "conoc|e", "usted": "conoc|e",
                "nosotros": "conoc|emos", "nosotras": "conoc|emos",
                "ellos": "conoc|en", "ellas": "conoc|en", "ustedes": "conoc|en"},
    "producir": {"yo": "produz|co", "tú": "produc|es", "él": "produc|e", "ella": "produc|e", "usted": "produc|e",
                 "nosotros": "produc|imos", "nosotras": "produc|imos",
                 "ellos": "produc|en", "ellas": "produc|en", "ustedes": "produc|en"},
    "construir": {"yo": "constr|uyo", "tú": "constr|uyes", "él": "constr|uye", "ella": "constr|uye", "usted": "constr|uye",
                  "nosotros": "constr|uimos", "nosotras": "constr|uimos",
                  "ellos": "constr|uyen", "ellas": "constr|uyen", "ustedes": "constr|uyen"},
    "conseguir": {"yo": "consig|o", "tú": "consig|ues", "él": "consig|ue", "ella": "consig|ue", "usted": "consig|ue",
                  "nosotros": "conseg|uimos", "nosotras": "conseg|uimos",
                  "ellos": "consig|uen", "ellas": "consig|uen", "ustedes": "consig|uen"},
    "recoger": {"yo": "reco|jo", "tú": "recog|es", "él": "recog|e", "ella": "recog|e", "usted": "recog|e",
                "nosotros": "recog|emos", "nosotras": "recog|emos",
                "ellos": "recog|en", "ellas": "recog|en", "ustedes": "recog|en"},
    "dirigir": {"yo": "diri|jo", "tú": "dirig|es", "él": "dirig|e", "ella": "dirig|e", "usted": "dirig|e",
                "nosotros": "dirig|imos", "nosotras": "dirig|imos",
                "ellos": "dirig|en", "ellas": "dirig|en", "ustedes": "dirig|en"},
    "convencer": {"yo": "conven|zo", "tú": "convenc|es", "él": "convenc|e", "ella": "convenc|e", "usted": "convenc|e",
                  "nosotros": "convenc|emos", "nosotras": "convenc|emos",
                  "ellos": "convenc|en", "ellas": "convenc|en", "ustedes": "convenc|en"},
    "continuar": {"yo": "contin|úo", "tú": "contin|úas", "él": "contin|úa", "ella": "contin|úa", "usted": "contin|úa",
                  "nosotros": "contin|uamos", "nosotras": "contin|uamos",
                  "ellos": "contin|úan", "ellas": "contin|úan", "ustedes": "contin|úan"},
}

VERB_GLOSS_EN = {
    "conocer": "to know (a person/place)", "producir": "to produce",
    "construir": "to build", "conseguir": "to obtain/get",
    "recoger": "to pick up", "dirigir": "to direct",
    "convencer": "to convince", "continuar": "to continue",
}

SUBBLOCKS = [
    {
        "key": "conocer_producir",
        "verbs": ["conocer", "producir"],
        "lesson_numbers": [1, 2, 2.5],
        "title_short": "conocer + producir",
        "intro_const": "SPELLING_CHANGES_CONOCER_PRODUCIR_INTRO",
        "intro_pitch": "Verbs ending in **-cer** / **-cir** preceded by a vowel insert a **z** before -co in the yo form: conoz**co**, produz**co**. The other forms stay regular.",
        "intro_text2": "This is a spelling-only change to keep the soft /θ/ or /s/ sound before the back vowel. The pattern repeats in many useful verbs (parecer, ofrecer, traducir).",
        "openers": [
            ("Do you know my brother?", "¿Conoces a mi hermano?"),
            ("Does your country produce coffee?", "¿Tu país produce café?"),
        ],
    },
    {
        "key": "construir_conseguir",
        "verbs": ["construir", "conseguir"],
        "lesson_numbers": [3, 4, 4.5],
        "title_short": "construir + conseguir",
        "intro_const": "SPELLING_CHANGES_CONSTRUIR_CONSEGUIR_INTRO",
        "intro_pitch": "**construir** inserts a **y** in all singular and 3rd-plural forms (constru**y**o). **conseguir** drops the **u** before -o/-a (consig**o**) — a pure spelling rule to keep the /g/ hard.",
        "intro_text2": "construir's y-insertion mirrors oír (GL 4.5). conseguir's spelling shift parallels seguir, distinguir.",
        "openers": [
            ("What are you building?", "¿Qué construyes?"),
            ("Do you get good prices?", "¿Consigues buenos precios?"),
        ],
    },
    {
        "key": "recoger_dirigir",
        "verbs": ["recoger", "dirigir"],
        "lesson_numbers": [5, 6, 6.5],
        "title_short": "recoger + dirigir",
        "intro_const": "SPELLING_CHANGES_RECOGER_DIRIGIR_INTRO",
        "intro_pitch": "**-ger** / **-gir** verbs change **g → j** before -o (yo only): reco**jo**, diri**jo**. Spelling-only — the sound stays the same.",
        "intro_text2": "All other forms use plain g (recoges, diriges). Same trick repeats in coger, escoger, exigir, fingir.",
        "openers": [
            ("Do you pick up the kids?", "¿Recoges a los niños?"),
            ("Who directs the project?", "¿Quién dirige el proyecto?"),
        ],
    },
    {
        "key": "convencer_continuar",
        "verbs": ["convencer", "continuar"],
        "lesson_numbers": [7, 8, 8.5],
        "title_short": "convencer + continuar",
        "intro_const": "SPELLING_CHANGES_CONVENCER_CONTINUAR_INTRO",
        "intro_pitch": "**-cer** preceded by a consonant changes **c → z** before -o (yo only): conven**zo**, ven**zo**. **continuar** carries a written accent on the **ú** in stressed forms (continúo, continúas, continúa, continúan).",
        "intro_text2": "The accent on continuar marks a stressed vowel that would otherwise glide into a diphthong — same trick in actuar, graduarse.",
        "openers": [
            ("Can you convince him?", "¿Puedes convencerlo?"),
            ("Do you continue with the plan?", "¿Continúas con el plan?"),
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
    "title": "Spelling Changes — {sb["title_short"]}",
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
    sid = f'grammar_spelling_changes_{sb["key"]}_{drill_idx}'
    a1, a2 = ANSWERS[v1], ANSWERS[v2]
    sentence_lit = fmt_sentence_lit(sentences)
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in drill_targets)
    intro_line = f'\n        "intro_chart": {sb["intro_const"]},' if with_intro else ""
    phases_0a = "True" if with_intro else "False"
    en_opener, es_opener = sb["openers"][drill_idx - 1]

    return f'''    "{sid}": {{
        "title": "Spelling Changes — {sb["title_short"]} ({drill_idx}/2)",
        "grammar_level": 5,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": "ZxefHnILbqs",
        "drill_type": "conjugation",
        "tense": "present",{intro_line}
        "rule_chart": SPELLING_CHANGES_RULE,
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
            "description": "Spelling Changes {sb["title_short"]} ({drill_idx}/2): {v1}, {v2}",
            "targets": [{target_lit}],
        }},
        "opener_en": "{en_opener}",
        "opener_es": "{es_opener}",
    }},'''


def emit_chat_lesson(sb: dict, lesson_number: float) -> str:
    v1, v2 = sb["verbs"]
    sid = f'grammar_spelling_changes_{sb["key"]}_chat'
    targets = []
    for i in range(5):
        targets.append((v1, DIVERSE_PRONOUNS[i]))
    for i in range(5):
        targets.append((v2, DIVERSE_PRONOUNS_2[i]))
    target_lit = ", ".join(f'{{"verb": "{v}", "pronoun": "{p}"}}' for v, p in targets)
    return f'''    "{sid}": {{
        "title": "Spelling Changes — {sb["title_short"]} Chat",
        "grammar_level": 5,
        "lesson_number": {lesson_number},
        "lesson_type": "conjugation",
        "word_workload": ["{v1}", "{v2}"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {{"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False}},
        "drill_sentences": [],
        "phase_2_config": {{"description": "Spelling Changes {sb["title_short"]} chat: {v1}, {v2}", "targets": [{target_lit}]}},
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
                tense_desc="Spanish simple present (with spelling changes)",
            ))
            task_meta.append((sb, drill_idx, spec))

    print(f"Authoring {len(tasks)} drill batches...")
    results = await asyncio.gather(*tasks)

    out_lines = ['"""Auto-generated by scripts/split_gl5.py — splice into grammar_situations.py.', '"""', '', '']
    out_lines.append("# ── Retire keys: grammar_spelling_changes_{1,2,3,4}{,_chat}")
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
