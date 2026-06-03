"""High-utility survival phrases for the Memory Miracle free-trial variant.

Maps a user's stated goal (from the 10-second goal pick) to ONE genuinely
useful, immediately-deployable Latin American Spanish phrase that they'll
memorize to 100% in the memory utility, then say out loud. Kept deliberately
short + universal so the win is real and fast.

LATAM rules (see project memory): never vosotros / `os` / `-áis`; usted-friendly;
nothing region-locked. Each phrase is something an expat can literally use the
same day.
"""

# goal key -> {"es", "en"}. `default` covers free-text / "something else".
TRIAL_PHRASES: dict[str, dict[str, str]] = {
    "restaurant": {"es": "¿Me puede traer la cuenta, por favor?", "en": "Can you bring me the check, please?"},
    "market_pay": {"es": "¿Puedo pagar con efectivo?", "en": "Can I pay with cash?"},
    "family":     {"es": "Gracias por invitarme, la pasé muy bien.", "en": "Thanks for having me, I had a great time."},
    "banking_medical": {"es": "¿Me puede ayudar con esto, por favor?", "en": "Can you help me with this, please?"},
    "work_realestate": {"es": "¿Cuándo podemos firmar el contrato?", "en": "When can we sign the contract?"},
    "fast_speech": {"es": "¿Puede hablar un poco más despacio, por favor?", "en": "Can you speak a little slower, please?"},
    "default":    {"es": "¿Puedo pagar con efectivo?", "en": "Can I pay with cash?"},
}

# Human labels for the goal-pick UI (FE mirrors these keys).
GOAL_LABELS: dict[str, str] = {
    "restaurant": "Order at restaurants & markets",
    "market_pay": "Shopping & paying",
    "family": "Talk with my partner's / friends' family",
    "banking_medical": "Banking, medical & errands",
    "work_realestate": "Work / real estate",
    "fast_speech": "Understand fast native speech",
}


def phrase_for_goal(goal: str | None) -> dict[str, str]:
    return TRIAL_PHRASES.get((goal or "").strip().lower(), TRIAL_PHRASES["default"])
