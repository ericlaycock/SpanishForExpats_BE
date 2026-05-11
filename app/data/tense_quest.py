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

import unicodedata
from typing import Any, Optional

from app.data.grammar_situations import (
    GRAMMAR_SITUATIONS,
    GL_TITLES,
    get_situations_for_gl,
    derive_intro_chart,
)

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
FAMILIES = {
    "present": "Present Tense",
    "near_future": "Near Future & Modals",
    "past": "The Past",
    "future_cond": "Future & Conditional",
    "moods": "Commands · -ing · Subjunctive",
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
    {"gl": 9, "id": "ir_a_infinitive", "family": "near_future",
     "title": "Going To (ir a + inf.)", "blurb": "voy a hablar, vas a comer… the everyday near future."},
    {"gl": 11, "id": "modal_infinitives", "family": "near_future",
     "title": "Have To / It's My Turn", "blurb": "tengo que · me toca · necesito + infinitive."},
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
    {"gl": 14, "id": "future_simple", "family": "future_cond",
     "title": "Future Simple", "blurb": "hablaré, comerás… one word for 'will'."},
    {"gl": 15, "id": "conditional", "family": "future_cond",
     "title": "Conditional", "blurb": "would: hablaría, comerías. Polite and hypothetical."},
    {"gl": 13.5, "id": "imperatives", "family": "moods",
     "title": "Commands", "blurb": "¡habla! ¡come! ¡no hables! Telling people what to do."},
    {"gl": 18, "id": "gerund", "family": "moods",
     "title": "-ing (Gerund)", "blurb": "hablando · comiendo · viviendo. estar + gerund = right now."},
    # GL 20's lessons bundle present + imperfect subjunctive; split into two
    # tiles by drill-id substring (`only`).
    {"gl": 20, "id": "present_subjunctive", "family": "moods", "only": "subj_pres",
     "title": "Present Subjunctive", "blurb": "the mood of wishes and 'maybe': espero que hables, quiero que comas."},
    {"gl": 20, "id": "subjunctive", "family": "moods", "only": "subj_impf",
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
    if drill_type == "rule" and config.get("intro_chart"):
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
    """Every conjugated form (pipe-stripped) in the drill's answer table — used to
    locate the verb in a practice sentence so the 'show translation' scaffold can
    blank it out."""
    answers = (config.get("drill_config") or {}).get("answers") or {}
    out: set[str] = set()
    for forms in answers.values():
        for f in (forms or {}).values():
            if f:
                out.add(_strip_pipe(f))
    return out


def _blanked_es(config: dict, es: str) -> Optional[str]:
    """`es` with the (1–3 word) span that is a conjugated form of one of the
    drill's verbs replaced by `____`. Returns None when no such span is found —
    the FE then shows no scaffold for that sentence."""
    if not es:
        return None
    forms = _conjugated_forms(config)
    if not forms:
        return None
    forms_norm = {_norm_es(f) for f in forms}
    tokens = es.split(" ")
    n = len(tokens)
    max_w = max((len(f.split(" ")) for f in forms), default=1)
    for w in range(min(max_w, n), 0, -1):
        for i in range(0, n - w + 1):
            window = tokens[i:i + w]
            bare = " ".join(t.strip(_PUNCT) for t in window)
            if _norm_es(bare) in forms_norm and bare.strip():
                head, tail = window[0], window[-1]
                lead = head[: len(head) - len(head.lstrip(_PUNCT))]
                trail = tail[len(tail.rstrip(_PUNCT)):]
                tokens[i:i + w] = [f"{lead}____{trail}"]
                return " ".join(tokens)
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
    """The warmup prompts: (verb, pronoun, answer). Use the lesson's authored
    drill_targets when present; otherwise sample a varied set from the table."""
    answers = (config.get("drill_config") or {}).get("answers") or {}
    targets = config.get("drill_targets") or []
    out: list[dict[str, Any]] = []
    if targets:
        for t in targets:
            verb, pron = t.get("verb"), t.get("pronoun")
            form = (answers.get(verb) or {}).get(pron)
            if verb and pron and form:
                out.append({"verb": verb, "pronoun": pron, "pronoun_en": PRONOUN_EN.get(pron, pron), "answer": form})
    if not out:
        # Build ~8: prefer varied pronouns, two of the table's verbs.
        verbs = [v for v in (config.get("word_workload") or []) if v in answers] or list(answers)
        preferred = ["ella", "ellas", "nosotras", "usted", "ustedes", "tú", "yo", "ellos", "él", "nosotros"]
        for verb in verbs[:2]:
            forms = answers.get(verb) or {}
            for pron in preferred:
                if forms.get(pron):
                    out.append({"verb": verb, "pronoun": pron, "pronoun_en": PRONOUN_EN.get(pron, pron), "answer": forms[pron]})
                if len([o for o in out if o["verb"] == verb]) >= 5:
                    break
    return out


def _quest_sentences(config: dict) -> list[dict[str, Any]]:
    """The 10 generalisation sentences. Response mode alternates type/speak by
    index (index 0 → type so the player eases in). `blank_es` is the Spanish
    sentence with the conjugated verb replaced by `____` — the "show translation"
    scaffold (null when the verb span can't be located)."""
    out: list[dict[str, Any]] = []
    for i, s in enumerate(_drill_sentences(config)):
        es = s.get("es") or ""
        out.append({
            "id": s["id"],
            "en": s.get("en") or "",
            "es": es,
            "blank_es": _blanked_es(config, es),
            "glosses": s.get("glosses") or {},
            "response_mode": "type" if i % 2 == 0 else "speak",
        })
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
        "rule_cards": _build_rule_cards(config),
        "charts": _build_charts(config),
        "conjugation_targets": _conjugation_targets(config),
        "sentences": _quest_sentences(config),
    }


def _sentence_card(config: dict, group_id: str, group_title: str, drill_id: str,
                   idx: int, s: dict, tense_label: str) -> dict[str, Any]:
    es = s.get("es") or ""
    return {
        "card_key": f"{drill_id}:{s['id']}",
        "drill_id": drill_id,
        "sentence_id": s["id"],
        "tense_group_id": group_id,
        "tense_group_title": group_title,
        "en": s.get("en") or "",
        "es": es,
        "blank_es": _blanked_es(config, es),
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
