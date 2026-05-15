"""One-shot: clear DailyEncounterLog rows from today (UTC) for a specific user.

Used to unblock dragonfyre09@gmail.com on 2026-05-14, who was trapped behind a
DAILY_LIMIT_REACHED 429 because the old /situations/{id}/start endpoint
recorded a daily encounter on every learn-page mount (fixed in the same PR).

Usage:
    python scripts/clear_daily_encounters_for_user.py <user_id>
or:
    python scripts/clear_daily_encounters_for_user.py --email <email>

Dry-run is the default; pass --apply to actually delete.
"""
import sys
import argparse
from datetime import datetime, timezone, time

from app.database import SessionLocal
from app.models import DailyEncounterLog, User


def main() -> int:
    parser = argparse.ArgumentParser()
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--user-id", help="Target user UUID")
    g.add_argument("--email", help="Target user email")
    parser.add_argument("--apply", action="store_true", help="Actually delete (default: dry-run)")
    args = parser.parse_args()

    db = SessionLocal()
    try:
        if args.email:
            user = db.query(User).filter(User.email == args.email).first()
            if not user:
                print(f"No user with email {args.email}")
                return 1
            user_id = user.id
        else:
            user_id = args.user_id

        today_start = datetime.combine(
            datetime.now(timezone.utc).date(), time.min, tzinfo=timezone.utc
        )
        q = db.query(DailyEncounterLog).filter(
            DailyEncounterLog.user_id == user_id,
            DailyEncounterLog.created_at >= today_start,
        )
        rows = q.all()
        print(f"Found {len(rows)} DailyEncounterLog rows from today for user {user_id}:")
        for r in rows:
            print(f"  {r.created_at}  situation={r.situation_id}")

        if not args.apply:
            print("\nDry-run. Re-run with --apply to delete.")
            return 0

        q.delete(synchronize_session=False)
        db.commit()
        print(f"\nDeleted {len(rows)} rows.")
        return 0
    finally:
        db.close()


if __name__ == "__main__":
    sys.exit(main())
