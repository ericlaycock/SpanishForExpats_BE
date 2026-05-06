from sqlalchemy import Column, String, Boolean, Integer, DateTime, Date, ForeignKey, Text, JSON, CheckConstraint, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from datetime import datetime, timezone
from app.database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    onboarding_completed = Column(Boolean, default=False, nullable=False)
    onboarding_completed_at = Column(DateTime(timezone=True), nullable=True)
    selected_animation_types = Column(JSONB, nullable=True)  # e.g., ["banking", "restaurant"]
    dialect = Column(String, nullable=True)  # 'mexico', 'colombia', 'costa_rica'
    grammar_score = Column(String, nullable=True)  # Quiz grammar score
    vocab_score = Column(String, nullable=True)  # Quiz vocab score
    is_admin = Column(Boolean, default=False, nullable=False)
    alt_language = Column(String, nullable=True)  # null=Spanish, 'catalan', 'swedish'
    # Server-side flags for first-time feature explainers (coachmarks).
    # Shape: {"vocab_word_cards": true, "verb_lesson": true, ...}. Lookup
    # whitelist lives in app/api/v1/auth.py.
    seen_explainers = Column(JSONB, nullable=False, server_default="{}", default=dict)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Onboarding V2 profile fields
    name = Column(String, nullable=True)
    q0_spanish_level = Column(String, nullable=True)   # a/b/c/d
    q1_situation = Column(String, nullable=True)        # a/b/c
    q1_1_time_in_latam = Column(String, nullable=True)  # a/b/c (conditional)
    q2_country = Column(String, nullable=True)           # country name from map
    q3_tools = Column(JSONB, nullable=True)              # ["duolingo", "classes", ...]
    q4_proximity = Column(String, nullable=True)         # high/mid/low
    q6_conversations = Column(String, nullable=True)     # none/few/some/most
    
    # Relationships
    subscription = relationship("Subscription", back_populates="user", uselist=False)
    user_words = relationship("UserWord", back_populates="user")
    user_situations = relationship("UserSituation", back_populates="user")
    conversations = relationship("Conversation", back_populates="user")
    reports = relationship("UserReport", back_populates="user")


