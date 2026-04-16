"""Alt-language mode: swap spanish → catalan/swedish for encounter/HF words."""
from typing import List, Optional
from sqlalchemy.orm import Session, make_transient
from app.models import Word


def apply_alt_language(words: List[Word], alt_language: Optional[str], db: Session) -> List[Word]:
    """Swap spanish → alt language translation for encounter/HF words.

    Returns detached copies with w.spanish replaced by the translation.
    If alt_language is None, returns words unchanged.
    """
    if not alt_language:
        return words
    result = []
    for w in words:
        translation = getattr(w, alt_language, None)
        if translation and w.word_category in ('encounter', 'high_frequency'):
            db.expunge(w)
            make_transient(w)
            w.spanish = translation
        result.append(w)
    return result


def get_target_language_name(alt_language: Optional[str]) -> str:
    """Return human-readable language name for prompts."""
    return {"catalan": "Catalan", "swedish": "Swedish"}.get(alt_language, "Spanish")


def get_language_code(alt_language: Optional[str]) -> str:
    """Return ISO-style short code for the target language."""
    return {"catalan": "ca", "swedish": "sv"}.get(alt_language, "es")
