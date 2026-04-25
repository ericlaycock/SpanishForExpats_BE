"""Generate the 12 missing GL units' situation dicts and append to
`app/data/grammar_situations.py`.

Invocation: `./venv/bin/python scripts/build_grammar_lessons.py`

Emits ~76 new GRAMMAR_SITUATIONS entries following the drill-drill-chat
cluster convention agreed with the user (1–2 verbs per drill, chat pulls
5 conjugations from each preceding drill).

Architecture:
- Regular conjugations are computed (imperfect, future, conditional, present
  + imperfect subjunctive). Irregulars are hand-curated as override dicts.
- Drill sentences are templated from a small bilingual sentence pool keyed
  by tense + pronoun + verb. Hand-edit later if any read awkwardly.
- The output is written to a temp file then SPLICED into the existing
  `grammar_situations.py` just before the closing `}` of GRAMMAR_SITUATIONS.
- New verbs not already in GRAMMAR_WORD_TRANSLATIONS get appended to that
  dict via a separate splice.

Idempotency: if a generated key already exists in GRAMMAR_SITUATIONS, the
splice skips it (so re-running the script is safe).
"""
from __future__ import annotations

import random
import re
from pathlib import Path
from typing import Optional

random.seed(7)  # deterministic targets so re-runs produce the same file

ALL_PRONOUNS = ["yo", "tú", "él", "ella", "usted", "nosotros", "nosotras", "ellos", "ellas", "ustedes"]
DIVERSE_PRONOUNS = ["ella", "ellas", "nosotras", "usted", "ustedes", "yo", "tú", "él", "nosotros", "ellos"]


# ── Regular conjugation rules ────────────────────────────────────────────────


def _stem(verb: str) -> str:
    return verb[:-2]


def _ending(verb: str) -> str:
    return verb[-2:]


def regular_imperfect(verb: str) -> dict[str, str]:
    """Imperfect: -ar uses -aba family, -er/-ir uses -ía family."""
    s = _stem(verb)
    if _ending(verb) == "ar":
        return {
            "yo": f"{s}aba", "tú": f"{s}abas", "él": f"{s}aba", "ella": f"{s}aba", "usted": f"{s}aba",
            "nosotros": f"{s}ábamos", "nosotras": f"{s}ábamos",
            "ellos": f"{s}aban", "ellas": f"{s}aban", "ustedes": f"{s}aban",
        }
    return {
        "yo": f"{s}ía", "tú": f"{s}ías", "él": f"{s}ía", "ella": f"{s}ía", "usted": f"{s}ía",
        "nosotros": f"{s}íamos", "nosotras": f"{s}íamos",
        "ellos": f"{s}ían", "ellas": f"{s}ían", "ustedes": f"{s}ían",
    }


def regular_future(verb: str, root: Optional[str] = None) -> dict[str, str]:
    """Future: infinitive + -é/-ás/-á/-emos/-án.  `root` overrides for irregulars."""
    base = root if root is not None else verb
    return {
        "yo": f"{base}é", "tú": f"{base}ás", "él": f"{base}á", "ella": f"{base}á", "usted": f"{base}á",
        "nosotros": f"{base}emos", "nosotras": f"{base}emos",
        "ellos": f"{base}án", "ellas": f"{base}án", "ustedes": f"{base}án",
    }


def regular_conditional(verb: str, root: Optional[str] = None) -> dict[str, str]:
    """Conditional: infinitive + -ía family (same irregular roots as future)."""
    base = root if root is not None else verb
    return {
        "yo": f"{base}ía", "tú": f"{base}ías", "él": f"{base}ía", "ella": f"{base}ía", "usted": f"{base}ía",
        "nosotros": f"{base}íamos", "nosotras": f"{base}íamos",
        "ellos": f"{base}ían", "ellas": f"{base}ían", "ustedes": f"{base}ían",
    }


def regular_present_subj(verb: str) -> dict[str, str]:
    """Present subjunctive: -ar → -e family, -er/-ir → -a family (off the yo-form stem)."""
    s = _stem(verb)
    if _ending(verb) == "ar":
        return {
            "yo": f"{s}e", "tú": f"{s}es", "él": f"{s}e", "ella": f"{s}e", "usted": f"{s}e",
            "nosotros": f"{s}emos", "nosotras": f"{s}emos",
            "ellos": f"{s}en", "ellas": f"{s}en", "ustedes": f"{s}en",
        }
    return {
        "yo": f"{s}a", "tú": f"{s}as", "él": f"{s}a", "ella": f"{s}a", "usted": f"{s}a",
        "nosotros": f"{s}amos", "nosotras": f"{s}amos",
        "ellos": f"{s}an", "ellas": f"{s}an", "ustedes": f"{s}an",
    }


def regular_imperfect_subj(verb: str) -> dict[str, str]:
    """Imperfect subjunctive (-ra form): from preterite 3rd-pl stem."""
    s = _stem(verb)
    if _ending(verb) == "ar":
        return {
            "yo": f"{s}ara", "tú": f"{s}aras", "él": f"{s}ara", "ella": f"{s}ara", "usted": f"{s}ara",
            "nosotros": f"{s}áramos", "nosotras": f"{s}áramos",
            "ellos": f"{s}aran", "ellas": f"{s}aran", "ustedes": f"{s}aran",
        }
    return {
        "yo": f"{s}iera", "tú": f"{s}ieras", "él": f"{s}iera", "ella": f"{s}iera", "usted": f"{s}iera",
        "nosotros": f"{s}iéramos", "nosotras": f"{s}iéramos",
        "ellos": f"{s}ieran", "ellas": f"{s}ieran", "ustedes": f"{s}ieran",
    }


# ── Hand-curated irregulars ──────────────────────────────────────────────────


IMPERFECT_IRREGULAR = {
    "ir": {"yo": "iba", "tú": "ibas", "él": "iba", "ella": "iba", "usted": "iba",
           "nosotros": "íbamos", "nosotras": "íbamos", "ellos": "iban", "ellas": "iban", "ustedes": "iban"},
    "ser": {"yo": "era", "tú": "eras", "él": "era", "ella": "era", "usted": "era",
            "nosotros": "éramos", "nosotras": "éramos", "ellos": "eran", "ellas": "eran", "ustedes": "eran"},
    "ver": {"yo": "veía", "tú": "veías", "él": "veía", "ella": "veía", "usted": "veía",
            "nosotros": "veíamos", "nosotras": "veíamos", "ellos": "veían", "ellas": "veían", "ustedes": "veían"},
}

# Future / conditional share these stems
FUT_COND_IRREGULAR_ROOTS = {
    "tener": "tendr", "hacer": "har", "decir": "dir", "poder": "podr",
    "saber": "sabr", "querer": "querr", "venir": "vendr", "salir": "saldr",
    "poner": "pondr",
}

