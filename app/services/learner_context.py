"""Learner-aware context carried into the conversation/grammar system prompts.

The v3 prompts in `app/prompts/prompts.json` need more than the current
persona — they need to know the learner's level, what chips the FE is
showing, which are already green, the conversation goal, and whether
the learner is stuck. Centralising those fields in a dataclass keeps
the prompt builders' signatures sane and makes the contract obvious to
every call-site (legacy `/voice-turn` and the WebRTC realtime ephemeral
session both must populate the same shape — divergence between them is
how the realtime flow drifted from the legacy one in the past).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ChipTarget:
    """One item in the FE's "Use these words to progress" panel.

    For vocab encounters, `verb`/`pronoun` are None and `spanish` is the
    word/phrase the learner must utter. For grammar chats the chip is a
    specific (verb, pronoun) conjugation — `spanish` is the conjugated
    form (e.g. "cantas") and `english` is the conjugated English gloss
    ("you sing").
    """

    id: str
    spanish: str
    english: str
    verb: Optional[str] = None
    pronoun: Optional[str] = None

    @property
    def is_grammar(self) -> bool:
        return self.verb is not None and self.pronoun is not None


@dataclass
class LearnerContext:
    """Everything the v3 system prompt needs about the learner + lesson.

    Fields default to "no information" so legacy call-sites that haven't
    been updated yet still produce a usable prompt — they just lose the
    level adaptation, goal, and anti-stuck behaviour. The prompt builder
    omits sections whose inputs are empty/None.
    """

    spanish_level: Optional[str] = None  # "a"|"b"|"c"|"d" (q0_spanish_level)
    vocab_level: int = 0
    grammar_level: float = 0.0
    goal: Optional[str] = None
    target_chips: List[ChipTarget] = field(default_factory=list)
    completed_chip_ids: List[str] = field(default_factory=list)
    consecutive_no_progress_turns: int = 0

    def pending_chips(self) -> List[ChipTarget]:
        """Chips not yet ticked. Order preserved from `target_chips`."""
        completed = set(self.completed_chip_ids)
        return [c for c in self.target_chips if c.id not in completed]
