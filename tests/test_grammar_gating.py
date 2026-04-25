"""Comprehensive tests for the VL/GL grammar gating system."""
import uuid
from datetime import datetime, timezone

from app.models import User, UserWord, UserSituation, Situation, Word, SituationWord
from app.api.v1.situations import get_vocab_level, get_grammar_level
from app.data.grammar_situations import (
    GRAMMAR_SITUATIONS,
    GL_VL_THRESHOLDS,
    GL_TITLES,
    GL_SORTED,
    get_next_gate,
    get_all_grammar_situation_ids,
)
from app.services.voice_turn_service import get_language_mode


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_user(db):
    from app.auth import get_password_hash
    user = User(
        id=uuid.uuid4(),
        email=f"gl_{uuid.uuid4().hex[:8]}@test.com",
        password_hash=get_password_hash("testpass123"),
    )
    db.add(user)
    db.flush()
    return user


def _make_hf_words(db, count: int) -> list[Word]:
    """Create N high-frequency words."""
    words = []
    for i in range(count):
        w = Word(
            id=f"gl_hf_{uuid.uuid4().hex[:6]}_{i}",
            spanish=f"hfword{i}",
            english=f"hfword_en{i}",
            word_category="high_frequency",
            frequency_rank=i + 1,
        )
        db.add(w)
        words.append(w)
    db.flush()
    return words


def _make_encounter_words(db, count: int) -> list[Word]:
    words = []
    for i in range(count):
        w = Word(
            id=f"gl_enc_{uuid.uuid4().hex[:6]}_{i}",
            spanish=f"encword{i}",
            english=f"encword_en{i}",
            word_category="encounter",
        )
        db.add(w)
        words.append(w)
    db.flush()
    return words


def _make_grammar_words(db, count: int) -> list[Word]:
    words = []
    for i in range(count):
        w = Word(
            id=f"gl_gram_{uuid.uuid4().hex[:6]}_{i}",
            spanish=f"gramword{i}",
            english=f"gramword_en{i}",
            word_category="grammar",
        )
        db.add(w)
        words.append(w)
    db.flush()
    return words


def _set_user_words(db, user, words, mastery_level: int):
    for w in words:
        uw = UserWord(
            user_id=user.id,
            word_id=w.id,
            mastery_level=mastery_level,
            status="mastered" if mastery_level >= 4 else "learning",
        )
        db.add(uw)
    db.flush()


def _complete_grammar(db, user, target_gl: float):
    """Mark all grammar situations with grammar_level <= target_gl as completed."""
    now = datetime.now(timezone.utc)
    for sid in get_all_grammar_situation_ids():
        cfg = GRAMMAR_SITUATIONS[sid]
        if cfg["grammar_level"] > target_gl:
            continue
        us = UserSituation(
            user_id=user.id,
            situation_id=sid,
            started_at=now,
            completed_at=now,
        )
        db.add(us)
    db.flush()


def _ensure_grammar_situations_exist(db):
    """Ensure grammar situations exist as Situation rows so UserSituation FKs work."""
    for sid, cfg in GRAMMAR_SITUATIONS.items():
        existing = db.query(Situation).filter(Situation.id == sid).first()
        if not existing:
            db.add(Situation(
                id=sid,
                title=cfg["title"],
                animation_type="grammar",
                encounter_number=int(cfg["grammar_level"] * 100),
                order_index=1000 + int(cfg["grammar_level"] * 100),
                is_free=True,
                situation_type="grammar",
            ))
    db.flush()


# ===========================================================================
# VOCAB LEVEL TESTS
# ===========================================================================

def test_vocab_level_counts_mastery_1_and_above(db):
    """VL should count HF words at mastery_level >= 1."""
    user = _make_user(db)
    words = _make_hf_words(db, 5)

    # mastery=0 → not counted
    _set_user_words(db, user, words, mastery_level=0)
    assert get_vocab_level(db, user.id) == 0

    # mastery=1 → counted
    for w in words:
        uw = db.query(UserWord).filter(UserWord.user_id == user.id, UserWord.word_id == w.id).one()
        uw.mastery_level = 1
    db.flush()
    assert get_vocab_level(db, user.id) == 5

    # mastery=2,3,4 → also counted
    for i, w in enumerate(words):
        uw = db.query(UserWord).filter(UserWord.user_id == user.id, UserWord.word_id == w.id).one()
        uw.mastery_level = 2 + (i % 3)  # 2, 3, 4, 2, 3
    db.flush()
    assert get_vocab_level(db, user.id) == 5


