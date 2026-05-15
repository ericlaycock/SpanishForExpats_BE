"""Tense Quest — derived game content over the existing grammar curriculum.

Tense Quest is a standalone verb-conjugation mini-game (FE route /tensequest).
It does NOT define any new linguistic content: every tense group, verb chart,
conjugation target and practice sentence is *derived* from
`app.data.grammar_situations.GRAMMAR_SITUATIONS`, which remains the single
source of truth. This module only adds the game-layer grouping (tense groups),
normalises the grammar `intro_chart` shapes into a simple {rule_cards, charts}
pair the FE can render with one component, and exposes the per-drill quest
payload + the review-card set for the SRS deck.

A "tense group" maps 1:1 to a grammar level (GL) that has at least one playable
conjugation drill. A "drill" is one grammar *situation* inside that GL whose
`drill_type` is conjugation-like and which carries practice sentences — i.e. one
quest run: rules + verb chart(s) → conjugation warmup → 10 alternating
speak/type sentences.
"""
from __future__ import annotations

import random
import unicodedata
from typing import Any, Optional

from app.data.grammar_situations import (
    GRAMMAR_SITUATIONS,
    GL_TITLES,
    get_situations_for_gl,
    derive_intro_chart,
)
from app.data.tense_quest_english import english_for

# Drill types that Tense Quest can render as a conjugation warmup.
_PLAYABLE_DRILL_TYPES = {"conjugation", "ir_a_inf"}
# Minimum practice sentences for a drill to be worth a quest run.
_MIN_SENTENCES = 4

# Subject pronouns in canonical order + their English subject form.
PRONOUN_ORDER = ["yo", "tú", "él", "ella", "usted", "nosotros", "nosotras", "ellos", "ellas", "ustedes"]
PRONOUN_EN: dict[str, str] = {
    "yo": "I",
    "tú": "you",
    "él": "he",
    "ella": "she",
    "usted": "you (formal)",
    "nosotros": "we (m)",
    "nosotras": "we (f)",
    "ellos": "they (m)",
    "ellas": "they (f)",
    "ustedes": "you all",
}

# 5-row display grouping for verb charts (mirrors the FE's VerbChart).
_CHART_ROWS: list[tuple[str, list[str]]] = [
    ("yo", ["yo"]),
    ("tú", ["tú"]),
    ("él / ella / usted", ["él", "ella", "usted"]),
    ("nosotros / nosotras", ["nosotros", "nosotras"]),
    ("ellos / ellas / ustedes", ["ellos", "ellas", "ustedes"]),
]

# Tense-group families — used by the FE to lay the quest map out in bands.
# These seven family ids match `app/data/grammar_categories.py:CATEGORIES`
# verbatim so the per-family unlock state on `user_category_progress` keys
# cleanly off them. Renaming a family is safe — no DB column depends on it
# (the SRS deck keys on tense_group_id, not family).
#
# Subjunctive is split into three buckets so users progress rule-recognition
# → present conjugation → past conjugation as separate diagnostics.
FAMILIES = {
    "present": "Present Tense",
    "past": "The Past",
    "future": "Future & Conditional",
    "modals": "Modals & Commands",
    "subjunctive_triggers": "Subjunctive Triggers",
    "present_subjunctive": "Present Subjunctive",
    "imperfect_subjunctive": "Imperfect Subjunctive",
}

