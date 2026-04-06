#!/usr/bin/env python3
"""One-off migration: set GL=1 for all paid (active subscription) users.

- Auto-completes grammar_pronouns (GL 1) for every paid user
- Removes any grammar completion records above GL 1
- Safe to re-run (idempotent)

Run with:
    python scripts/migrate_gl1_paid_users.py

Or dry-run first:
    python scripts/migrate_gl1_paid_users.py --dry-run
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime, timezone
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import insert

from app.config import settings
from app.models import User, Subscription, UserSituation
from app.data.grammar_situations import GRAMMAR_SITUATIONS, get_all_grammar_situation_ids

engine = create_engine(settings.database_url, pool_pre_ping=True)
Session = sessionmaker(bind=engine)

PRONOUNS_SID = "grammar_pronouns"  # GL 1

# All grammar situation IDs with grammar_level > 1
GRAMMAR_ABOVE_GL1 = [
    sid for sid in get_all_grammar_situation_ids()
    if GRAMMAR_SITUATIONS[sid]["grammar_level"] > 1
]


def migrate(dry_run: bool = False):
    db = Session()
    try:
        # Find all paid users
        paid_users = (
            db.query(User)
            .join(Subscription, Subscription.user_id == User.id)
            .filter(Subscription.active == True)
            .all()
        )

        print(f"Found {len(paid_users)} paid users.")

        now = datetime.now(timezone.utc)
        completed_count = 0
        removed_count = 0

        for user in paid_users:
            # 1. Ensure grammar_pronouns (GL 1) is completed
            existing = db.query(UserSituation).filter(
                UserSituation.user_id == user.id,
                UserSituation.situation_id == PRONOUNS_SID,
            ).first()

            if existing and existing.completed_at:
                pass  # Already done
            elif existing:
                existing.completed_at = now
                completed_count += 1
            else:
                db.add(UserSituation(
                    user_id=user.id,
                    situation_id=PRONOUNS_SID,
                    started_at=now,
                    completed_at=now,
                ))
                completed_count += 1

            # 2. Remove completion records for grammar above GL 1
            for sid in GRAMMAR_ABOVE_GL1:
                us = db.query(UserSituation).filter(
                    UserSituation.user_id == user.id,
                    UserSituation.situation_id == sid,
                ).first()
                if us and us.completed_at:
                    db.delete(us)
                    removed_count += 1
                    gl = GRAMMAR_SITUATIONS[sid]["grammar_level"]
                    print(f"  Removing GL {gl} ({sid}) completion for {user.email}")

        print(f"\nSummary:")
        print(f"  Paid users: {len(paid_users)}")
        print(f"  Pronouns (GL 1) completions added: {completed_count}")
        print(f"  Grammar completions above GL 1 removed: {removed_count}")

        if dry_run:
            print("\n  DRY RUN — rolling back all changes.")
            db.rollback()
        else:
            db.commit()
            print("\n  COMMITTED successfully.")

    except Exception as e:
        db.rollback()
        print(f"Migration failed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("=== DRY RUN MODE ===\n")
    migrate(dry_run=dry_run)