def test_vocab_level_excludes_encounter_words(db):
    """Encounter words at any mastery level should not count toward VL."""
    user = _make_user(db)
    enc_words = _make_encounter_words(db, 3)
    _set_user_words(db, user, enc_words, mastery_level=1)
    assert get_vocab_level(db, user.id) == 0


def test_vocab_level_excludes_grammar_words(db):
    """Grammar words at any mastery level should not count toward VL."""
    user = _make_user(db)
    gram_words = _make_grammar_words(db, 3)
    _set_user_words(db, user, gram_words, mastery_level=1)
    assert get_vocab_level(db, user.id) == 0


def test_vocab_level_mixed_categories(db):
    """Only HF words count, even when mixed with other categories."""
    user = _make_user(db)
    hf = _make_hf_words(db, 3)
    enc = _make_encounter_words(db, 2)
    gram = _make_grammar_words(db, 2)
    _set_user_words(db, user, hf + enc + gram, mastery_level=1)
    assert get_vocab_level(db, user.id) == 3


# ===========================================================================
# GRAMMAR LEVEL TESTS
# ===========================================================================

def test_grammar_level_zero_with_no_completions(db):
    """New user with no completed grammar situations → GL=0."""
    _ensure_grammar_situations_exist(db)
    user = _make_user(db)
    assert get_grammar_level(db, user.id) == 0


def test_grammar_level_from_single_completion(db):
    """Completing grammar_pronouns → GL=1."""
    _ensure_grammar_situations_exist(db)
    user = _make_user(db)
    _complete_grammar(db, user, 1)
    assert get_grammar_level(db, user.id) == 1


def test_grammar_level_is_max_of_completions(db):
    """GL = max grammar_level of completed situations."""
    _ensure_grammar_situations_exist(db)
    user = _make_user(db)
    _complete_grammar(db, user, 3)  # Completes GL 1, 2, 3
    assert get_grammar_level(db, user.id) == 3


def test_grammar_level_handles_float_values(db):
    """GL handles float values like 4.5, 10.3, 10.6."""
    _ensure_grammar_situations_exist(db)
    user = _make_user(db)
    _complete_grammar(db, user, 4.5)
    assert get_grammar_level(db, user.id) == 4.5


def test_grammar_level_sequential_enforcement(db):
    """GL requires sequential completion — skipping GL 9 caps you at GL 8."""
    _ensure_grammar_situations_exist(db)
    user = _make_user(db)
    # Complete GL 1 through 8 and GL 17 (skip 9-10.6)
    now = datetime.now(timezone.utc)
    for sid in get_all_grammar_situation_ids():
        cfg = GRAMMAR_SITUATIONS[sid]
        gl = cfg["grammar_level"]
        if gl <= 8 or gl == 17:
            db.add(UserSituation(
                user_id=user.id,
                situation_id=sid,
                started_at=now,
                completed_at=now,
            ))
    db.flush()
    # GL stops at 8 because GL 9 is incomplete — can't skip ahead
    assert get_grammar_level(db, user.id) == 8


def test_grammar_level_ignores_non_grammar_situations(db):
    """Completing a main (non-grammar) situation doesn't affect GL."""
    _ensure_grammar_situations_exist(db)
    user = _make_user(db)

    main_sit = Situation(
        id=f"main_{uuid.uuid4().hex[:6]}",
        title="Main Situation",
        animation_type="banking",
        encounter_number=1,
        order_index=1,
        is_free=True,
    )
    db.add(main_sit)
    db.flush()

    db.add(UserSituation(
        user_id=user.id,
        situation_id=main_sit.id,
        started_at=datetime.now(timezone.utc),
        completed_at=datetime.now(timezone.utc),
    ))
    db.flush()

    assert get_grammar_level(db, user.id) == 0


