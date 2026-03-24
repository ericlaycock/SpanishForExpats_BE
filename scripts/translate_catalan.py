"""Translate all encounter words from Spanish to Catalan using GPT-4.1-mini.

Reads seed_bank.py, finds encounter words with empty catalan fields,
batches them through GPT, and rewrites the file with translations filled in.

Also handles the 18 missing high-frequency words in hf_words.py.

Usage:
    cd SpanishForExpats_BE
    python scripts/translate_catalan.py          # dry-run: print translations
    python scripts/translate_catalan.py --write  # overwrite seed_bank.py + hf_words.py
"""

import json
import os
import re
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Load .env from the BE root
BE_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(BE_ROOT / ".env")

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

SEED_BANK_PATH = BE_ROOT / "app" / "data" / "seed_bank.py"
HF_WORDS_PATH = BE_ROOT / "app" / "data" / "hf_words.py"

BATCH_SIZE = 50  # words per GPT call


def translate_batch(words: list[tuple[str, str]]) -> dict[str, str]:
    """Translate a batch of (spanish, english) pairs to Catalan.

    Returns dict mapping spanish -> catalan.
    """
    # Build the prompt with numbered items for reliable parsing
    items = []
    for i, (spanish, english) in enumerate(words, 1):
        items.append(f"{i}. {spanish} ({english})")

    prompt = f"""Translate these Spanish words/phrases to Catalan.
Return ONLY a JSON object mapping each Spanish word/phrase to its Catalan translation.
Keep the same register and formality level. For short phrases, translate naturally.
Do not add explanations.

{chr(10).join(items)}

Return format: {{"spanish_word": "catalan_translation", ...}}"""

    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert Spanish-to-Catalan translator. "
                        "You produce natural, everyday Catalan (central dialect). "
                        "For vocabulary used in everyday situations (banking, airports, "
                        "restaurants, etc.), use standard Catalan equivalents.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.2,
                response_format={"type": "json_object"},
            )
            raw = response.choices[0].message.content
            result = json.loads(raw)

            # Validate we got translations for all inputs
            translations = {}
            for spanish, _english in words:
                catalan = result.get(spanish, "")
                if catalan:
                    translations[spanish] = catalan
                else:
                    print(f"  WARNING: No translation returned for '{spanish}'")
                    translations[spanish] = ""
            return translations

        except Exception as e:
            print(f"  Attempt {attempt + 1} failed: {e}")
            if attempt < 2:
                time.sleep(2 ** attempt)
            else:
                # Return empty translations on total failure
                return {spanish: "" for spanish, _ in words}


def collect_missing_encounter_words() -> list[tuple[str, str, str, int]]:
    """Parse seed_bank.py and find all encounter word tuples with empty catalan.

    Returns list of (spanish, english, category, line_hint) for words needing translation.
    """
    # Import from the actual module
    sys.path.insert(0, str(BE_ROOT))
    from app.data.seed_bank import _SUB_SITUATIONS

    missing = []
    for category, sub_list in _SUB_SITUATIONS.items():
        for sub in sub_list:
            for spanish, english, catalan in sub["words"]:
                if not catalan:
                    missing.append((spanish, english, category, 0))
    return missing


def collect_missing_hf_words() -> list[tuple[str, str]]:
    """Find HF words with empty catalan field."""
    sys.path.insert(0, str(BE_ROOT))
    from app.data.hf_words import HIGH_FREQUENCY_WORDS

    return [
        (w["spanish"], w["english"])
        for w in HIGH_FREQUENCY_WORDS
        if not w.get("catalan")
    ]


def patch_seed_bank(translations: dict[str, str]) -> str:
    """Read seed_bank.py, replace empty catalan strings with translations."""
    content = SEED_BANK_PATH.read_text()

    # Match tuples like ("spanish", "english", "")
    # Replace the empty "" with the translation
    def replacer(match):
        spanish = match.group(1)
        english = match.group(2)
        catalan = translations.get(spanish, "")
        # Escape any quotes in the catalan string
        catalan_escaped = catalan.replace('"', '\\"')
        return f'("{spanish}", "{english}", "{catalan_escaped}")'

    # Pattern: ("...", "...", "")
    pattern = r'\("([^"]+)", "([^"]+)", ""\)'
    patched = re.sub(pattern, replacer, content)
    return patched


