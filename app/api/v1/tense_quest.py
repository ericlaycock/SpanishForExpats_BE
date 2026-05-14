"""Tense Quest — verb-conjugation mini-game API (FE route /tensequest).

All content is derived from the existing grammar curriculum (see
`app/data/tense_quest.py`); this router only adds the game layer: tense-group
progress, the activity leaderboard, the per-drill quest payload, the SRS review
deck (+ shuffle), and a thin STT proxy for the spoken-sentence phase.

Grading is deterministic and happens on the FE (it mirrors the grammar-drill
matcher); these endpoints just record outcomes — the same shape the rest of the
app uses for grammar drills.
"""
from __future__ import annotations

import random
import re
from datetime import datetime, timezone
from typing import Optional

from fastapi import APIRouter, Depends, File, Form, HTTPException, Request, UploadFile, status
from pydantic import BaseModel, Field
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.data import tense_quest as tq
from app.models import (
    TenseQuestCard,
    TenseQuestDiagnostic,
    TenseQuestDrillCompletion,
    TenseQuestSentenceCompletion,
    User,
)

router = APIRouter()

REVIEW_DECK_LIMIT = 40

# Public quester name: 3–20 chars, letters/digits/underscore, not all underscores.
USERNAME_RE = re.compile(r"^[A-Za-z0-9_]{3,20}$")
USERNAME_RULES = "3–20 characters — letters, numbers and underscores only."
RESERVED_USERNAMES = {"you", "player", "quester", "admin"}


# ── response models ─────────────────────────────────────────────────────────

class TenseGroupSummary(BaseModel):
    id: str
    title: str
    blurb: str
    family: str
    family_label: str
    total_drills: int
    completed_drills: int
    percent: int  # 0..100, rounded
    diagnostic: Optional[str] = None  # 'ok' | 'needs_work' | None (not assessed)


class AvatarInfo(BaseModel):
    """The equipped Tense Quest avatar — surfaced on the leaderboard so each
    rank shows its owner's pixel sprite, and on the overview so the top bar
    can render the current player's avatar. `id` is the `quest_avatars.id`
    sentinel the FE maps to a renderer (see Sprites.tsx)."""
    id: str
    name: str
    image_path: str


class LeaderboardEntry(BaseModel):
    rank: int
    name: str
    points: int
    is_you: bool
    avatar: Optional[AvatarInfo] = None


class Leaderboard(BaseModel):
    entries: list[LeaderboardEntry]
    you_rank: int
    you_points: int
    total_players: int


class ShopAvatar(BaseModel):
    id: str
    name: str
    image_path: str
    price_coins: int
    is_default: bool
    sort_order: int
    owned: bool
    equipped: bool


class ShopResponse(BaseModel):
    avatars: list[ShopAvatar]
    lifetime_earned: int  # = _user_points; leaderboard truth, unchanged by spends
    current_balance: int  # = lifetime_earned − sum(spends); the spendable wallet


class PurchaseResponse(BaseModel):
    avatar_id: str
    owned: bool
    equipped: bool
    current_balance: int


class EquipRequest(BaseModel):
    avatar_id: str


class EquipResponse(BaseModel):
    avatar_id: str
    equipped: bool


class ReviewCard(BaseModel):
    """A practice-sentence review card. The FE matches what the player produces
    against `es`; `blank_es` is the optional 'show translation' scaffold (Spanish
    with the conjugated verb shown as `____`)."""
    card_key: str
    tense_group_id: str
    tense_group_title: str
    tense_label: str
    en: str
    es: str
    blank_es: Optional[str] = None
    glosses: dict[str, str] = Field(default_factory=dict)
    response_mode: str  # 'type' | 'speak'
    box: int
    due: bool
    last_result: Optional[str] = None


class ReviewDeck(BaseModel):
    cards: list[ReviewCard]
    due_count: int
    total_count: int