PRESENT_SUBJ_IRREGULAR = {
    "ser": {"yo": "sea", "tú": "seas", "él": "sea", "ella": "sea", "usted": "sea",
            "nosotros": "seamos", "nosotras": "seamos", "ellos": "sean", "ellas": "sean", "ustedes": "sean"},
    "estar": {"yo": "esté", "tú": "estés", "él": "esté", "ella": "esté", "usted": "esté",
              "nosotros": "estemos", "nosotras": "estemos", "ellos": "estén", "ellas": "estén", "ustedes": "estén"},
    "ir": {"yo": "vaya", "tú": "vayas", "él": "vaya", "ella": "vaya", "usted": "vaya",
           "nosotros": "vayamos", "nosotras": "vayamos", "ellos": "vayan", "ellas": "vayan", "ustedes": "vayan"},
    "dar": {"yo": "dé", "tú": "des", "él": "dé", "ella": "dé", "usted": "dé",
            "nosotros": "demos", "nosotras": "demos", "ellos": "den", "ellas": "den", "ustedes": "den"},
    "saber": {"yo": "sepa", "tú": "sepas", "él": "sepa", "ella": "sepa", "usted": "sepa",
              "nosotros": "sepamos", "nosotras": "sepamos", "ellos": "sepan", "ellas": "sepan", "ustedes": "sepan"},
    "haber": {"yo": "haya", "tú": "hayas", "él": "haya", "ella": "haya", "usted": "haya",
              "nosotros": "hayamos", "nosotras": "hayamos", "ellos": "hayan", "ellas": "hayan", "ustedes": "hayan"},
}

# Imperfect subjunctive stems (from preterite 3rd plural, drop -ron, add -ra family)
IMPERFECT_SUBJ_IRREGULAR_STEMS = {
    "ser": "fue", "ir": "fue",
    "tener": "tuvie", "querer": "quisie", "hacer": "hicie", "decir": "dije",
    "poder": "pudie", "venir": "vinie", "estar": "estuvie", "saber": "supie",
    "poner": "pusie", "haber": "hubie",
}


def imperfect_subj_from_stem(stem: str) -> dict[str, str]:
    return {
        "yo": f"{stem}ra", "tú": f"{stem}ras", "él": f"{stem}ra", "ella": f"{stem}ra", "usted": f"{stem}ra",
        "nosotros": f"{stem}´ramos".replace("e´", "é").replace("o´", "ó").replace("i´", "í"),
        "nosotras": f"{stem}´ramos".replace("e´", "é").replace("o´", "ó").replace("i´", "í"),
        "ellos": f"{stem}ran", "ellas": f"{stem}ran", "ustedes": f"{stem}ran",
    }


# Preterite spelling changes — only the irregular forms (mostly yo or 3rd-pers)
PRETERITE_SPELLING = {
    # g→gu in yo
    "pagar": {"yo": "pagué", "tú": "pagaste", "él": "pagó", "ella": "pagó", "usted": "pagó",
              "nosotros": "pagamos", "nosotras": "pagamos", "ellos": "pagaron", "ellas": "pagaron", "ustedes": "pagaron"},
    "jugar": {"yo": "jugué", "tú": "jugaste", "él": "jugó", "ella": "jugó", "usted": "jugó",
              "nosotros": "jugamos", "nosotras": "jugamos", "ellos": "jugaron", "ellas": "jugaron", "ustedes": "jugaron"},
    # c→qu in yo
    "buscar": {"yo": "busqué", "tú": "buscaste", "él": "buscó", "ella": "buscó", "usted": "buscó",
               "nosotros": "buscamos", "nosotras": "buscamos", "ellos": "buscaron", "ellas": "buscaron", "ustedes": "buscaron"},
    "tocar": {"yo": "toqué", "tú": "tocaste", "él": "tocó", "ella": "tocó", "usted": "tocó",
              "nosotros": "tocamos", "nosotras": "tocamos", "ellos": "tocaron", "ellas": "tocaron", "ustedes": "tocaron"},
    # z→c in yo
    "empezar": {"yo": "empecé", "tú": "empezaste", "él": "empezó", "ella": "empezó", "usted": "empezó",
                "nosotros": "empezamos", "nosotras": "empezamos", "ellos": "empezaron", "ellas": "empezaron", "ustedes": "empezaron"},
    "almorzar": {"yo": "almorcé", "tú": "almorzaste", "él": "almorzó", "ella": "almorzó", "usted": "almorzó",
                 "nosotros": "almorzamos", "nosotras": "almorzamos", "ellos": "almorzaron", "ellas": "almorzaron", "ustedes": "almorzaron"},
    # i→y in 3rd-person
    "creer": {"yo": "creí", "tú": "creíste", "él": "creyó", "ella": "creyó", "usted": "creyó",
              "nosotros": "creímos", "nosotras": "creímos", "ellos": "creyeron", "ellas": "creyeron", "ustedes": "creyeron"},
    "leer": {"yo": "leí", "tú": "leíste", "él": "leyó", "ella": "leyó", "usted": "leyó",
             "nosotros": "leímos", "nosotras": "leímos", "ellos": "leyeron", "ellas": "leyeron", "ustedes": "leyeron"},
    "caer": {"yo": "caí", "tú": "caíste", "él": "cayó", "ella": "cayó", "usted": "cayó",
             "nosotros": "caímos", "nosotras": "caímos", "ellos": "cayeron", "ellas": "cayeron", "ustedes": "cayeron"},
    "oír": {"yo": "oí", "tú": "oíste", "él": "oyó", "ella": "oyó", "usted": "oyó",
            "nosotros": "oímos", "nosotras": "oímos", "ellos": "oyeron", "ellas": "oyeron", "ustedes": "oyeron"},
    "construir": {"yo": "construí", "tú": "construiste", "él": "construyó", "ella": "construyó", "usted": "construyó",
                  "nosotros": "construimos", "nosotras": "construimos", "ellos": "construyeron", "ellas": "construyeron", "ustedes": "construyeron"},
    "fluir": {"yo": "fluí", "tú": "fluiste", "él": "fluyó", "ella": "fluyó", "usted": "fluyó",
              "nosotros": "fluimos", "nosotras": "fluimos", "ellos": "fluyeron", "ellas": "fluyeron", "ustedes": "fluyeron"},
}

# Strong-stem preterites (no accent on yo / él endings: -e / -o)
PRETERITE_STRONG = {
    "estar": "estuv", "tener": "tuv", "poder": "pud", "poner": "pus",
    "saber": "sup", "querer": "quis", "andar": "anduv", "venir": "vin",
    "haber": "hub", "caber": "cup", "mantener": "mantuv", "obtener": "obtuv",
}


def preterite_strong(verb: str, stem: str) -> dict[str, str]:
    """Strong-stem preterite: yo→-e, él→-o, others standard endings."""
    return {
        "yo": f"{stem}e", "tú": f"{stem}iste", "él": f"{stem}o", "ella": f"{stem}o", "usted": f"{stem}o",
        "nosotros": f"{stem}imos", "nosotras": f"{stem}imos",
        "ellos": f"{stem}ieron", "ellas": f"{stem}ieron", "ustedes": f"{stem}ieron",
    }


# DUCIR-family preterite: -ducir → -duje, -dujimos, -dujeron (no i in 3rd-pl)
PRETERITE_DUCIR = {
    "traducir": "traduj", "conducir": "conduj", "producir": "produj", "introducir": "introduj",
}


def preterite_ducir(stem: str) -> dict[str, str]:
    return {
        "yo": f"{stem}e", "tú": f"{stem}iste", "él": f"{stem}o", "ella": f"{stem}o", "usted": f"{stem}o",
        "nosotros": f"{stem}imos", "nosotras": f"{stem}imos",
        "ellos": f"{stem}eron", "ellas": f"{stem}eron", "ustedes": f"{stem}eron",
    }