def patch_hf_words(translations: dict[str, str]) -> str:
    """Read hf_words.py, replace empty catalan strings with translations."""
    content = HF_WORDS_PATH.read_text()

    for spanish, catalan in translations.items():
        if catalan:
            catalan_escaped = catalan.replace('"', '\\"')
            # Match the specific entry: "spanish": "...", ... "catalan": ""
            # We need to find the line with this spanish word and replace its catalan
            old = f'"spanish": "{spanish}", "english"'
            if old in content:
                # Find the line and replace catalan: "" with catalan: "translation"
                lines = content.split("\n")
                for i, line in enumerate(lines):
                    if f'"spanish": "{spanish}"' in line and '"catalan": ""' in line:
                        lines[i] = line.replace(
                            '"catalan": ""', f'"catalan": "{catalan_escaped}"'
                        )
                        break
                content = "\n".join(lines)
    return content


def main():
    write_mode = "--write" in sys.argv

    print("=== Catalan Translation Script ===\n")

    # --- Encounter words ---
    missing_enc = collect_missing_encounter_words()
    print(f"Encounter words needing translation: {len(missing_enc)}")

    if not missing_enc and not collect_missing_hf_words():
        print("Nothing to translate!")
        return

    # Deduplicate (same spanish word may appear in multiple encounters)
    unique_pairs = list({(s, e) for s, e, _, _ in missing_enc})
    unique_pairs.sort()  # deterministic order
    print(f"Unique Spanish words/phrases: {len(unique_pairs)}")

    all_translations: dict[str, str] = {}

    # Batch and translate
    total_batches = (len(unique_pairs) + BATCH_SIZE - 1) // BATCH_SIZE
    for i in range(0, len(unique_pairs), BATCH_SIZE):
        batch = unique_pairs[i : i + BATCH_SIZE]
        batch_num = i // BATCH_SIZE + 1
        print(f"\nBatch {batch_num}/{total_batches} ({len(batch)} words)...")
        translations = translate_batch(batch)
        all_translations.update(translations)

        # Brief delay between batches
        if i + BATCH_SIZE < len(unique_pairs):
            time.sleep(0.5)

    # Retry pass for any words that came back empty
    still_missing = [(s, e) for s, e in unique_pairs if not all_translations.get(s)]
    if still_missing:
        print(f"\n--- Retry pass: {len(still_missing)} words still missing ---")
        retry_batches = (len(still_missing) + 25 - 1) // 25  # smaller batches
        for i in range(0, len(still_missing), 25):
            batch = still_missing[i : i + 25]
            batch_num = i // 25 + 1
            print(f"  Retry batch {batch_num}/{retry_batches} ({len(batch)} words)...")
            translations = translate_batch(batch)
            for spanish, catalan in translations.items():
                if catalan:
                    all_translations[spanish] = catalan
            time.sleep(0.5)

    # Print sample translations
    print(f"\n--- Sample translations ({min(20, len(all_translations))}) ---")
    for spanish, catalan in list(all_translations.items())[:20]:
        print(f"  {spanish} → {catalan}")

    filled = sum(1 for v in all_translations.values() if v)
    print(f"\nTranslated: {filled}/{len(unique_pairs)} unique words")

    # --- High-frequency words ---
    missing_hf = collect_missing_hf_words()
    hf_translations: dict[str, str] = {}
    if missing_hf:
        print(f"\nHF words needing translation: {len(missing_hf)}")
        hf_translations = translate_batch(missing_hf)
        hf_filled = sum(1 for v in hf_translations.values() if v)
        print(f"Translated: {hf_filled}/{len(missing_hf)} HF words")
        for spanish, catalan in hf_translations.items():
            print(f"  {spanish} → {catalan}")

    if write_mode:
        # Patch seed_bank.py
        patched_seed = patch_seed_bank(all_translations)
        SEED_BANK_PATH.write_text(patched_seed)
        print(f"\n✓ Wrote {SEED_BANK_PATH}")

        # Patch hf_words.py
        if hf_translations:
            patched_hf = patch_hf_words(hf_translations)
            HF_WORDS_PATH.write_text(patched_hf)
            print(f"✓ Wrote {HF_WORDS_PATH}")

        print("\nDone! Run the seed script to update the database.")
    else:
        print("\n[DRY RUN] Pass --write to update seed_bank.py and hf_words.py")


if __name__ == "__main__":
    main()
