# Spanish for Expats — Learning Flow & Pedagogy

> Defines the learning phase system, situation types, and progression mechanics.
> For technical implementation details, see `architecture.md` (sibling).

## Situation Types

### Main Situations (Encounters)

Real-world scenarios (banking, airport, groceries, etc.). Each situation category (e.g., "Banking") has **50 encounters** (total_in_series = 50). Each individual encounter has:
- **Encounter words**: 3 situation-specific vocabulary items
- **High-frequency words**: 2 top-N common Spanish words (onboarded alongside encounters)
- Word workload: 5 words total per encounter

### Grammar Situations

Unlocked by vocab level. Each grammar situation has:
- **Custom word workload**: Specific to the grammar topic (e.g., all pronouns)
- **No high-frequency word onboarding**: Only the custom words
- **Video lesson**: Descript embed (phase 0a)
- **Grammar drills**: Occasionally included (phase 0b)

## Vocab Level (VL) & Grammar Level (GL)

**Vocab Level (VL)** = count of high-frequency words with `mastery_level >= 1` (learned at least once).

**Grammar Level (GL)** = the `grammar_level` value of the highest completed grammar situation (0 if none completed).

### Grammar Gating — "Overmatched" VL

A user is **gated** when their VL exceeds the VL threshold for the next grammar level above their current GL. Grammar gates block progression in main situations until the grammar unit is completed (or, for "coming soon" levels, until content is available).

| GL | Grammar Topic | VL Threshold | Has Content? |
|----|---------------|-------------|-------------|
| 1 | Pronouns | 10 | Yes |
| 2 | Grammatical Gender | 15 | Yes |
| 3 | Regular Present | 100 | Yes |
| 4 | Irregular Present | 200 | Yes |
| 4.5 | Irregular Present II | 240 | Yes |
| 5 | Spelling Changes | 260 | Yes |
| 6 | Present O→UE | 300 | Yes |
| 7 | Present E→IE | 330 | Yes |
| 8 | Present E→I | 400 | Yes |
| 9 | Ir A + Infinitive | 500 | Yes |
| 10 | Gustar Part 1 | 510 | Yes |
| 10.3 | Gustar Part 2 | 515 | Yes |
| 10.6 | Gustar Part 3 | 520 | Yes |
| 11 | Tengo que / Me toca / Necesito | 550 | Coming soon |
| 12 | Imperfect | 600 | Coming soon |
| 13 | Reflexive | 700 | Coming soon |
| 14 | Future Simple | 750 | Coming soon |
| 15 | Conditional | 800 | Coming soon |
| 16 | Preterite vs Imperfect | 900 | Coming soon |
| 17 | Preterite Regular | 1000 | Yes |
| 17.1 | Preterite Highly Irregular | 1010 | Yes |
| 17.2 | Preterite Weird Spelling Changes | 1020 | Coming soon |
| 17.3 | Preterite Stem Changers | 1030 | Coming soon |
| 17.4 | Preterite DUCIR | 1050 | Coming soon |
| 17.5 | Preterite e-to-i Irregular | 1060 | Coming soon |
| 18 | Gerund | 1300 | Yes |
| 19 | Direct + Indirect Obj Pronouns | 1400 | Coming soon |
| 20 | Subjunctive | 1500 | Coming soon |

### Language Mode

Voice chat uses Spanish when **both** `VL >= 500` AND `GL >= 10`. Otherwise English.

## Learning Phases

### Main Situation Phases

Main (non-grammar) situations use a **single combined learning component** (`WordCardsPhase`), not the multi-step 1a/1b/1c pipeline.

| Phase | Name | Description |
|-------|------|-------------|
| WordCards | Learn + Recall | Combined component with two modes. **Learn mode**: cards show Spanish + English + pronunciation play button; user records each word via mic, API checks pronunciation. **Recall mode**: after all cards pass, they flip to show only English (shuffled); user must pronounce again from memory. All cards must pass both modes to advance. |
| 2 | Voice Conversation (hints) | Full AI conversation with word hints visible (Spanish + English in word checklist) |
| 3 | Voice Conversation (no hints) | Same conversation, hints show English only. Completion marks situation done |

Flow: **WordCards → Phase 2 → Phase 3**

The `useLearnFlow.ts` hook detects non-grammar situations and routes directly from WordCards completion to `/situation/{id}/voice-chat?phase=2`.

**Refresh events run the chat too.** Both first-encounters and refresh events flow through to phase 2 (English target hints visible, hints available on click). Refreshes used to short-circuit at WordCards recall, but the conversation phase is the value of the lesson — refresh now re-runs it with the SRS-targeted vocabulary.

**Grammar entry phase.** First-time grammar situations enter at `learn` (1a) even when the grammar config has `0a`/`0b` (drill enabled), so a brand-new user is taught the tokens before being drilled on them. Drill is reserved for refreshes, where the user has already completed the situation at least once.

### Encounter Language Progression

The AI assistant's language in voice chat (phases 2/3) adapts based on encounter number and user's vocab level:

