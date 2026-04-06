#!/usr/bin/env python3
"""Production migration: replace 16 old grammar situations with 42 new multi-lesson ones.

What this does:
1. Clears all grammar user_situations (old IDs won't exist after migration)
2. Sets GL=2 (pronouns + gender) for all paid subscribers
3. Replaces old grammar situations + words with new ones from grammar_situations.py
4. Preserves all non-grammar data (main situations, user_words, etc.)

Usage:
    python scripts/migrate_grammar_prod.py --dry-run   # preview only
    python scripts/migrate_grammar_prod.py              # execute

Requires DATABASE_URL env var pointing to production.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, text
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import sessionmaker

from app.config import settings
from app.data.grammar_situations import (
    GRAMMAR_SITUATIONS, GRAMMAR_WORD_TRANSLATIONS, GL_VL_THRESHOLDS,
)

DRY_RUN = "--dry-run" in sys.argv


def main():
    engine = create_engine(settings.database_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    with Session() as db:
        try:
            # ── Step 1: Show current state ──
            old_grammar = db.execute(text(
                "SELECT id FROM situations WHERE situation_type = 'grammar' ORDER BY id"
            )).fetchall()
            print(f"Current grammar situations: {len(old_grammar)}")
            for r in old_grammar:
                print(f"  {r[0]}")

            # ── Step 2: Find all users with grammar completions ──
            users_with_grammar = db.execute(text("""
                SELECT DISTINCT u.email, u.id FROM users u
                JOIN user_situations us ON u.id = us.user_id
                JOIN situations s ON us.situation_id = s.id
                WHERE s.situation_type = 'grammar' AND us.completed_at IS NOT NULL
            """)).fetchall()
            print(f"\nUsers with grammar completions: {len(users_with_grammar)}")
            for email, uid in users_with_grammar:
                count = db.execute(text("""
                    SELECT COUNT(*) FROM user_situations us
                    JOIN situations s ON us.situation_id = s.id
                    WHERE us.user_id = :uid AND s.situation_type = 'grammar' AND us.completed_at IS NOT NULL
                """), {"uid": uid}).scalar()
                print(f"  {email}: {count} grammar completions")

            # ── Step 3: Find paid subscribers ──
            paid_users = db.execute(text("""
                SELECT u.id, u.email FROM users u
                JOIN subscriptions s ON u.id = s.user_id
                WHERE s.active = true
            """)).fetchall()
            print(f"\nPaid subscribers: {len(paid_users)}")
            for uid, email in paid_users:
                print(f"  {email}")

            if DRY_RUN:
                print("\n=== DRY RUN — no changes made ===")
                return

            # ── Step 4: Clear all grammar user_situations ──
            deleted_us = db.execute(text("""
                DELETE FROM user_situations WHERE situation_id IN (
                    SELECT id FROM situations WHERE situation_type = 'grammar'
                )
            """)).rowcount
            print(f"\nDeleted {deleted_us} grammar user_situations")

            # ── Step 5: Clear grammar FK references ──
            db.execute(text("DELETE FROM daily_encounter_logs WHERE situation_id IN (SELECT id FROM situations WHERE situation_type = 'grammar')"))
            db.execute(text("DELETE FROM conversations WHERE situation_id IN (SELECT id FROM situations WHERE situation_type = 'grammar')"))
            db.execute(text("UPDATE user_words SET source_situation_id = NULL WHERE source_situation_id IN (SELECT id FROM situations WHERE situation_type = 'grammar')"))

            # ── Step 6: Delete old grammar situations + words ──
            db.execute(text("DELETE FROM situation_words WHERE situation_id LIKE 'grammar_%'"))
            db.execute(text("DELETE FROM situation_words WHERE word_id LIKE 'grammar_%'"))
            db.execute(text("DELETE FROM situations WHERE situation_type = 'grammar'"))
            db.execute(text("DELETE FROM user_words WHERE word_id LIKE 'grammar_%'"))
            db.execute(text("DELETE FROM words WHERE word_category = 'grammar'"))
            print("Deleted old grammar situations + words")

            # ── Step 7: Insert new grammar words ──
            grammar_word_set = set()
            for sid, cfg in GRAMMAR_SITUATIONS.items():
                for word in cfg["word_workload"]:
                    if word not in grammar_word_set:
                        grammar_word_set.add(word)
                        word_id = f"grammar_{word}"
                        english = GRAMMAR_WORD_TRANSLATIONS.get(word, word)
                        stmt = insert(
                            __import__('app.models', fromlist=['Word']).Word
                        ).values(
                            id=word_id, spanish=word, english=english,
                            word_category="grammar"
                        ).on_conflict_do_update(
                            index_elements=["id"],
                            set_={"english": english, "spanish": word},
                        )
                        db.execute(stmt)
            print(f"Inserted {len(grammar_word_set)} grammar words")

            # ── Step 8: Insert new grammar situations ──
            from app.models import Situation, SituationWord
            order_offset = 1000
            for sid, cfg in GRAMMAR_SITUATIONS.items():
                gl = cfg["grammar_level"]
                vl_threshold = GL_VL_THRESHOLDS.get(gl, 0)
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
                ).on_conflict_do_update(
                    index_elements=["id"],
                    set_={
                        "title": cfg["title"],
                        "encounter_number": order_key,
                        "order_index": order_offset + order_key,
                        "vocab_level_required": vl_threshold,
                        "video_embed_id": cfg["video_embed_id"],
                    },
                )
                db.execute(stmt)

                for pos, word in enumerate(cfg["word_workload"], 1):
                    word_id = f"grammar_{word}"
                    stmt = insert(SituationWord).values(
                        situation_id=sid, word_id=word_id, position=pos
                    ).on_conflict_do_nothing()
                    db.execute(stmt)

            print(f"Inserted {len(GRAMMAR_SITUATIONS)} grammar situations")

            # ── Step 9: Set GL=2 for all paid subscribers ──
            gl2_situations = ["grammar_pronouns", "grammar_gender"]
            from app.models import UserSituation
            for uid, email in paid_users:
                for sid in gl2_situations:
                    stmt = insert(UserSituation).values(
                        user_id=uid, situation_id=sid,
                        completed_at=text("NOW()")
                    ).on_conflict_do_update(
                        index_elements=["user_id", "situation_id"],
                        set_={"completed_at": text("NOW()")},
                    )
                    db.execute(stmt)
                print(f"  {email}: GL=2 set")

            # ── Step 10: Verify ──
            new_count = db.execute(text(
                "SELECT COUNT(*) FROM situations WHERE situation_type = 'grammar'"
            )).scalar()
            print(f"\nVerification: {new_count} grammar situations in DB")

            db.commit()
            print("\n=== Migration complete ===")

        except Exception as e:
            db.rollback()
            print(f"\n=== MIGRATION FAILED — rolled back ===")
            print(f"Error: {e}")
            raise


if __name__ == "__main__":
    main()