# Per-GL Tense-Quest presentation. `gl` is the source grammar level. Anything
# not listed here is excluded from the game (non-verb grammar like pronouns,
# gender, por/para, object pronouns, plus virtual GLs with no situations).
# `title` overrides GL_TITLES for the game; `blurb` is short flavour text.
_TENSE_GROUP_DEFS: list[dict[str, Any]] = [
    {"gl": 3, "id": "regular_present", "family": "present",
     "title": "Regular Present", "blurb": "-ar · -er · -ir. The bread and butter — drop the ending, add a new one."},
    {"gl": 4, "id": "irregular_present_1", "family": "present",
     "title": "Ser, Estar & Co.", "blurb": "ser · estar · ir · dar · tener · venir. The wild ones you say every day."},
    {"gl": 4.5, "id": "irregular_present_2", "family": "present",
     "title": "More Irregulars", "blurb": "hacer · poner · oír · caer · salir · decir · traer · valer."},
    {"gl": 5, "id": "spelling_change_present", "family": "present",
     "title": "Spelling Tricksters", "blurb": "conocer · conseguir · construir · recoger… spelling shifts that keep the sound."},
    {"gl": 6, "id": "stem_o_ue", "family": "present",
     "title": "Boot Verbs: o → ue", "blurb": "dormir · poder · volver · almorzar. The o flips to ue in the boot."},
    {"gl": 7, "id": "stem_e_ie", "family": "present",
     "title": "Boot Verbs: e → ie", "blurb": "querer · pensar · cerrar · empezar. The e flips to ie in the boot."},
    {"gl": 8, "id": "stem_e_i", "family": "present",
     "title": "Boot Verbs: e → i", "blurb": "pedir · servir · repetir · seguir. The e flips to i in the boot."},
    {"gl": 13, "id": "reflexive_present", "family": "present",
     "title": "Reflexive Verbs", "blurb": "levantarse · ducharse · acostarse. Verbs that loop back on you."},
    {"gl": 9, "id": "ir_a_infinitive", "family": "modals",
     "title": "Going To (ir a + inf.)", "blurb": "voy a hablar, vas a comer… the everyday near future."},
    {"gl": 11, "id": "modal_infinitives", "family": "modals",
     "title": "Have To / It's My Turn", "blurb": "tengo que · me toca · necesito + infinitive."},
    {"gl": 13.5, "id": "imperatives", "family": "modals",
     "title": "Commands", "blurb": "¡habla! ¡come! ¡no hables! Telling people what to do."},
    # Gerund moved here from `family: "present"` because it's a periphrasis
    # (estar + -ndo) — semantically closer to modal constructions than the
    # plain present tense.
    {"gl": 18, "id": "gerund", "family": "modals",
     "title": "-ing (Gerund)", "blurb": "hablando · comiendo · viviendo. estar + gerund = right now."},
    {"gl": 12, "id": "imperfect", "family": "past",
     "title": "Imperfect", "blurb": "used to / was -ing. The background tense of the past."},
    {"gl": 17, "id": "preterite_regular", "family": "past",
     "title": "Preterite — Regular", "blurb": "the snapshot past: it happened, it's done."},
    {"gl": 17.1, "id": "preterite_irregular", "family": "past",
     "title": "Preterite — Wild Cards", "blurb": "ser/ir · hacer · estar · tener · poder… the must-know irregulars."},
    {"gl": 17.2, "id": "preterite_spelling", "family": "past",
     "title": "Preterite — Spelling Shifts", "blurb": "buscar → busqué, llegar → llegué, empezar → empecé."},
    {"gl": 17.3, "id": "preterite_stem", "family": "past",
     "title": "Preterite — Stem Changers", "blurb": "third-person stem flips: durmió, pidió, sintió."},
    {"gl": 17.4, "id": "preterite_ducir", "family": "past",
     "title": "Preterite — -ducir Verbs", "blurb": "traducir · conducir · producir → -duje, -dujo, -dujeron."},
    {"gl": 17.5, "id": "preterite_e_i", "family": "past",
     "title": "Preterite — e→i Tricky Ones", "blurb": "more third-person e→i flips in the preterite."},
    {"gl": 16, "id": "preterite_vs_imperfect", "family": "past",
     "title": "Preterite vs. Imperfect", "blurb": "which past? the snapshot (preterite) or the backdrop (imperfect)."},
    {"gl": 18.5, "id": "perfect_tenses", "family": "past",
     "title": "Perfect Tenses", "blurb": "he hablado · había comido. haber + past participle."},
    {"gl": 18.6, "id": "irregular_participles", "family": "past",
     "title": "Perfect — Irregular Participles", "blurb": "he abierto · ha escrito · han hecho — the participles that go their own way."},
    {"gl": 14, "id": "future_simple", "family": "future",
     "title": "Future Simple", "blurb": "hablaré, comerás… one word for 'will'."},
    {"gl": 15, "id": "conditional", "family": "future",
     "title": "Conditional", "blurb": "would: hablaría, comerías. Polite and hypothetical."},
    # WEIRDO trigger phrases (a single rule-only lesson, drill_type=binary_choice).
    # `subjunctive_triggers` is the lockable category id; the TQ tile id below
    # is `subjunctive_triggers_drill` (distinct so the `category_id` field on
    # the tile doesn't collide with the `drill_id` field).
    {"gl": 19.5, "id": "subjunctive_triggers", "family": "subjunctive_triggers",
     "title": "Subjunctive Triggers", "blurb": "WEIRDO — wishes, doubt, emotions, ojalá… pick subjunctive or indicative based on the cue."},
    # GL 20's lessons bundle present + imperfect subjunctive; split into two
    # tiles by drill-id substring (`only`). Each family is its own lockable
    # bucket so users diagnose → unlock present and imperfect separately.
    {"gl": 20, "id": "present_subjunctive", "family": "present_subjunctive", "only": "subj_pres",
     "title": "Present Subjunctive", "blurb": "the mood of wishes and 'maybe': espero que hables, quiero que comas."},
    {"gl": 20.5, "id": "subjunctive", "family": "imperfect_subjunctive", "only": "subj_impf",
     "title": "Imperfect Subjunctive", "blurb": "the past subjunctive: si hablara… ojalá comieran…"},
]

_ID_TO_DEF: dict[str, dict[str, Any]] = {d["id"]: d for d in _TENSE_GROUP_DEFS}


# ── hand-authored Tense-Quest-only content ──────────────────────────────────
# Irregular past participles aren't a curriculum lesson — author the module
# here. The entry is shaped exactly like a `GRAMMAR_SITUATIONS` conjugation
# lesson so every helper below works unchanged. Synthetic grammar_level 18.6
# slots it just after the regular Perfect Tenses tile. Forms are pipe-encoded
# so the changing part renders red. (Present subjunctive isn't here — the
# curriculum's GL-20 lessons already cover it; it's just split off into its
# own tile.)

_HABER_PRESENT = {"yo": "he", "tú": "has", "él": "ha", "ella": "ha", "usted": "ha",
                  "nosotros": "hemos", "nosotras": "hemos", "ellos": "han", "ellas": "han", "ustedes": "han"}


def _perfect_answers(participle: str) -> dict[str, str]:
    # "|he abierto" → ConjForm reddens "he" (the haber form), keeps the participle black.
    return {p: f"|{h} {participle}" for p, h in _HABER_PRESENT.items()}


def _g(en: str, es: str, glosses: dict[str, str] | None = None) -> dict[str, Any]:
    return {"en": en, "es": es, "noun_id": None, "type": "written", "glosses": glosses or {}}