# e→i preterite verbs (3rd person stem changes e → i)
PRETERITE_E_TO_I = {
    "pedir": {"yo": "pedí", "tú": "pediste", "él": "pidió", "ella": "pidió", "usted": "pidió",
              "nosotros": "pedimos", "nosotras": "pedimos", "ellos": "pidieron", "ellas": "pidieron", "ustedes": "pidieron"},
    "sentir": {"yo": "sentí", "tú": "sentiste", "él": "sintió", "ella": "sintió", "usted": "sintió",
               "nosotros": "sentimos", "nosotras": "sentimos", "ellos": "sintieron", "ellas": "sintieron", "ustedes": "sintieron"},
    "repetir": {"yo": "repetí", "tú": "repetiste", "él": "repitió", "ella": "repitió", "usted": "repitió",
                "nosotros": "repetimos", "nosotras": "repetimos", "ellos": "repitieron", "ellas": "repitieron", "ustedes": "repitieron"},
    "servir": {"yo": "serví", "tú": "serviste", "él": "sirvió", "ella": "sirvió", "usted": "sirvió",
               "nosotros": "servimos", "nosotras": "servimos", "ellos": "sirvieron", "ellas": "sirvieron", "ustedes": "sirvieron"},
}

# Reflexive present (with reflexive pronoun prefix)
REFLEXIVE_PRONOUNS = {
    "yo": "me", "tú": "te", "él": "se", "ella": "se", "usted": "se",
    "nosotros": "nos", "nosotras": "nos", "ellos": "se", "ellas": "se", "ustedes": "se",
}


def reflexive_present(verb_se: str, stem_changes: Optional[dict] = None) -> dict[str, str]:
    """Reflexive present. verb_se is the infinitive ending in -se. stem_changes
    is an optional dict {'yo': 'levanto', 'tú': 'levantas', ...} of base conjugations
    if the verb has stem changes."""
    stem = verb_se[:-2]  # drop 'se'  → e.g. 'levantar' from 'levantarse'
    base_inf = stem
    base = {
        "yo": f"{base_inf[:-2]}o", "tú": f"{base_inf[:-2]}as", "él": f"{base_inf[:-2]}a", "ella": f"{base_inf[:-2]}a", "usted": f"{base_inf[:-2]}a",
        "nosotros": f"{base_inf[:-2]}amos", "nosotras": f"{base_inf[:-2]}amos",
        "ellos": f"{base_inf[:-2]}an", "ellas": f"{base_inf[:-2]}an", "ustedes": f"{base_inf[:-2]}an",
    } if base_inf.endswith("ar") else {
        "yo": f"{base_inf[:-2]}o", "tú": f"{base_inf[:-2]}es", "él": f"{base_inf[:-2]}e", "ella": f"{base_inf[:-2]}e", "usted": f"{base_inf[:-2]}e",
        "nosotros": f"{base_inf[:-2]}emos", "nosotras": f"{base_inf[:-2]}emos",
        "ellos": f"{base_inf[:-2]}en", "ellas": f"{base_inf[:-2]}en", "ustedes": f"{base_inf[:-2]}en",
    }
    if stem_changes:
        base.update(stem_changes)
    return {p: f"{REFLEXIVE_PRONOUNS[p]} {base[p]}" for p in ALL_PRONOUNS}


# ── Templating helpers ───────────────────────────────────────────────────────


# Pool of object nouns referenced from the encounter/HF word lists. noun_id is
# the spanish key — leaving as None when sentence has no countable noun.
SAMPLE_OBJECTS_AR = [
    ("la canción", "the song", None), ("español", "Spanish", None), ("inglés", "English", None),
    ("en casa", "at home", "casa"), ("el café", "the coffee", "café"), ("la música", "the music", "música"),
]
SAMPLE_OBJECTS_ER_IR = [
    ("la carta", "the letter", "carta"), ("el libro", "the book", "libro"), ("agua", "water", "agua"),
    ("el pan", "the bread", "pan"), ("aquí", "here", None), ("la verdad", "the truth", None),
]


def pick_targets(verbs: list[str], n: int = 5) -> list[dict]:
    """Pick n {verb,pronoun} pairs biased toward diverse pronouns."""
    pool = []
    for v in verbs:
        for p in DIVERSE_PRONOUNS:
            pool.append({"verb": v, "pronoun": p})
    rng = random.Random(hash(tuple(verbs)) & 0xFFFFFFFF)
    rng.shuffle(pool)
    out = []
    seen = set()
    for entry in pool:
        key = (entry["verb"], entry["pronoun"])
        if key in seen:
            continue
        seen.add(key)
        out.append(entry)
        if len(out) == n:
            break
    return out


def pronoun_label(pronoun: str) -> str:
    return {
        "yo": "I", "tú": "You", "él": "He", "ella": "She", "usted": "You (formal)",
        "nosotros": "We", "nosotras": "We (f)",
        "ellos": "They", "ellas": "They (f)", "ustedes": "You all",
    }[pronoun]


def pronoun_es(pronoun: str) -> str:
    return {
        "yo": "Yo", "tú": "Tú", "él": "Él", "ella": "Ella", "usted": "Usted",
        "nosotros": "Nosotros", "nosotras": "Nosotras",
        "ellos": "Ellos", "ellas": "Ellas", "ustedes": "Ustedes",
    }[pronoun]


def template_sentences(answers: dict, verbs: list[str], tense_label: str) -> list[dict]:
    """Generate ~10 drill_sentences alternating written/auditory and pronoun.
    Uses simple bilingual templates — readable but not handcrafted prose.
    Hand-edit later for naturalism."""
    out = []
    rng = random.Random(hash((tuple(verbs), tense_label)) & 0xFFFFFFFF)
    targets = []
    for v in verbs:
        for p in DIVERSE_PRONOUNS[:7]:  # top 7 diverse pronouns
            if v in answers and p in answers[v]:
                targets.append((v, p))
    rng.shuffle(targets)
    for i, (v, p) in enumerate(targets[:10]):
        conj = answers[v][p]
        obj_pool = SAMPLE_OBJECTS_AR if v.endswith("ar") else SAMPLE_OBJECTS_ER_IR
        es_obj, en_obj, noun_id = obj_pool[i % len(obj_pool)]
        out.append({
            "en": f"{pronoun_label(p)} {tense_label} {en_obj}".replace("  ", " ").strip(),
            "es": f"{pronoun_es(p)} {conj} {es_obj}".strip(),
            "noun_id": noun_id,
            "type": "written" if i % 2 == 0 else "auditory",
        })
    while len(out) < 10:
        # pad with simplest sentences if we ran out of (verb, pronoun) combos
        v = verbs[len(out) % len(verbs)]
        p = "ella"
        conj = answers.get(v, {}).get(p, verbs[0])
        out.append({
            "en": f"She {tense_label}",
            "es": f"Ella {conj}",
            "noun_id": None,
            "type": "written" if len(out) % 2 == 0 else "auditory",
        })
    return out


# ── Drill / chat dict factories ──────────────────────────────────────────────


def drill_dict(
    *, sid: str, title: str, gl: float, lesson_number: int,
    verbs: list[str], answers: dict, drill_type: str, tense: str,
    tense_label_en: str, opener_es: Optional[str] = None, opener_en: Optional[str] = None,
) -> dict:
    """Drill-only situation. Phases 0a/0b on, 2/3 off."""
    targets = pick_targets(verbs, n=5)
    return {
        "title": title,
        "grammar_level": gl,
        "lesson_number": lesson_number,
        "lesson_type": "conjugation",
        "word_workload": list(verbs),
        "video_embed_id": None,  # backfill once recorded
        "drill_type": drill_type,
        "tense": tense,
        "drill_config": {"answers": answers},
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": template_sentences(answers, verbs, tense_label_en),
        "drill_targets": targets,
        "phase_2_config": {"description": title, "targets": targets},
        "opener_en": opener_en,
        "opener_es": opener_es,
    }


