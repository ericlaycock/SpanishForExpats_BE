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
3. **Drill lesson anatomy**: rule slides / conjugation table slides → **mandatory recall quiz** → 10-20 generalizing drills.
   - **Rule slides**: multi-slide explanations of one rule, big-font, very high signal-to-noise. Non-grammatical language except for the core concept (e.g. "possessive pronouns").
   - **Conjugation table slides**: rendered as a `mini_table` card (one verb per card, max 2 verbs per lesson) with the changing letters in crimson via pipe-encoded forms (`habl|o`).
   - **Recall quiz**: the intro_chart carries a `recall: {verb, answers}` field. After the last rule slide, the table is hidden and the user types each conjugation from memory before drills start. Powered by the existing `RecallQuiz` component.
   - **Generalizing drills**: 10-20 drills that apply the rule by combining it with other common words. Every drill sentence carries a `glosses` dict covering **only nouns, adjectives, and adverbs** (bidirectional EN↔ES).

     **VERB FORMS AND PRONOUNS ARE NEVER GLOSSED, NO EXCEPTIONS.** This is a universal invariant across every grammar lesson, every tense, every group. The conjugated verb being tested, every other verb form in the sentence (gerunds, infinitives, auxiliaries, copulas), every pronoun (subject, object, reflexive), every article, and pure-glue prepositions are all excluded. Glosses exist to remove vocabulary friction on nouns/adjectives/adverbs the user hasn't met yet — they are NOT a general-purpose translator.

     If you encounter existing drill_sentences whose glosses include verb forms or pronouns, **the data is wrong and must be corrected**. Do not template off of legacy violations. See `docs/learning-flow.md` "THE GLOSS RULE" section for the authoritative spec and worked examples.
4. **Chat lesson**: one consolidating voice conversation per `[drill][drill][chat]` block. No P2/P3 split.

Any data field, doc, or audit that contradicts the above is wrong.

## Runtime gap (must be flagged in user-facing docs)

`grammar_situations.py` does NOT yet encode this shape. Until migrated:
- The data model is wrong.
- Reading the data fields directly will mislead.
- `docs/grammar-curriculum.md` must include a prominent "Data migration needed" callout.

## Migration progress (2026-05-01)

The grammar audit identified a 5-step migration path. Status:

1. ✅ **Quick wins** — 3 `gustar` `_chat` `phase_2_config.targets` normalized from `int`+`pattern` to proper pronoun-phrase lists.
2. ✅ **Block-pattern fix** — GL 11 `modal` re-sequenced from `[D D D C C]` → `[D D C][D C]`.
3. ✅ **Anatomy backfill** — 30+ module-level slide constants (`*_INTRO`, `*_RULE`) added to `grammar_situations.py` and wired into 90+ drill entries across 25 grammar groups (every conjugation drill now renders a 3-card intro + endings table).
4. ✅ **Stub build-out** — GL 18.5 `perfect_tenses` expanded from a 1-entry stub into a proper `[D D C]` block (present perfect drill + pluperfect drill + recap chat). GL 19 `obj_chat_1`/`obj_chat_2` recap chats kept in place with clarified descriptions.
5. ⛔ **Vestigial `phases` dict cleanup — BLOCKED.** Although the dict is documented as "wrong and bad" above, grep proves it is *actively consumed* in production:
   - `app/api/v1/situations.py:887` — `phases=config["phases"]` (BE serializes the dict to API responses).
   - `SpanishForExpats_FE/app/[locale]/app/situation/[id]/learn/hooks/useLearnFlow.ts:49` — `const phases = grammarConfig?.phases` (FE drives phase routing from the dict).
   Removing the dict in `grammar_situations.py` would break both BE serialization and FE phase routing. Migration of the BE serializer + FE `useLearnFlow.ts` to a different signal (probably `lesson_type` + `drill_type` checks, or an explicit phase-list field) must land first.

## Code references

- `SpanishForExpats_BE/app/data/grammar_situations.py` — partially migrated to the new shape (per-lesson split + slide packs in place); `phases` dict still present pending step 5.
- `SpanishForExpats_BE/app/data/situation_roles.py:104+` — `GRAMMAR_STRUCTURES` dict, keyed by group ID.
- `SpanishForExpats_BE/app/api/v1/situations.py:887` — BE consumer of `phases` dict (blocker for step 5).
- `SpanishForExpats_FE/app/[locale]/app/situation/[id]/learn/hooks/useLearnFlow.ts:49` — FE consumer of `phases` dict (blocker for step 5).

## Related docs

- `docs/grammar-curriculum.md` — describes the intended model and flags the runtime gap.
- `docs/proposals/grammar-audit-v3.md` — earlier proposal, NOT authoritative.