_EXTRA_SITUATIONS: dict[str, dict[str, Any]] = {
    "tq_irregular_participles": {
        "title": "Perfect — Irregular Participles",
        "grammar_level": 18.6,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "tense": "perfect",
        "drill_type": "conjugation",
        "video_embed_id": None,
        "word_workload": ["abrir", "escribir", "hacer", "decir", "ver", "poner", "volver", "romper"],
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "intro_chart": {
            "kind": "cards",
            "title": "Perfect tense — irregular past participles",
            "cards": [
                {"kind": "text", "title": "Most participles are regular — a few aren't",
                 "body": "The present perfect is **haber** (he, has, ha, hemos, han) + a past participle. Regular participles end in **-ado** / **-ido** (*hablado*, *comido*). But a handful of very common verbs have *irregular* participles you simply memorise."},
                {"kind": "rule_pack", "title": "The ones you'll actually use",
                 "sections": [{"heading": "infinitive → participle", "items": [
                     "abrir → abierto", "escribir → escrito", "hacer → hecho", "decir → dicho",
                     "ver → visto", "poner → puesto", "volver → vuelto", "romper → roto",
                 ]}],
                 "footnote": "Same idea for compounds: descubrir → descubierto, devolver → devuelto, deshacer → deshecho."},
                {"kind": "text", "title": "Putting it together",
                 "body": "Conjugate **haber** in the present, then bolt on the participle: *yo* **he** abierto, *tú* **has** escrito, *ella* **ha** hecho, *nosotros* **hemos** visto, *ellos* **han** puesto. The participle never changes — only *haber* does."},
            ],
        },
        "drill_config": {"answers": {
            "abrir": _perfect_answers("abierto"),
            "escribir": _perfect_answers("escrito"),
            "hacer": _perfect_answers("hecho"),
            "decir": _perfect_answers("dicho"),
            "ver": _perfect_answers("visto"),
            "poner": _perfect_answers("puesto"),
            "volver": _perfect_answers("vuelto"),
            "romper": _perfect_answers("roto"),
        }},
        "drill_targets": [
            {"verb": "abrir", "pronoun": "yo"}, {"verb": "escribir", "pronoun": "tú"},
            {"verb": "hacer", "pronoun": "ella"}, {"verb": "ver", "pronoun": "nosotros"},
            {"verb": "decir", "pronoun": "ellos"}, {"verb": "poner", "pronoun": "yo"},
            {"verb": "volver", "pronoun": "tú"}, {"verb": "romper", "pronoun": "él"},
            {"verb": "escribir", "pronoun": "nosotras"}, {"verb": "ver", "pronoun": "ustedes"},
        ],
        "drill_sentences": [
            _g("I have opened the window", "He abierto la ventana", {"window": "ventana", "ventana": "window"}),
            _g("You have written a letter", "Has escrito una carta", {"letter": "carta", "carta": "letter"}),
            _g("She has done the work", "Ella ha hecho el trabajo", {"work": "trabajo", "trabajo": "work"}),
            _g("We have seen the movie", "Hemos visto la película", {"movie": "película", "película": "movie"}),
            _g("They have told the truth", "Han dicho la verdad", {"truth": "verdad", "verdad": "truth"}),
            _g("I have put the book here", "He puesto el libro aquí", {"here": "aquí", "aquí": "here"}),
            _g("You have come back home", "Has vuelto a casa", {}),
            _g("He has broken the glass", "Él ha roto el vaso", {"glass": "vaso", "vaso": "glass"}),
            _g("We have written the emails", "Hemos escrito los correos", {"emails": "correos", "correos": "emails"}),
            _g("Have you seen María?", "¿Has visto a María?", {}),
        ],
        "opener_en": "Have you done your homework?",
        "opener_es": "¿Has hecho la tarea?",
    },
}

_EXTRA_GL_TO_SITUATIONS: dict[float, list[str]] = {}
for _sid, _cfg in _EXTRA_SITUATIONS.items():
    _EXTRA_GL_TO_SITUATIONS.setdefault(_cfg["grammar_level"], []).append(_sid)
del _sid, _cfg


def _situation(sid: str) -> Optional[dict[str, Any]]:
    """Look up a drill config — hand-authored extras first, then the curriculum."""
    return _EXTRA_SITUATIONS.get(sid) or GRAMMAR_SITUATIONS.get(sid)


def drill_title(drill_id: str) -> str:
    cfg = _situation(drill_id)
    return (cfg.get("title") if cfg else None) or drill_id


# ── drill discovery ─────────────────────────────────────────────────────────

def _drill_sentences(config: dict) -> list[dict]:
    """The lesson's practice sentences, each given a stable id (`s{index}` over
    the es-non-empty list) so review cards can key off it across restarts."""
    raw = [s for s in (config.get("drill_sentences") or []) if s.get("es")]
    return [{**s, "id": s.get("id") or f"s{i}"} for i, s in enumerate(raw)]


def _is_playable_drill(situation_id: str) -> bool:
    config = _situation(situation_id)
    if not config:
        return False
    if len(_drill_sentences(config)) < _MIN_SENTENCES:
        return False
    drill_type = config.get("drill_type")
    answers = (config.get("drill_config") or {}).get("answers") or {}
    if drill_type in _PLAYABLE_DRILL_TYPES and answers:
        return True
    # `rule`-type drills (e.g. Preterite vs. Imperfect) have no conjugation
    # table — the quest is rules + sentences, no warmup. They only become a
    # Tense-Quest module via `_TENSE_GROUP_DEFS`, so this can't pull in the
    # non-verb rule lessons (pronouns/gender/por-para/object-pronouns).
    # `binary_choice` is the A/B-decision shape of pret-vs-imperfect and the
    # new subjunctive-triggers module — same payload as `rule` from
    # tense-quest's perspective (rule cards + sentences, no warmup table).
    if drill_type in ("rule", "binary_choice") and config.get("intro_chart"):
        return True
    return False