def chat_dict(
    *, sid: str, title: str, gl: float, lesson_number: int,
    drill1: dict, drill2: dict, opener_es: str, opener_en: str,
) -> dict:
    """Voice-chat-only situation. drill_type=skip; targets = union of two drills."""
    merged_workload = list(dict.fromkeys(drill1["word_workload"] + drill2["word_workload"]))
    targets = (drill1["drill_targets"] + drill2["drill_targets"])[:10]
    return {
        "title": title,
        "grammar_level": gl,
        "lesson_number": lesson_number,
        "lesson_type": "conjugation",
        "word_workload": merged_workload,
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": drill1["tense"],
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": True},
        "phase_2_config": {
            "description": f"{title}: pulls from previous two drill lessons",
            "targets": targets,
        },
        "opener_en": opener_en,
        "opener_es": opener_es,
    }


def rule_dict(
    *, sid: str, title: str, gl: float, lesson_number: int,
    word_workload: list[str], tense: str, drill_sentences: list[dict],
    p2_targets: list[dict] | int, p2_description: str,
    opener_es: str, opener_en: str,
) -> dict:
    """Rule lesson (no drill). Mirrors grammar_ser_estar_rules."""
    return {
        "title": title,
        "grammar_level": gl,
        "lesson_number": lesson_number,
        "lesson_type": "rule",
        "word_workload": word_workload,
        "video_embed_id": None,
        "drill_type": "rule",
        "tense": tense,
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": drill_sentences,
        "phase_2_config": {"description": p2_description, "targets": p2_targets},
        "opener_en": opener_en,
        "opener_es": opener_es,
    }


# ── Per-GL builders ──────────────────────────────────────────────────────────


def build_gl11() -> list[tuple[str, dict]]:
    """GL 11: tengo que / me toca / necesito + infinitive. drill_type=ir_a_inf."""
    out = []
    helpers = [
        ("tengo_que", "Tengo Que", "tengo que", ["hablar", "comer"]),
        ("me_toca", "Me Toca", "me toca", ["vivir", "estudiar"]),
        ("necesito", "Necesito", "necesito", ["dormir", "escribir"]),
    ]
    drills = []
    for i, (slug, title_word, helper, verbs) in enumerate(helpers, start=1):
        # Build "answers" for this helper: pronoun-keyed conjugation of helper + infinitive.
        # Since the helper conjugates by pronoun, we build per-verb.
        # tengo que: yo tengo que, tú tienes que, él tiene que, etc.
        # me toca: a mí me toca, a ti te toca, a él le toca, etc. (use simplified "X + infinitive")
        # necesito: yo necesito, tú necesitas, etc.
        if helper == "tengo que":
            base = {"yo": "tengo que", "tú": "tienes que", "él": "tiene que", "ella": "tiene que", "usted": "tiene que",
                    "nosotros": "tenemos que", "nosotras": "tenemos que", "ellos": "tienen que", "ellas": "tienen que", "ustedes": "tienen que"}
        elif helper == "me toca":
            base = {"yo": "me toca", "tú": "te toca", "él": "le toca", "ella": "le toca", "usted": "le toca",
                    "nosotros": "nos toca", "nosotras": "nos toca", "ellos": "les toca", "ellas": "les toca", "ustedes": "les toca"}
        else:
            base = {"yo": "necesito", "tú": "necesitas", "él": "necesita", "ella": "necesita", "usted": "necesita",
                    "nosotros": "necesitamos", "nosotras": "necesitamos", "ellos": "necesitan", "ellas": "necesitan", "ustedes": "necesitan"}
        answers = {}
        for v in verbs:
            answers[v] = {p: f"{base[p]} {v}" for p in ALL_PRONOUNS}
        d = drill_dict(
            sid=f"grammar_modal_{slug}",
            title=f"{title_word} + Inf ({i}/3)",
            gl=11, lesson_number=i, verbs=verbs, answers=answers,
            drill_type="ir_a_inf", tense="modal_inf",
            tense_label_en=f"{helper} + verb",
            opener_es=None, opener_en=None,
        )
        drills.append(d)
        out.append((f"grammar_modal_{slug}", d))

    # Two chats: one merging tengo_que+me_toca, one for necesito (standalone-ish)
    out.append(("grammar_modal_chat_1", chat_dict(
        sid="grammar_modal_chat_1",
        title="Tengo Que / Me Toca — Voice Chat",
        gl=11, lesson_number=4, drill1=drills[0], drill2=drills[1],
        opener_es="¿Qué tienes que hacer hoy?",
        opener_en="What do you have to do today?",
    )))
    out.append(("grammar_modal_chat_2", chat_dict(
        sid="grammar_modal_chat_2",
        title="Necesito — Voice Chat",
        gl=11, lesson_number=5, drill1=drills[2], drill2=drills[2],
        opener_es="¿Qué necesitas comprar mañana?",
        opener_en="What do you need to buy tomorrow?",
    )))
    return out


def build_cluster(
    *, gl: float, prefix: str, title_base: str,
    verb_pairs: list[list[str]], answers_for: dict[str, dict],
    drill_type: str, tense: str, tense_label_en: str,
    chat_openers: list[tuple[str, str]],
) -> list[tuple[str, dict]]:
    """Build drill-drill-chat clusters from a list of verb-pair drills.

    Args:
      verb_pairs: e.g. [["hablar", "comer"], ["vivir", "estudiar"], ...]
      answers_for: dict mapping verb → conjugation answer dict
      chat_openers: list of (opener_en, opener_es) — len = number of chats

    Returns ordered (sid, dict) list.
    """
    out: list[tuple[str, dict]] = []
    drills_in_window: list[dict] = []
    drill_idx = 0
    chat_idx = 0
    lesson_no = 0
    for pair in verb_pairs:
        drill_idx += 1
        lesson_no += 1
        sid = f"{prefix}_{lesson_no}"
        ans = {v: answers_for[v] for v in pair if v in answers_for}
        d = drill_dict(
            sid=sid,
            title=f"{title_base} ({lesson_no})",
            gl=gl, lesson_number=lesson_no, verbs=pair, answers=ans,
            drill_type=drill_type, tense=tense, tense_label_en=tense_label_en,
        )
        out.append((sid, d))
        drills_in_window.append(d)
        if len(drills_in_window) == 2:
            lesson_no += 1
            chat_sid = f"{prefix}_{lesson_no}"
            opener_en, opener_es = chat_openers[chat_idx] if chat_idx < len(chat_openers) else (
                "Tell me about your day.", "Cuéntame de tu día.")
            chat_idx += 1
            out.append((chat_sid, chat_dict(
                sid=chat_sid,
                title=f"{title_base} — Chat {chat_idx}",
                gl=gl, lesson_number=lesson_no, drill1=drills_in_window[0], drill2=drills_in_window[1],
                opener_es=opener_es, opener_en=opener_en,
            )))
            drills_in_window = []
    # Final odd-count drill: pair with itself for the chat
    if drills_in_window:
        lesson_no += 1
        chat_sid = f"{prefix}_{lesson_no}"
        opener_en, opener_es = chat_openers[chat_idx] if chat_idx < len(chat_openers) else (
            "Tell me more.", "Cuéntame más.")
        out.append((chat_sid, chat_dict(
            sid=chat_sid,
            title=f"{title_base} — Chat {chat_idx + 1}",
            gl=gl, lesson_number=lesson_no, drill1=drills_in_window[0], drill2=drills_in_window[0],
            opener_es=opener_es, opener_en=opener_en,
        )))
    return out


