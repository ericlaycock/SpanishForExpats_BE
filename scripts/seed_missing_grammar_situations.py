#!/usr/bin/env python3
"""Idempotently seed any GRAMMAR_SITUATIONS keys that are missing from the
`situations` table (and the matching grammar `words` + `situation_words`
rows). Non-destructive — never touches existing rows or any non-grammar data.

Why this exists: `_auto_complete_grammar` in onboarding.py loops the static
GRAMMAR_SITUATIONS dict and inserts user_situations referencing each id. If
prod was deployed without a corresponding situations-table seed (e.g. a new
grammar lesson was added in code but the seed step was forgotten), every
new signup hits a ForeignKeyViolation mid-onboarding. This script closes
that gap without the destructive replace that migrate_grammar_prod.py does.

Usage:
    DATABASE_URL=... python scripts/seed_missing_grammar_situations.py --dry-run
    DATABASE_URL=... python scripts/seed_missing_grammar_situations.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import sessionmaker

from app.config import settings
from app.data.grammar_situations import (
    GRAMMAR_SITUATIONS,
    GRAMMAR_WORD_TRANSLATIONS,
    GL_VL_THRESHOLDS,
)
from app.models import Situation, SituationWord, Word


def _grammar_verbs() -> set[str]:
    """Verbs are exactly the top-level keys of any lesson's drill_config.answers."""
    verbs: set[str] = set()
    for cfg in GRAMMAR_SITUATIONS.values():
        answers = (cfg.get("drill_config") or {}).get("answers") or {}
        verbs.update(answers.keys())
    return verbs

DRY_RUN = "--dry-run" in sys.argv
ORDER_OFFSET = 1000  # mirrors migrate_grammar_prod.py


def main() -> int:
    engine = create_engine(settings.database_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    with Session() as db:
        existing_ids = {sid for (sid,) in db.query(Situation.id).filter(
            Situation.id.in_(list(GRAMMAR_SITUATIONS.keys()))
        ).all()}
        missing_ids = [sid for sid in GRAMMAR_SITUATIONS.keys() if sid not in existing_ids]

        print(f"GRAMMAR_SITUATIONS keys: {len(GRAMMAR_SITUATIONS)}")
        print(f"Already seeded: {len(existing_ids)}")
        print(f"Missing from DB: {len(missing_ids)}")
        for sid in missing_ids:
            cfg = GRAMMAR_SITUATIONS[sid]
            print(f"  {sid:50s}  GL={cfg['grammar_level']}  '{cfg['title']}'")

        if not missing_ids:
            print("\nNothing to seed.")
            return 0

        if DRY_RUN:
            print("\n=== DRY RUN — no changes made ===")
            return 0

        # Insert grammar Word rows for any words referenced by missing
        # situations that aren't already in the words table. on_conflict_do_nothing
        # leaves any pre-existing translations alone. word_type='verb' is
        # set only for actual verbs (top-level keys of drill_config.answers
        # across lessons) so the grenade + last_seen_form paths can detect
        # them; pronouns / adjectives in word_workload stay NULL.
        verb_set = _grammar_verbs()
        words_inserted = 0
        seen_words: set[str] = set()
        for sid in missing_ids:
            for word in GRAMMAR_SITUATIONS[sid]["word_workload"]:
                if word in seen_words:
                    continue
                seen_words.add(word)
                word_id = f"grammar_{word}"
                english = GRAMMAR_WORD_TRANSLATIONS.get(word, word)
                values = {
                    "id": word_id,
                    "spanish": word,
                    "english": english,
                    "word_category": "grammar",
                }
                if word in verb_set:
                    values["word_type"] = "verb"
                stmt = insert(Word).values(**values).on_conflict_do_nothing(index_elements=["id"])
                result = db.execute(stmt)
                if result.rowcount:
                    words_inserted += 1
        print(f"\nInserted {words_inserted} new grammar word rows")

        # Insert the missing situations + their situation_words mapping.
        for sid in missing_ids:
            cfg = GRAMMAR_SITUATIONS[sid]
            gl = cfg["grammar_level"]
            order_key = int(gl * 100)
            stmt = insert(Situation).values(
                id=sid,
                title=cfg["title"],
                animation_type="grammar",
                encounter_number=order_key,
                order_index=ORDER_OFFSET + order_key,
                is_free=True,
                situation_type="grammar",
                vocab_level_required=GL_VL_THRESHOLDS.get(gl, 0),
                video_embed_id=cfg["video_embed_id"],
            ).on_conflict_do_nothing(index_elements=["id"])
            db.execute(stmt)

            for pos, word in enumerate(cfg["word_workload"], 1):
                word_id = f"grammar_{word}"
                stmt = insert(SituationWord).values(
                    situation_id=sid, word_id=word_id, position=pos
                ).on_conflict_do_nothing()
                db.execute(stmt)

        db.commit()
        print(f"Inserted {len(missing_ids)} grammar situation rows")
        print("\n=== Seed complete ===")
        return 0


if __name__ == "__main__":
    sys.exit(main())
