"""Tiered "first perfect word" banks for the Memory Miracle free-trial opener.

Instead of memorizing one long goal-matched phrase, the trial now opens on a
single, carefully-chosen first WORD the user is very unlikely to already know.
The word must be: (1) new (not a recognizable cognate), (2) obviously useful,
(3) easy to memorize (a quick win), and — for intermediates — (4) a verb
conjugation worth mastering (3rd-person preterite irregulars), since
intermediates aren't impressed by learning a noun.

Three ordered tiers. Index 0 of each tier is the word shown first when a user
lands on that tier. The learner's up-front self-rating sets the starting tier;
the "I recognize this word" button bumps them UP one tier in real time (capped
at the top tier — no infinite climb).

LATAM rules (see project memory): never vosotros / `os` / `-áis`; usted-friendly.
See docs/proposals/trial-first-word-memory-loop.md for the full design.
"""

# Each entry: {"es", "en"}; ordered first -> later within a tier.
TIER_BANKS: list[list[dict[str, str]]] = [
    # Tier 0 — Absolute beginner ("I'm new"). High-utility, near-zero chance an
    # absolute beginner already knows them. `quisiera` leads: maximally useful,
    # non-cognate, still an easy win.
    [
        {"es": "quisiera", "en": "I would like"},
        {"es": "busco", "en": "I'm looking for"},
        {"es": "pido", "en": "I'll order / I ask for"},
        {"es": "hay", "en": "there is / there are"},
    ],
    # Tier 1 — Mid-beginner ("Not new, but I can't make sentences yet").
    # 1st-person irregulars + a 3rd-person-plural stretch.
    [
        {"es": "consigo", "en": "I get / I manage to"},
        {"es": "suelo", "en": "I usually (do)"},
        {"es": "quieren", "en": "they want"},
        {"es": "pueden", "en": "they can"},
    ],
    # Tier 2 — Intermediate ("Can make sentences, but verbs need work").
    # 3rd-person PRETERITE IRREGULARS — the conjugation flex that impresses.
    [
        {"es": "quiso", "en": "he / she wanted"},
        {"es": "pudo", "en": "he / she could"},
        {"es": "tuvo", "en": "he / she had"},
        {"es": "dijo", "en": "he / she said"},
        {"es": "hizo", "en": "he / she did / made"},
    ],
]

MAX_TIER = len(TIER_BANKS) - 1

# The up-front 3-button self-rating -> starting tier. Keys mirror the FE level
# keys so the same value flows downstream (fluency map, round 2, CTA).
LEVEL_TO_TIER: dict[str, int] = {
    "beginner": 0,   # "I'm new"
    "words": 1,      # "Not new to Spanish but I can't make sentences yet"
    "sentences": 2,  # "Can make sentences but verbs need work"
}


def tier_for_level(level: str | None) -> int:
    return LEVEL_TO_TIER.get((level or "").strip().lower(), 0)


def word_at(tier: int, index: int) -> dict[str, str]:
    """The word at (tier, index), clamped into range. Never raises."""
    t = max(0, min(tier, MAX_TIER))
    bank = TIER_BANKS[t]
    i = max(0, min(index, len(bank) - 1))
    return {**bank[i], "tier": t, "index": i}
