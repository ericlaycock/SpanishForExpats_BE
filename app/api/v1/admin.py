"""Admin endpoints — user management and plan assignment."""
import logging
from datetime import datetime, timezone
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from sqlalchemy import text, func
from app.auth import get_current_user, get_password_hash, create_access_token
from app.database import get_db
from datetime import timedelta
from app.models import User, Subscription, Cohort, CohortRegistration, TrialReminder
from app.schemas import (
    AdminCohortListResponse,
    AdminCohortRegistrant,
    AdminCohortRow,
    CohortSession,
    FreeflowResponse,
    FreeflowUserRow,
    MilestoneInfo,
    WebpageflowResponse,
    WebpageflowStep,
)

logger = logging.getLogger(__name__)
router = APIRouter()

VALID_PLANS = {"free", "app", "pronounce", "app_pronounce"}


def _require_admin(user: User):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")


@router.get("/users")
def list_users(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _require_admin(current_user)

    rows = db.execute(text("""
        SELECT u.id, u.email, u.created_at, u.is_admin,
               s.tier, s.active
        FROM users u
        LEFT JOIN subscriptions s ON s.user_id = u.id
        ORDER BY u.created_at DESC
    """)).fetchall()

    return [
        {
            "id": str(r.id),
            "email": r.email,
            "created_at": r.created_at.isoformat() if r.created_at else None,
            "is_admin": r.is_admin,
            "plan": r.tier or "free",
            "subscription_active": r.active,
        }
        for r in rows
    ]


@router.patch("/users/{user_id}/plan")
def set_user_plan(
    user_id: str,
    body: dict,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _require_admin(current_user)

    plan = (body.get("plan") or "free").strip().lower()
    if plan not in VALID_PLANS:
        raise HTTPException(status_code=400, detail=f"Invalid plan. Must be one of: {', '.join(sorted(VALID_PLANS))}")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    sub = db.query(Subscription).filter(Subscription.user_id == user_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="Subscription record not found")

    sub.tier = plan if plan != "free" else None
    sub.active = plan in ("app", "app_pronounce")
    db.commit()

    logger.info(f"[Admin] {current_user.email} changed {user.email} plan to '{plan}'")
    return {"id": user_id, "plan": plan, "subscription_active": sub.active}


@router.get("/freeflow", response_model=FreeflowResponse)
def get_freeflow(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    _require_admin(current_user)

    rows = db.execute(text("""
        WITH
        user_m2 AS (
            SELECT user_id, MIN(started_at) AS m2_ts
            FROM user_situations
            GROUP BY user_id
        ),
        user_m3 AS (
            SELECT user_id, MIN(occurred_at) AS m3_ts
            FROM user_milestone_events
            WHERE milestone_key IN ('phase_1a', 'phase_video')
            GROUP BY user_id
        ),
        user_m4 AS (
            SELECT user_id, MIN(occurred_at) AS m4_ts
            FROM user_milestone_events
            WHERE milestone_key IN ('phase_1b', 'phase_drill')
            GROUP BY user_id
        ),
        user_m5 AS (
            SELECT user_id, MIN(occurred_at) AS m5_ts
            FROM user_milestone_events
            WHERE milestone_key = 'first_word'
            GROUP BY user_id
        ),
        user_m6 AS (
            SELECT user_id, MIN(completed_at) AS m6_ts
            FROM conversations
            WHERE conversation_type = 'lesson' AND completed_at IS NOT NULL
            GROUP BY user_id
        ),
        ranked_situations AS (
            SELECT user_id, started_at, completed_at,
                   ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY started_at ASC) AS rn
            FROM user_situations
        ),
        user_lesson_ts AS (
            SELECT user_id,
                MAX(CASE WHEN rn = 2 THEN started_at   END) AS m7_ts,
                MAX(CASE WHEN rn = 2 THEN completed_at END) AS m8_ts,
                MAX(CASE WHEN rn = 3 THEN started_at   END) AS m9_ts,
                MAX(CASE WHEN rn = 3 THEN completed_at END) AS m10_ts,
                MAX(CASE WHEN rn = 4 THEN started_at   END) AS m11_ts,
                MAX(CASE WHEN rn = 4 THEN completed_at END) AS m12_ts,
                MAX(CASE WHEN rn = 5 THEN started_at   END) AS m13_ts,
                MAX(CASE WHEN rn = 5 THEN completed_at END) AS m14_ts,
                MAX(CASE WHEN rn = 6 THEN started_at   END) AS m15_ts,
                MAX(CASE WHEN rn = 6 THEN completed_at END) AS m16_ts,
                MAX(CASE WHEN rn = 7 THEN started_at   END) AS m17_ts,
                MAX(CASE WHEN rn = 7 THEN completed_at END) AS m18_ts
            FROM ranked_situations
            WHERE rn BETWEEN 2 AND 7
            GROUP BY user_id
        ),
        user_m19 AS (
            SELECT user_id, MIN(occurred_at) AS m19_ts
            FROM user_milestone_events
            WHERE milestone_key = 'paywall_hit'
            GROUP BY user_id
        ),
        user_pathway AS (
            SELECT user_id,
                MAX(CASE WHEN milestone_key IN ('phase_1a', 'phase_1b') THEN 'V' END) AS v_path,
                MAX(CASE WHEN milestone_key IN ('phase_video', 'phase_drill') THEN 'G' END) AS g_path
            FROM user_milestone_events
            GROUP BY user_id
        )
        SELECT
            u.id AS user_id,
            u.email,
            u.is_admin,
            u.created_at AS m0_ts,
            u.onboarding_completed_at AS m1_ts,
            u.dialect,
            u.grammar_score,
            u.vocab_score,
            u.selected_animation_types,
            u.name,
            u.q0_spanish_level,
            u.q1_situation,
            u.q1_1_time_in_latam,
            u.q2_country,
            u.q3_tools,
            u.q4_proximity,
            u.q6_conversations,
            COALESCE(s.active, false) AS subscription_active,
            m2.m2_ts,
            m3.m3_ts,
            m4.m4_ts,
            m5.m5_ts,
            m6.m6_ts,
            ult.m7_ts,
            ult.m8_ts,
            ult.m9_ts,
            ult.m10_ts,
            ult.m11_ts,
            ult.m12_ts,
            ult.m13_ts,
            ult.m14_ts,
            ult.m15_ts,
            ult.m16_ts,
            ult.m17_ts,
            ult.m18_ts,
            m19.m19_ts,
            COALESCE(pw.v_path, pw.g_path) AS pathway
        FROM users u
        LEFT JOIN subscriptions s ON s.user_id = u.id
        LEFT JOIN user_m2 m2 ON m2.user_id = u.id
        LEFT JOIN user_m3 m3 ON m3.user_id = u.id
        LEFT JOIN user_m4 m4 ON m4.user_id = u.id
        LEFT JOIN user_m5 m5 ON m5.user_id = u.id
        LEFT JOIN user_m6 m6 ON m6.user_id = u.id
        LEFT JOIN user_lesson_ts ult ON ult.user_id = u.id
        LEFT JOIN user_m19 m19 ON m19.user_id = u.id
        LEFT JOIN user_pathway pw ON pw.user_id = u.id
        ORDER BY u.created_at DESC
    """)).fetchall()

    def _delta(ts, prev_ts):
        if ts is None or prev_ts is None:
            return None
        # Keep sub-1s precision — int() used to truncate 0.999s → 0, which made
        # most consecutive milestones render as "+0s" since real users hit
        # M3→M4 in 200–800 ms.
        return (ts - prev_ts).total_seconds()

    def _mi(ts, prev_ts):
        return MilestoneInfo(
            timestamp=ts,
            delta_seconds=_delta(ts, prev_ts),
        )

    users = []
    for r in rows:
        timestamps = [
            r.m0_ts, r.m1_ts, r.m2_ts, r.m3_ts, r.m4_ts, r.m5_ts, r.m6_ts, r.m7_ts, r.m8_ts,
            r.m9_ts, r.m10_ts, r.m11_ts, r.m12_ts, r.m13_ts, r.m14_ts, r.m15_ts, r.m16_ts,
            r.m17_ts, r.m18_ts, r.m19_ts,
        ]
        current_milestone = 0
        for i, ts in enumerate(timestamps):
            if ts is not None:
                current_milestone = i

        users.append(FreeflowUserRow(
            user_id=str(r.user_id),
            email=r.email,
            is_admin=bool(r.is_admin),
            subscription_active=bool(r.subscription_active),
            pathway=r.pathway,
            dialect=r.dialect,
            grammar_score=r.grammar_score,
            vocab_score=r.vocab_score,
            selected_animation_types=r.selected_animation_types or [],
            m0=_mi(r.m0_ts, None),
            m1=_mi(r.m1_ts, r.m0_ts),
            m2=_mi(r.m2_ts, r.m1_ts),
            m3=_mi(r.m3_ts, r.m2_ts),
            m4=_mi(r.m4_ts, r.m3_ts),
            m5=_mi(r.m5_ts, r.m4_ts),
            m6=_mi(r.m6_ts, r.m5_ts),
            m7=_mi(r.m7_ts, r.m6_ts),
            m8=_mi(r.m8_ts, r.m7_ts),
            m9=_mi(r.m9_ts, r.m8_ts),
            m10=_mi(r.m10_ts, r.m9_ts),
            m11=_mi(r.m11_ts, r.m10_ts),
            m12=_mi(r.m12_ts, r.m11_ts),
            m13=_mi(r.m13_ts, r.m12_ts),
            m14=_mi(r.m14_ts, r.m13_ts),
            m15=_mi(r.m15_ts, r.m14_ts),
            m16=_mi(r.m16_ts, r.m15_ts),
            m17=_mi(r.m17_ts, r.m16_ts),
            m18=_mi(r.m18_ts, r.m17_ts),
            m19=_mi(r.m19_ts, r.m18_ts),
            current_milestone=current_milestone,
            name=r.name,
            q0_spanish_level=r.q0_spanish_level,
            q1_situation=r.q1_situation,
            q1_1_time_in_latam=r.q1_1_time_in_latam,
            q2_country=r.q2_country,
            q3_tools=r.q3_tools,
            q4_proximity=r.q4_proximity,
            q6_conversations=r.q6_conversations,
        ))

    return FreeflowResponse(users=users)


class SeedTestUserRequest(BaseModel):
    email: EmailStr
    password: str
    is_admin: bool = False
    plan: str = "free"


class SeedTestUserResponse(BaseModel):
    user_id: str
    email: str
    is_admin: bool
    access_token: str


@router.post("/users/seed-test", response_model=SeedTestUserResponse)
def seed_test_user(
    body: SeedTestUserRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Provision a fully-onboarded test user without driving the onboarding portal.
    Skips the country picker and quiz steps that are tedious or inaccessible
    via Playwright. The created user lands directly on the dashboard.
    """
    _require_admin(current_user)

    if body.plan not in VALID_PLANS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid plan. Must be one of: {', '.join(sorted(VALID_PLANS))}",
        )

    if db.query(User).filter(User.email == body.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    now = datetime.now(timezone.utc)
    user = User(
        email=body.email,
        password_hash=get_password_hash(body.password),
        is_admin=body.is_admin,
        onboarding_completed=True,
        onboarding_completed_at=now,
        # Realistic defaults so the dashboard and recommendation engine have
        # something to chew on. Mirrors qa@test.com pattern in seed_qa.py.
        name="Seeded Test User",
        dialect="mexico",
        selected_animation_types=["restaurant", "small_talk"],
        q0_spanish_level="b",
        q1_situation="c",
        q1_1_time_in_latam="c",
        q2_country="MX",
        q3_tools=["duolingo"],
        q4_proximity="high",
        q6_conversations="few",
        vocab_score="beginner",
        grammar_score="beginner",
    )
    db.add(user)
    db.flush()  # populate user.id before referencing it

    sub = Subscription(
        user_id=user.id,
        tier=body.plan if body.plan != "free" else None,
        active=body.plan in ("app", "app_pronounce"),
    )
    db.add(sub)
    db.commit()
    db.refresh(user)

    token = create_access_token({"sub": str(user.id), "plan": body.plan})
    logger.info(
        "[Admin] %s seeded test user %s (is_admin=%s, plan=%s)",
        current_user.email, user.email, user.is_admin, body.plan,
    )
    return SeedTestUserResponse(
        user_id=str(user.id),
        email=user.email,
        is_admin=bool(user.is_admin),
        access_token=token,
    )


# ---------------------------------------------------------------------------
# Webpageflow — anonymous pre-signup funnel
# ---------------------------------------------------------------------------

# Funnel order matters here. Both the BE response and the FE bar chart trust
# this list as the canonical step ordering. Update in lockstep with the
# whitelist in app/schemas.py::WEBPAGEFLOW_EVENT_KEYS.
WEBPAGEFLOW_STEPS = [
    ("landing_view",      "Landing visit (Hero)"),
    ("build_plan_click",  "Hero → How it Works"),
    ("how_it_works_cta",  "How it Works → Try Free"),
    ("book_call_click",   "Book free trial (Calendly)"),
    # Free-trial memorize → SMS follow-up funnel (drop-off readable top→bottom).
    ("ft_start",            "Free trial: start"),
    ("ft_memorize_start",   "Free trial: memorize utility"),
    ("ft_cycle_1",          "Free trial: 1 cycle done"),
    ("ft_cycle_2",          "Free trial: 2 cycles done"),
    ("ft_cycle_3",          "Free trial: 3 cycles done"),
    ("ft_cycle_4",          "Free trial: 4 cycles done"),
    ("ft_cycle_5",          "Free trial: 5 cycles done"),
    ("ft_cycle_6plus",      "Free trial: 6+ cycles done"),
    ("ft_mastered",         "Free trial: mastered (100%)"),
    ("ft_signup_submitted", "Free trial: phone signup"),
    ("ft_recall_open",      "Free trial: opened SMS link"),
    ("ft_recall_correct",   "Free trial: recalled correctly"),
    ("ft_recall_wrong",     "Free trial: recall missed"),
    ("ft_application_done", "Free trial: finished speaking"),
    ("ft_cta_view",         "Free trial: reached CTA"),
]


@router.get("/webpageflow", response_model=WebpageflowResponse)
def get_webpageflow(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    source: Optional[str] = Query(
        None,
        description=(
            "Filter funnel by utm_source captured in event_metadata. "
            "Restricts each step's count to sessions that ever fired ANY "
            "event with the matching source."
        ),
    ),
):
    _require_admin(current_user)

    if source:
        # Limit to sessions that have at least one event row tagged with
        # the requested source. Using EXISTS instead of a join keeps the
        # COUNT(DISTINCT) honest (no row multiplication).
        rows = db.execute(
            text("""
                SELECT a.event_key, COUNT(DISTINCT a.session_id) AS n
                FROM anonymous_funnel_events a
                WHERE EXISTS (
                    SELECT 1 FROM anonymous_funnel_events b
                    WHERE b.session_id = a.session_id
                      AND b.event_metadata ->> 'utm_source' = :source
                )
                GROUP BY a.event_key
            """),
            {"source": source},
        ).fetchall()
    else:
        rows = db.execute(text("""
            SELECT event_key, COUNT(DISTINCT session_id) AS n
            FROM anonymous_funnel_events
            GROUP BY event_key
        """)).fetchall()

    counts = {r.event_key: int(r.n) for r in rows}

    return WebpageflowResponse(steps=[
        WebpageflowStep(event_key=key, label=label, count=counts.get(key, 0))
        for key, label in WEBPAGEFLOW_STEPS
    ])


class TrialConversionsResponse(BaseModel):
    # Website → free-trial → call funnel (distinct anonymous sessions).
    visits: int            # landing_view
    trial_starts: int      # ft_start
    memorize_started: int  # ft_memorize_start
    mastered: int          # ft_mastered (finished the memorize loop)
    calls_booked: int      # book_call_click
    # Per-person SMS follow-up (trial_reminders — chains across the day gap).
    phone_signups: int     # distinct users who gave a phone number
    texts_sent: int        # reminders actually texted
    returned: int          # reminders completed (came back + finished recall)


@router.get("/trial-conversions", response_model=TrialConversionsResponse)
def get_trial_conversions(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Full conversion: website visits → free-trial start → mastered → phone
    signup → texted → returned → call booked."""
    _require_admin(current_user)

    rows = db.execute(text("""
        SELECT event_key, COUNT(DISTINCT session_id) AS n
        FROM anonymous_funnel_events
        WHERE event_key IN (
            'landing_view', 'ft_start', 'ft_memorize_start',
            'ft_mastered', 'book_call_click'
        )
        GROUP BY event_key
    """)).fetchall()
    c = {r.event_key: int(r.n) for r in rows}

    signups = db.query(func.count(func.distinct(TrialReminder.user_id))).scalar() or 0
    texts = (
        db.query(func.count(TrialReminder.id))
        .filter(TrialReminder.sent_at.isnot(None))
        .scalar()
        or 0
    )
    returned = (
        db.query(func.count(TrialReminder.id))
        .filter(TrialReminder.completed_at.isnot(None))
        .scalar()
        or 0
    )

    return TrialConversionsResponse(
        visits=c.get("landing_view", 0),
        trial_starts=c.get("ft_start", 0),
        memorize_started=c.get("ft_memorize_start", 0),
        mastered=c.get("ft_mastered", 0),
        calls_booked=c.get("book_call_click", 0),
        phone_signups=int(signups),
        texts_sent=int(texts),
        returned=int(returned),
    )


@router.post("/webpageflow/reset")
def reset_webpageflow(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Wipe every row from anonymous_funnel_events. Admin-only.

    Used to clear the funnel chart after a tracking-schema change so the
    history of broken/orphaned events doesn't keep inflating the numbers.
    """
    _require_admin(current_user)
    result = db.execute(text("DELETE FROM anonymous_funnel_events"))
    db.commit()
    return {"status": "ok", "rows_deleted": int(result.rowcount or 0)}


@router.get("/cohorts", response_model=AdminCohortListResponse)
def admin_list_cohorts(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Return every cohort with its registrant list. Used by the admin
    Cohorts tab to monitor sign-ups."""
    _require_admin(current_user)

    cohorts = (
        db.query(Cohort)
        .order_by(Cohort.session_1_start.asc(), Cohort.id.asc())
        .all()
    )

    rows: list[AdminCohortRow] = []
    for cohort in cohorts:
        regs = (
            db.query(CohortRegistration)
            .filter(CohortRegistration.cohort_id == cohort.id)
            .order_by(CohortRegistration.created_at.asc())
            .all()
        )
        duration = timedelta(minutes=cohort.duration_minutes)
        sessions = [
            CohortSession(index=i + 1, start_utc=start, end_utc=start + duration)
            for i, start in enumerate(
                (cohort.session_1_start, cohort.session_2_start, cohort.session_3_start)
            )
        ]
        rows.append(
            AdminCohortRow(
                id=cohort.id,
                slug=cohort.slug,
                name=cohort.name,
                visibility=cohort.visibility,
                timezone=cohort.timezone,
                capacity=cohort.capacity,
                duration_minutes=cohort.duration_minutes,
                spots_filled=len(regs),
                sessions=sessions,
                registrants=[
                    AdminCohortRegistrant(
                        name=r.name,
                        email=r.email,
                        registered_at=r.created_at,
                    )
                    for r in regs
                ],
            )
        )

    return AdminCohortListResponse(cohorts=rows)
