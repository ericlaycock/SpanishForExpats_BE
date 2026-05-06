#!/usr/bin/env python3
"""Backfill `word_type='verb'` on grammar Word rows that represent verbs.

Why: grammar Word rows were inserted with `word_category='grammar'` but no
`word_type`. Several downstream paths gate verb-only behaviour on
`word.word_type == 'verb'` — the daily Grenade's target-form resolution
(`_resolve_target_form` + `find_any_grammar_form`), the per-lesson
`set_initial_mastery` form pick, and the grenade-pool verb preference.
With word_type NULL, all of those silently fall through to the lemma —
so a learner who just drilled `escribir → escribo, escribes…` sees
`escribir` as their grenade word.

Idempotent. Reads the canonical verb list from every grammar lesson's
`drill_config.answers` keys, then `UPDATE words SET word_type='verb'
WHERE id = 'grammar_<verb>' AND word_type IS NULL`. Pronouns/adjectives
in grammar word_category stay NULL (those rows aren't in any
drill_config as a top-level key — the conjugation tables are keyed on
the verb).

Usage:
    DATABASE_URL=... python scripts/backfill_grammar_word_type.py --dry-run
    DATABASE_URL=... python scripts/backfill_grammar_word_type.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.config import settings
from app.data.grammar_situations import GRAMMAR_SITUATIONS

DRY_RUN = "--dry-run" in sys.argv


def main() -> int:
    grammar_verbs: set[str] = set()
    for cfg in GRAMMAR_SITUATIONS.values():
        answers = (cfg.get("drill_config") or {}).get("answers") or {}
        for verb in answers.keys():
            grammar_verbs.add(verb)
    grammar_verb_ids = [f"grammar_{v}" for v in sorted(grammar_verbs)]
    print(f"Grammar verbs (from drill_config): {len(grammar_verb_ids)}")

    engine = create_engine(settings.database_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    with Session() as db:
        existing = db.execute(text(
            "SELECT id, word_type FROM words WHERE id = ANY(:ids)"
        ), {"ids": grammar_verb_ids}).all()
        present = {r[0]: r[1] for r in existing}
        missing_rows = [vid for vid in grammar_verb_ids if vid not in present]
        already_set = [vid for vid in grammar_verb_ids if present.get(vid) == "verb"]
        to_update = [vid for vid in grammar_verb_ids if vid in present and present[vid] != "verb"]

        print(f"Already word_type='verb': {len(already_set)}")
        print(f"Need update (NULL or other): {len(to_update)}")
        print(f"Missing entirely from words table: {len(missing_rows)}")
        if missing_rows[:5]:
            print(f"  e.g. {missing_rows[:5]}")

        if not to_update:
            print("\nNothing to update.")
            return 0

        if DRY_RUN:
            print("\n=== DRY RUN — no changes made ===")
            print(f"Would UPDATE words SET word_type='verb' for {len(to_update)} rows.")
            return 0

        result = db.execute(text(
            "UPDATE words SET word_type='verb' WHERE id = ANY(:ids) AND (word_type IS NULL OR word_type <> 'verb')"
        ), {"ids": to_update})
        db.commit()
        print(f"Updated {result.rowcount} rows.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