| Vocab Level | Encounters 1-20 | Encounters 21-40 | Encounters 41-50 |
|-------------|-----------------|-------------------|-------------------|
| VL < 300 | English | Simple Spanish (text visible) | Simple Spanish (audio only) |
| VL >= 300 | Simple Spanish (text visible) | Simple Spanish (text visible) | Simple Spanish (audio only) |

Language modes:
- **`english`**: AI speaks English. Text subtitle shown. (Default for beginners)
- **`spanish_text`**: AI speaks simple Spanish (short sentences, 5-8 words max). Text subtitle shown.
- **`spanish_audio`**: AI speaks simple Spanish. **No text subtitle** — user must listen. Chat history shows "[Audio message]" with replay and transcribe buttons.

The mode is computed server-side in `voice_turn_service.py:get_language_mode()` based on `series_number` and vocab level, and returned in the `CreateConversationResponse`.

### Encounter Goals

Each encounter displays a prominent goal banner (e.g., "Complete the check-in process by answering all the check-in assistant's questions"). Goals are per-situation (stored in the `goal` column of the `situations` table) — all encounters within a situation share the same goal text.

### Grammar Situation Phases

Grammar situations use a **configurable multi-phase system**. Each grammar situation has a `phases` config object with boolean flags (e.g., `{ "0a": true, "0b": false, "1a": true, ... }`) that toggles individual phases on/off.

| Phase | Name | Description |
|-------|------|-------------|
| 0a | Grammar Video | Descript video embed explaining the grammar concept |
| 0b | Grammar Drills | Customized exercises (conjugation, article matching, gustar, ir a + inf). Drill type set per situation. 2 wrong on same item → reveal answer. 2 total fails → rewatch video |
| 1a | Learn | Typing exercise — user types Spanish word from prompt (`LearnPhase` component) |
| 1b | Written Test | Recall — shows English, user types Spanish from memory. 2 fails → reset to 1a (`WrittenTestPhase`) |
| 1c | Spoken Test | Pronunciation — shows English, user records Spanish. 2 fails → reset to 1a. Can be limited to N items via `phase_1c_config.total_items` (`SpokenTestPhase`) |
| 2 | Voice Conversation (hints) | Same as main situations |
| 3 | Voice Conversation (no hints) | Same as main situations |

The frontend phase type is defined as: `type Phase = 'video' | 'drill' | 'learn' | 'written-test' | 'spoken-test'`

### Phase Persistence

Phase state is **not persisted in the database**. It exists only during the active session:
- Learn phases: managed by `useLearnFlow.ts` hook (grammar: 0a→0b→1a→1b→1c; regular: WordCards)
- Phases 2/3: passed via URL query param `?phase=2` or `?phase=3`
- `X-Learning-Phase` header is sent to the backend but used **only for logging/telemetry**, not business logic
- Only `UserSituation.started_at` and `completed_at` are saved to the DB

## Mastery & Spaced Repetition

Words progress through a **5-level spaced repetition system** (`mastery_level` on `UserWord`):

| Level | Meaning | Next refresh due |
|-------|---------|-----------------|
| 0 | Unseen | — |
| 1 | Learned (lesson completed) | 24 hours |
| 2 | Refreshed once | 7 days |
| 3 | Refreshed twice | 30 days |
| 4 | Mastered (final) | Never |

- **Level 0 → 1**: Set by `refresh_service.set_initial_mastery()` after a lesson is completed
- **Level N → N+1**: Set by `refresh_service.bump_mastery_after_refresh()` when the user revisits a situation after `next_refresh_at` is due
- **Level 4**: `status` field changes to `"mastered"`, `next_refresh_at` set to `None`
- **Vocab level (VL)**: Counts high-frequency words with `mastery_level >= 1` (learned at least once)
- **Grammar words** (`word_category='grammar'`) do NOT count toward vocab level

## Grammar Situation Details

### Full Configuration Table