class OverviewResponse(BaseModel):
    points: int
    tense_groups: list[TenseGroupSummary]
    leaderboard: Leaderboard
    review: ReviewDeck
    diagnostic_taken: bool
    username: Optional[str] = None  # public quester name; None until the player picks one


class UsernameRequest(BaseModel):
    username: str


class UsernameResponse(BaseModel):
    username: str


# ── placement diagnostic ────────────────────────────────────────────────────

class DiagnosticPrompt(BaseModel):
    verb: str
    pronoun: str
    pronoun_en: str
    answer: str  # piped
    english: Optional[str] = None  # natural English of the conjugated form ("We eat")


class DiagnosticGroup(BaseModel):
    tense_group_id: str
    title: str
    family: str
    prompts: list[DiagnosticPrompt]


class DiagnosticQuiz(BaseModel):
    groups: list[DiagnosticGroup]


class DiagnosticResultItem(BaseModel):
    tense_group_id: str
    passed: bool  # all sampled conjugations correct
    slow: bool = False  # at least one was answered slowly (>7s); only meaningful when passed


class DiagnosticSubmitRequest(BaseModel):
    results: list[DiagnosticResultItem]


class DrillSummary(BaseModel):
    drill_id: str
    title: str
    index: int  # 1-based position in the group
    completed: bool


class TenseGroupDetail(BaseModel):
    id: str
    title: str
    blurb: str
    family: str
    family_label: str
    total_drills: int
    completed_drills: int
    percent: int
    drills: list[DrillSummary]
    next_drill_id: Optional[str] = None
    all_complete: bool


class RuleCard(BaseModel):
    kind: str
    title: str
    body: str
    footnote: Optional[str] = None


class VerbChart(BaseModel):
    title: str
    rows: list[list[str]]
    footnote: Optional[str] = None


class ConjugationTarget(BaseModel):
    verb: str
    pronoun: str
    pronoun_en: str
    answer: str  # piped
    english: Optional[str] = None  # natural English of the conjugated form ("We eat")


class QuestSentence(BaseModel):
    id: str
    en: str
    es: str
    blank_es: Optional[str] = None  # Spanish with the conjugated verb shown as `____`
    glosses: dict[str, str] = Field(default_factory=dict)
    response_mode: str  # 'type' | 'speak'
    # The fields below are populated only for `drill_type=binary_choice`
    # lessons (pret-vs-imperfect, subjunctive triggers). They let the FE
    # render A/B buttons (the correct verb form vs the wrong-tense/mood
    # distractor) instead of a typed input.
    choice: Optional[str] = None              # 'preterite' / 'imperfect' / 'subjunctive' / 'indicative'
    choice_verb_es: Optional[str] = None      # the verb form the learner picks
    choice_distractor_es: Optional[str] = None  # the wrong form (the OTHER button)


class DrillPayload(BaseModel):
    drill_id: str
    tense_group_id: str
    tense_group_title: str
    title: str
    tense_label: str
    video_embed_id: Optional[str] = None
    # 'conjugation' / 'rule' / 'binary_choice' — FE QuestRunner reads this
    # to route between SentenceGauntlet and BinaryChoiceGauntlet.
    drill_type: Optional[str] = None
    # Display labels for the A/B buttons when drill_type=binary_choice.
    # Shape: {"left": {"value": str, "label": str}, "right": {...}}.
    binary_choice_config: Optional[dict] = None
    rule_cards: list[RuleCard]
    charts: list[VerbChart]
    conjugation_targets: list[ConjugationTarget]
    sentences: list[QuestSentence]


class CompleteResponse(BaseModel):
    drill_id: str
    tense_group_id: str
    was_new: bool
    points: int
    completed_drills: int
    total_drills: int
    percent: int
    cards_added: int
    deck_total: int
    next_drill_id: Optional[str] = None
    all_complete: bool


class SentenceAttemptRequest(BaseModel):
    sentence_id: str
    correct: bool