class Subscription(Base):
    __tablename__ = "subscriptions"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    active = Column(Boolean, default=False, nullable=False)
    tier = Column(String, nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Stripe
    stripe_customer_id = Column(String, nullable=True)
    stripe_subscription_id = Column(String, nullable=True)
    plan = Column(String, nullable=True)           # "pro" | "fluency"
    billing_cycle = Column(String, nullable=True)  # "monthly" | "6month"

    # Lifecycle (driven by Stripe webhook + the in-app cancel flow). When
    # `cancel_at_period_end` is true, `active` stays true until Stripe
    # actually deletes the subscription at the period end — at which point
    # the deleted webhook flips `active` to false.
    cancel_at_period_end = Column(Boolean, nullable=False, server_default="false", default=False)
    current_period_end = Column(DateTime(timezone=True), nullable=True)
    canceled_at = Column(DateTime(timezone=True), nullable=True)
    cancel_reason = Column(Text, nullable=True)

    # Relationships
    user = relationship("User", back_populates="subscription")


class Word(Base):
    __tablename__ = "words"
    
    id = Column(String, primary_key=True)
    spanish = Column(String, nullable=False)
    english = Column(String, nullable=False)
    word_category = Column(String, nullable=True)  # 'encounter' or 'high_frequency'
    frequency_rank = Column(Integer, nullable=True)  # Rank in frequency list (1-1000)
    word_type = Column(String, nullable=True, index=True)  # 'noun' | 'verb' | 'adjective' | 'adverb' | 'other'
    catalan = Column(String, nullable=True)
    swedish = Column(String, nullable=True)
    notes = Column(Text, nullable=True)  # Grammar/usage notes for frontend popup
    
    # Relationships
    situation_words = relationship("SituationWord", back_populates="word")
    user_words = relationship("UserWord", back_populates="word")


class Situation(Base):
    __tablename__ = "situations"
    
    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    animation_type = Column(String, nullable=False, index=True)  # e.g., "banking", "small_talk", "groceries"
    encounter_number = Column(Integer, nullable=False)  # 1-50 within each situation
    order_index = Column(Integer, nullable=False, index=True)
    is_free = Column(Boolean, default=False, nullable=False)
    goal = Column(Text, nullable=True)  # Goal/objective for this situation
    situation_type = Column(String, default='main', nullable=False)  # 'main' or 'grammar'
    vocab_level_required = Column(Integer, nullable=True)  # null for main situations
    video_embed_id = Column(String, nullable=True)  # Descript embed ID for grammar video

    # Relationships
    situation_words = relationship("SituationWord", back_populates="situation", order_by="SituationWord.position")
    user_situations = relationship("UserSituation", back_populates="situation")
    conversations = relationship("Conversation", back_populates="situation")


class SituationWord(Base):
    __tablename__ = "situation_words"
    
    situation_id = Column(String, ForeignKey("situations.id"), primary_key=True)
    word_id = Column(String, ForeignKey("words.id"), primary_key=True)
    position = Column(Integer, nullable=False)
    
    # Relationships
    situation = relationship("Situation", back_populates="situation_words")
    word = relationship("Word", back_populates="situation_words")


class UserWord(Base):
    __tablename__ = "user_words"
    __table_args__ = (
        CheckConstraint("status IN ('learning', 'mastered')", name="ck_user_words_status"),
    )

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    word_id = Column(String, ForeignKey("words.id"), primary_key=True)
    seen_count = Column(Integer, default=0, nullable=False)
    typed_correct_count = Column(Integer, default=0, nullable=False)
    spoken_correct_count = Column(Integer, default=0, nullable=False)
    hint_count = Column(Integer, default=0, nullable=False, server_default="0")
    status = Column(String, default="learning", nullable=False)
    mastery_level = Column(Integer, default=0, nullable=False)  # 0=unseen, 1=learned, 2-3=refreshed, 4=mastered
    next_refresh_at = Column(DateTime(timezone=True), nullable=True)
    source_situation_id = Column(String, ForeignKey("situations.id"), nullable=True)
    # The most recent surface form the user actually saw/heard for this word.
    # For verbs this is the conjugated form (e.g. "hará") rather than the
    # infinitive — used by the daily Grenade so the prompt deploys the form
    # the user has just learned, not a generic lemma.
    last_seen_form = Column(String, nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="user_words")
    word = relationship("Word", back_populates="user_words")
    source_situation = relationship("Situation")


class UserSituation(Base):
    __tablename__ = "user_situations"
    
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    situation_id = Column(String, ForeignKey("situations.id"), primary_key=True)
    started_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="user_situations")
    situation = relationship("Situation", back_populates="user_situations")


