#!/usr/bin/env python3
"""One-time script: generate Catalan translations for all encounter + HF words.

Reads words from the seed data, batch-translates via GPT-4o-mini,
and writes results to app/data/catalan_translations.json.

Run: python scripts/generate_catalan.py
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import OpenAI
from app.data.seed_bank import ENCOUNTER_WORDS, HIGH_FREQUENCY_WORDS

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

OUTPUT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "app", "data", "catalan_translations.json",
)

BATCH_SIZE = 50


def collect_words():
    """Collect all encounter + HF words as (id, spanish) pairs."""
    words = []
    for category_words in ENCOUNTER_WORDS.values():
        for w in category_words:
            words.append((w["id"], w["spanish"]))
    for w in HIGH_FREQUENCY_WORDS:
        words.append((w["id"], w["spanish"]))
    return words


def translate_batch(batch: list[tuple[str, str]]) -> dict[str, str]:
    """Translate a batch of (id, spanish) pairs to Catalan via GPT-4o-mini."""
    word_list = "\n".join(f"{wid}: {spanish}" for wid, spanish in batch)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a Spanish-to-Catalan translator. "
                    "Translate each Spanish word/phrase to its Catalan equivalent. "
                    "Return a JSON object mapping word_id to the Catalan translation. "
                    "Keep translations concise — match the length/style of the Spanish original. "
                    "For articles (el, la, los, las, un, una), use the Catalan equivalents (el, la, els, les, un, una). "
                    "For short function words that are identical in both languages, keep them as-is."
                ),
            },
            {
                "role": "user",
                "content": f"Translate these Spanish words to Catalan:\n\n{word_list}",
            },
        ],
    )
    return json.loads(response.choices[0].message.content)


def main():
    words = collect_words()
    print(f"Collected {len(words)} words to translate")

    translations = {}
    for i in range(0, len(words), BATCH_SIZE):
        batch = words[i : i + BATCH_SIZE]
        print(f"  Translating batch {i // BATCH_SIZE + 1}/{(len(words) + BATCH_SIZE - 1) // BATCH_SIZE} ({len(batch)} words)...")
        result = translate_batch(batch)
        translations.update(result)
        time.sleep(0.5)  # Rate limit courtesy

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(translations, f, ensure_ascii=False, indent=2, sort_keys=True)

    print(f"Wrote {len(translations)} translations to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