def build_gl12() -> list[tuple[str, dict]]:
    """GL 12 Imperfect: regular -aba/-ía + ir/ser/ver irregulars."""
    answers = {
        "hablar": regular_imperfect("hablar"),
        "escuchar": regular_imperfect("escuchar"),
        "comer": regular_imperfect("comer"),
        "vivir": regular_imperfect("vivir"),
        "ir": IMPERFECT_IRREGULAR["ir"],
        "ser": IMPERFECT_IRREGULAR["ser"],
        "ver": IMPERFECT_IRREGULAR["ver"],
        "escribir": regular_imperfect("escribir"),
    }
    pairs = [["hablar", "escuchar"], ["comer", "vivir"], ["ir", "ser"], ["ver", "escribir"]]
    chats = [
        ("What did you used to do as a kid?", "¿Qué hacías de niño?"),
        ("Tell me how things used to be.", "Cuéntame cómo eran las cosas antes."),
    ]
    return build_cluster(
        gl=12, prefix="grammar_imperfect", title_base="Imperfect",
        verb_pairs=pairs, answers_for=answers,
        drill_type="conjugation", tense="imperfect",
        tense_label_en="used to (imperfect)",
        chat_openers=chats,
    )


def build_gl13() -> list[tuple[str, dict]]:
    """GL 13 Reflexive."""
    answers = {
        "lavarse": reflexive_present("lavarse"),
        "llamarse": reflexive_present("llamarse"),
        "levantarse": reflexive_present("levantarse"),
        "ducharse": reflexive_present("ducharse"),
        # despertarse: e→ie stem change
        "despertarse": reflexive_present("despertarse", stem_changes={
            "yo": "despierto", "tú": "despiertas", "él": "despierta", "ella": "despierta", "usted": "despierta",
            "ellos": "despiertan", "ellas": "despiertan", "ustedes": "despiertan",
        }),
        "acostarse": reflexive_present("acostarse", stem_changes={
            "yo": "acuesto", "tú": "acuestas", "él": "acuesta", "ella": "acuesta", "usted": "acuesta",
            "ellos": "acuestan", "ellas": "acuestan", "ustedes": "acuestan",
        }),
        "vestirse": reflexive_present("vestirse", stem_changes={
            "yo": "visto", "tú": "vistes", "él": "viste", "ella": "viste", "usted": "viste",
            "ellos": "visten", "ellas": "visten", "ustedes": "visten",
        }),
        "sentarse": reflexive_present("sentarse", stem_changes={
            "yo": "siento", "tú": "sientas", "él": "sienta", "ella": "sienta", "usted": "sienta",
            "ellos": "sientan", "ellas": "sientan", "ustedes": "sientan",
        }),
    }
    # Reapply reflexive pronoun prefix on the stem-change overrides
    for v in ["despertarse", "acostarse", "vestirse", "sentarse"]:
        answers[v] = {p: f"{REFLEXIVE_PRONOUNS[p]} {answers[v][p].split(' ', 1)[1]}" for p in ALL_PRONOUNS}
    pairs = [["lavarse", "llamarse"], ["levantarse", "ducharse"],
             ["despertarse", "acostarse"], ["vestirse", "sentarse"]]
    chats = [
        ("Tell me about your morning routine.", "Cuéntame sobre tu rutina de la mañana."),
        ("How do you get ready in the morning?", "¿Cómo te preparas en la mañana?"),
    ]
    return build_cluster(
        gl=13, prefix="grammar_reflexive", title_base="Reflexive",
        verb_pairs=pairs, answers_for=answers,
        drill_type="conjugation", tense="reflexive_present",
        tense_label_en="(reflexive present)",
        chat_openers=chats,
    )


def build_gl14() -> list[tuple[str, dict]]:
    """GL 14 Future Simple."""
    answers = {}
    for v in ["hablar", "comer", "vivir", "estudiar"]:
        answers[v] = regular_future(v)
    for v, root in FUT_COND_IRREGULAR_ROOTS.items():
        answers[v] = regular_future(v, root=root)
    pairs = [
        ["hablar", "comer"], ["vivir", "estudiar"],
        ["tener", "hacer"], ["decir", "poder"],
        ["saber", "querer"], ["venir", "salir"],
    ]
    chats = [
        ("What will you do tomorrow?", "¿Qué harás mañana?"),
        ("Tell me your plans for the weekend.", "Cuéntame tus planes para el fin de semana."),
        ("What will the next year bring?", "¿Qué traerá el próximo año?"),
    ]
    return build_cluster(
        gl=14, prefix="grammar_future", title_base="Future Simple",
        verb_pairs=pairs, answers_for=answers,
        drill_type="conjugation", tense="future",
        tense_label_en="will",
        chat_openers=chats,
    )


def build_gl15() -> list[tuple[str, dict]]:
    """GL 15 Conditional."""
    answers = {}
    for v in ["hablar", "comer", "vivir", "estudiar"]:
        answers[v] = regular_conditional(v)
    for v in ["tener", "hacer", "decir", "poder"]:
        answers[v] = regular_conditional(v, root=FUT_COND_IRREGULAR_ROOTS[v])
    pairs = [["hablar", "comer"], ["vivir", "estudiar"],
             ["tener", "hacer"], ["decir", "poder"]]
    chats = [
        ("What would you do with a million dollars?", "¿Qué harías con un millón de dólares?"),
        ("Where would you live if you could choose?", "¿Dónde vivirías si pudieras elegir?"),
    ]
    return build_cluster(
        gl=15, prefix="grammar_conditional", title_base="Conditional",
        verb_pairs=pairs, answers_for=answers,
        drill_type="conjugation", tense="conditional",
        tense_label_en="would",
        chat_openers=chats,
    )


def build_gl16() -> list[tuple[str, dict]]:
    """GL 16 Preterite vs Imperfect (1 rule lesson)."""
    drill_sentences = [
        {"en": "I was reading when she arrived (background + completed)", "es": "Yo leía cuando ella llegó", "noun_id": None, "type": "written"},
        {"en": "We used to play every day (habitual)", "es": "Jugábamos todos los días", "noun_id": None, "type": "auditory"},
        {"en": "He ate the bread (completed)", "es": "Él comió el pan", "noun_id": "pan", "type": "written"},
        {"en": "She was eating when I called (background)", "es": "Ella comía cuando yo llamé", "noun_id": None, "type": "auditory"},
        {"en": "It was raining all morning (ongoing)", "es": "Llovía toda la mañana", "noun_id": None, "type": "written"},
        {"en": "It rained yesterday (completed)", "es": "Llovió ayer", "noun_id": None, "type": "auditory"},
        {"en": "I was tired (state)", "es": "Yo estaba cansado", "noun_id": None, "type": "written"},
        {"en": "I was tired for an hour (delimited state → preterite)", "es": "Estuve cansado por una hora", "noun_id": None, "type": "auditory"},
        {"en": "When I was a kid, I used to live in Mexico (habitual past)", "es": "Cuando era niño, vivía en México", "noun_id": None, "type": "written"},
        {"en": "She lived in Mexico for five years (completed)", "es": "Ella vivió en México por cinco años", "noun_id": None, "type": "auditory"},
    ]
    return [("grammar_pret_vs_imperfect", rule_dict(
        sid="grammar_pret_vs_imperfect",
        title="Preterite vs. Imperfect",
        gl=16, lesson_number=1,
        word_workload=["preterite", "imperfect"],
        tense="preterite_imperfect",
        drill_sentences=drill_sentences,
        p2_targets=[{"word": "preterite"}, {"word": "imperfect"}],
        p2_description="Choosing between preterite (completed) and imperfect (ongoing/habitual)",
        opener_en="Tell me about a memorable day from your childhood.",
        opener_es="Cuéntame de un día memorable de tu niñez.",
    ))]


