#!/usr/bin/env python3
"""Replace encounter words that overlap with the HF word list.

Reads master_triplets_50_per_scenario_fixed.md, identifies overlapping words,
uses GPT-4.1-mini to generate replacements, and outputs a cleaned JSON file.

Usage: .venv/bin/python scripts/replace_hf_overlaps.py
"""

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import OpenAI
from app.data.hf_words import HIGH_FREQUENCY_WORDS

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

MASTER_FILE = "/home/eric/Documents/master_triplets_50_per_scenario_fixed.md"
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "cleaned_triplets.json")

# Build HF set
HF_SET = {w["spanish"].lower() for w in HIGH_FREQUENCY_WORDS}


def normalize_quotes(text):
    """Replace smart quotes and other unicode punctuation with ASCII equivalents."""
    replacements = {
        "\u201c": '"', "\u201d": '"',  # smart double quotes
        "\u2018": "'", "\u2019": "'",  # smart single quotes
        "\u2014": "--", "\u2013": "-",  # em/en dashes
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def parse_master_file():
    """Parse the master triplets file into structured data."""
    with open(MASTER_FILE, encoding="utf-8") as f:
        content = normalize_quotes(f.read())

    sections = re.split(r"^## ", content, flags=re.MULTILINE)
    categories = {}

    for section in sections[1:]:
        lines = section.strip().split("\n")
        cat_name = lines[0].strip()
        triplets = []

        current_words = None
        for line in lines[1:]:
            word_match = re.match(
                r'\d+\.\s+\("(.+?)",\s*"(.+?)",\s*"(.+?)"\)', line.strip()
            )
            opener_match = re.match(r'\s*-\s+"(.+)"', line.strip())

            if word_match:
                current_words = list(word_match.groups())
            elif opener_match and current_words:
                triplets.append(
                    {"words": current_words, "opener": opener_match.group(1)}
                )
                current_words = None

        categories[cat_name] = triplets
        print(f"Parsed {cat_name}: {len(triplets)} triplets")

    return categories


def find_overlaps(categories):
    """Find all encounter words that overlap with HF words."""
    overlaps = []
    for cat, triplets in categories.items():
        for i, t in enumerate(triplets):
            for j, word in enumerate(t["words"]):
                if word.lower() in HF_SET:
                    overlaps.append((cat, i, j, word))
    return overlaps


def generate_replacement(cat_name, encounter_num, position, old_word, triplet_words, opener):
    """Use GPT to generate a replacement word."""
    other_words = [w for k, w in enumerate(triplet_words) if k != position]

    prompt = f"""You are helping build a Spanish vocabulary learning app.

Category: {cat_name}
Encounter #{encounter_num + 1} of 50
Current triplet: {triplet_words[0]}, {triplet_words[1]}, {triplet_words[2]}
Current opener: "{opener}"

The word "{old_word}" needs to be replaced because it already appears in the high-frequency word list and would be a duplicate.

Generate ONE replacement Spanish word or short phrase (max 3 words) that:
- Fits the same category ({cat_name}) and scenario context
- Works well alongside the other words: {other_words}
- Is at a similar difficulty level
- Is NOT any of these common words: {', '.join(sorted(list(HF_SET)[:50]))}...
- Is a word/phrase a Spanish learner would naturally encounter in this situation

Reply with ONLY the replacement Spanish word/phrase, nothing else."""

    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=20,
        temperature=0.7,
    )
    return resp.choices[0].message.content.strip().strip('"').strip("'")


def main():
    categories = parse_master_file()

    overlaps = find_overlaps(categories)
    print(f"\nFound {len(overlaps)} overlapping words to replace\n")

    # Replace overlapping words
    replaced = 0
    for cat, trip_idx, word_idx, old_word in overlaps:
        triplet = categories[cat][trip_idx]
        new_word = generate_replacement(
            cat, trip_idx, word_idx, old_word,
            triplet["words"], triplet["opener"]
        )

        # Check the replacement isn't ALSO in HF
        attempts = 0
        while new_word.lower() in HF_SET and attempts < 3:
            attempts += 1
            new_word = generate_replacement(
                cat, trip_idx, word_idx, old_word,
                triplet["words"], triplet["opener"]
            )

        if new_word.lower() in HF_SET:
            print(f"  WARNING: Could not find non-HF replacement for '{old_word}' in {cat} #{trip_idx+1}")
            continue

        categories[cat][trip_idx]["words"][word_idx] = new_word
        replaced += 1

        if replaced % 10 == 0 or replaced <= 3:
            print(f"  [{replaced}/{len(overlaps)}] {cat} #{trip_idx+1}: '{old_word}' → '{new_word}'")

    # Verify no remaining overlaps
    remaining = find_overlaps(categories)
    print(f"\nReplaced {replaced} words. Remaining overlaps: {len(remaining)}")
    if remaining:
        for cat, i, j, w in remaining:
            print(f"  STILL OVERLAPPING: {cat} #{i+1} word {j}: '{w}'")

    # Save cleaned data
    with open(OUTPUT_FILE, "w") as f:
        json.dump(categories, f, ensure_ascii=False, indent=2)

    print(f"\nSaved cleaned triplets to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