class SentenceAttemptResponse(BaseModel):
    was_new: bool  # first time this sentence was credited (so the FE can pop a +1)
    points: int  # the user's coin total after this attempt


class ReviewAttemptRequest(BaseModel):
    card_key: str
    correct: bool
    response_ms: Optional[int] = None


class ReviewAttemptResponse(BaseModel):
    card_key: str
    result: str  # 'great' (fast+correct) | 'good' (medium+correct) | 'lapse' (slow or wrong)
    box: int
    coins_earned: int  # 2 / 1 / 0


class ShuffleResponse(BaseModel):
    shuffled: int


class TranscribeResponse(BaseModel):
    transcript: str


# ── helpers ─────────────────────────────────────────────────────────────────

def _completed_drill_ids(db: Session, user_id) -> set[str]:
    return {
        r.drill_id
        for r in db.query(TenseQuestDrillCompletion.drill_id)
        .filter(TenseQuestDrillCompletion.user_id == user_id)
        .all()
    }


def _percent(done: int, total: int) -> int:
    if total <= 0:
        return 0
    return round(done * 100 / total)


def _public_name(user: Optional[User], rank: int) -> str:
    """Name shown on the leaderboard. Only the player-chosen `tq_username` is ever
    exposed — never the email or the real onboarding `name`. Players without one
    yet (or a missing user row) fall back to a neutral, non-identifying label."""
    if user is not None and getattr(user, "tq_username", None):
        return user.tq_username.strip()
    return f"Quester #{rank}"


def _normalize_username(raw: str) -> str:
    """Validate a requested quester name and return it trimmed. Raises 422 on a
    malformed or reserved name."""
    name = (raw or "").strip()
    if not USERNAME_RE.match(name) or set(name) == {"_"}:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=USERNAME_RULES)
    if name.lower() in RESERVED_USERNAMES:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="That name is reserved — pick another.")
    return name


def _review_coins(db: Session, user_id) -> int:
    return int(
        db.query(func.coalesce(func.sum(TenseQuestCard.coins_earned), 0))
        .filter(TenseQuestCard.user_id == user_id)
        .scalar()
        or 0
    )


def _sentence_coins(db: Session, user_id) -> int:
    return int(
        db.query(func.count(TenseQuestSentenceCompletion.id))
        .filter(TenseQuestSentenceCompletion.user_id == user_id)
        .scalar()
        or 0
    )


def _user_points(db: Session, user_id) -> int:
    """A user's **lifetime earned** coin total = drill completions (1 each) +
    correct in-drill sentences (1 each) + coins from reviews. This is what
    the leaderboard reads, so it is intentionally **never** reduced by coin
    spends — the leaderboard reflects effort over time, not wallet balance."""
    completions = (
        db.query(func.count(TenseQuestDrillCompletion.id))
        .filter(TenseQuestDrillCompletion.user_id == user_id)
        .scalar()
        or 0
    )
    return int(completions) + _sentence_coins(db, user_id) + _review_coins(db, user_id)


def _user_balance(db: Session, user_id) -> int:
    """Spendable balance = lifetime earned − sum(positive spends). Used only
    by the shop's affordability check and the wallet UI. The leaderboard's
    `_user_points` does NOT subtract this; that's the whole point of the
    split — buying an avatar can never demote your rank."""
    from app.models import TenseQuestCoinSpend
    earned = _user_points(db, user_id)
    spent = (
        db.query(func.coalesce(func.sum(TenseQuestCoinSpend.amount), 0))
        .filter(TenseQuestCoinSpend.user_id == user_id)
        .scalar()
        or 0
    )
    return max(0, earned - int(spent))


def _avatar_info_for(db: Session, user: User) -> Optional[AvatarInfo]:
    """The user's equipped avatar (None → FE renders the default sprite)."""
    from app.models import QuestAvatar
    if not user or not user.tq_avatar_id:
        return None
    av = db.query(QuestAvatar).filter(QuestAvatar.id == user.tq_avatar_id).one_or_none()
    if not av:
        return None
    return AvatarInfo(id=av.id, name=av.name, image_path=av.image_path)