def _playable_drill_ids(gl: float) -> list[str]:
    sids = _EXTRA_GL_TO_SITUATIONS.get(gl) if gl in _EXTRA_GL_TO_SITUATIONS else get_situations_for_gl(gl)
    return [sid for sid in (sids or []) if _is_playable_drill(sid)]


# ── conjugation helpers ─────────────────────────────────────────────────────

def _strip_pipe(form: str) -> str:
    return (form or "").replace("|", "")


# ── translation scaffold ("show translation" toggle) ────────────────────────

_PUNCT = ".,!?;:¿¡\"'()«»…—–-"


def _norm_es(s: str) -> str:
    s = unicodedata.normalize("NFD", (s or "").lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("ñ", "n").strip()


def _conjugated_forms(config: dict) -> set[str]:
    """Every conjugated form (pipe-stripped) in the drill's answer table."""
    answers = (config.get("drill_config") or {}).get("answers") or {}
    out: set[str] = set()
    for forms in answers.values():
        for f in (forms or {}).values():
            if f:
                out.add(_strip_pipe(f))
    return out


# For periphrastic tenses the curriculum's answer values include the action
# infinitive (e.g. "tengo que hablar"), but pedagogically the tested form is
# the *head* — the bit that conjugates — and the infinitive should stay visible
# in the scaffold. These overrides give `_form_pronouns` a head-only view for
# those tenses so the scaffold blanks "tengo que" out of "Yo tengo que estudiar
# mucho", not "tengo que estudiar". (They also surface me toca / necesito,
# which the underlying lesson doesn't drill but the module covers conceptually.)
_TESTED_HEADS: dict[str, dict[str, set[str]]] = {
    "modal_inf": {
        "tengo que": {"yo"}, "tienes que": {"tú"},
        "tiene que": {"él", "ella", "usted"},
        "tenemos que": {"nosotros", "nosotras"},
        "tienen que": {"ellos", "ellas", "ustedes"},
        "me toca": {"yo"}, "te toca": {"tú"},
        "le toca": {"él", "ella", "usted"},
        "nos toca": {"nosotros", "nosotras"},
        "les toca": {"ellos", "ellas", "ustedes"},
        "necesito": {"yo"}, "necesitas": {"tú"},
        "necesita": {"él", "ella", "usted"},
        "necesitamos": {"nosotros", "nosotras"},
        "necesitan": {"ellos", "ellas", "ustedes"},
    },
    "ir_a_infinitive": {
        "voy a": {"yo"}, "vas a": {"tú"},
        "va a": {"él", "ella", "usted"},
        "vamos a": {"nosotros", "nosotras"},
        "van a": {"ellos", "ellas", "ustedes"},
    },
}


# Preterite-vs-Imperfect is a rule lesson with no conjugation table; its
# contrast sentences ("Yo leía cuando ella llegó") still want a scaffold, so we
# match against a broad set of past-tense forms: every form across the
# curriculum's preterite + imperfect lessons, plus a hand-generated supplement
# for common verbs those contrast sentences use (leer, llegar, jugar, llover,
# estar, ser, ir, ver, tener, hacer, decir, …). Built once at import.
def _build_past_form_pronouns() -> dict[str, set[str]]:
    YO3 = {"yo", "él", "ella", "usted"}      # imperfect 1-sing == 3-sing
    TU, NOS, ELL = {"tú"}, {"nosotros", "nosotras"}, {"ellos", "ellas", "ustedes"}
    YO, T3 = {"yo"}, {"él", "ella", "usted"}
    out: dict[str, set[str]] = {}

    def add(form: str, prons: set[str]) -> None:
        if form:
            out.setdefault(_norm_es(form), set()).update(prons)

    def add_set(forms: tuple[tuple[str, set[str]], ...]) -> None:
        for f, p in forms:
            add(f, p)

    # from the curriculum
    for cfg in GRAMMAR_SITUATIONS.values():
        if cfg.get("tense") not in ("preterite", "imperfect"):
            continue
        for forms in (cfg.get("drill_config") or {}).get("answers", {}).values():
            for pron, f in (forms or {}).items():
                if f:
                    add(_strip_pipe(f), {pron})

    # regular -ar (imperfect + preterite); -gar verbs need the -gué 1-sing
    for v in ("hablar", "llamar", "trabajar", "estudiar", "caminar", "comprar", "cantar",
              "escuchar", "cocinar", "visitar", "viajar", "mirar", "jugar", "llegar", "pagar"):
        s = v[:-2]
        add_set(((s + "aba", YO3), (s + "abas", TU), (s + "ábamos", NOS), (s + "aban", ELL)))
        first = (s[:-1] + "gué") if v.endswith("gar") else (s + "é")
        third = (s[:-1] + "gó") if v.endswith("gar") else (s + "ó")
        add_set(((first, YO), (s + "aste", TU), (third, T3), (s + "amos", NOS), (s + "aron", ELL)))
    # regular -er / -ir (imperfect + preterite)
    for v in ("comer", "beber", "correr", "aprender", "vivir", "escribir", "abrir", "recibir", "salir", "subir"):
        s = v[:-2]
        add_set(((s + "ía", YO3), (s + "ías", TU), (s + "íamos", NOS), (s + "ían", ELL)))
        add_set(((s + "í", YO), (s + "iste", TU), (s + "ió", T3), (s + "imos", NOS), (s + "ieron", ELL)))
    # irregulars
    add_set((("era", YO3), ("eras", TU), ("éramos", NOS), ("eran", ELL),
             ("fui", YO), ("fuiste", TU), ("fue", T3), ("fuimos", NOS), ("fueron", ELL)))   # ser (+ ir preterite)
    add_set((("iba", YO3), ("ibas", TU), ("íbamos", NOS), ("iban", ELL)))                    # ir imperfect
    add_set((("veía", YO3), ("veías", TU), ("veíamos", NOS), ("veían", ELL),
             ("vi", YO), ("viste", TU), ("vio", T3), ("vimos", NOS), ("vieron", ELL)))        # ver
    add_set((("estaba", YO3), ("estabas", TU), ("estábamos", NOS), ("estaban", ELL),
             ("estuve", YO), ("estuviste", TU), ("estuvo", T3), ("estuvimos", NOS), ("estuvieron", ELL)))  # estar
    add_set((("tenía", YO3), ("tenías", TU), ("teníamos", NOS), ("tenían", ELL),
             ("tuve", YO), ("tuviste", TU), ("tuvo", T3), ("tuvimos", NOS), ("tuvieron", ELL)))            # tener
    add_set((("hacía", YO3), ("hacías", TU), ("hacíamos", NOS), ("hacían", ELL),
             ("hice", YO), ("hiciste", TU), ("hizo", T3), ("hicimos", NOS), ("hicieron", ELL)))           # hacer
    add_set((("decía", YO3), ("decías", TU), ("decíamos", NOS), ("decían", ELL),
             ("dije", YO), ("dijiste", TU), ("dijo", T3), ("dijimos", NOS), ("dijeron", ELL)))            # decir
    add_set((("daba", YO3), ("dabas", TU), ("dábamos", NOS), ("daban", ELL),
             ("di", YO), ("diste", TU), ("dio", T3), ("dimos", NOS), ("dieron", ELL)))                    # dar
    for st3 in ("pud", "quis", "pus", "sup", "vin", "estuv"):  # poder/querer/poner/saber/venir/estar
        add_set(((st3 + "e", YO), (st3 + "iste", TU), (st3 + "o", T3), (st3 + "imos", NOS), (st3 + "ieron", ELL)))
    add_set((("leía", YO3), ("leías", TU), ("leíamos", NOS), ("leían", ELL),
             ("leí", YO), ("leíste", TU), ("leyó", T3), ("leímos", NOS), ("leyeron", ELL)))               # leer
    add_set((("había", YO3), ("habías", TU), ("habíamos", NOS), ("habían", ELL), ("hubo", T3)))           # haber
    add("llovía", T3)
    add("llovió", T3)
    return out


_PAST_FORM_PRONOUNS = _build_past_form_pronouns()


# Normalised form → set of pronouns it could spell out (e.g. "habla" → {"él",
# "ella", "usted"}, "jugabamos" → {"nosotros", "nosotras"}). For periphrastic
# tenses uses the head-only override; for the Preterite-vs-Imperfect rule
# lesson uses the union of all past-tense forms.
def _form_pronouns(config: dict) -> dict[str, set[str]]:
    tense = config.get("tense")
    override = _TESTED_HEADS.get(tense)
    if override is not None:
        return override
    if tense == "preterite_imperfect":
        return _PAST_FORM_PRONOUNS
    answers = (config.get("drill_config") or {}).get("answers") or {}
    out: dict[str, set[str]] = {}
    for forms in answers.values():
        for pron, f in (forms or {}).items():
            if not f:
                continue
            out.setdefault(_norm_es(_strip_pipe(f)), set()).add(pron)
    return out


_SUBJECT_PRONS = {"yo", "tu", "el", "ella", "usted", "nosotros", "nosotras", "ellos", "ellas", "ustedes"}
_PRON_LABEL = {
    "yo": "Yo", "tú": "Tú", "él": "Él", "ella": "Ella", "usted": "Usted",
    "nosotros": "Nosotros", "nosotras": "Nosotras",
    "ellos": "Ellos", "ellas": "Ellas", "ustedes": "Ustedes",
}


def _implied_subject(en: str, prons: set[str]) -> Optional[str]:
    """Pick the most plausible Spanish subject from a candidate set, biased by
    cues in the English prompt ('We (m)' → nosotros, 'She' → ella, etc.). For
    forms that map to a single pronoun, just use it."""
    if len(prons) == 1:
        return next(iter(prons))
    e = (en or "").lower().lstrip("¿¡ ")
    # Impersonal / dummy "it" (raining, "it's important that…") — no subject.
    if e.startswith("it ") or e.startswith("it's ") or e.startswith("it'") or e.startswith("its "):
        return None
    # English-side cues
    cues: list[tuple[str, str]] = [
        ("we (m", "nosotros"), ("we (f", "nosotras"), ("we ", "nosotros"),
        ("they (m", "ellos"), ("they (f", "ellas"), ("they ", "ellos"),
        ("you all", "ustedes"), ("you (formal", "usted"),
        ("she ", "ella"), ("he ", "él"),
        ("you ", "tú"), ("i ", "yo"),
    ]
    for needle, pron in cues:
        if needle in e and pron in prons:
            return pron
    # canonical fallback
    for p in PRONOUN_ORDER:
        if p in prons:
            return p
    return None


def _blanked_es(config: dict, es: str, en: str = "") -> Optional[str]:
    """`es` with the (1–3 word) verb span replaced by `____` — the
    'show translation' scaffold. When `es` doesn't already start with a
    subject pronoun, prepend the implied one (so e.g. "Jugábamos todos los
    días" becomes "Nosotros ____ todos los días", surfacing who's doing the
    action). Returns None only when no verb form can be located in `es`."""
    if not es:
        return None
    form_prons = _form_pronouns(config)
    if not form_prons:
        return None
    tokens = es.split(" ")
    n = len(tokens)
    max_w = max((len(f.split(" ")) for f in form_prons.keys()), default=1)
    for w in range(min(max_w, n), 0, -1):
        for i in range(0, n - w + 1):
            window = tokens[i:i + w]
            bare = " ".join(t.strip(_PUNCT) for t in window)
            normed = _norm_es(bare)
            if normed not in form_prons or not bare.strip():
                continue
            head, tail = window[0], window[-1]
            lead = head[: len(head) - len(head.lstrip(_PUNCT))]
            trail = tail[len(tail.rstrip(_PUNCT)):]
            tokens[i:i + w] = [f"{lead}____{trail}"]
            out = " ".join(tokens)
            # If `es` has no leading subject pronoun, prepend the implied one
            # for clarity. Only do this when the matched span starts the
            # sentence (otherwise the sentence already opens with something else
            # — a connector, a possessive, etc. — that we shouldn't displace).
            first_bare = _norm_es((es.split(" ", 1)[0] if es else "").strip(_PUNCT))
            if i == 0 and first_bare not in _SUBJECT_PRONS:
                pron = _implied_subject(en, form_prons[normed])
                if pron:
                    label = _PRON_LABEL.get(pron, pron.capitalize())
                    # Carry any opening punctuation (¿ / ¡) across the prepend so
                    # we end up with "¿Tú ____ hablar?" not "Tú ¿____ hablar?".
                    if out[:1] in "¿¡":
                        out = f"{out[0]}{label} {out[1:]}"
                    else:
                        out = f"{label} {out}"
            return out
    return None


def _verb_chart(verb: str, answers_for_verb: dict[str, str]) -> dict[str, Any]:
    rows = []
    for label, keys in _CHART_ROWS:
        form = next((answers_for_verb[k] for k in keys if answers_for_verb.get(k)), "—")
        rows.append([label, form])
    return {"title": verb, "rows": rows, "footnote": None}


# The "tengo que / me toca / necesito + inf" lesson only drills `tengo que`;
# surface the other two patterns as reference charts so they're not missing.
_MODAL_REFERENCE_CHARTS = [
    {"title": "necesitar (to need to) + inf.", "rows": [
        ["yo", "necesit|o hablar"], ["tú", "necesit|as hablar"],
        ["él / ella / usted", "necesit|a hablar"],
        ["nosotros / nosotras", "necesit|amos hablar"],
        ["ellos / ellas / ustedes", "necesit|an hablar"],
    ], "footnote": "Regular -ar. The second verb stays in the infinitive (necesito comer, necesitas estudiar…)."},
    {"title": "tocar(le) — it's …'s turn to + inf.", "rows": [
        ["it's my turn to…", "me toca hablar"], ["it's your turn to…", "te toca hablar"],
        ["it's his/her turn to…", "le toca hablar"],
        ["it's our turn to…", "nos toca hablar"],
        ["it's their turn to…", "les toca hablar"],
    ], "footnote": "Works like gustar: the verb stays 3rd-person (toca); the pronoun (me / te / le / nos / les) changes."},
]


def _build_charts(config: dict) -> list[dict[str, Any]]:
    """Verb charts for the warmup — always built straight from the drill's own
    conjugation table so we never depend on whether the lesson author supplied
    a hand-written mini-table."""
    answers = (config.get("drill_config") or {}).get("answers") or {}
    # Preserve word_workload order when possible.
    order = [v for v in (config.get("word_workload") or []) if v in answers]
    order += [v for v in answers if v not in order]
    charts = [_verb_chart(v, answers[v]) for v in order[:3]]
    if config.get("tense") == "modal_inf":
        charts.extend({**c, "rows": [list(r) for r in c["rows"]]} for c in _MODAL_REFERENCE_CHARTS)
    return charts


# Lesson-author meta cards we don't want in the game's rule view (e.g. the
# "Why these two together" note on the why-these-verbs-are-bundled grouping).
def _skip_rule_card(title: str) -> bool:
    return title.strip().lower().startswith("why these")


def _build_rule_cards(config: dict) -> list[dict[str, Any]]:
    """Plain-text teaching cards. Pull the `text`/`rule_pack` cards out of the
    lesson's intro_chart; fall back to a one-liner if there are none."""
    cards: list[dict[str, Any]] = []
    chart = derive_intro_chart(config)
    if chart:
        kind = chart.get("kind")
        if kind == "cards":
            for c in chart.get("cards") or []:
                ck = c.get("kind")
                if ck == "text":
                    title = c.get("title") or ""
                    if _skip_rule_card(title):
                        continue
                    cards.append({"kind": "text", "title": title, "body": c.get("body") or "", "footnote": None})
                elif ck == "rule_pack":
                    lines: list[str] = []
                    for sec in c.get("sections") or []:
                        if sec.get("heading"):
                            lines.append(f"**{sec['heading']}**")
                        for it in sec.get("items") or []:
                            lines.append(str(it))
                    cards.append({"kind": "rule_pack", "title": c.get("title") or "", "body": "\n".join(lines), "footnote": c.get("footnote")})
        elif kind in ("text",):
            cards.append({"kind": "text", "title": chart.get("title") or "", "body": chart.get("body") or "", "footnote": None})
        elif kind == "comparison":
            # comparison charts have {left:{title,items}, right:{title,items}} — flatten.
            for side in ("left", "right"):
                s = chart.get(side) or {}
                if s:
                    body = "\n".join(str(i) for i in (s.get("items") or []))
                    cards.append({"kind": "text", "title": s.get("title") or "", "body": body, "footnote": None})
    if not cards:
        tense = (config.get("tense") or "this tense").replace("_", " ")
        cards.append({
            "kind": "text",
            "title": config.get("title") or "Verb chart",
            "body": f"Study the chart below, then conjugate each verb. Notice the pattern in the endings for *{tense}*.",
            "footnote": None,
        })
    return cards


def _conjugation_targets(config: dict) -> list[dict[str, Any]]:
    """The warmup prompts: (verb, pronoun, answer, english). Use the lesson's
    authored drill_targets when present; otherwise sample a varied set from the
    table. `english` is a natural rendering of the conjugated form ("We eat") —
    None when the verb/tense isn't covered by the English helper."""
    answers = (config.get("drill_config") or {}).get("answers") or {}
    tense = config.get("tense")

    def _prompt(verb: str, pron: str, form: str) -> dict[str, Any]:
        return {
            "verb": verb,
            "pronoun": pron,
            "pronoun_en": PRONOUN_EN.get(pron, pron),
            "answer": form,
            "english": english_for(verb, pron, tense),
        }

    targets = config.get("drill_targets") or []
    out: list[dict[str, Any]] = []
    if targets:
        for t in targets:
            verb, pron = t.get("verb"), t.get("pronoun")
            form = (answers.get(verb) or {}).get(pron)
            if verb and pron and form:
                out.append(_prompt(verb, pron, form))
    if not out:
        # Build ~8: prefer varied pronouns, two of the table's verbs.
        verbs = [v for v in (config.get("word_workload") or []) if v in answers] or list(answers)
        preferred = ["ella", "ellas", "nosotras", "usted", "ustedes", "tú", "yo", "ellos", "él", "nosotros"]
        for verb in verbs[:2]:
            forms = answers.get(verb) or {}
            for pron in preferred:
                if forms.get(pron):
                    out.append(_prompt(verb, pron, forms[pron]))
                if len([o for o in out if o["verb"] == verb]) >= 5:
                    break
    return out


def _quest_sentences(config: dict) -> list[dict[str, Any]]:
    """The 10 generalisation sentences. Response mode alternates type/speak by
    index (index 0 → type so the player eases in). `blank_es` is the Spanish
    sentence with the conjugated verb replaced by `____` — the "show translation"
    scaffold (null when the verb span can't be located).

    For `drill_type=binary_choice` lessons (pret-vs-imperfect, subjunctive
    triggers), each sentence ALSO carries `choice` / `choice_verb_es` /
    `choice_distractor_es` so the FE renders A/B buttons (the correct form vs
    the wrong-tense/mood form) instead of a typed input. `response_mode` for
    these is always `type` since the user is tapping a button, not speaking."""
    is_binary = (config.get("drill_type") == "binary_choice")
    out: list[dict[str, Any]] = []
    for i, s in enumerate(_drill_sentences(config)):
        es = s.get("es") or ""
        en = s.get("en") or ""
        entry: dict[str, Any] = {
            "id": s["id"],
            "en": en,
            "es": es,
            "blank_es": _blanked_es(config, es, en),
            "glosses": s.get("glosses") or {},
            "response_mode": "type" if (is_binary or i % 2 == 0) else "speak",
        }
        if is_binary:
            entry["choice"] = s.get("choice")
            entry["choice_verb_es"] = s.get("choice_verb_es")
            entry["choice_distractor_es"] = s.get("choice_distractor_es")
        out.append(entry)
    return out


# ── public API ──────────────────────────────────────────────────────────────

def _group_drill_ids(d: dict[str, Any]) -> list[str]:
    """Playable drills for a tense-group def: all playable drills at its GL,
    optionally filtered to those whose id contains `only` (lets one GL split
    into several tiles, e.g. present vs. imperfect subjunctive)."""
    ids = _playable_drill_ids(d["gl"])
    only = d.get("only")
    return [did for did in ids if not only or only in did]


def _group_dict(d: dict[str, Any], drill_ids: list[str]) -> dict[str, Any]:
    return {
        "id": d["id"],
        "title": d["title"],
        "blurb": d["blurb"],
        "family": d["family"],
        "family_label": FAMILIES.get(d["family"], d["family"]),
        "gl": d["gl"],
        "drill_ids": drill_ids,
        "total_drills": len(drill_ids),
    }


def list_tense_groups() -> list[dict[str, Any]]:
    """All tense groups with their drill ids, in curriculum order. Each item:
    {id, title, blurb, family, family_label, gl, drill_ids: [...], total_drills}.
    Groups with no playable drill are dropped."""
    out: list[dict[str, Any]] = []
    # stable order: gl, then a sub-key so the two GL-20 tiles are deterministic
    for d in sorted(_TENSE_GROUP_DEFS, key=lambda x: (x["gl"], x.get("only", ""))):
        drill_ids = _group_drill_ids(d)
        if drill_ids:
            out.append(_group_dict(d, drill_ids))
    return out


def get_tense_group(group_id: str) -> Optional[dict[str, Any]]:
    d = _ID_TO_DEF.get(group_id)
    if not d:
        return None
    drill_ids = _group_drill_ids(d)
    if not drill_ids:
        return None
    return _group_dict(d, drill_ids)


def tense_group_id_for_drill(drill_id: str) -> Optional[str]:
    config = _situation(drill_id)
    if not config:
        return None
    gl = config.get("grammar_level")
    for d in _TENSE_GROUP_DEFS:
        if d["gl"] != gl:
            continue
        only = d.get("only")
        if not only or only in drill_id:
            return d["id"]
    return None


def get_drill_payload(drill_id: str) -> Optional[dict[str, Any]]:
    """Full quest payload for one drill: rule cards, verb charts, conjugation
    targets, and the 10 alternating sentences."""
    config = _situation(drill_id)
    if not config or not _is_playable_drill(drill_id):
        return None
    group_id = tense_group_id_for_drill(drill_id)
    if not group_id:
        return None
    return {
        "drill_id": drill_id,
        "tense_group_id": group_id,
        "title": config.get("title") or "",
        "tense_label": (config.get("tense") or "present").replace("_", " "),
        "video_embed_id": config.get("video_embed_id"),
        # `drill_type` rides along so the FE QuestRunner can swap to the
        # A/B BinaryChoiceGauntlet for `binary_choice` lessons instead of
        # the typed SentenceGauntlet.
        "drill_type": config.get("drill_type") or "conjugation",
        "binary_choice_config": config.get("binary_choice_config"),
        "rule_cards": _build_rule_cards(config),
        "charts": _build_charts(config),
        "conjugation_targets": _conjugation_targets(config),
        "sentences": _quest_sentences(config),
    }


def _sentence_card(config: dict, group_id: str, group_title: str, drill_id: str,
                   idx: int, s: dict, tense_label: str) -> dict[str, Any]:
    es = s.get("es") or ""
    en = s.get("en") or ""
    return {
        "card_key": f"{drill_id}:{s['id']}",
        "drill_id": drill_id,
        "sentence_id": s["id"],
        "tense_group_id": group_id,
        "tense_group_title": group_title,
        "en": en,
        "es": es,
        "blank_es": _blanked_es(config, es, en),
        "glosses": s.get("glosses") or {},
        "response_mode": "type" if idx % 2 == 0 else "speak",
        "tense_label": tense_label,
    }


def review_cards_for_drill(drill_id: str) -> list[dict[str, Any]]:
    """The cards a completed drill contributes to the SRS review deck — one per
    practice sentence (NOT the warmup conjugations). card_key = '{drill_id}:{sentence_id}'."""
    config = _situation(drill_id)
    if not config:
        return []
    group_id = tense_group_id_for_drill(drill_id)
    if not group_id:
        return []
    group = get_tense_group(group_id)
    group_title = group["title"] if group else ""
    tense_label = (config.get("tense") or "present").replace("_", " ")
    return [
        _sentence_card(config, group_id, group_title, drill_id, i, s, tense_label)
        for i, s in enumerate(_drill_sentences(config))
    ]


def lookup_sentence(card_key: str) -> Optional[dict[str, Any]]:
    """Resolve a sentence card_key ('{drill_id}:{sentence_id}') back to its
    display data (en / es / blank_es / glosses / response_mode / tense + group).
    Returns None if the key (or the underlying lesson) no longer resolves."""
    parts = card_key.split(":", 1)
    if len(parts) != 2:
        return None
    drill_id, sentence_id = parts
    config = _situation(drill_id)
    if not config:
        return None
    group_id = tense_group_id_for_drill(drill_id)
    group = get_tense_group(group_id) if group_id else None
    group_title = group["title"] if group else ""
    tense_label = (config.get("tense") or "present").replace("_", " ")
    for i, s in enumerate(_drill_sentences(config)):
        if s["id"] == sentence_id:
            return _sentence_card(config, group_id or "", group_title, drill_id, i, s, tense_label)
    return None


# Back-compat alias for the router's deck assembler.
def card_display(card_key: str) -> Optional[dict[str, Any]]:
    return lookup_sentence(card_key)


# ── placement diagnostic ────────────────────────────────────────────────────

def _group_conjugation_targets(group_id: str) -> list[dict[str, Any]]:
    """All distinct (verb, pronoun) conjugation prompts across a tense group's
    drills."""
    group = get_tense_group(group_id)
    if not group:
        return []
    seen: set[tuple[str, str]] = set()
    out: list[dict[str, Any]] = []
    for did in group["drill_ids"]:
        cfg = _situation(did)
        if not cfg:
            continue
        for t in _conjugation_targets(cfg):
            key = (t["verb"], t["pronoun"])
            if key in seen:
                continue
            seen.add(key)
            out.append(t)
    return out


def diagnostic_prompts(per_group: int = 3) -> list[dict[str, Any]]:
    """For each tense group with conjugation drills, `per_group` random warmup
    conjugation prompts ({verb, pronoun, pronoun_en, answer}). Groups with no
    conjugations (e.g. Preterite vs. Imperfect) are skipped."""
    out: list[dict[str, Any]] = []
    for g in list_tense_groups():
        targets = _group_conjugation_targets(g["id"])
        if not targets:
            continue
        picked = random.sample(targets, min(per_group, len(targets)))
        out.append({
            "tense_group_id": g["id"],
            "title": g["title"],
            "family": g["family"],
            "prompts": picked,
        })
    return out


def diagnostic_group_ids() -> set[str]:
    return {g["id"] for g in list_tense_groups() if _group_conjugation_targets(g["id"])}