def build_gl17_2() -> list[tuple[str, dict]]:
    """GL 17.2 Preterite Spelling Changes."""
    answers = PRETERITE_SPELLING
    pairs = [
        ["pagar", "jugar"], ["buscar", "tocar"],
        ["empezar", "almorzar"], ["creer", "leer"],
        ["caer", "oír"], ["construir", "fluir"],
    ]
    chats = [
        ("Tell me what you bought yesterday.", "Cuéntame qué compraste ayer."),
        ("What did you read this week?", "¿Qué leíste esta semana?"),
        ("Did you hear the news?", "¿Oíste las noticias?"),
    ]
    return build_cluster(
        gl=17.2, prefix="grammar_pret_spelling", title_base="Preterite Spelling Changes",
        verb_pairs=pairs, answers_for=answers,
        drill_type="conjugation", tense="preterite",
        tense_label_en="(preterite)",
        chat_openers=chats,
    )


def build_gl17_3() -> list[tuple[str, dict]]:
    """GL 17.3 Preterite Strong-Stem (12 verbs)."""
    answers = {v: preterite_strong(v, stem) for v, stem in PRETERITE_STRONG.items()}
    pairs = [
        ["estar", "tener"], ["poder", "poner"],
        ["saber", "querer"], ["andar", "venir"],
        ["haber", "caber"], ["mantener", "obtener"],
    ]
    chats = [
        ("Where were you yesterday?", "¿Dónde estuviste ayer?"),
        ("What did you have to do last week?", "¿Qué tuviste que hacer la semana pasada?"),
        ("Tell me about a time you couldn't do something.", "Cuéntame de una vez que no pudiste hacer algo."),
    ]
    return build_cluster(
        gl=17.3, prefix="grammar_pret_strong", title_base="Preterite Strong-Stem",
        verb_pairs=pairs, answers_for=answers,
        drill_type="conjugation", tense="preterite",
        tense_label_en="(preterite)",
        chat_openers=chats,
    )


def build_gl17_4() -> list[tuple[str, dict]]:
    """GL 17.4 Preterite DUCIR."""
    answers = {v: preterite_ducir(stem) for v, stem in PRETERITE_DUCIR.items()}
    pairs = [["traducir", "conducir"], ["producir", "introducir"]]
    chats = [("Did you drive yesterday?", "¿Condujiste ayer?")]
    return build_cluster(
        gl=17.4, prefix="grammar_pret_ducir", title_base="Preterite DUCIR",
        verb_pairs=pairs, answers_for=answers,
        drill_type="conjugation", tense="preterite",
        tense_label_en="(preterite)",
        chat_openers=chats,
    )


def build_gl17_5() -> list[tuple[str, dict]]:
    """GL 17.5 Preterite e→i."""
    answers = PRETERITE_E_TO_I
    pairs = [["pedir", "sentir"], ["repetir", "servir"]]
    chats = [("What did you order at the restaurant?", "¿Qué pediste en el restaurante?")]
    return build_cluster(
        gl=17.5, prefix="grammar_pret_e_to_i", title_base="Preterite e→i",
        verb_pairs=pairs, answers_for=answers,
        drill_type="conjugation", tense="preterite",
        tense_label_en="(preterite)",
        chat_openers=chats,
    )


