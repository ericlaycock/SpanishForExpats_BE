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
from datetime import datetime, timezone
from typing import Optional

from fastapi import APIRouter, Depends, File, Form, HTTPException, Request, UploadFile, status
from pydantic import BaseModel, Field
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.data import tense_quest as tq
from app.models import TenseQuestCard, TenseQuestDrillCompletion, User

router = APIRouter()

REVIEW_DECK_LIMIT = 40


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


class LeaderboardEntry(BaseModel):
    rank: int
    name: str
    points: int
    is_you: bool


class Leaderboard(BaseModel):
    entries: list[LeaderboardEntry]
    you_rank: int
    you_points: int
    total_players: int


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


class QuestSentence(BaseModel):
    id: str
    en: str
    es: str
    blank_es: Optional[str] = None  # Spanish with the conjugated verb shown as `____`
    glosses: dict[str, str] = Field(default_factory=dict)
    response_mode: str  # 'type' | 'speak'


class DrillPayload(BaseModel):
    drill_id: str
    tense_group_id: str
    tense_group_title: str
    title: str
    tense_label: str
    video_embed_id: Optional[str] = None
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


class ReviewAttemptRequest(BaseModel):
    card_key: str
    correct: bool
    response_ms: Optional[int] = None


class ReviewAttemptResponse(BaseModel):
    card_key: str
    result: str  # 'great' | 'good' | 'lapse'
    box: int


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


def _display_name(user: User) -> str:
    if getattr(user, "name", None):
        return user.name.strip()
    return (user.email or "player").split("@")[0]


def _leaderboard(db: Session, current_user: User) -> Leaderboard:
    rows = (
        db.query(
            User.id.label("uid"),
            User.name.label("name"),
            User.email.label("email"),
            func.count(TenseQuestDrillCompletion.id).label("pts"),
        )
        .join(TenseQuestDrillCompletion, TenseQuestDrillCompletion.user_id == User.id)
        .group_by(User.id, User.name, User.email)
        .order_by(func.count(TenseQuestDrillCompletion.id).desc(), User.created_at.asc())
        .all()
    )
    you_points = 0
    you_rank = len(rows) + 1
    entries: list[LeaderboardEntry] = []
    for i, r in enumerate(rows):
        is_you = r.uid == current_user.id
        if is_you:
            you_points = int(r.pts)
            you_rank = i + 1
        if i < 10:
            name = (r.name.strip() if r.name else (r.email or "player").split("@")[0])
            entries.append(LeaderboardEntry(rank=i + 1, name=name, points=int(r.pts), is_you=is_you))
    return Leaderboard(
        entries=entries,
        you_rank=you_rank,
        you_points=you_points,
        total_players=len(rows),
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


def _group_summaries(db: Session, user_id) -> list[TenseGroupSummary]:
    done = _completed_drill_ids(db, user_id)
    out: list[TenseGroupSummary] = []
    for g in tq.list_tense_groups():
        completed = sum(1 for d in g["drill_ids"] if d in done)
        out.append(TenseGroupSummary(
            id=g["id"], title=g["title"], blurb=g["blurb"],
            family=g["family"], family_label=g["family_label"],
            total_drills=g["total_drills"], completed_drills=completed,
            percent=_percent(completed, g["total_drills"]),
        ))
    return out


# ── endpoints ───────────────────────────────────────────────────────────────

@router.get("/overview", response_model=OverviewResponse)
async def overview(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    groups = _group_summaries(db, current_user.id)
    points = (
        db.query(func.count(TenseQuestDrillCompletion.id))
        .filter(TenseQuestDrillCompletion.user_id == current_user.id)
        .scalar()
        or 0
    )
    return OverviewResponse(
        points=int(points),
        tense_groups=groups,
        leaderboard=_leaderboard(db, current_user),
        review=_review_deck(db, current_user.id),
    )


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
            title=(tq.GRAMMAR_SITUATIONS.get(did, {}).get("title") or did),
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
    points = (
        db.query(func.count(TenseQuestDrillCompletion.id))
        .filter(TenseQuestDrillCompletion.user_id == current_user.id)
        .scalar()
        or 0
    )
    next_drill_id = next((d for d in (group["drill_ids"] if group else []) if d not in done), None)
    all_complete = total > 0 and completed >= total
    return CompleteResponse(
        drill_id=drill_id,
        tense_group_id=group_id,
        was_new=was_new,
        points=int(points),
        completed_drills=completed,
        total_drills=total,
        percent=_percent(completed, total),
        cards_added=int(deck_after) - int(deck_before),
        deck_total=int(deck_after),
        next_drill_id=next_drill_id or (group["drill_ids"][0] if group and group["drill_ids"] else None),
        all_complete=all_complete,
    )


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
    from app.services.tense_quest_srs import apply_review

    card = (
        db.query(TenseQuestCard)
        .filter(TenseQuestCard.user_id == current_user.id, TenseQuestCard.card_key == body.card_key)
        .first()
    )
    if not card:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Card not in your deck")
    result = apply_review(card, correct=body.correct, response_ms=body.response_ms, now=_now())
    db.commit()
    return ReviewAttemptResponse(card_key=card.card_key, result=result, box=card.box or 1)


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
