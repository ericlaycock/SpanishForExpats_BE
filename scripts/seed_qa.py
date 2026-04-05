#!/usr/bin/env python3
"""Seed QA database with minimal realistic data.

Run with: python scripts/seed_qa.py
Uses DATABASE_URL from environment (same as the app).
Idempotent: uses ON CONFLICT DO UPDATE for encounter/situation data.

All word/situation data comes from app/data/seed_bank.py and
app/data/grammar_situations.py — never hardcoded here.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import insert
from app.config import settings
from app.models import Base, User, Subscription, Word, Situation, SituationWord, UserWord, UserSituation
from app.auth import get_password_hash
from datetime import datetime, timezone
from app.data.seed_bank import (
    HIGH_FREQUENCY_WORDS,
    ENCOUNTER_WORDS,
    SITUATIONS,
    SITUATION_WORDS,
)
from app.data.grammar_situations import GRAMMAR_SITUATIONS, GRAMMAR_WORD_TRANSLATIONS, GL_VL_THRESHOLDS

engine = create_engine(settings.database_url, pool_pre_ping=True)
Session = sessionmaker(bind=engine)


def _seed_vl_gl_test_users(db, password_hash):
    """Create test users at specific VL/GL combinations for QA verification.

    Each user gets HF words seeded to target VL and grammar situations
    auto-completed to target GL.
    """
    from app.data.grammar_situations import get_all_grammar_situation_ids, GRAMMAR_SITUATIONS

    test_users = [
        # (email, uuid_suffix, target_vl, target_gl, description)
        ("beginner@test.com",          "10", 0,    0,    "Not gated, fresh start"),
        ("vl10-gl0@test.com",          "11", 10,   0,    "Gated on GL 1 (Pronouns)"),
        ("vl100-gl2@test.com",         "12", 100,  2,    "Gated on GL 3 (Regular Present)"),
        ("balanced@test.com",          "13", 300,  6,    "Not gated (next GL 7 needs VL 330)"),
        ("overmatched@test.com",       "14", 550,  10.6, "Gated on GL 11 (Coming Soon)"),
        ("grammar-ahead@test.com",     "15", 400,  9,    "Not gated (next GL 10 needs VL 510)"),
        ("stuck-coming-soon@test.com", "16", 1000, 10.6, "Gated on GL 11 (Coming Soon) despite high VL"),
        ("advanced@test.com",          "17", 1000, 20,   "Never gated — GL 20 is max"),
    ]

    now = datetime.now(timezone.utc)

    # Get all HF words sorted by frequency_rank for VL seeding
    hf_words = (
        db.query(Word)
        .filter(Word.word_category == "high_frequency")
        .order_by(Word.frequency_rank.asc())
        .all()
    )

    # Get grammar situation IDs sorted by grammar_level
    grammar_sids = get_all_grammar_situation_ids()

    for email, uuid_suffix, target_vl, target_gl, description in test_users:
        user_id = f"00000000-0000-0000-0000-0000000000{uuid_suffix}"
        stmt = insert(User).values(
            id=user_id,
            email=email,
            password_hash=password_hash,
            onboarding_completed=True,
            selected_animation_types=["banking"],
            dialect="mexico",
        ).on_conflict_do_nothing()
        db.execute(stmt)

        stmt = insert(Subscription).values(
            user_id=user_id, active=True,
        ).on_conflict_do_nothing()
        db.execute(stmt)

        # Seed HF words to achieve target VL (mastery_level=1 counts toward VL now)
        for w in hf_words[:target_vl]:
            stmt = insert(UserWord).values(
                user_id=user_id,
                word_id=w.id,
                seen_count=1,
                typed_correct_count=1,
                spoken_correct_count=1,
                mastery_level=1,
                status="learning",
            ).on_conflict_do_nothing(index_elements=["user_id", "word_id"])
            db.execute(stmt)

        # Auto-complete grammar situations up to target GL
        for sid in grammar_sids:
            cfg = GRAMMAR_SITUATIONS[sid]
            if cfg["grammar_level"] > target_gl:
                continue
            stmt = insert(UserSituation).values(
                user_id=user_id,
                situation_id=sid,
                started_at=now,
                completed_at=now,
            ).on_conflict_do_nothing(index_elements=["user_id", "situation_id"])
            db.execute(stmt)

        print(f"  Seeded {email}: VL={target_vl}, GL={target_gl} — {description}")


def seed():
    db = Session()
    try:
        # --- Encounter words (upsert to fix stale data) ---
        for category_words in ENCOUNTER_WORDS.values():
            for w in category_words:
                stmt = insert(Word).values(
                    id=w["id"], spanish=w["spanish"], english=w["english"],
                    word_category="encounter", catalan=w["catalan"]
                ).on_conflict_do_update(
                    index_elements=["id"],
                    set_={"spanish": w["spanish"], "english": w["english"], "catalan": w["catalan"]},
                )
                db.execute(stmt)

        # --- High-frequency words ---
        for w in HIGH_FREQUENCY_WORDS:
            stmt = insert(Word).values(
                id=w["id"], spanish=w["spanish"], english=w["english"],
                word_category="high_frequency", frequency_rank=w["frequency_rank"],
                catalan=w["catalan"]
            ).on_conflict_do_update(
                index_elements=["id"],
                set_={"spanish": w["spanish"], "english": w["english"], "catalan": w["catalan"]},
            )
            db.execute(stmt)

        # --- Delete orphaned situations from old seed formats ---
        current_situation_ids = {s["id"] for s in SITUATIONS}
        current_situation_ids.update(GRAMMAR_SITUATIONS.keys())
        placeholders = ", ".join(f":id_{i}" for i in range(len(current_situation_ids)))
        params = {f"id_{i}": sid for i, sid in enumerate(current_situation_ids)}
        db.execute(text(f"DELETE FROM situation_words WHERE situation_id NOT IN ({placeholders})"), params)
        db.execute(text(f"DELETE FROM conversations WHERE situation_id NOT IN ({placeholders})"), params)
        db.execute(text(f"DELETE FROM user_situations WHERE situation_id NOT IN ({placeholders})"), params)
        db.execute(text(f"DELETE FROM situations WHERE id NOT IN ({placeholders})"), params)

        # --- Situations (upsert to fix stale data) ---
        for s in SITUATIONS:
            stmt = insert(Situation).values(**s).on_conflict_do_update(
                index_elements=["id"],
                set_={k: v for k, v in s.items() if k != "id"},
            )
            db.execute(stmt)

        # --- SituationWords (upsert to fix stale data) ---
        for link in SITUATION_WORDS:
            stmt = insert(SituationWord).values(**link).on_conflict_do_update(
                index_elements=["situation_id", "word_id"],
                set_={"position": link["position"]},
            )
            db.execute(stmt)

        # --- Grammar situations + words ---
        # Clean slate for grammar: delete referencing rows first (FK order), then words
        # This ensures orphan records from old seeds with different accent handling are removed
        db.execute(text("DELETE FROM user_words WHERE word_id LIKE 'grammar_%'"))
        db.execute(text("DELETE FROM situation_words WHERE situation_id LIKE 'grammar_%'"))
        db.execute(text("DELETE FROM situation_words WHERE word_id LIKE 'grammar_%'"))
        db.execute(text("DELETE FROM words WHERE word_category = 'grammar'"))

        grammar_word_set = set()
        for sid, cfg in GRAMMAR_SITUATIONS.items():
            for word in cfg["word_workload"]:
                if word not in grammar_word_set:
                    grammar_word_set.add(word)
                    word_id = f"grammar_{word}"
                    english = GRAMMAR_WORD_TRANSLATIONS.get(word, word)
                    stmt = insert(Word).values(
                        id=word_id, spanish=word, english=english,
                        word_category="grammar"
                    ).on_conflict_do_update(
                        index_elements=["id"],
                        set_={"english": english, "spanish": word},
                    )
                    db.execute(stmt)

        order_offset = 1000
        for sid, cfg in GRAMMAR_SITUATIONS.items():
            gl = cfg["grammar_level"]
            vl_threshold = GL_VL_THRESHOLDS.get(gl, 0)
            # Use grammar_level * 100 for ordering to handle floats (1, 2, 4.5, 10.3 etc.)
            order_key = int(gl * 100)
            stmt = insert(Situation).values(
                id=sid,
                title=cfg["title"],
                animation_type="grammar",
                encounter_number=order_key,
                order_index=order_offset + order_key,
                is_free=True,
                situation_type="grammar",
                vocab_level_required=vl_threshold,
                video_embed_id=cfg["video_embed_id"],
            ).on_conflict_do_nothing()
            db.execute(stmt)

            for pos, word in enumerate(cfg["word_workload"], 1):
                word_id = f"grammar_{word}"
                stmt = insert(SituationWord).values(
                    situation_id=sid, word_id=word_id, position=pos
                ).on_conflict_do_nothing()
                db.execute(stmt)

        # --- Test user ---
        password_hash = get_password_hash("testpassword123")
        test_user_id = "00000000-0000-0000-0000-000000000001"
        stmt = insert(User).values(
            id=test_user_id,
            email="qa@test.com",
            password_hash=password_hash,
            onboarding_completed=True,
            selected_animation_types=["banking"],
            dialect="mexico",
        ).on_conflict_do_nothing()
        db.execute(stmt)

        stmt = insert(Subscription).values(
            user_id=test_user_id, active=False
        ).on_conflict_do_nothing()
        db.execute(stmt)

        # --- QA admin account ---
        qa_admin_hash = get_password_hash("qaqaqa")
        qa_admin_id = "00000000-0000-0000-0000-000000000002"
        stmt = insert(User).values(
            id=qa_admin_id,
            email="qa@a.com",
            password_hash=qa_admin_hash,
            onboarding_completed=True,
            selected_animation_types=["banking"],
            dialect="mexico",
            is_admin=True,
        ).on_conflict_do_nothing()
        db.execute(stmt)

        stmt = insert(Subscription).values(
            user_id=qa_admin_id, active=True
        ).on_conflict_do_nothing()
        db.execute(stmt)

        # --- Set admin flag for admin users ---
        for admin_email in ('ericlaycock44@gmail.com', 'qa@a.com', 'eric@spanishforexpats.com'):
            db.execute(text(
                "UPDATE users SET is_admin = true WHERE email = :email"
            ), {"email": admin_email})

        # --- QA test users at specific VL/GL combinations ---
        _seed_vl_gl_test_users(db, password_hash)

        db.commit()
        print("QA seed data inserted successfully.")
    except Exception as e:
        db.rollback()
        print(f"Seed failed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