class Conversation(Base):
    __tablename__ = "conversations"
    __table_args__ = (
        CheckConstraint("mode IN ('text', 'voice')", name="ck_conversations_mode"),
        CheckConstraint("status IN ('active', 'complete')", name="ck_conversations_status"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    situation_id = Column(String, ForeignKey("situations.id"), nullable=False)
    mode = Column(String, nullable=False)  # 'text' or 'voice'
    conversation_type = Column(String, default="lesson", nullable=False)  # 'lesson' or 'refresh'
    target_word_ids = Column(JSONB, nullable=False)
    used_typed_word_ids = Column(JSONB, default=list, nullable=False)
    used_spoken_word_ids = Column(JSONB, default=list, nullable=False)
    status = Column(String, default="active", nullable=False)  # 'active' or 'complete'
    # Count of persisted user turns. Incremented by voice_turn_service.persist_turn
    # so the realtime flow (and legacy /voice-turn) can enforce the 30-turn hard
    # limit in check_completion even when the backend isn't orchestrating each
    # round-trip. Migration 020 adds it with default 0.
    turn_count = Column(Integer, default=0, nullable=False, server_default="0")
    # Per-conversation counter for "Need help?" sentence hints. Capped by
    # sentence_hint_service to prevent farming. Migration 026.
    sentence_hints_used = Column(Integer, default=0, nullable=False, server_default="0")
    # Counts user turns since the last new target was detected. Reset to 0 on
    # any turn that adds a fresh id to `used_spoken_word_ids`; incremented
    # otherwise. Drives the v3 system prompt's anti-stuck rule and the FE's
    # "Need help?" nudge toast.
    consecutive_no_progress_turns = Column(
        Integer, default=0, nullable=False, server_default="0",
    )
    # Snapshot of the FE's per-(verb, pronoun) chip list for grammar chat
    # lessons (`*_chat` situations). Populated at conversation creation from
    # `get_chat_target_forms`; used by `check_chat_chip_completion` so the
    # backend gates completion on the same chips the FE shows. NULL for
    # vocab encounters and non-chat grammar — those keep the legacy
    # infinitive-level completion path.
    chat_target_forms_json = Column(JSONB, nullable=True)
    # Cumulative set of chip ids ticked across all turns. Updated by
    # `voice_turn_service.persist_turn` (ANY voice turn — legacy or realtime),
    # so the FE can render green checks straight from the API response and the
    # `/realtime-turn` flow stays history-free.
    completed_chip_ids = Column(
        JSONB, default=list, nullable=False, server_default="'[]'::jsonb",
    )
    # Counts assistant turns flagged by `validate_assistant_reply` for either
    # leaking a pending chip's exact form OR closing the floor without a
    # question. Telemetry-only today — incremented in `/voice-turn/respond`
    # and `/realtime-turn` so we can quantify how often the LLM ignores the
    # turn-closing / no-leak rules in the v3 prompt. Migration 028.
    avatar_dead_end_turns = Column(
        Integer, default=0, nullable=False, server_default="0",
    )
    # Realtime steering state — id of the chip currently being elicited and
    # how many user turns we've stuck with it. Picked by
    # `realtime_steering.pick_next_target` after each /realtime-turn; reset
    # to NULL/0 when the user lands the form. NULL means "no active steer"
    # (first turn or just landed). See realtime_steering.py for the policy.
    steering_target_id = Column(Text, nullable=True)
    steering_target_age = Column(
        Integer, default=0, nullable=False, server_default="0",
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="conversations")
    situation = relationship("Situation", back_populates="conversations")


# Single source of truth for the category/status closed sets used by the
# Pydantic schemas and the CHECK constraints in migration 016.
REPORT_CATEGORIES = (
    'platform', 'translation', 'pronunciation',
    'voice_chat', 'subscription', 'suggestion', 'other',
)
REPORT_STATUSES = ('new', 'investigating', 'resolved', 'dismissed')


class UserReport(Base):
    __tablename__ = "user_reports"
    __table_args__ = (
        CheckConstraint(
            "category IN ('" + "','".join(REPORT_CATEGORIES) + "')",
            name="ck_user_reports_category",
        ),
        CheckConstraint(
            "status IN ('" + "','".join(REPORT_STATUSES) + "')",
            name="ck_user_reports_status",
        ),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    category = Column(String(32), nullable=False)
    description = Column(Text, nullable=False)
    context = Column(JSONB, nullable=False, default=dict, server_default="{}")
    status = Column(String(16), nullable=False, default="new", server_default="new", index=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), index=True)
    resolved_at = Column(DateTime(timezone=True), nullable=True)

    user = relationship("User", back_populates="reports")


class DailyEncounterLog(Base):
    __tablename__ = "daily_encounter_logs"
    __table_args__ = (
        {"comment": "Append-only log tracking each encounter start (including restarts) for daily limits"},
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    situation_id = Column(String, ForeignKey("situations.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User")
    situation = relationship("Situation")


class Grenade(Base):
    """A daily one-word challenge: the user must deploy the word in a real
    Spanish conversation. One per (user, assigned_date). Generated on demand
    after the user clicks "Make a grenade for me" — `question_es`/`question_en`
    are populated then. Recall is tracked via `used`/`answered_at` the day after.
    """
    __tablename__ = "grenades"
    __table_args__ = (
        UniqueConstraint("user_id", "assigned_date", name="uq_grenades_user_date"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    word_id = Column(String, ForeignKey("words.id"), nullable=False)
    # The exact form the user is challenged to deploy. For verbs this is the
    # conjugation (e.g. "hará"); for other word types the lemma. Stored
    # separately from word_id so renaming/reconjugating the source word doesn't
    # rewrite history.
    target_form = Column(String, nullable=False)
    pos = Column(String, nullable=True)  # 'verb' | 'noun' | 'adjective' | 'other'
    audience = Column(String, nullable=True)  # 'friend' | 'merchant'
    question_es = Column(Text, nullable=True)
    question_en = Column(Text, nullable=True)
    assigned_date = Column(Date, nullable=False, index=True)
    # Recall outcome: True = used, False = missed, None = not yet answered.
    used = Column(Boolean, nullable=True)
    answered_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user = relationship("User")
    word = relationship("Word")


class UserMilestoneEvent(Base):
    __tablename__ = "user_milestone_events"
    __table_args__ = (
        UniqueConstraint("user_id", "milestone_key", "situation_id", name="uq_user_milestone_situation"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    milestone_key = Column(String, nullable=False)  # phase_1a | phase_1b | phase_video | phase_drill | first_word
    situation_id = Column(String, ForeignKey("situations.id"), nullable=True)
    conversation_id = Column(UUID(as_uuid=True), ForeignKey("conversations.id"), nullable=True)
    occurred_at = Column(DateTime(timezone=True), server_default=func.now())


class SentenceHint(Base):
    """Audit row for each sentence hint generated in /voice-chat.

    Migration 026 introduces this table alongside `conversations.sentence_hints_used`.
    The counter on `conversations` enforces the per-encounter cap; this table
    keeps the human-readable artefacts (Spanish + gloss + audio URL) plus
    pointers back to the LLM/TTS rows so we can replay or investigate later.
    """
    __tablename__ = "sentence_hints"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id = Column(
        UUID(as_uuid=True),
        ForeignKey("conversations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    situation_id = Column(String, ForeignKey("situations.id"), nullable=True)
    spanish = Column(Text, nullable=False)
    english_gloss = Column(Text, nullable=False)
    audio_url = Column(Text, nullable=True)
    used_item_ids = Column(JSONB, default=list, nullable=False, server_default="[]")
    pending_count = Column(Integer, nullable=True)
    llm_request_id = Column(
        UUID(as_uuid=True),
        ForeignKey("llm_requests.id", ondelete="SET NULL"),
        nullable=True,
    )
    tts_request_id = Column(
        UUID(as_uuid=True),
        ForeignKey("tts_requests.id", ondelete="SET NULL"),
        nullable=True,
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class Cohort(Base):
    """A scheduled 3-day live cohort the user can register for at the end
    of the marketing webflow. Times are timezone-aware (stored as UTC); UI
    and email render in `timezone` plus the user's local zone.
    """
    __tablename__ = "cohorts"
    __table_args__ = (
        CheckConstraint(
            "visibility IN ('public', 'business_owner')",
            name="ck_cohorts_visibility",
        ),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    slug = Column(String(64), unique=True, nullable=False)
    name = Column(String(64), nullable=False)
    visibility = Column(String(32), nullable=False, server_default="public")
    capacity = Column(Integer, nullable=False, server_default="8")
    timezone = Column(String(64), nullable=False, server_default="America/Los_Angeles")
    session_1_start = Column(DateTime(timezone=True), nullable=False)
    session_2_start = Column(DateTime(timezone=True), nullable=False)
    session_3_start = Column(DateTime(timezone=True), nullable=False)
    duration_minutes = Column(Integer, nullable=False, server_default="60")
    is_active = Column(Boolean, nullable=False, server_default="true")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    registrations = relationship("CohortRegistration", back_populates="cohort")


class CohortRegistration(Base):
    """A single user's registration for a cohort. Created atomically with
    the User row at the end of the webflow. `confirmation_token` gates the
    public .ics download URL, so it must be unguessable.
    """
    __tablename__ = "cohort_registrations"
    __table_args__ = (
        UniqueConstraint("cohort_id", "email", name="uq_cohort_email"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    cohort_id = Column(Integer, ForeignKey("cohorts.id"), nullable=False, index=True)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=True,
        index=True,
    )
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, index=True)
    confirmation_token = Column(String(64), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    cohort = relationship("Cohort", back_populates="registrations")
    user = relationship("User")


class CohortWaitlist(Base):
    """Email collection for the picker's "all visible cohorts are full"
    state. Not tied to any particular cohort — interested users opt in to
    "next available", and we drain this list manually when we add windows.
    """
    __tablename__ = "cohort_waitlist"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=True)
    email = Column(String, nullable=False, unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class AnonymousFunnelEvent(Base):
    """One row per (session_id, event_key) — anonymous wizard funnel.

    Pre-signup tracking. The post-signup counterpart is `user_milestone_events`.
    Migration 030 introduces this table; the unique constraint provides
    idempotency so re-firing the same step is a no-op.

    Note: the JSONB column is `event_metadata`, not `metadata`. Declarative
    Base reserves the `metadata` attribute for table-collection introspection,
    so a column literally named `metadata` raises at class-definition time.
    """
    __tablename__ = "anonymous_funnel_events"
    __table_args__ = (
        UniqueConstraint("session_id", "event_key", name="uq_funnel_session_event"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(String(64), nullable=False, index=True)
    event_key = Column(String(64), nullable=False, index=True)
    occurred_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    event_metadata = Column(
        JSONB, nullable=False, server_default="{}", default=dict
    )


