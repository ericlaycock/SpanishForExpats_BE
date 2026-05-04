#!/usr/bin/env python3
"""Generate inline word glosses for every grammar drill sentence missing them.

Walks GRAMMAR_SITUATIONS, collects each `drill_sentence` that has no `glosses`,
asks the LLM to produce a bidirectional EN↔ES gloss map matching the schema
already used by `grammar_pronouns`, validates the response, and writes the
result to `app/data/grammar_drill_glosses.py` as a sidecar dict
`DRILL_GLOSSES[situation_id] = [glosses_per_sentence_in_order]`.

Run: `cd SpanishForExpats_BE && python3 scripts/generate_drill_glosses.py`
"""
import os
import sys
import json
import time
import textwrap
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import OpenAI
from app.config import settings
from app.data.grammar_situations import GRAMMAR_SITUATIONS

MODEL = "gpt-4.1-mini"
SIDECAR_PATH = Path(__file__).parent.parent / "app" / "data" / "grammar_drill_glosses.py"
PROGRESS_PATH = Path(__file__).parent / "_drill_glosses_progress.json"

SYSTEM_PROMPT = textwrap.dedent("""
    You generate inline NOUN-ONLY translation glosses for short bilingual
    sentence pairs used in a Spanish grammar drill app. The glosses help
    learners look up unfamiliar nouns without revealing the verb/grammar
    answer the drill is testing.

    For each pair you receive an English sentence (`en`) and a Spanish
    sentence (`es`). Return a single JSON object whose keys/values give a
    *bidirectional*, *lowercase* mapping ONLY for the NOUNS in the
    sentence.

    Rules:
    - Output JSON only, no prose.
    - All keys and values lowercase.
    - Include ONLY nouns (concrete things, people, places, abstract
      objects). Examples to include: house, book, friend, coffee, dog,
      teacher, problem, trip, animal, party, store, school, doctor.
    - DO NOT include: verbs (in any form), adjectives, adverbs, pronouns,
      articles, possessive adjectives (my, your, his), prepositions,
      conjunctions, interjections.
    - The mapping MUST be symmetric: if "casa" -> "house" appears, then
      "house" -> "casa" must also appear.
    - Use the exact spelling as it appears in the sentence (with
      accents), lowercased. Strip surrounding punctuation.
    - If a sentence has NO nouns at all, return {"glosses": {}}.

    Schema:
    {
      "glosses": { "<lowercase noun>": "<lowercase translation>", ... }
    }

    Examples:

    Input:  {"en": "my house", "es": "mi casa"}
    Output: {"glosses": {"house": "casa", "casa": "house"}}

    Input:  {"en": "I speak Spanish", "es": "Yo hablo español"}
    Output: {"glosses": {"spanish": "español", "español": "spanish"}}
    (Spanish here is a language noun.)

    Input:  {"en": "She is tall", "es": "Ella es alta"}
    Output: {"glosses": {}}
    (No nouns — "tall" / "alta" is an adjective.)

    Input:  {"en": "We give the book to the teacher", "es": "Le damos el libro al maestro"}
    Output: {"glosses": {"book": "libro", "teacher": "maestro",
                         "libro": "book", "maestro": "teacher"}}
    (Verb "give"/"damos" excluded.)

    Input:  {"en": "I am going to the store", "es": "Voy a la tienda"}
    Output: {"glosses": {"store": "tienda", "tienda": "store"}}
""").strip()


def collect_pending() -> list[dict]:
    """Return all (sid, idx, en, es) tuples for sentences missing glosses."""
    pending = []
    for sid, cfg in GRAMMAR_SITUATIONS.items():
        if cfg.get("drill_type") == "skip":
            continue
        sents = cfg.get("drill_sentences") or []
        for idx, s in enumerate(sents):
            if not isinstance(s, dict):
                continue
            if s.get("glosses"):
                continue
            en = s.get("en")
            es = s.get("es")
            if not en or not es:
                continue
            pending.append({"sid": sid, "idx": idx, "en": en, "es": es})
    return pending


