"""Emit clean candidate word pools for the FE vocab modules.

Reads the two BE corpora (`app/data/hf_words.py`, `app/data/seed_bank.py`),
runs every entry through `vocab_word_filter`, and writes a JSON file of
candidate pools keyed by vocab-module id. The FE generator
(`scripts/generate_vocab_data.mjs`) consumes it.

Why a separate step: the corpora are Python, the target is TypeScript. Keeping
the filtering here means the "no conjugated verbs / no proper names" rule has
exactly one implementation, and its audit numbers are printed where a human
will read them.

Usage:
    python scripts/build_vocab_pools.py            # writes scripts/vocab_pools.json
    python scripts/build_vocab_pools.py --report   # also dumps what was rejected
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))

from vocab_word_filter import REJECT_CONJUGATED, REJECT_PROPER_NAME, classify  # noqa: E402

OUT_PATH = os.path.join(os.path.dirname(__file__), "vocab_pools.json")
CURRENT_PATH = os.path.join(os.path.dirname(__file__), "vocab_current_words.json")
VERDICT_PATH = os.path.join(os.path.dirname(__file__), "vocab_verdicts.json")

# Vocab-module id prefix -> ENCOUNTER_WORDS category key.
SITUATION_CATEGORIES = {
    "airport": "airport",
    "banking": "banking",
    "clothing": "clothing",
    "contractor": "contractor",
    "groceries": "groceries",
    "mechanic": "mechanic",
    "police": "police",
    "restaurant": "restaurant",
    "small-talk": "small_talk",
    "internet": "internet",
}

# Frequency-band modules. The id is frozen forever (it is the `module_id` FK in
# vocab_card / vocab_chapter_completion), so we key the pool off the id and
# source from the rank neighbourhood rather than the literal 15-rank window —
# after filtering, a 15-rank window rarely yields 15 teachable words.
FREQ_MODULE_START = {
    "freq-500-514": 500, "freq-600-614": 600, "freq-700-714": 700,
    "freq-800-814": 800, "freq-900-914": 900, "freq-1000-1014": 1000,
    "freq-1100-1114": 1100, "freq-1200-1214": 1200, "freq-1300-1314": 1300,
    "freq-1400-1414": 1400, "freq-1500-1514": 1500, "freq-1600-1614": 1600,
    "freq-1700-1714": 1700, "freq-1800-1814": 1800, "freq-1900-1914": 1900,
}

# How many candidates to offer per module. The generator dedupes against words
# already present across every module, so the pool must overshoot the 30-word
# target comfortably.
POOL_DEPTH = 90


def load_hf() -> list[dict]:
    from app.data.hf_words import HIGH_FREQUENCY_WORDS

    return HIGH_FREQUENCY_WORDS


def load_encounters() -> dict[str, list[dict]]:
    from app.data.seed_bank import ENCOUNTER_WORDS

    return ENCOUNTER_WORDS


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true", help="print rejected samples")
    args = ap.parse_args()

    hf = load_hf()
    encounters = load_encounters()

    rejected: Counter[str] = Counter()
    rejected_samples: dict[str, list[str]] = {}

    def keep(spanish: str, english: str, *, allow_multiword: bool = False) -> bool:
        pos, reason = classify(spanish, english, allow_multiword=allow_multiword)
        if pos is None:
            rejected[reason] += 1
            rejected_samples.setdefault(reason, [])
            if len(rejected_samples[reason]) < 12:
                rejected_samples[reason].append(f"{spanish} ({english})")
            return False
        return True

    pools: dict[str, list[dict]] = {}

    # --- frequency bands -------------------------------------------------
    hf_sorted = sorted(
        (w for w in hf if w.get("frequency_rank")), key=lambda w: w["frequency_rank"]
    )
    for module_id, start in FREQ_MODULE_START.items():
        pool = []
        for w in hf_sorted:
            if w["frequency_rank"] < start:
                continue
            if not keep(w["spanish"], w["english"]):
                continue
            pool.append({"es": w["spanish"], "en": w["english"]})
            if len(pool) >= POOL_DEPTH:
                break
        pools[module_id] = pool

    # --- situation decks -------------------------------------------------
    # Encounter words are hand-curated per category, so they pass the filter at
    # a far higher rate than the subtitle-sourced HF tail. Both `<cat>-1-15` and
    # `<cat>-16-30` draw from one shared, ordered pool; the generator hands out
    # non-overlapping slices.
    for prefix, category in SITUATION_CATEGORIES.items():
        words = encounters.get(category, [])
        pool = [
            {"es": w["spanish"], "en": w["english"]}
            for w in words
            if keep(w["spanish"], w["english"], allow_multiword=True)
        ]
        pools[f"{prefix}-shared"] = pool

    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        json.dump(pools, fh, ensure_ascii=False, indent=1)

    # --- vet the words already shipping ----------------------------------
    # The FE generator dumps its current inventory here first. Running it through
    # the same filter is what lets the generator purge pre-existing junk
    # ("steve", "os") instead of preserving it forever under append-only.
    if os.path.exists(CURRENT_PATH):
        with open(CURRENT_PATH, encoding="utf-8") as fh:
            current = json.load(fh)
        verdicts = []
        for entry in current:
            pos, reason = classify(entry["es"], entry["en"], allow_multiword=True)
            band = entry["bandId"]
            is_single = " " not in entry["es"].strip()

            # What counts as "unteachable" depends on what the deck promises.
            #
            #   phrases     — teaches whole utterances; a finite verb IS the
            #                 lesson ("quiero dormir"). Never purged.
            #   frequency   — promises single-word citation forms at a rank.
            #                 Strictest: anything the filter rejects goes.
            #   foundation  — closed-class decks. "de", "muy", "y" are the
            #                 syllabus, not noise. Only real intruders go:
            #                 proper names and conjugated verbs.
            #   situations  — teaches conversational chunks from the encounter
            #                 dialogues ("no arranca", "más grande"). Keep the
            #                 chunks; drop single-word conjugations and names.
            if band == "phrases":
                ok = True
            elif band == "frequency":
                ok = pos is not None
            elif reason == REJECT_PROPER_NAME:
                # A tech token glossed as itself (PIN, wifi, SSID) trips the
                # name heuristic but is a legitimate thing to teach. Real
                # subtitle names always carry an explicit "(name)" gloss.
                ok = "(name)" not in entry["en"].lower()
            elif reason == REJECT_CONJUGATED:
                ok = not is_single
            else:
                ok = True

            verdicts.append({**entry, "ok": ok, "reason": reason})
        with open(VERDICT_PATH, "w", encoding="utf-8") as fh:
            json.dump(verdicts, fh, ensure_ascii=False, indent=1)
        bad = [v for v in verdicts if not v["ok"]]
        print(f"  vetted {len(current)} shipping words -> {len(bad)} unteachable")
        by_reason = Counter(v["reason"] for v in bad)
        for reason, count in by_reason.most_common():
            print(f"    {reason:16s} {count}")

    total = sum(len(v) for v in pools.values())
    print(f"wrote {OUT_PATH}")
    print(f"  pools: {len(pools)}  candidates: {total}")
    print("  rejected during pool build:")
    for reason, count in rejected.most_common():
        print(f"    {reason:16s} {count}")
    thin = [k for k, v in pools.items() if len(v) < 30]
    if thin:
        print(f"  !! pools with <30 candidates: {thin}")
    if args.report:
        print("\n  rejected samples:")
        for reason, samples in rejected_samples.items():
            print(f"    {reason}: {', '.join(samples)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