def test_grammar_level_requires_all_lessons_at_gl(db):
    """GL 3 has 3 lessons. Completing only 1 or 2 should NOT credit GL 3."""
    _ensure_grammar_situations_exist(db)
    user = _make_user(db)
    now = datetime.now(timezone.utc)

    # Complete GL 1 and 2 first (prerequisites)
    _complete_grammar(db, user, 2)
    assert get_grammar_level(db, user.id) == 2

    # Complete only the first lesson of GL 3
    gl3_situations = [
        sid for sid, cfg in GRAMMAR_SITUATIONS.items()
        if cfg["grammar_level"] == 3
    ]
    assert len(gl3_situations) >= 2, "GL 3 should have multiple lessons"

    # Complete just the first lesson
    db.add(UserSituation(
        user_id=user.id,
        situation_id=gl3_situations[0],
        started_at=now,
        completed_at=now,
    ))
    db.flush()
    # GL should still be 2 — not all GL 3 lessons are done
    assert get_grammar_level(db, user.id) == 2

    # Complete all remaining GL 3 lessons
    for sid in gl3_situations[1:]:
        db.add(UserSituation(
            user_id=user.id,
            situation_id=sid,
            started_at=now,
            completed_at=now,
        ))
    db.flush()
    # NOW GL should be 3
    assert get_grammar_level(db, user.id) == 3


# ===========================================================================
# GATING LOGIC TESTS (get_next_gate)
# ===========================================================================

def test_not_gated_when_vl_below_threshold():
    """GL=0, VL=9 → not gated (GL 1 needs VL 10)."""
    assert get_next_gate(0, 9) is None


def test_gated_exactly_at_threshold():
    """GL=0, VL=10 → gated on GL 1 (Pronouns)."""
    gate = get_next_gate(0, 10)
    assert gate is not None
    assert gate["grammar_level"] == 1
    assert gate["title"] == "Pronouns"
    assert gate["vl_threshold"] == 10
    assert gate["has_content"] is True
    assert gate["situation_id"] == "grammar_pronouns"


def test_gated_above_threshold():
    """GL=0, VL=50 → gated on GL 1 (Pronouns), not GL 2."""
    gate = get_next_gate(0, 50)
    assert gate is not None
    assert gate["grammar_level"] == 1


def test_not_gated_after_completing_grammar():
    """GL=1, VL=10 → not gated (next is GL 2 at VL 15, 10 < 15)."""
    assert get_next_gate(1, 10) is None


def test_gated_on_next_level():
    """GL=1, VL=15 → gated on GL 2 (Grammatical Gender)."""
    gate = get_next_gate(1, 15)
    assert gate is not None
    assert gate["grammar_level"] == 2
    assert gate["title"] == "Grammatical Gender"


def test_coming_soon_gate():
    """GL=10.6, VL=550 → gated on GL 11 (Tengo que / Me toca / Necesito).

    Originally asserted has_content=False — GL 11 was a placeholder. After
    the GL 11–20 build-out, every GL through 20 has content; the test is
    re-asserted to match the new ground truth.
    """
    gate = get_next_gate(10.6, 550)
    assert gate is not None
    assert gate["grammar_level"] == 11
    assert gate["has_content"] is True
    assert gate["situation_id"] is not None
    assert gate["title"] == "Tengo que / Me toca / Necesito"


def test_coming_soon_blocks_even_with_high_vl():
    """GL=10.6, VL=1000 → gated on GL 11 (the next level above 10.6)."""
    gate = get_next_gate(10.6, 1000)
    assert gate is not None
    assert gate["grammar_level"] == 11  # Not 17!
    assert gate["has_content"] is True


def test_not_gated_at_max_gl():
    """GL=20 → never gated regardless of VL."""
    assert get_next_gate(20, 9999) is None


def test_grammar_ahead_of_vocab():
    """GL=9, VL=400 → not gated (next GL 10 needs VL 510, 400 < 510)."""
    assert get_next_gate(9, 400) is None


def test_gated_with_gap_in_completions():
    """GL=9, VL=520 → gated on GL 10 (Gustar Part 1)."""
    gate = get_next_gate(9, 520)
    assert gate is not None
    assert gate["grammar_level"] == 10
    assert gate["title"] == "Gustar Part 1"
    assert gate["has_content"] is True


def test_multiple_coming_soon_levels():
    """GL=10.6, VL=900 → gated on GL 11, not GL 16 or 17."""
    gate = get_next_gate(10.6, 900)
    assert gate is not None
    assert gate["grammar_level"] == 11
    assert gate["has_content"] is True  # GL 11 is now built out


def test_gated_on_preterite_after_coming_soon_cleared():
    """GL=16, VL=1000 → gated on GL 17 (Preterite Regular, has content)."""
    gate = get_next_gate(16, 1000)
    assert gate is not None
    assert gate["grammar_level"] == 17
    assert gate["title"] == "Preterite Regular"
    assert gate["has_content"] is True
    assert gate["situation_id"] == "grammar_preterite_regular_1"