def _leaderboard(db: Session, current_user: User) -> Leaderboard:
    # completions per user
    comp = dict(
        db.query(TenseQuestDrillCompletion.user_id, func.count(TenseQuestDrillCompletion.id))
        .group_by(TenseQuestDrillCompletion.user_id)
        .all()
    )
    # review coins per user
    rev = dict(
        db.query(TenseQuestCard.user_id, func.coalesce(func.sum(TenseQuestCard.coins_earned), 0))
        .group_by(TenseQuestCard.user_id)
        .all()
    )
    # correct in-drill sentences per user (1 coin each)
    sent = dict(
        db.query(TenseQuestSentenceCompletion.user_id, func.count(TenseQuestSentenceCompletion.id))
        .group_by(TenseQuestSentenceCompletion.user_id)
        .all()
    )
    uids = set(comp) | set(rev) | set(sent)
    if uids:
        users = {u.id: u for u in db.query(User).filter(User.id.in_(uids)).all()}
    else:
        users = {}
    scored = []
    for uid in uids:
        pts = int(comp.get(uid, 0)) + int(rev.get(uid, 0)) + int(sent.get(uid, 0))
        u = users.get(uid)
        created = getattr(u, "created_at", None)
        scored.append((pts, str(created or ""), uid, u))
    # highest points first; ties broken by who registered first
    scored.sort(key=lambda x: (-x[0], x[1], str(x[2])))
    you_points = 0
    you_rank = len(scored) + 1
    entries: list[LeaderboardEntry] = []
    for i, (pts, _created, uid, u) in enumerate(scored):
        is_you = uid == current_user.id
        if is_you:
            you_points = pts
            you_rank = i + 1
        if i < 10:
            entries.append(LeaderboardEntry(
                rank=i + 1,
                name=_public_name(u, i + 1),
                points=pts,
                is_you=is_you,
                avatar=_avatar_info_for(db, u) if u else None,
            ))
    return Leaderboard(
        entries=entries,
        you_rank=you_rank,
        you_points=you_points,
        total_players=len(scored),
    )


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _is_due(card: TenseQuestCard, now: datetime) -> bool:
    due = card.due_at
    if due is None:
        return True
    if due.tzinfo is None:
        due = due.replace(tzinfo=timezone.utc)
    return due <= now


def _review_deck(db: Session, user_id, limit: int = REVIEW_DECK_LIMIT) -> ReviewDeck:
    from app.services.tense_quest_srs import order_cards

    now = _now()
    all_cards = db.query(TenseQuestCard).filter(TenseQuestCard.user_id == user_id).all()
    ordered = order_cards(all_cards, now=now)
    due_count = sum(1 for c in all_cards if _is_due(c, now))
    out: list[ReviewCard] = []
    for c in ordered:
        disp = tq.card_display(c.card_key)
        if not disp:  # underlying lesson changed / unknown key — drop it from the deck
            continue
        out.append(ReviewCard(
            card_key=c.card_key,
            tense_group_id=c.tense_group_id or disp.get("tense_group_id") or "",
            tense_group_title=disp.get("tense_group_title") or "",
            tense_label=disp.get("tense_label") or "",
            en=disp.get("en") or "",
            es=disp.get("es") or "",
            blank_es=disp.get("blank_es"),
            glosses=disp.get("glosses") or {},
            response_mode=disp.get("response_mode") or "type",
            box=c.box or 1,
            due=_is_due(c, now),
            last_result=c.last_result,
        ))
        if len(out) >= limit:
            break
    return ReviewDeck(cards=out, due_count=due_count, total_count=len(all_cards))


def _diagnostic_map(db: Session, user_id) -> dict[str, str]:
    return {
        r.tense_group_id: r.result
        for r in db.query(TenseQuestDiagnostic.tense_group_id, TenseQuestDiagnostic.result)
        .filter(TenseQuestDiagnostic.user_id == user_id)
        .all()
    }