| VL | Situation | Word Workload | 0a Video | 0b Drill | 1a | 1b | 1c | Phase 2 Instructions | Phase 3 |
|----|-----------|---------------|----------|----------|----|----|----|--------------------|---------|
| 15 | Pronouns | yo, tu, el, ella, usted, nosotros, nosotras, ellos, ellas, ustedes, su | bLZk006G5ge | Skip | Include | Include | Skip | All pronouns + "su" in conversation | Skip |
| 20 | Grammatical Gender | el, los, la, las, un, unos, una, unas | aJguo8cBgm7 | Article matching (DIONZA/MAJE LONERS) | Skip | Skip | Skip | Skip | Skip |
| 30 | Regular Present | hablar, escuchar, beber, comer, vivir, escribir | 6jpCj97AHMN | Conjugation (present) | Skip | Skip | 5 total | All pronouns for hablar, comer, vivir | Same as 2 |
| 60 | Irregular Present | ser, estar, ir, dar, tener, venir | sD2tovQc7pB | Conjugation (present) | Skip | Skip | 5 total | All pronouns for all verbs | Same as 2 |
| 65 | Irregular Present II | caer, traer, hacer, poner, salir, valer, decir, oir | tPXOw1Rz82y | Conjugation (present) | Skip | Skip | 5 total | 2 random pronouns per verb | Same as 2 |
| 70 | Spelling Changes | conseguir, recoger, dirigir, convencer, conocer, producir, construir, continuar | dYyywu1hOVp | Conjugation (present) | Skip | Skip | 5 total | "yo" + 1 random pronoun per verb | Same as 2 |
| 80 | Present O→UE | mover, almorzar, morir | My2TaOGsmet | Conjugation (present) | Skip | Skip | 5 total | All pronouns for all verbs | Same as 2 |
| 90 | Present E→IE | cerrar, entender | BwvOV8xReZZ | Conjugation (present) | Skip | Skip | 5 total | All pronouns for all verbs | Same as 2 |
| 99 | Present E→I | pedir, repetir | meS3lef4ubp | Conjugation (present) | Skip | Skip | 5 total | All pronouns for all verbs | Same as 2 |
| 120 | Preterite Regular | hablar, encontrar, comer, unir, beber, salir | uBOH6A3vO0U | Conjugation (preterite) | Skip | Skip | 5 total | All pronouns for hablar, comer, salir | Same as 2 |
| 200 | Preterite Highly Irregular | ser, ir, dar, ver, hacer, decir, traer, dormir, morir | Ib68zJ3q7i8 | Conjugation (preterite) | Skip | Skip | 5 total | All pronouns for all verbs | Same as 2 |
| 210 | Gerund | hablar, beber, caminar, charlar, comer, inhibir, prohibir, salir | Xpma6w0jy7m | Conjugation (gerund) | Skip | Skip | 5 total | 1 random pronoun per verb | Same as 2 |
| 220 | Gustar Part 1 | gusta | rfPPtJI9prc | Pronoun+gusta+singular noun | Skip | Skip | 5 total | 5 pronoun+gusta+noun combos | Same as 2 |
| 225 | Gustar Part 2 | gustan | WjOxPPu1uQo | Pronoun+gustan+plural noun | Skip | Skip | 5 total | 5 pronoun+gustan+noun combos | Same as 2 |
| 230 | Gustar Part 3 | gusta, gustan | lIAdqI5fpun | "a + direct object" prefix | Skip | Skip | 5 total | 1 per pronoun type (10 total) | Skip |
| 235 | Ir A + Infinitive | hablar, comer, dormir, vivir, escribir | geHPDI9tMdH | Conjugation (ir a + inf) | Skip | Skip | 5 total | All pronouns for 2 verbs | Same as 2 |

### 0b Drill Patterns

**Standard conjugation drill** (VL 30-235, most situations): Show random pronoun + infinitive, user types correct conjugation. 2 wrong on same item → reveal answer. 2 total fails → rewatch video or restart.

**Grammatical Gender (VL 20)**: Show curated noun + translation, user selects correct article (el/la/un/una). Masculine endings: LONERS (-l, -o, -n, -e, -r, -s) + MAJE (-ma, -je). Feminine endings: DIONZA (-d, -ion, -z, -a).

**Gustar 1 (VL 220)**: English translation + Spanish noun shown, user types indirect object pronoun + "gusta". Nouns from user's mastered/learning words. 2 per pronoun, random order.

**Gustar 2 (VL 225)**: Same as Gustar 1 but plural nouns + "gustan".

**Gustar 3 (VL 230)**: "me gusta el gato" shown, user types "a mi" before it. Each pronoun done twice.

**Ir A + Inf (VL 235)**: Standard drill format but answer is "voy a [infinitive]" etc.

### Phase 2/3 Elicitation Pedagogy

The AI agent creates short, vivid scenarios that naturally require the student to produce the target verb+pronoun combo. It does NOT ask "how do you say X?" — it paints a relatable situation where the student naturally needs the structure. Only falls back to translation if the student doesn't understand the elicitation.

### Special Cases

- **Pronouns (15)**: No conjugation — conversation practices using all pronouns + "su"
- **Grammatical Gender (20)**: Ends after 0b — video + drill only, no conversation phases
- **Gustar (220-230)**: Conversation practices gustar structures, not standard conjugation
- **Gustar Part 3 (230)**: Skips phase 3

### Grammar Word Category

Grammar situation words use `word_category='grammar'` in the database. They do NOT count toward vocab level (which only counts `high_frequency` words with `mastery_level >= 2`).

## Seed Bank (Vocabulary Source of Truth)

All vocabulary lives permanently in the seed bank files:

| File | Contents |
|------|----------|
| `BE/app/data/hf_words.py` | Top 1000 high-frequency Latin American Spanish words |
| `BE/app/data/seed_bank.py` | Encounter words, situations, situation-word links, category names. Imports and re-exports `HIGH_FREQUENCY_WORDS` from `hf_words.py` |
| `BE/app/data/grammar_situations.py` | Grammar situation configs (video IDs, drill types, word workloads) |

The seed script (`scripts/seed_qa.py`) reads from these files and uses `ON CONFLICT DO NOTHING` for idempotent inserts. After the initial seed run, **no re-seeding is needed** — all vocabulary is already in the database. Re-running the seed script is safe (it only adds new entries, never duplicates or overwrites).

To correct existing words, use `ON CONFLICT DO UPDATE` or a one-off SQL migration.