def test_not_gated_between_thresholds():
    """GL=3, VL=199 → not gated (next GL 4 needs VL 200)."""
    assert get_next_gate(3, 199) is None


def test_gated_at_exact_boundary():
    """GL=3, VL=200 → gated on GL 4."""
    gate = get_next_gate(3, 200)
    assert gate is not None
    assert gate["grammar_level"] == 4


def test_gl_at_float_boundary():
    """GL=4 (not 4.5), VL=240 → gated on GL 4.5 (Irregular Present II)."""
    gate = get_next_gate(4, 240)
    assert gate is not None
    assert gate["grammar_level"] == 4.5
    assert gate["title"] == "Irregular Present II"


# ===========================================================================
# DATA INTEGRITY TESTS
# ===========================================================================

def test_gl_vl_thresholds_covers_all_gl_titles():
    """Every GL in GL_TITLES has a corresponding VL threshold."""
    for gl in GL_TITLES:
        assert gl in GL_VL_THRESHOLDS, f"GL {gl} missing from GL_VL_THRESHOLDS"


def test_gl_sorted_is_actually_sorted():
    """GL_SORTED is in ascending order."""
    for i in range(len(GL_SORTED) - 1):
        assert GL_SORTED[i] < GL_SORTED[i + 1], f"GL_SORTED not sorted at index {i}"


def test_all_grammar_situations_have_valid_gl():
    """Every GRAMMAR_SITUATIONS entry has a grammar_level in GL_VL_THRESHOLDS."""
    for sid, cfg in GRAMMAR_SITUATIONS.items():
        gl = cfg["grammar_level"]
        assert gl in GL_VL_THRESHOLDS, f"{sid} has grammar_level={gl} not in GL_VL_THRESHOLDS"


def test_vl_thresholds_are_monotonically_increasing():
    """VL thresholds increase as GL increases."""
    prev_vl = -1
    for gl in GL_SORTED:
        vl = GL_VL_THRESHOLDS[gl]
        assert vl > prev_vl, f"VL threshold not increasing: GL {gl} has VL {vl}, prev was {prev_vl}"
        prev_vl = vl


# ===========================================================================
# LANGUAGE MODE TESTS
# ===========================================================================

# After the alt-language refactor, get_language_mode() unconditionally returns
# "spanish_text" — the AI always speaks the target language, regardless of VL/GL.
# The "english → spanish_text" VL/GL threshold is no longer enforced here;
# difficulty gating is handled elsewhere. These tests document the new contract.

def test_language_target_when_low_vl():
    """VL=499, GL=10 → spanish_text (always target language now)."""
    assert get_language_mode(1, 499, 10) == "spanish_text"


def test_language_target_when_low_gl():
    """VL=500, GL=9 → spanish_text (always target language now)."""
    assert get_language_mode(1, 500, 9) == "spanish_text"


def test_language_spanish_when_both_met():
    """VL=500, GL=10 → spanish_text."""
    assert get_language_mode(1, 500, 10) == "spanish_text"


def test_language_spanish_with_high_stats():
    """VL=800, GL=15 → spanish_text."""
    assert get_language_mode(1, 800, 15) == "spanish_text"


def test_language_target_when_both_zero():
    """VL=0, GL=0 → spanish_text (always target language now)."""
    assert get_language_mode(1, 0, 0) == "spanish_text"


def test_language_default_without_grammar_level():
    """When grammar_level not passed (default 0), still spanish_text."""
    assert get_language_mode(1, 600) == "spanish_text"


# ===========================================================================
# ONBOARDING QUIZ → GL MAPPING TESTS
# ===========================================================================

def test_quiz_g1_assigns_gl_0(db):
    """Quiz score G1 → GL 0, no grammar auto-completed."""
    from app.api.v1.onboarding import QUIZ_SCORE_TO_GL, _auto_complete_grammar
    _ensure_grammar_situations_exist(db)
    user = _make_user(db)

    target_gl = QUIZ_SCORE_TO_GL["G1"]
    assert target_gl == 0

    completed = _auto_complete_grammar(db, user.id, target_gl)
    assert completed == 0
    assert get_grammar_level(db, user.id) == 0


def test_quiz_g101_assigns_gl_3(db):
    """Quiz score G101 → GL 3, Pronouns + Gender + Regular Present completed."""
    from app.api.v1.onboarding import QUIZ_SCORE_TO_GL, _auto_complete_grammar
    _ensure_grammar_situations_exist(db)
    user = _make_user(db)

    target_gl = QUIZ_SCORE_TO_GL["G101"]
    assert target_gl == 3

    completed = _auto_complete_grammar(db, user.id, target_gl)
    db.flush()  # autoflush=False in test sessions
    # GL 1 (1 sit) + GL 2 (1 sit) + GL 3 (3 lessons) = 5 situations
    assert completed == 5
    assert get_grammar_level(db, user.id) == 3


