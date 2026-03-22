"""Catalan mode: swap spanish → catalan for encounter/HF words."""
from typing import List
from sqlalchemy.orm import Session, make_transient
from app.models import Word


def apply_catalan_mode(words: List[Word], db: Session) -> List[Word]:
    """Swap spanish → catalan for encounter/HF words. Returns detached copies."""
    result = []
    for w in words:
        if w.catalan and w.word_category in ('encounter', 'high_frequency'):
            db.expunge(w)
            make_transient(w)
            w.spanish = w.catalan
        result.append(w)
    return result