def build_gl19() -> list[tuple[str, dict]]:
    """GL 19 Direct + Indirect Object Pronouns — 4 rule lessons + 2 chats."""
    out = []
    rule_lessons = [
        ("direct", 1, "Direct Object Pronouns",
         ["lo", "la", "los", "las"],
         [
            {"en": "I see it (the book)", "es": "Lo veo", "noun_id": "libro", "type": "written"},
            {"en": "She buys them (the apples)", "es": "Las compra", "noun_id": None, "type": "auditory"},
            {"en": "We eat it (the bread)", "es": "Lo comemos", "noun_id": "pan", "type": "written"},
            {"en": "They bring her (Maria)", "es": "La traen", "noun_id": None, "type": "auditory"},
            {"en": "You hear them (the children)", "es": "Los oyes", "noun_id": None, "type": "written"},
            {"en": "I read it (the letter)", "es": "La leo", "noun_id": "carta", "type": "auditory"},
            {"en": "He drinks it (the coffee)", "es": "Lo bebe", "noun_id": "café", "type": "written"},
            {"en": "We see them (the cars)", "es": "Los vemos", "noun_id": None, "type": "auditory"},
            {"en": "She wants it (the book)", "es": "Lo quiere", "noun_id": "libro", "type": "written"},
            {"en": "I take her", "es": "La llevo", "noun_id": None, "type": "auditory"},
         ]),
        ("indirect", 2, "Indirect Object Pronouns",
         ["le", "les"],
         [
            {"en": "I give him the book", "es": "Le doy el libro", "noun_id": "libro", "type": "written"},
            {"en": "She tells them the truth", "es": "Les dice la verdad", "noun_id": None, "type": "auditory"},
            {"en": "We bring her the food", "es": "Le traemos la comida", "noun_id": "comida", "type": "written"},
            {"en": "They send him the letter", "es": "Le mandan la carta", "noun_id": "carta", "type": "auditory"},
            {"en": "I write him a message", "es": "Le escribo un mensaje", "noun_id": None, "type": "written"},
            {"en": "We pay them the money", "es": "Les pagamos el dinero", "noun_id": "dinero", "type": "auditory"},
            {"en": "You give them the gift", "es": "Les das el regalo", "noun_id": None, "type": "written"},
            {"en": "She buys him the shirt", "es": "Le compra la camisa", "noun_id": "camisa", "type": "auditory"},
            {"en": "I show him the photo", "es": "Le muestro la foto", "noun_id": None, "type": "written"},
            {"en": "We tell them everything", "es": "Les decimos todo", "noun_id": None, "type": "auditory"},
         ]),
        ("combined_a", 4, "Combined Object Pronouns (1/2)",
         ["se", "lo", "la", "me", "te"],
         [
            {"en": "She gives it to me", "es": "Me lo da", "noun_id": None, "type": "written"},
            {"en": "I give it to you", "es": "Te lo doy", "noun_id": None, "type": "auditory"},
            {"en": "She gives it to him", "es": "Se lo da", "noun_id": None, "type": "written"},
            {"en": "We bring it to her", "es": "Se lo traemos", "noun_id": None, "type": "auditory"},
            {"en": "I tell it to you", "es": "Te lo digo", "noun_id": None, "type": "written"},
            {"en": "He sends it to me", "es": "Me lo manda", "noun_id": None, "type": "auditory"},
            {"en": "She writes it to me", "es": "Me la escribe", "noun_id": None, "type": "written"},
            {"en": "We bring it to you", "es": "Te la traemos", "noun_id": None, "type": "auditory"},
            {"en": "They give it to him", "es": "Se la dan", "noun_id": None, "type": "written"},
            {"en": "I show it to her", "es": "Se la muestro", "noun_id": None, "type": "auditory"},
         ]),
        ("combined_b", 5, "Combined Object Pronouns (2/2)",
         ["nos", "los", "las", "se"],
         [
            {"en": "They bring them to us", "es": "Nos los traen", "noun_id": None, "type": "written"},
            {"en": "She tells them to us", "es": "Nos los dice", "noun_id": None, "type": "auditory"},
            {"en": "He gives them to them", "es": "Se los da", "noun_id": None, "type": "written"},
            {"en": "We send them to her", "es": "Se las mandamos", "noun_id": None, "type": "auditory"},
            {"en": "They show them to us", "es": "Nos las muestran", "noun_id": None, "type": "written"},
            {"en": "I write them to him", "es": "Se las escribo", "noun_id": None, "type": "auditory"},
            {"en": "We pay them to them", "es": "Se los pagamos", "noun_id": None, "type": "written"},
            {"en": "You give them to us", "es": "Nos los das", "noun_id": None, "type": "auditory"},
            {"en": "She brings them to me", "es": "Me las trae", "noun_id": None, "type": "written"},
            {"en": "I send them to you", "es": "Te las mando", "noun_id": None, "type": "auditory"},
         ]),
    ]
    for slug, lesson_no, title, workload, sentences in rule_lessons:
        sid = f"grammar_obj_{slug}"
        out.append((sid, rule_dict(
            sid=sid, title=title, gl=19, lesson_number=lesson_no,
            word_workload=workload, tense="object_pronouns",
            drill_sentences=sentences,
            p2_targets=[{"word": w} for w in workload],
            p2_description=title,
            opener_en="Tell me what you do for your friends.",
            opener_es="Cuéntame qué haces por tus amigos.",
        )))
    # Insert chats after L1+L2 and after L4+L5
    drill_lookup = {sid: d for sid, d in out}
    chat1_targets = ([{"word": w} for w in drill_lookup["grammar_obj_direct"]["word_workload"]]
                     + [{"word": w} for w in drill_lookup["grammar_obj_indirect"]["word_workload"]])
    chat2_targets = ([{"word": w} for w in drill_lookup["grammar_obj_combined_a"]["word_workload"]]
                     + [{"word": w} for w in drill_lookup["grammar_obj_combined_b"]["word_workload"]])
    out.append(("grammar_obj_chat_1", {
        "title": "Object Pronouns — Chat 1",
        "grammar_level": 19, "lesson_number": 3,
        "lesson_type": "rule",
        "word_workload": ["lo", "la", "los", "las", "le", "les"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "object_pronouns",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": True},
        "phase_2_config": {
            "description": "Voice chat: substitute nouns with direct + indirect pronouns",
            "targets": chat1_targets,
        },
        "opener_en": "Let's talk about who does what for whom.",
        "opener_es": "Hablemos de quién hace qué por quién.",
    }))
    out.append(("grammar_obj_chat_2", {
        "title": "Object Pronouns — Chat 2",
        "grammar_level": 19, "lesson_number": 6,
        "lesson_type": "rule",
        "word_workload": ["se", "me", "te", "nos", "lo", "la", "los", "las"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "object_pronouns",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": True},
        "phase_2_config": {
            "description": "Voice chat: combined object pronouns (se lo, me la, te los, etc.)",
            "targets": chat2_targets,
        },
        "opener_en": "Tell me about gifts you've given recently.",
        "opener_es": "Cuéntame de regalos que has dado recientemente.",
    }))
    # Re-order so chats come after their drills
    desired_order = [
        "grammar_obj_direct", "grammar_obj_indirect", "grammar_obj_chat_1",
        "grammar_obj_combined_a", "grammar_obj_combined_b", "grammar_obj_chat_2",
    ]
    by_sid = dict(out)
    return [(sid, by_sid[sid]) for sid in desired_order]


def build_gl20() -> list[tuple[str, dict]]:
    """GL 20 Subjunctive — present + imperfect."""
    out = []
    # Present subjunctive answers
    pres_answers = {
        "hablar": regular_present_subj("hablar"),
        "comer": regular_present_subj("comer"),
        "vivir": regular_present_subj("vivir"),
        "estudiar": regular_present_subj("estudiar"),
        "ser": PRESENT_SUBJ_IRREGULAR["ser"],
        "ir": PRESENT_SUBJ_IRREGULAR["ir"],
        "estar": PRESENT_SUBJ_IRREGULAR["estar"],
        "dar": PRESENT_SUBJ_IRREGULAR["dar"],
        "saber": PRESENT_SUBJ_IRREGULAR["saber"],
        "haber": PRESENT_SUBJ_IRREGULAR["haber"],
    }
    pres_pairs = [
        ["hablar", "comer"], ["vivir", "estudiar"],
        ["ser", "ir"], ["estar", "dar"], ["saber", "haber"],
    ]
    pres_chats = [
        ("What do you hope happens this week?", "¿Qué esperas que pase esta semana?"),
        ("What do you want them to do?", "¿Qué quieres que hagan?"),
        ("What do you need them to know?", "¿Qué necesitas que sepan?"),
    ]
    pres_block = build_cluster(
        gl=20, prefix="grammar_subj_pres", title_base="Present Subjunctive",
        verb_pairs=pres_pairs, answers_for=pres_answers,
        drill_type="conjugation", tense="present_subjunctive",
        tense_label_en="(that ___ ) — present subj",
        chat_openers=pres_chats,
    )
    out.extend(pres_block)

    # Imperfect subjunctive answers
    impf_answers = {
        "hablar": regular_imperfect_subj("hablar"),
        "comer": regular_imperfect_subj("comer"),
        "vivir": regular_imperfect_subj("vivir"),
        "estudiar": regular_imperfect_subj("estudiar"),
    }
    # Build irregulars from preterite stems
    for v in ["ser", "ir", "tener", "hacer", "decir", "querer", "poder"]:
        stem = IMPERFECT_SUBJ_IRREGULAR_STEMS.get(v)
        if stem:
            # Manually build with correct accent on nosotros
            base = {
                "yo": f"{stem}ra", "tú": f"{stem}ras", "él": f"{stem}ra", "ella": f"{stem}ra", "usted": f"{stem}ra",
                "ellos": f"{stem}ran", "ellas": f"{stem}ran", "ustedes": f"{stem}ran",
            }
            # Nosotros gets stress mark on the syllable before -ramos
            # e.g. fueramos → fuéramos, tuvieramos → tuviéramos
            if stem.endswith("e"):
                noso = stem[:-1] + "éramos"
            elif stem.endswith("ie"):
                noso = stem + "ramos"  # tuvie → tuviéramos but using é
                noso = stem[:-2] + "iéramos"
            else:
                noso = stem + "ramos"
            base["nosotros"] = noso
            base["nosotras"] = noso
            impf_answers[v] = base

    impf_pairs = [
        ["hablar", "comer"], ["vivir", "estudiar"],
        ["ser", "tener"], ["hacer", "querer"], ["decir", "poder"],
    ]
    impf_chats = [
        ("If you had more time, what would you do?", "Si tuvieras más tiempo, ¿qué harías?"),
        ("What if you had a different job?", "¿Y si tuvieras un trabajo diferente?"),
        ("Tell me what you wished you had said.", "Cuéntame qué quisieras haber dicho."),
    ]
    # Continue lesson numbers from where present block left off
    last_pres_lesson = max(d["lesson_number"] for _sid, d in pres_block)
    impf_block = build_cluster(
        gl=20, prefix="grammar_subj_impf", title_base="Imperfect Subjunctive",
        verb_pairs=impf_pairs, answers_for=impf_answers,
        drill_type="conjugation", tense="imperfect_subjunctive",
        tense_label_en="(if ___ ) — imperfect subj",
        chat_openers=impf_chats,
    )
    # Bump impf lesson numbers so they continue past present
    for _sid, d in impf_block:
        d["lesson_number"] += last_pres_lesson
    out.extend(impf_block)
    return out


# ── Word translation additions ───────────────────────────────────────────────


# All verbs introduced or referenced — added to GRAMMAR_WORD_TRANSLATIONS if missing.
NEW_TRANSLATIONS = {
    # Reflexive
    "lavarse": "to wash oneself",
    "llamarse": "to be called",
    "levantarse": "to get up",
    "ducharse": "to shower",
    "despertarse": "to wake up",
    "acostarse": "to go to bed",
    "vestirse": "to get dressed",
    "sentarse": "to sit down",
    # Future / Conditional irregulars
    "salir": "to leave/go out",
    # Preterite spelling change verbs
    "pagar": "to pay",
    "jugar": "to play",
    "buscar": "to look for",
    "tocar": "to touch/play (instrument)",
    "empezar": "to begin",
    "almorzar": "to have lunch",
    "creer": "to believe",
    "leer": "to read",
    "caer": "to fall",
    "oír": "to hear",
    "construir": "to build",
    "fluir": "to flow",
    # Preterite strong-stem
    "estar": "to be (temporary)",
    "andar": "to walk/wander",
    "haber": "to have (auxiliary)",
    "caber": "to fit",
    "mantener": "to maintain",
    "obtener": "to obtain",
    # DUCIR
    "traducir": "to translate",
    "conducir": "to drive",
    "producir": "to produce",
    "introducir": "to introduce",
    # e→i
    "pedir": "to ask for",
    "sentir": "to feel",
    "repetir": "to repeat",
    "servir": "to serve",
    # Object pronouns
    "lo": "him/it (direct, masc.)",
    "la": "her/it (direct, fem.)",
    "los": "them (direct, masc./mixed)",
    "las": "them (direct, fem.)",
    "le": "to him/her/you (indirect)",
    "les": "to them (indirect)",
    "se": "to him/her/them (used before lo/la/los/las)",
    "me": "to/for me",
    "te": "to/for you",
    "nos": "to/for us",
    # Subjunctive markers (use words for word_workload)
    "preterite": "preterite (completed past)",
    "imperfect": "imperfect (ongoing past)",
}


# ── Source emission ─────────────────────────────────────────────────────────


def emit_dict(d: dict, indent: int = 4) -> str:
    """Pretty-print a situation dict as Python source matching the existing
    grammar_situations.py style."""
    pad = " " * indent
    lines = ["{"]
    for key in [
        "title", "grammar_level", "lesson_number", "lesson_type", "word_workload",
        "video_embed_id", "drill_type", "tense", "drill_config", "phases",
        "phase_1c_config", "drill_sentences", "drill_targets", "phase_2_config",
        "opener_en", "opener_es",
    ]:
        if key not in d:
            continue
        v = d[key]
        lines.append(f"{pad}    {key!r}: {repr_value(v, indent + 4)},")
    lines.append(f"{pad}}}")
    return "\n".join(lines)


def repr_value(v, indent: int = 8) -> str:
    pad = " " * indent
    if isinstance(v, dict):
        if not v:
            return "{}"
        items = [f"{pad}    {k!r}: {repr_value(val, indent + 4)}" for k, val in v.items()]
        return "{\n" + ",\n".join(items) + f"\n{pad}}}"
    if isinstance(v, list):
        if not v:
            return "[]"
        items = [f"{pad}    {repr_value(it, indent + 4)}" for it in v]
        return "[\n" + ",\n".join(items) + f"\n{pad}]"
    return repr(v)


def emit_all() -> str:
    """Emit the full block of new entries to splice into GRAMMAR_SITUATIONS."""
    builders = [
        ("GL 11 — Tengo Que / Me Toca / Necesito", build_gl11),
        ("GL 12 — Imperfect", build_gl12),
        ("GL 13 — Reflexive", build_gl13),
        ("GL 14 — Future Simple", build_gl14),
        ("GL 15 — Conditional", build_gl15),
        ("GL 16 — Preterite vs Imperfect", build_gl16),
        ("GL 17.2 — Preterite Spelling Changes", build_gl17_2),
        ("GL 17.3 — Preterite Strong-Stem", build_gl17_3),
        ("GL 17.4 — Preterite DUCIR", build_gl17_4),
        ("GL 17.5 — Preterite e→i", build_gl17_5),
        ("GL 19 — Direct + Indirect Object Pronouns", build_gl19),
        ("GL 20 — Subjunctive (present + imperfect)", build_gl20),
    ]
    chunks = []
    for title, fn in builders:
        chunks.append(f"    # === {title} ===")
        for sid, d in fn():
            chunks.append(f"    {sid!r}: {emit_dict(d, indent=4)},")
    return "\n".join(chunks)


# ── Splicing ────────────────────────────────────────────────────────────────


def splice_into_grammar_situations() -> None:
    target = Path("app/data/grammar_situations.py")
    src = target.read_text()

    # 1. Append new entries before the closing `}` of GRAMMAR_SITUATIONS.
    closing = "\n}\n\n\ndef get_grammar_config"
    if closing not in src:
        raise RuntimeError("Couldn't find GRAMMAR_SITUATIONS closing marker")
    new_block = "\n    # ─── Generated by scripts/build_grammar_lessons.py ───\n" + emit_all() + "\n"

    # Skip splicing if any of our generated keys already exist (idempotency)
    sids = set()
    for fn in [build_gl11, build_gl12, build_gl13, build_gl14, build_gl15, build_gl16,
               build_gl17_2, build_gl17_3, build_gl17_4, build_gl17_5, build_gl19, build_gl20]:
        for sid, _ in fn():
            sids.add(sid)
    already = sum(1 for sid in sids if f"\"{sid}\":" in src or f"'{sid}':" in src)
    if already > 0:
        print(f"⚠️  {already}/{len(sids)} generated SIDs already present — skipping splice.")
        print("    Delete the generated block manually if you want to regenerate.")
        return

    src = src.replace(closing, new_block + closing)

    # 2. Append missing translations to GRAMMAR_WORD_TRANSLATIONS.
    trans_close_match = re.search(r'GRAMMAR_WORD_TRANSLATIONS\s*=\s*\{(.*?)\n\}\n', src, re.DOTALL)
    if not trans_close_match:
        raise RuntimeError("Couldn't find GRAMMAR_WORD_TRANSLATIONS")
    existing_trans = trans_close_match.group(1)
    additions = []
    for word, gloss in NEW_TRANSLATIONS.items():
        if f"\"{word}\":" in existing_trans or f"'{word}':" in existing_trans:
            continue
        additions.append(f"    {word!r}: {gloss!r},")
    if additions:
        new_trans_block = (trans_close_match.group(0).rstrip("}\n")
                           + "    # Added by build_grammar_lessons.py\n"
                           + "\n".join(additions) + "\n}\n")
        src = src.replace(trans_close_match.group(0), new_trans_block)

    target.write_text(src)
    print(f"✅ Spliced {len(sids)} new situations + {len(additions)} new translations into {target}")


if __name__ == "__main__":
    splice_into_grammar_situations()