def test_quiz_g701_assigns_gl_9(db):
    """Quiz score G701 → GL 9, everything through Ir A+Inf completed."""
    from app.api.v1.onboarding import QUIZ_SCORE_TO_GL, _auto_complete_grammar
    _ensure_grammar_situations_exist(db)
    user = _make_user(db)

    target_gl = QUIZ_SCORE_TO_GL["G701"]
    assert target_gl == 9

    completed = _auto_complete_grammar(db, user.id, target_gl)
    db.flush()
    # Count all situations at GL <= 9
    expected = sum(1 for cfg in GRAMMAR_SITUATIONS.values() if cfg["grammar_level"] <= 9)
    assert completed == expected
    assert get_grammar_level(db, user.id) == 9


def test_quiz_g2001_assigns_gl_20(db):
    """Quiz score G2001 → GL 20, ALL existing grammar completed."""
    from app.api.v1.onboarding import QUIZ_SCORE_TO_GL, _auto_complete_grammar
    _ensure_grammar_situations_exist(db)
    user = _make_user(db)

    target_gl = QUIZ_SCORE_TO_GL["G2001"]
    assert target_gl == 20

    completed = _auto_complete_grammar(db, user.id, target_gl)
    db.flush()
    assert completed == len(GRAMMAR_SITUATIONS)  # All existing situations
    # GL should be max of all existing situations
    max_existing_gl = max(cfg["grammar_level"] for cfg in GRAMMAR_SITUATIONS.values())
    assert get_grammar_level(db, user.id) == max_existing_gl


def test_quiz_no_score_assigns_gl_0():
    """No grammar score → GL 0."""
    from app.api.v1.onboarding import QUIZ_SCORE_TO_GL
    assert QUIZ_SCORE_TO_GL.get(None, 0) == 0
    assert QUIZ_SCORE_TO_GL.get("", 0) == 0


def test_quiz_seeds_hf_words_from_max_score(db):
    """Onboarding seeds max(vocab_digits, grammar_digits) HF words."""
    from app.api.v1.onboarding import _parse_score_level
    assert _parse_score_level("V501") == 501
    assert _parse_score_level("G701") == 701
    assert max(_parse_score_level("V501"), _parse_score_level("G701")) == 701


# ===========================================================================
# INTEGRATION: FULL VL/GL GATING FLOW
# ===========================================================================

def test_full_gating_flow_beginner(db):
    """New user: VL=0, GL=0 → not gated. Learn words → VL=10 → gated on GL 1."""
    _ensure_grammar_situations_exist(db)
    user = _make_user(db)

    assert get_vocab_level(db, user.id) == 0
    assert get_grammar_level(db, user.id) == 0
    assert get_next_gate(0, 0) is None  # Not gated

    # User learns 10 HF words
    words = _make_hf_words(db, 10)
    _set_user_words(db, user, words, mastery_level=1)
    vl = get_vocab_level(db, user.id)
    assert vl == 10

    # Now gated
    gate = get_next_gate(0, vl)
    assert gate is not None
    assert gate["grammar_level"] == 1
    assert gate["title"] == "Pronouns"

    # Complete Pronouns
    _complete_grammar(db, user, 1)
    gl = get_grammar_level(db, user.id)
    assert gl == 1

    # No longer gated (next GL 2 needs VL 15, we only have 10)
    assert get_next_gate(gl, vl) is None


def test_full_gating_flow_advanced(db):
    """User at GL=10.6 hits coming-soon wall at VL=550."""
    _ensure_grammar_situations_exist(db)
    user = _make_user(db)

    _complete_grammar(db, user, 10.6)
    gl = get_grammar_level(db, user.id)
    assert gl == 10.6

    # At VL=520, not gated (next is GL 11 at VL 550)
    assert get_next_gate(gl, 520) is None

    # At VL=550, gated on GL 11 (Tengo que / Me toca / Necesito — now built out)
    gate = get_next_gate(gl, 550)
    assert gate is not None
    assert gate["grammar_level"] == 11
    assert gate["has_content"] is True
    assert gate["title"] == "Tengo que / Me toca / Necesito"