def _group_summaries(db: Session, user_id) -> list[TenseGroupSummary]:
    done = _completed_drill_ids(db, user_id)
    diag = _diagnostic_map(db, user_id)
    out: list[TenseGroupSummary] = []
    for g in tq.list_tense_groups():
        total = g["total_drills"]
        result = diag.get(g["id"])
        completed = sum(1 for d in g["drill_ids"] if d in done)
        # A tense the diagnostic marked "ok" (Known) reads as fully complete on
        # the map — full fraction, counts in "tenses beaten", gets the crown.
        # (`ok_slow` / `needs_work` keep real progress.)
        if result == "ok":
            completed = total
        out.append(TenseGroupSummary(
            id=g["id"], title=g["title"], blurb=g["blurb"],
            family=g["family"], family_label=g["family_label"],
            total_drills=total, completed_drills=completed,
            percent=100 if result == "ok" else _percent(completed, total),
            diagnostic=result,
        ))
    return out


# ── endpoints ───────────────────────────────────────────────────────────────

@router.get("/overview", response_model=OverviewResponse)
async def overview(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    taken = (
        db.query(TenseQuestDiagnostic.id)
        .filter(TenseQuestDiagnostic.user_id == current_user.id)
        .first()
        is not None
    )
    return OverviewResponse(
        points=_user_points(db, current_user.id),
        tense_groups=_group_summaries(db, current_user.id),
        leaderboard=_leaderboard(db, current_user),
        review=_review_deck(db, current_user.id),
        diagnostic_taken=taken,
        username=current_user.tq_username,
    )


@router.post("/username", response_model=UsernameResponse)
async def set_username(
    body: UsernameRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Set (or change) the player's public quester name. Case-insensitively
    unique; the FE forces players to pick one before reaching the map."""
    name = _normalize_username(body.username)
    clash = (
        db.query(User.id)
        .filter(func.lower(User.tq_username) == name.lower(), User.id != current_user.id)
        .first()
    )
    if clash is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="That name's taken — pick another.")
    current_user.tq_username = name
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="That name's taken — pick another.")
    return UsernameResponse(username=name)


@router.get("/diagnostic", response_model=DiagnosticQuiz)
async def get_diagnostic(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """3 random warmup conjugations per tense group (groups with no
    conjugations are skipped). The FE grades each; a group passes only if all
    of its prompts are right."""
    return DiagnosticQuiz(groups=[
        DiagnosticGroup(
            tense_group_id=g["tense_group_id"], title=g["title"], family=g["family"],
            prompts=[DiagnosticPrompt(**p) for p in g["prompts"]],
        )
        for g in tq.diagnostic_prompts()
    ])


@router.post("/diagnostic", response_model=dict)
async def submit_diagnostic(
    body: DiagnosticSubmitRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    valid = tq.diagnostic_group_ids()
    for item in body.results:
        if item.tense_group_id not in valid:
            continue
        result = "needs_work" if not item.passed else ("ok_slow" if item.slow else "ok")
        stmt = (
            insert(TenseQuestDiagnostic)
            .values(user_id=current_user.id, tense_group_id=item.tense_group_id, result=result)
            .on_conflict_do_update(
                constraint="uq_tq_diagnostic",
                set_={"result": result, "updated_at": func.now()},
            )
        )
        db.execute(stmt)
    db.commit()
    return {"ok": True}


@router.get("/groups/{group_id}", response_model=TenseGroupDetail)
async def group_detail(
    group_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    g = tq.get_tense_group(group_id)
    if not g:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unknown tense group")
    done = _completed_drill_ids(db, current_user.id)
    drills = [
        DrillSummary(
            drill_id=did,
            title=tq.drill_title(did),
            index=i + 1,
            completed=did in done,
        )
        for i, did in enumerate(g["drill_ids"])
    ]
    completed = sum(1 for d in drills if d.completed)
    all_complete = completed >= len(drills) and len(drills) > 0
    next_drill_id = next((d.drill_id for d in drills if not d.completed), drills[0].drill_id if drills else None)
    return TenseGroupDetail(
        id=g["id"], title=g["title"], blurb=g["blurb"],
        family=g["family"], family_label=g["family_label"],
        total_drills=g["total_drills"], completed_drills=completed,
        percent=_percent(completed, g["total_drills"]),
        drills=drills, next_drill_id=next_drill_id, all_complete=all_complete,
    )


@router.get("/drills/{drill_id}", response_model=DrillPayload)
async def drill_payload(
    drill_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    payload = tq.get_drill_payload(drill_id)
    if not payload:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unknown or unplayable drill")
    group = tq.get_tense_group(payload["tense_group_id"])
    return DrillPayload(
        drill_id=payload["drill_id"],
        tense_group_id=payload["tense_group_id"],
        tense_group_title=(group["title"] if group else ""),
        title=payload["title"],
        tense_label=payload["tense_label"],
        video_embed_id=payload.get("video_embed_id"),
        drill_type=payload.get("drill_type"),
        binary_choice_config=payload.get("binary_choice_config"),
        rule_cards=[RuleCard(**c) for c in payload["rule_cards"]],
        charts=[VerbChart(**c) for c in payload["charts"]],
        conjugation_targets=[ConjugationTarget(**t) for t in payload["conjugation_targets"]],
        sentences=[QuestSentence(**s) for s in payload["sentences"]],
    )


@router.post("/transcribe", response_model=TranscribeResponse)
async def transcribe(
    request: Request,
    audio: UploadFile = File(...),
    expected_text: Optional[str] = Form(None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """STT for the spoken-sentence phase. Biases Whisper to the exact target
    sentence so a near-miss comes back close (same trick as the grammar
    drill's voice mode)."""
    from app.services.openai_media_gateway import transcribe_audio as _stt

    audio_bytes = await audio.read()
    request_id = getattr(request.state, "request_id", "unknown")
    prompt = None
    if expected_text:
        prompt = f"The user is saying a Spanish sentence: {expected_text}. Transcribe exactly what they say."
    transcript = await _stt(
        audio_bytes=audio_bytes,
        filename=audio.filename or "audio.wav",
        prompt=prompt,
        language="es",
        request_id=request_id,
        user_id=str(current_user.id),
        db=db,
        learning_phase="tensequest",
    )
    return TranscribeResponse(transcript=transcript or "")


@router.post("/drills/{drill_id}/complete", response_model=CompleteResponse)
async def complete_drill(
    drill_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    payload = tq.get_drill_payload(drill_id)
    if not payload:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unknown or unplayable drill")
    group_id = payload["tense_group_id"]
    group = tq.get_tense_group(group_id)

    # Record completion (idempotent).
    res = db.execute(
        insert(TenseQuestDrillCompletion)
        .values(user_id=current_user.id, drill_id=drill_id, tense_group_id=group_id)
        .on_conflict_do_nothing(constraint="uq_tq_drill_completion")
    )
    was_new = bool(res.rowcount)

    # Add this drill's practice sentences to the review deck (new cards only).
    deck_before = (
        db.query(func.count(TenseQuestCard.id))
        .filter(TenseQuestCard.user_id == current_user.id)
        .scalar()
        or 0
    )
    base_pos = (
        db.query(func.coalesce(func.max(TenseQuestCard.deck_position), -1))
        .filter(TenseQuestCard.user_id == current_user.id)
        .scalar()
    )
    base_pos = int(base_pos) if base_pos is not None else -1
    now = _now()
    cards = tq.review_cards_for_drill(drill_id)
    if cards:
        rows = [
            {
                "user_id": current_user.id,
                "card_key": c["card_key"],
                "tense_group_id": c["tense_group_id"],
                "drill_id": c["drill_id"],
                "sentence_id": c["sentence_id"],
                "box": 1,
                "reps": 0,
                "lapses": 0,
                "deck_position": base_pos + 1 + i,
                "due_at": now,
            }
            for i, c in enumerate(cards)
        ]
        db.execute(
            insert(TenseQuestCard).values(rows).on_conflict_do_nothing(constraint="uq_tq_card")
        )
    db.commit()

    deck_after = (
        db.query(func.count(TenseQuestCard.id))
        .filter(TenseQuestCard.user_id == current_user.id)
        .scalar()
        or 0
    )
    done = _completed_drill_ids(db, current_user.id)
    completed = sum(1 for d in (group["drill_ids"] if group else []) if d in done)
    total = group["total_drills"] if group else 0
    next_drill_id = next((d for d in (group["drill_ids"] if group else []) if d not in done), None)
    all_complete = total > 0 and completed >= total
    return CompleteResponse(
        drill_id=drill_id,
        tense_group_id=group_id,
        was_new=was_new,
        points=_user_points(db, current_user.id),
        completed_drills=completed,
        total_drills=total,
        percent=_percent(completed, total),
        cards_added=int(deck_after) - int(deck_before),
        deck_total=int(deck_after),
        next_drill_id=next_drill_id or (group["drill_ids"][0] if group and group["drill_ids"] else None),
        all_complete=all_complete,
    )


@router.post("/drills/{drill_id}/sentence", response_model=SentenceAttemptResponse)
async def complete_sentence(
    drill_id: str,
    body: SentenceAttemptRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Credit a correctly-answered sentence from the in-drill gauntlet: +1 coin,
    idempotent per (user, drill, sentence). A wrong attempt is a no-op."""
    payload = tq.get_drill_payload(drill_id)
    if not payload:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unknown or unplayable drill")
    if body.sentence_id not in {s["id"] for s in payload["sentences"]}:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unknown sentence for this drill")

    was_new = False
    if body.correct:
        res = db.execute(
            insert(TenseQuestSentenceCompletion)
            .values(user_id=current_user.id, drill_id=drill_id, sentence_id=body.sentence_id)
            .on_conflict_do_nothing(constraint="uq_tq_sentence_completion")
        )
        was_new = bool(res.rowcount)
        db.commit()
    return SentenceAttemptResponse(was_new=was_new, points=_user_points(db, current_user.id))


@router.get("/review", response_model=ReviewDeck)
async def review_deck(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return _review_deck(db, current_user.id)


@router.post("/review/attempt", response_model=ReviewAttemptResponse)
async def review_attempt(
    body: ReviewAttemptRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    from app.services.tense_quest_srs import apply_review, coins_for_result

    card = (
        db.query(TenseQuestCard)
        .filter(TenseQuestCard.user_id == current_user.id, TenseQuestCard.card_key == body.card_key)
        .first()
    )
    if not card:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Card not in your deck")
    result = apply_review(card, correct=body.correct, response_ms=body.response_ms, now=_now())
    coins = coins_for_result(result)
    card.coins_earned = (card.coins_earned or 0) + coins
    db.commit()
    return ReviewAttemptResponse(card_key=card.card_key, result=result, box=card.box or 1, coins_earned=coins)


@router.post("/review/shuffle", response_model=ShuffleResponse)
async def review_shuffle(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    cards = db.query(TenseQuestCard).filter(TenseQuestCard.user_id == current_user.id).all()
    positions = list(range(len(cards)))
    random.shuffle(positions)
    for c, p in zip(cards, positions):
        c.deck_position = p
    db.commit()
    return ShuffleResponse(shuffled=len(cards))


# ─── Quest Shop ─────────────────────────────────────────────────────────────


@router.get("/shop", response_model=ShopResponse)
async def get_shop(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Avatar catalog + the user's lifetime/spendable coin split.

    `lifetime_earned` is the leaderboard truth (never reduced by spends).
    `current_balance` is what's actually available to spend in the shop.
    Owned/equipped are flagged per avatar so the FE can render Buy vs Equip
    vs "Equipped" states without extra round-trips.
    """
    from app.models import QuestAvatar, UserQuestAvatar
    avatars_q = db.query(QuestAvatar).order_by(QuestAvatar.sort_order, QuestAvatar.id).all()
    owned_ids = {
        row.avatar_id
        for row in db.query(UserQuestAvatar)
        .filter(UserQuestAvatar.user_id == current_user.id)
        .all()
    }
    equipped_id = current_user.tq_avatar_id
    return ShopResponse(
        avatars=[
            ShopAvatar(
                id=a.id,
                name=a.name,
                image_path=a.image_path,
                price_coins=a.price_coins,
                is_default=a.is_default,
                sort_order=a.sort_order,
                owned=(a.id in owned_ids) or a.is_default,
                equipped=(a.id == equipped_id),
            )
            for a in avatars_q
        ],
        lifetime_earned=_user_points(db, current_user.id),
        current_balance=_user_balance(db, current_user.id),
    )


@router.post("/shop/{avatar_id}/purchase", response_model=PurchaseResponse)
async def purchase_avatar(
    avatar_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Buy an avatar with coins. Idempotent on already-owned (returns the
    current ownership/equipped state without re-charging). 402 on
    insufficient balance, 404 on unknown avatar id. Inserts into
    `user_quest_avatars` AND `tense_quest_coin_spends` in one transaction so
    the audit row is never orphaned from the inventory grant."""
    from app.models import QuestAvatar, UserQuestAvatar, TenseQuestCoinSpend

    av = db.query(QuestAvatar).filter(QuestAvatar.id == avatar_id).one_or_none()
    if not av:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unknown avatar")

    already_owned = (
        db.query(UserQuestAvatar)
        .filter(
            UserQuestAvatar.user_id == current_user.id,
            UserQuestAvatar.avatar_id == avatar_id,
        )
        .one_or_none()
    )
    equipped = current_user.tq_avatar_id == avatar_id
    if already_owned or av.is_default:
        # Idempotent — re-purchase is a no-op. Default avatars are owned by
        # everyone implicitly so they always succeed without a charge.
        return PurchaseResponse(
            avatar_id=avatar_id,
            owned=True,
            equipped=equipped,
            current_balance=_user_balance(db, current_user.id),
        )

    balance = _user_balance(db, current_user.id)
    if balance < av.price_coins:
        # 402 Payment Required — standard HTTP code for "you can't afford this".
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail=f"Need {av.price_coins} coins; you have {balance}.",
        )

    db.add(UserQuestAvatar(user_id=current_user.id, avatar_id=avatar_id))
    db.add(TenseQuestCoinSpend(
        user_id=current_user.id,
        amount=av.price_coins,
        reason=f"avatar:{avatar_id}",
    ))
    db.commit()
    return PurchaseResponse(
        avatar_id=avatar_id,
        owned=True,
        equipped=False,
        current_balance=_user_balance(db, current_user.id),
    )


@router.post("/avatar/equip", response_model=EquipResponse)
async def equip_avatar(
    body: EquipRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Set the user's equipped avatar. 403 if the user doesn't own it
    (default avatars are owned implicitly so equipping them always works)."""
    from app.models import QuestAvatar, UserQuestAvatar

    av = db.query(QuestAvatar).filter(QuestAvatar.id == body.avatar_id).one_or_none()
    if not av:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unknown avatar")

    if not av.is_default:
        owns = (
            db.query(UserQuestAvatar)
            .filter(
                UserQuestAvatar.user_id == current_user.id,
                UserQuestAvatar.avatar_id == body.avatar_id,
            )
            .one_or_none()
        )
        if not owns:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You don't own that avatar")

    current_user.tq_avatar_id = body.avatar_id
    db.commit()
    return EquipResponse(avatar_id=body.avatar_id, equipped=True)
