"""Vocab Map — chapter learning + spaced-repetition API (FE route /expatquest/vocab).

The vocab module taxonomy lives in the FE (`components/tensequest/vocabData.ts`)
because the cap is 25 words = 5 chapters of 5, and the actual content is
hand-curated per module. This router does not maintain a parallel Python copy
of that taxonomy — instead the FE submits the word list when it completes a
chapter, and the BE just stores what it's told. STT for the press-and-speak
gauntlet reuses `POST /v1/tensequest/transcribe`.

The two segregated decks (module-only vs main vocab) are encoded in the
`status` column on `vocab_card`. Promotion from module → main is the whole
point of the module-SRS review: fast+correct (≤15s) promotes; everything
else re-queues. The main pool is intentionally separate from the verb review
deck in `tense_quest_cards`.
"""
from __future__ import annotations

import random
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import User, VocabCard, VocabChapterCompletion
from app.services import srs

router = APIRouter()


# Both vocab decks ride the shared Leitner engine in `app/services/srs.py` — the
# same ladder + transition rules the verb deck uses. A module card that's
# answered correctly within the (typed) slow ceiling promotes to the main deck
# at box 1; everything else re-queues ~10 min out. Main-deck cards then space out
# along the shared ladder (box 1 = 4h … box 7 = 60d), demoting by 2 on a lapse.
CHAPTERS_PER_MODULE = 3  # 3 chapters × 5 words = 15-word module cap


# ── response models ─────────────────────────────────────────────────────────


class VocabWordIn(BaseModel):
    es: str
    en: str


class ChapterCompleteRequest(BaseModel):
    """FE submits the 5 (or fewer, for a partial trailing chapter) words it
    just gauntlet-passed. Idempotent: re-submitting an already-completed
    chapter is a no-op but still seeds any missing words into the deck."""
    words: list[VocabWordIn] = Field(default_factory=list)


class ChapterCompleteResponse(BaseModel):
    module_id: str
    chapter_index: int
    was_new: bool        # first time this chapter was completed
    cards_seeded: int    # number of vocab_card rows inserted on this call
    coins_awarded: int   # 1 sun per newly seeded card == words recalled for first time
    points: int          # user's new lifetime-earned coin total


class ChapterCompletionInfo(BaseModel):
    module_id: str
    chapter_indices: list[int]


class ModuleDeckInfo(BaseModel):
    module_id: str
    total: int       # total module-status cards in this module
    due: int         # module-status cards with due_at <= now (re-queued cards wait ~10 min)


class MainDeckInfo(BaseModel):
    total: int       # total status='main' cards
    due: int         # cards with due_at <= now


class ProgressResponse(BaseModel):
    chapter_completions: list[ChapterCompletionInfo]
    module_decks: list[ModuleDeckInfo]
    main_deck: MainDeckInfo


class VocabReviewCard(BaseModel):
    card_id: str
    module_id: str
    word_es: str
    word_en: str
    status: str  # 'module' | 'main'
    box: int


class ModuleReviewDeck(BaseModel):
    module_id: str
    cards: list[VocabReviewCard]


class MainReviewDeck(BaseModel):
    cards: list[VocabReviewCard]
    total: int
    due: int


class ReviewAttemptRequest(BaseModel):
    card_id: str
    correct: bool
    response_ms: int = 0


class ModuleReviewAttemptResult(BaseModel):
    card_id: str
    promoted: bool   # status flipped to 'main'
    requeued: bool   # stayed in module deck, due_at bumped


class MainReviewAttemptResult(BaseModel):
    card_id: str
    box: int          # new box after the attempt
    due_at: str       # ISO timestamp of next due


# ── helpers ─────────────────────────────────────────────────────────────────


def _module_decks_summary(db: Session, user_id) -> list[ModuleDeckInfo]:
    """Group module-status cards by module so the FE can show per-module deck
    counts (e.g. for the sidebar review-CTA). `due` counts only cards whose
    due_at has passed — a re-queued card waits ~10 min before it's due
    again, so `due` can be < total."""
    now = datetime.now(timezone.utc)
    rows = (
        db.query(
            VocabCard.module_id,
            func.count(VocabCard.id),
            func.count(VocabCard.id).filter(VocabCard.due_at <= now),
        )
        .filter(VocabCard.user_id == user_id, VocabCard.status == "module")
        .group_by(VocabCard.module_id)
        .all()
    )
    return [ModuleDeckInfo(module_id=mid, total=total, due=due) for (mid, total, due) in rows]


