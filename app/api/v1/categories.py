"""Per-user grammar-category unlock state.

New users land on the dashboard map with all five categories locked (no row
in `user_category_progress` → treated as locked). Tapping a locked category
on the FE routes to that category's diagnostic page; when the diagnostic
completes, the FE POSTs here to flip `unlocked_at`.

Existing users (pre-2026-05-14) were grandfathered to fully-unlocked via
migration `044_user_category_progress.py`.
"""
from datetime import datetime, timezone
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.data.grammar_categories import CATEGORIES, CATEGORY_LABELS
from app.models import User, UserCategoryProgress

router = APIRouter()


# ─── Schemas ──────────────────────────────────────────────────────────────────


class CategoryStatus(BaseModel):
    category: str
    label: str
    unlocked: bool
    diagnostic_result: str | None  # 'ok' | 'needs_work' | None
    unlocked_at: datetime | None
    diagnostic_at: datetime | None


class CategoryStatusResponse(BaseModel):
    categories: list[CategoryStatus]


class DiagnosticSubmission(BaseModel):
    # Mirrors Tense Quest's diagnostic taxonomy (see migration 043's widened
    # check on `tense_quest_diagnostic.result`):
    # - 'ok'         all prompts correct AND none exceeded the hidden 7s budget
    # - 'ok_slow'    all prompts correct but at least one was slow (>7s)
    # - 'needs_work' any prompt was wrong (regardless of speed)
    # Either result unlocks the category — the diagnostic's job is to gate
    # access and record the user's starting point, not to fail them out.
    result: Literal["ok", "ok_slow", "needs_work"]


class DiagnosticResponse(BaseModel):
    category: str
    unlocked: bool
    diagnostic_result: str  # 'ok' | 'ok_slow' | 'needs_work'
    unlocked_at: datetime


# ─── Helpers ──────────────────────────────────────────────────────────────────


def _validate_category(category: str) -> None:
    if category not in CATEGORIES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unknown category: {category!r}. Valid: {CATEGORIES}",
        )


# ─── Endpoints ────────────────────────────────────────────────────────────────


@router.get("/status", response_model=CategoryStatusResponse)
async def get_category_status(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Return unlock state for every category. Missing rows are reported as
    locked — that's how new users see the map by default."""
    rows = (
        db.query(UserCategoryProgress)
        .filter(UserCategoryProgress.user_id == current_user.id)
        .all()
    )
    by_cat = {row.category: row for row in rows}

    categories = []
    for cat in CATEGORIES:
        row = by_cat.get(cat)
        categories.append(
            CategoryStatus(
                category=cat,
                label=CATEGORY_LABELS[cat],
                unlocked=bool(row and row.unlocked_at),
                diagnostic_result=row.diagnostic_result if row else None,
                unlocked_at=row.unlocked_at if row else None,
                diagnostic_at=row.diagnostic_at if row else None,
            )
        )
    return CategoryStatusResponse(categories=categories)


@router.post("/{category}/diagnostic", response_model=DiagnosticResponse)
async def submit_category_diagnostic(
    category: str,
    submission: DiagnosticSubmission,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Record a diagnostic outcome and unlock the category.

    Idempotent on `(user_id, category)` — re-running the diagnostic
    overwrites the result and refreshes `diagnostic_at`. `unlocked_at` is
    set on first unlock and preserved on subsequent submissions so the
    "you've been here a while" semantic is monotonic.
    """
    _validate_category(category)
    now = datetime.now(timezone.utc)

    row = (
        db.query(UserCategoryProgress)
        .filter(
            UserCategoryProgress.user_id == current_user.id,
            UserCategoryProgress.category == category,
        )
        .one_or_none()
    )

    if row is None:
        row = UserCategoryProgress(
            user_id=current_user.id,
            category=category,
            diagnostic_result=submission.result,
            unlocked_at=now,
            diagnostic_at=now,
        )
        db.add(row)
    else:
        row.diagnostic_result = submission.result
        row.diagnostic_at = now
        if row.unlocked_at is None:
            row.unlocked_at = now

    db.commit()
    db.refresh(row)
    return DiagnosticResponse(
        category=category,
        unlocked=True,
        diagnostic_result=row.diagnostic_result,
        unlocked_at=row.unlocked_at,
    )
