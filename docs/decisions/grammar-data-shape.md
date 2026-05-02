# Grammar data shape: groups + alternating drill/chat lessons

- **Status**: Accepted (intent); **runtime gap** — data still uses old shape
- **Date**: 2026-04-30
- **Confirmed by**: Eric

## Context

`grammar_situations.py` carries an old per-lesson `phases` flag dict (`{0a, 0b, 1a, 1b, 1c, 2, 3}`) along with `intro_chart`, `rule_chart`, `drill_sentences`, and `drill_config` fields. Earlier docs (`LEARNING_FLOW.md`, `GRAMMAR_AUDIT.md` v3) describe several different conceptions of the grammar pipeline. None match the current intended model.

Eric's verdict on the old fields: **"those old phases in the code are wrong and bad."**

## Decision

The intended grammar curriculum shape is:

1. **Grammar groups** are the highest level of organization (e.g. "Present Tense Regular" is a group). Group identity is derived from the lesson ID prefix; no explicit `group` field exists yet. Group-level structures live in `app/data/situation_roles.py:GRAMMAR_STRUCTURES`.
2. **Inside each group**, lessons follow the pattern `[1-2 drill lessons][1 chat lesson]`, repeating. Examples:
   - `[drill_1][drill_2][chat_1][drill_3][drill_4][chat_2]`
   - `[drill_1][chat_1]`
3. **Drill lesson anatomy**: rule slides / conjugation table slides → *(sometimes)* table practice → 10-20 generalizing drills.
   - **Rule slides**: multi-slide explanations of one rule, big-font, very high signal-to-noise. Non-grammatical language except for the core concept (e.g. "possessive pronouns").
   - **Conjugation/pronoun table slides**: just the tables. The user can quickly try to recall them.
   - **Generalizing drills**: 10-20 drills that apply the rule by combining it with other common (translated) words. Alternates between typing and speech.
4. **Chat lesson**: one consolidating voice conversation per `[drill][drill][chat]` block. No P2/P3 split.

Any data field, doc, or audit that contradicts the above is wrong.

## Runtime gap (must be flagged in user-facing docs)

`grammar_situations.py` does NOT yet encode this shape. Until migrated:
- The data model is wrong.
- Reading the data fields directly will mislead.
- `docs/grammar-curriculum.md` must include a prominent "Data migration needed" callout.

## Code references

- `SpanishForExpats_BE/app/data/grammar_situations.py` — current (wrong) data shape.
- `SpanishForExpats_BE/app/data/situation_roles.py:104+` — `GRAMMAR_STRUCTURES` dict, keyed by group ID.

## Related docs

- `docs/grammar-curriculum.md` — describes the intended model and flags the runtime gap.
- `docs/proposals/grammar-audit-v3.md` — earlier proposal, NOT authoritative.