def _main_deck_summary(db: Session, user_id) -> MainDeckInfo:
    total = (
        db.query(func.count(VocabCard.id))
        .filter(VocabCard.user_id == user_id, VocabCard.status == "main")
        .scalar()
    ) or 0
    now = datetime.now(timezone.utc)
    due = (
        db.query(func.count(VocabCard.id))
        .filter(
            VocabCard.user_id == user_id,
            VocabCard.status == "main",
            VocabCard.due_at <= now,
        )
        .scalar()
    ) or 0
    return MainDeckInfo(total=total, due=due)


def _chapter_completions_summary(db: Session, user_id) -> list[ChapterCompletionInfo]:
    rows = (
        db.query(VocabChapterCompletion.module_id, VocabChapterCompletion.chapter_index)
        .filter(VocabChapterCompletion.user_id == user_id)
        .all()
    )
    grouped: dict[str, list[int]] = {}
    for (mid, idx) in rows:
        grouped.setdefault(mid, []).append(int(idx))
    return [
        ChapterCompletionInfo(module_id=mid, chapter_indices=sorted(set(idxs)))
        for (mid, idxs) in sorted(grouped.items())
    ]


# ── endpoints ───────────────────────────────────────────────────────────────


@router.get("/progress", response_model=ProgressResponse)
async def vocab_progress(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """One-shot read used by the Vocab Map dashboard panel + every module
    page (which uses the chapter_completions to render sidebar lock state)."""
    return ProgressResponse(
        chapter_completions=_chapter_completions_summary(db, current_user.id),
        module_decks=_module_decks_summary(db, current_user.id),
        main_deck=_main_deck_summary(db, current_user.id),
    )


@router.post(
    "/chapter/{module_id}/{chapter_idx}/complete",
    response_model=ChapterCompleteResponse,
)
async def complete_chapter(
    module_id: str,
    chapter_idx: int,
    body: ChapterCompleteRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Record a finished chapter + seed its words into the module SRS deck.
    Both halves are idempotent: replaying the chapter does not double-credit
    completion and does not duplicate cards."""
    if chapter_idx < 0 or chapter_idx >= CHAPTERS_PER_MODULE:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid chapter index")

    # Record completion (idempotent).
    res = db.execute(
        insert(VocabChapterCompletion)
        .values(user_id=current_user.id, module_id=module_id, chapter_index=chapter_idx)
        .on_conflict_do_nothing(constraint="uq_vocab_chapter")
    )
    was_new = bool(res.rowcount)

    # Seed module-status cards for any words not already in the user's deck
    # for this module. Cards already in the deck (whether 'module' or 'main')
    # are skipped — replaying a chapter doesn't reset a promoted card. Each
    # newly seeded card carries `recall_coins_earned=1` since reaching this
    # endpoint means the word was correctly recalled in the chapter's Recall
    # phase. The unique constraint makes the award idempotent.
    seeded = 0
    for w in body.words:
        es = (w.es or "").strip()
        en = (w.en or "").strip()
        if not es:
            continue
        stmt = (
            insert(VocabCard)
            .values(
                user_id=current_user.id,
                module_id=module_id,
                word_es=es,
                word_en=en,
                status="module",
                box=1,
                recall_coins_earned=1,
            )
            .on_conflict_do_nothing(constraint="uq_vocab_card")
        )
        r = db.execute(stmt)
        if r.rowcount:
            seeded += 1

    db.commit()

    # Late import to avoid circular dependency with tense_quest module.
    from app.api.v1.tense_quest import _user_points  # noqa: WPS433
    points = _user_points(db, current_user.id)

    return ChapterCompleteResponse(
        module_id=module_id,
        chapter_index=chapter_idx,
        was_new=was_new,
        cards_seeded=seeded,
        coins_awarded=seeded,
        points=points,
    )


@router.get("/module/{module_id}/review", response_model=ModuleReviewDeck)
async def module_review_deck(
    module_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Module-only SRS deck: status='module' cards for this module that are due
    now (due_at <= now), shuffled. Freshly-seeded cards default due_at=now() so
    they're due immediately after a chapter; a re-queued card waits
    ~10 min before it resurfaces. The FE gates access by checking
    chapter_completions in the progress payload first (no point reviewing if no
    chapters are done)."""
    now = datetime.now(timezone.utc)
    cards = (
        db.query(VocabCard)
        .filter(
            VocabCard.user_id == current_user.id,
            VocabCard.module_id == module_id,
            VocabCard.status == "module",
            VocabCard.due_at <= now,
        )
        .all()
    )
    out = [
        VocabReviewCard(
            card_id=str(c.id),
            module_id=c.module_id,
            word_es=c.word_es,
            word_en=c.word_en,
            status=c.status,
            box=c.box,
        )
        for c in cards
    ]
    random.shuffle(out)
    return ModuleReviewDeck(module_id=module_id, cards=out)


@router.post(
    "/module/{module_id}/review/attempt",
    response_model=ModuleReviewAttemptResult,
)
async def module_review_attempt(
    module_id: str,
    body: ReviewAttemptRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Record a module-deck review attempt. Promote on fast+correct;
    otherwise re-queue (status stays 'module', due_at bumped forward)."""
    card = (
        db.query(VocabCard)
        .filter(
            VocabCard.id == body.card_id,
            VocabCard.user_id == current_user.id,
            VocabCard.module_id == module_id,
        )
        .one_or_none()
    )
    if card is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Card not found")
    if card.status != "module":
        # Already promoted — treat the attempt as a no-op success rather than
        # an error; the FE will just advance to the next card.
        return ModuleReviewAttemptResult(card_id=str(card.id), promoted=False, requeued=False)

    now = datetime.now(timezone.utc)
    # Promote when the answer clears the engine's grade bar (correct and within
    # the typed slow ceiling — i.e. not a lapse). The new main-deck card enters
    # the shared ladder at box 1 (first review ~4h out).
    if srs.classify(body.correct, body.response_ms, "type") != "lapse":
        card.status = "main"
        card.box = srs.MIN_BOX
        card.due_at = now + srs.interval_for(srs.MIN_BOX)
        card.last_seen_at = now
        card.last_response_ms = body.response_ms
        db.commit()
        return ModuleReviewAttemptResult(card_id=str(card.id), promoted=True, requeued=False)

    # Re-queue: keep in module deck, bump last_seen and due forward a touch.
    card.last_seen_at = now
    card.last_response_ms = body.response_ms
    card.due_at = now + timedelta(minutes=srs.LAPSE_MINUTES)
    db.commit()
    return ModuleReviewAttemptResult(card_id=str(card.id), promoted=False, requeued=True)


@router.get("/review", response_model=MainReviewDeck)
async def main_review_deck(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Main vocab review deck — all status='main' cards with due_at <= now,
    ordered by due_at then shuffled within the due batch."""
    now = datetime.now(timezone.utc)
    cards = (
        db.query(VocabCard)
        .filter(
            VocabCard.user_id == current_user.id,
            VocabCard.status == "main",
            VocabCard.due_at <= now,
        )
        .order_by(VocabCard.due_at.asc())
        .all()
    )
    random.shuffle(cards)
    out = [
        VocabReviewCard(
            card_id=str(c.id),
            module_id=c.module_id,
            word_es=c.word_es,
            word_en=c.word_en,
            status=c.status,
            box=c.box,
        )
        for c in cards
    ]
    summary = _main_deck_summary(db, current_user.id)
    return MainReviewDeck(cards=out, total=summary.total, due=summary.due)


@router.post("/review/attempt", response_model=MainReviewAttemptResult)
async def main_review_attempt(
    body: ReviewAttemptRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Shared Leitner ladder on the main vocab deck (see `app/services/srs.py`).
    Vocab is typed-only: very-fast correct → box +2, correct → box +1 (cap box
    7), slow/wrong → box −2 (floored at 1) and a ~10 min re-queue."""
    card = (
        db.query(VocabCard)
        .filter(
            VocabCard.id == body.card_id,
            VocabCard.user_id == current_user.id,
            VocabCard.status == "main",
        )
        .one_or_none()
    )
    if card is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Card not found")

    now = datetime.now(timezone.utc)
    srs.apply_review(card, correct=body.correct, response_ms=body.response_ms,
                     response_mode="type", now=now)
    card.last_seen_at = now
    db.commit()
    return MainReviewAttemptResult(
        card_id=str(card.id),
        box=int(card.box),
        due_at=card.due_at.isoformat(),
    )
