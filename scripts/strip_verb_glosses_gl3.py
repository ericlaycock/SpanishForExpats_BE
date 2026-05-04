"""One-off: strip verb-form entries from GL 3 drill_sentences glosses.

Per the canonical drill-gloss rule (docs/learning-flow.md), glosses cover
only nouns, adjectives, and adverbs — never verb forms or pronouns.

This script reads `app/data/grammar_situations.py` as text and removes any
gloss entry whose key is a verb form from the GL 3 verb pool. Other entries
(nouns/adjectives/adverbs) are preserved unchanged.

After running, eyeball the GL 3 lessons and run `python -c 'from app.data.grammar_situations import GRAMMAR_SITUATIONS'` to confirm syntax integrity.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "app" / "data" / "grammar_situations.py"

# Every verb form (EN + ES) used in GL 3 drill sentences. Remove both
# `"key": "value"` and `"value": "key"` entries from any glosses dict.
VERB_FORMS = {
    # hablar
    "speak", "speaks",
    "hablo", "hablas", "habla", "hablamos", "hablan",
    # escuchar
    "listen", "listens",
    "escucho", "escuchas", "escucha", "escuchamos", "escuchan",
    # cantar
    "sing", "sings",
    "canto", "cantas", "canta", "cantamos", "cantan",
    # beber
    "drink", "drinks",
    "bebo", "bebes", "bebe", "bebemos", "beben",
    # comer
    "eat", "eats",
    "como", "comes", "come", "comemos", "comen",
    # leer
    "read", "reads",
    "leo", "lees", "lee", "leemos", "leen",
    # vivir
    "live", "lives",
    "vivo", "vives", "vive", "vivimos", "viven",
    # escribir
    "write", "writes",
    "escribo", "escribes", "escribe", "escribimos", "escriben",
    # abrir
    "open", "opens",
    "abro", "abres", "abre", "abrimos", "abren",
}


def strip_verb_entries(glosses_inner: str) -> str:
    """Take the contents inside a `{...}` glosses dict literal and remove
    every entry whose key is a verb form. Preserves order of remaining entries.

    Inner format: `"speak": "hablo", "Spanish": "español", ...`
    """
    # Match individual `"key": "value"` entries (allowing simple non-quote
    # values; sufficient for the well-formed dicts we have).
    entries = re.findall(r'"([^"]+)":\s*"([^"]+)"', glosses_inner)
    kept = [(k, v) for k, v in entries if k not in VERB_FORMS]
    return ", ".join(f'"{k}": "{v}"' for k, v in kept)


def main() -> int:
    src = TARGET.read_text()

    # Match `"glosses": {...}` — assumes single-line dict literal (which is
    # how the file is currently authored).
    pattern = re.compile(r'"glosses":\s*\{([^{}]+)\}')

    edits = 0
    skipped = 0

    def replace(m: re.Match[str]) -> str:
        nonlocal edits, skipped
        inner = m.group(1)
        new_inner = strip_verb_entries(inner)
        if new_inner == inner.strip().rstrip(","):
            skipped += 1
            return m.group(0)
        if not new_inner:
            # Don't allow empty glosses dicts — flag for manual review.
            return m.group(0)
        edits += 1
        return f'"glosses": {{{new_inner}}}'

    out = pattern.sub(replace, src)
    TARGET.write_text(out)
    print(f"edits applied: {edits}")
    print(f"already clean: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
