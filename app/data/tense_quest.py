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
    {"gl": 14, "id": "future_simple", "family": "future_cond",
     "title": "Future Simple", "blurb": "hablaré, comerás… one word for 'will'."},
    {"gl": 15, "id": "conditional", "family": "future_cond",
     "title": "Conditional", "blurb": "would: hablaría, comerías. Polite and hypothetical."},
    {"gl": 13.5, "id": "imperatives", "family": "moods",
     "title": "Commands", "blurb": "¡habla! ¡come! ¡no hables! Telling people what to do."},
    {"gl": 18, "id": "gerund", "family": "moods",
     "title": "-ing (Gerund)", "blurb": "hablando · comiendo · viviendo. estar + gerund = right now."},
    {"gl": 20, "id": "subjunctive", "family": "moods",
     "title": "Subjunctive", "blurb": "the mood of doubt, wishes and 'maybe': que hables, que comas."},
]

# Stable id <-> GL maps.
_ID_TO_DEF: dict[str, dict[str, Any]] = {d["id"]: d for d in _TENSE_GROUP_DEFS}
_GL_TO_ID: dict[float, str] = {d["gl"]: d["id"] for d in _TENSE_GROUP_DEFS}


# ── drill discovery ─────────────────────────────────────────────────────────

def _drill_sentences(config: dict) -> list[dict]:
    """The lesson's practice sentences, each given a stable id (`s{index}` over
    the es-non-empty list) so review cards can key off it across restarts."""
    raw = [s for s in (config.get("drill_sentences") or []) if s.get("es")]
    return [{**s, "id": s.get("id") or f"s{i}"} for i, s in enumerate(raw)]


def _is_playable_drill(situation_id: str) -> bool:
    config = GRAMMAR_SITUATIONS.get(situation_id)
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
    return [sid for sid in get_situations_for_gl(gl) if _is_playable_drill(sid)]


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


def _build_charts(config: dict) -> list[dict[str, Any]]:
    """Verb charts for the warmup — always built straight from the drill's own
    conjugation table so we never depend on whether the lesson author supplied
    a hand-written mini-table."""
    answers = (config.get("drill_config") or {}).get("answers") or {}
    # Preserve word_workload order when possible.
    order = [v for v in (config.get("word_workload") or []) if v in answers]
    order += [v for v in answers if v not in order]
    return [_verb_chart(v, answers[v]) for v in order[:3]]


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

def list_tense_groups() -> list[dict[str, Any]]:
    """All tense groups with their drill ids, in curriculum order. Each item:
    {id, title, blurb, family, family_label, gl, drill_ids: [...], total_drills}.
    Groups whose GL has no playable drill are dropped."""
    out: list[dict[str, Any]] = []
    for d in sorted(_TENSE_GROUP_DEFS, key=lambda x: x["gl"]):
        drill_ids = _playable_drill_ids(d["gl"])
        if not drill_ids:
            continue
        out.append({
            "id": d["id"],
            "title": d["title"],
            "blurb": d["blurb"],
            "family": d["family"],
            "family_label": FAMILIES.get(d["family"], d["family"]),
            "gl": d["gl"],
            "drill_ids": drill_ids,
            "total_drills": len(drill_ids),
        })
    return out


def get_tense_group(group_id: str) -> Optional[dict[str, Any]]:
    d = _ID_TO_DEF.get(group_id)
    if not d:
        return None
    drill_ids = _playable_drill_ids(d["gl"])
    if not drill_ids:
        return None
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


def tense_group_id_for_drill(drill_id: str) -> Optional[str]:
    config = GRAMMAR_SITUATIONS.get(drill_id)
    if not config:
        return None
    return _GL_TO_ID.get(config.get("grammar_level"))


def get_drill_payload(drill_id: str) -> Optional[dict[str, Any]]:
    """Full quest payload for one drill: rule cards, verb charts, conjugation
    targets, and the 10 alternating sentences."""
    config = GRAMMAR_SITUATIONS.get(drill_id)
    if not config or not _is_playable_drill(drill_id):
        return None
    group_id = _GL_TO_ID.get(config.get("grammar_level"))
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
    config = GRAMMAR_SITUATIONS.get(drill_id)
    if not config:
        return []
    group_id = _GL_TO_ID.get(config.get("grammar_level"))
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
    config = GRAMMAR_SITUATIONS.get(drill_id)
    if not config:
        return None
    group_id = _GL_TO_ID.get(config.get("grammar_level"))
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