def call_llm(client: OpenAI, en: str, es: str) -> dict:
    """Single call to the LLM. Returns the parsed glosses dict or raises.
    Retries 429s with exponential backoff so transient TPM/RPM bursts
    don't drop sentences on the floor."""
    user_msg = json.dumps({"en": en, "es": es}, ensure_ascii=False)
    last_err = None
    for attempt in range(5):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_msg},
                ],
                response_format={"type": "json_object"},
                temperature=0,
            )
            break
        except Exception as e:
            last_err = e
            msg = str(e)
            if "429" in msg or "rate_limit" in msg.lower():
                time.sleep(2 ** attempt + 0.25 * attempt)
                continue
            raise
    else:
        raise last_err  # type: ignore[misc]
    content = resp.choices[0].message.content
    parsed = json.loads(content)
    glosses = parsed.get("glosses")
    if not isinstance(glosses, dict):
        raise ValueError(f"non-dict glosses for {en!r} / {es!r}: {content}")
    # Empty is valid — sentences without nouns get {}.
    # Validate symmetry — every value should also appear as a key.
    missing = [v for v in glosses.values() if v not in glosses]
    if missing:
        raise ValueError(f"asymmetric glosses for {en!r}: missing keys {missing}")
    return glosses


def load_progress() -> dict:
    if not PROGRESS_PATH.exists():
        return {}
    with open(PROGRESS_PATH) as f:
        return json.load(f)


def save_progress(progress: dict) -> None:
    with open(PROGRESS_PATH, "w") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def write_sidecar(progress: dict) -> None:
    """Write progress dict as a sorted, importable Python module."""
    # Re-key by sid -> [glosses by idx]
    by_sid: dict[str, list[dict]] = {}
    for sid, cfg in GRAMMAR_SITUATIONS.items():
        if cfg.get("drill_type") == "skip":
            continue
        n = len(cfg.get("drill_sentences") or [])
        if not n:
            continue
        # Use a list of length n; entries that are missing stay None.
        bucket: list[dict | None] = [None] * n
        for idx in range(n):
            key = f"{sid}::{idx}"
            if key in progress:
                bucket[idx] = progress[key]
        if any(b is not None for b in bucket):
            by_sid[sid] = bucket  # type: ignore[assignment]

    lines = [
        '"""Auto-generated by scripts/generate_drill_glosses.py — do not edit by hand.',
        "",
        "Maps situation_id -> list[glosses_dict | None] aligned with each",
        "drill_sentence in GRAMMAR_SITUATIONS[sid]['drill_sentences'].",
        "Merged into GRAMMAR_SITUATIONS at import time.",
        '"""',
        "",
        "DRILL_GLOSSES: dict[str, list[dict[str, str] | None]] = {",
    ]
    for sid in sorted(by_sid):
        bucket = by_sid[sid]
        lines.append(f"    {sid!r}: [")
        for entry in bucket:
            if entry is None:
                lines.append("        None,")
            else:
                lines.append(f"        {entry!r},")
        lines.append("    ],")
    lines.append("}")
    lines.append("")
    SIDECAR_PATH.write_text("\n".join(lines), encoding="utf-8")


def main():
    pending_all = collect_pending()
    progress = load_progress()
    pending = [
        item for item in pending_all
        if f"{item['sid']}::{item['idx']}" not in progress
    ]
    print(f"Total drill sentences missing glosses: {len(pending_all)}")
    print(f"Already done in prior run:             {len(pending_all) - len(pending)}")
    print(f"Remaining this run:                    {len(pending)}")
    if not pending:
        print("Nothing to do. Writing sidecar from progress…")
        write_sidecar(progress)
        return

    client = OpenAI(api_key=settings.openai_api_key)

    failures: list[tuple[str, str]] = []
    started = time.time()
    lock = threading.Lock()
    completed = 0
    MAX_WORKERS = 6

    def worker(item):
        key = f"{item['sid']}::{item['idx']}"
        try:
            glosses = call_llm(client, item["en"], item["es"])
            return key, glosses, None
        except Exception as e:
            return key, None, str(e)

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(worker, item): item for item in pending}
        for fut in as_completed(futures):
            key, glosses, err = fut.result()
            with lock:
                completed += 1
                if err is None:
                    progress[key] = glosses
                else:
                    failures.append((key, err))
                    print(f"  FAIL {key}: {err}")
                if completed % 50 == 0 or completed == len(pending):
                    save_progress(progress)
                    elapsed = time.time() - started
                    rate = completed / elapsed if elapsed else 0
                    remaining = (len(pending) - completed) / rate if rate else 0
                    print(f"  [{completed}/{len(pending)}] checkpoint — {rate:.1f}/s, ETA {remaining:.0f}s")
    save_progress(progress)
    write_sidecar(progress)
    print(f"\nDone. Wrote {SIDECAR_PATH}")
    print(f"Successful: {len(pending) - len(failures)}/{len(pending)}")
    if failures:
        print(f"Failures: {len(failures)}")
        for k, e in failures[:10]:
            print(f"  {k}: {e}")


if __name__ == "__main__":
    main()
