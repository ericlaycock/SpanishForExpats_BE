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

Grammar situations use a **configurable multi-phase system**. Each grammar situation has a `phases` config object with boolean flags (e.g., `{ "0a": true, "0b": false, ... }`) that toggles individual phases on/off.

For **conjugation lessons** the runtime flow is:

1. **Intro cards** — multi-step explanation of one rule (text + `mini_table` cards showing pipe-encoded conjugations with crimson endings).
2. **Recall quiz** — driven by the intro_chart's `recall: { verb, answers }` field. The conjugation chart is hidden and the user must type each form from memory before drills begin (`RecallQuiz` in `RuleIntroPhase.tsx`). 2 wrong attempts on a single row resets to the intro card.
3. **Sentence drill** — 10–20 generalizing sentences exercising the rule. Every content word is tap-translatable via the per-sentence `glosses` dict. Alternates between typed (`written`) and audio (`auditory`) prompts.
4. **(optional) Voice chat** — phase 2 conversation companion lesson, attached as a separate `_chat` lesson within the same group block.

| Phase | Name | Description |
|-------|------|-------------|
| 0a | Grammar Video | Descript video embed explaining the grammar concept |
| 0b | Grammar Drills | Intro cards → recall quiz → sentence drill (above). 2 wrong on same drill item → reveal answer. 2 total fails → rewatch video |
| 1a | Learn | (legacy) Typing exercise — user types Spanish word from prompt |
| 1b | Written Test | (legacy) Recall — shows English, user types Spanish from memory |
| 1c | Spoken Test | (legacy) Pronunciation — shows English, user records Spanish |
| 2 | Voice Conversation (hints) | Same as main situations |
| 3 | Voice Conversation (no hints) | Same as main situations |

The frontend phase type is defined as: `type Phase = 'video' | 'drill' | 'learn' | 'written-test' | 'spoken-test'`. Phases 1a-1c are kept for backwards compatibility; conjugation lessons today rely on the 0b drill phase only.

#### Blank-fill drill rendering

For the early grammar units the sentence drill renders as **fill-in-the-blank** instead of "English prompt → type the Spanish": the Spanish sentence shows with the drilled word replaced by a blank slot, the full English translation sits directly below it, and a short instruction sits on top ("Complete the sentence using the correct pronoun" / "…possessive adjective" / "…article" / "…verb form"). The learner reproduces the *whole* Spanish sentence (typed or spoken). This is purely a `DrillPhase.tsx` (`SentenceDrill`) rendering decision keyed off `tense` + `lesson_type` — no backend data change. The blanked token is always at a fixed position in the authored sentences:

| `tense` | `lesson_type` | Units | Blanked token |
|---------|---------------|-------|---------------|
| `pronouns` | `rule` | GL 1 Pronouns (singular + plural) | token 0 (the subject pronoun) |
| `possessive` | `rule` | GL 1.5 Possessive Adjectives | token 0 (the possessive adjective) |
| `gender` | `rule` | GL 2 Grammatical Gender (definite + indefinite) | token 0 (the article) |
| `present` | `conjugation` | GL 3 Regular Present (-AR/-ER/-IR), GL 4 Irregular Present (ser+estar, ir+dar, tener+venir) | token 1 (the conjugated verb) |

Every other drill (e.g. `demonstratives`, `por_para`, gustar, legacy `article_matching`/`conjugation`) keeps the original rendering. Grading for the determiner cases (`pronouns`/`possessive`/`gender`) is an **exact** normalized match — the usual "leading subject pronoun is optional" leniency would let the learner skip the very word being drilled, and `el`/`tu` collide with `él`/`tú` after normalization. Verb-conjugation drills keep the lenient match.

When the learner misses three times on one sentence (or taps "I don't know" three times across the drill), the answer is revealed in place and the screen **waits for a "Try this lesson again" button** rather than flashing the answer and bouncing. Likewise a single "I don't know" reveals the answer and waits for a "Continue" tap — no auto-advance timer.

### Grammar chat lesson invariants

Every grammar chat lesson (`drill_type: "skip"`, `phases.2: True`) MUST satisfy these rules. Many of these regressed in the past — they're load-bearing UX requirements, not stylistic preferences.

1. **Custom opener (no fallback to "How can I help you today?").** Every chat lesson appears in `app/data/grammar_chat_openers.py` with both `opener_es` and `opener_en` and a `scene` field. The opener must use the verbs / patterns drilled in the preceding drill lessons of the same sub-block — that's literally what the user just learned to deploy. **When you add a new chat lesson, you also add an entry to `CHAT_OPENERS` — there is no "TODO add later". Skipping this falls through to the rainforest scene + "How can I help you today?", which is broken UX.**

2. **Real-life scene, never the rainforest.** The default scene `"core"` (Eric in a Latin American rainforest) is for vocab encounters, not grammar chats. Grammar chats MUST set `scene` to one of the situational scenes in `SITUATION_ROLES` — `small_talk` (neighbor), `groceries` (cashier), `restaurant` (waiter), `clothing` (shop assistant), `banking` (teller), `airport` (check-in agent), `mechanic`, `contractor`, `police`, `internet` (technician). Pick the scene where the lesson's verbs would naturally come up: -ER verbs (drink/eat) → restaurant or groceries; reflexive (get up / get dressed) → small_talk; transactional (querer/poder) → groceries; preterite of past events → small_talk.

3. **Word checklist = drilled conjugations, NOT infinitives.** The "Use these words to progress" panel must display a random sample of **8 conjugations from the 2 preceding drill lessons** of the sub-block — e.g. for the AR chat, sample from the AR drill_1 + AR drill_2 drill_targets. Each chip shows the English conjugation (`"you speak"`, `"we eat"`, `"she lives"`) and is detected when the user says the Spanish form. Showing infinitives (`"to speak"`) defeats the lesson — the user just drilled `hablas`/`hablamos`/`hablan`, not `hablar`.

   This is computed at API response time by `get_chat_target_forms(situation_id)`; chat lesson configs do not store the forms statically (they'd drift from the drills).

### Daily Grenade invariants

The daily grenade (`app/services/grenade_service.py`) generates a one-sentence Spanish question using the user's most recently-drilled word.

1. **Vocabulary stays inside `learned_vocab`.** The grenade prompt is given the user's 60 most-recently-touched learned words. Every content word in the generated question must come from this list (plus the target form itself, plus closed-class function words: pronouns, articles, basic prepositions, conjunctions, question words). The LLM is explicitly forbidden from leaning on `gustar + INFINITIVE` or `ir a + INFINITIVE` framings unless `gustar` / `ir` are in the user's learned_vocab.

2. **Conjugated form, never the bare infinitive.** `_pick_grammar_form` returns a conjugated form from the latest drill (with the pipe delimiter stripped). When the target form is somehow an infinitive, the system prompt instructs the LLM to conjugate it for tú itself — never wrap it in another verb's periphrasis.

3. **Cold-open viable.** The grenade is a question dropped on a stranger with no shared context. No demonstratives or possessives that need a referent (`¿Es tu perro?`, `¿Te gusta esto?` — both forbidden). Prefer general / habitual / preference framings (`¿Comes pescado?`, `¿Hablas inglés?`).

### Verb-chart visual invariants

The verb chart looks the **same** in every place it appears — drill_1 intro, drill_2 intro, refresh-time rule_chart, drill-time rule_chart. There is exactly one visual layout for every conjugation table; it never silently degrades.

The canonical layout (`MinimalTable` in `RuleIntroPhase.tsx`, also produced by `RuleChart` `TableView` for conjugation-shaped tables):

- **One mini-table per verb.** A drill that teaches two verbs renders two mini-tables stacked vertically, each titled with the verb and its EN gloss (`"hablar (to speak)"`).
- **5 rows per mini-table**, in this exact order: `yo`, `tú`, `él / ella / usted`, `nosotros / nosotras`, `ellos / ellas / ustedes`.
- **2 columns**: pronoun (left, gray, regular weight) + conjugated form (right, mono font, gray-900). Left-aligned. No center alignment.
- **Endings in crimson** via `ConjugationCell` — the form data is pipe-encoded (`habl|o`); the renderer splits on `|` and applies the crimson Tailwind token to the suffix. Strings without `|` render unchanged.
- **Optional footnote** below the table, italic gray-500.

Tables that aren't pronoun-major conjugation tables (e.g. 4-column reference tables with a "Note" column, or comparison tables) keep their existing flat-row layout; the RuleChart `TableView` heuristically detects conjugation tables (first column header is "Pronoun", remaining columns look like single-word verbs with optional EN gloss in parens) and switches to the mini-table render only for those.

Code paths that must stay aligned:
- `components/grammar/RuleChart.tsx` `TableView` — produces stacked mini-tables for conjugation-shaped data, falls back to flat for everything else.
- `app/[locale]/app/situation/[id]/learn/components/RuleIntroPhase.tsx` `MinimalTable` — same layout for the intro `mini_table` card kind.
- BE: every conjugation lesson populates `intro_chart` AND `rule_chart` (the latter is hidden when intro fires, but is the fallback for refresh users).

### Conjugation lesson invariants

To ensure consistency across grammar groups, every conjugation lesson must satisfy:

- **`word_workload` has at most 2 verbs.** Larger groups are split into sub-blocks (e.g. Irregular Present's 6 verbs split into ser+estar / ir+dar / tener+venir).
### THE GLOSS RULE (universal, no exceptions)

> **Drill sentence glosses cover ONLY nouns, adjectives, and adverbs.**
> **VERB FORMS AND PRONOUNS ARE NEVER GLOSSED. EVER.**

This applies to **every drill sentence in every grammar lesson, regardless of GL, tense, or topic**. There is no exception. If you find existing data that violates this rule, the data is wrong and must be corrected — do not template off of it.

What goes IN a `glosses` dict (each entry bidirectional EN↔ES):
- ✅ Nouns: `"water": "agua", "agua": "water"`, `"trucks": "camiones", "camiones": "trucks"`
- ✅ Adjectives: `"happy": "feliz", "feliz": "happy"`, `"tall": "alto", "alto": "tall"`
- ✅ Adverbs: `"quickly": "rápidamente", "rápidamente": "quickly"`, `"out loud": "en voz alta", "en voz alta": "out loud"`
- ✅ Multi-word noun/adjective/adverb phrases that translate as a unit

What is NEVER in a glosses dict, **without exception**:
- ❌ The conjugated verb being tested (revealing it defeats the drill)
- ❌ ANY other verb form in the sentence — gerunds, infinitives, auxiliaries (haber, ir+a, estar+gerundio, etc.)
- ❌ Copulas in any form (am, is, are, was, were, be, been; soy, eres, es, somos, son, era, fue, sido, …)
- ❌ Subject pronouns (yo, tú, él, ella, usted, nosotros, nosotras, ellos, ellas, ustedes; I, you, he, she, we, they)
- ❌ Object pronouns (me, te, lo, la, le, nos, los, las, les; me, you, him, her, us, them)
- ❌ Reflexive pronouns (me, te, se, nos)
- ❌ Articles (el, la, los, las, un, una; the, a, an)
- ❌ Pure-glue prepositions when they're grammatical (a, de, en, con; to, of, in, with) — unless they're part of a glossable adverbial phrase

Worked examples:
| Sentence | Glosses dict |
|----------|-------------|
| "I love eating cheese" / "Yo amo comer queso" | `{"cheese": "queso", "queso": "cheese"}` |
| "The trucks move quickly" / "Los camiones mueven rápidamente" | `{"trucks": "camiones", "quickly": "rápidamente", "camiones": "trucks", "rápidamente": "quickly"}` |
| "I am tall" / "Yo soy alto" | `{"tall": "alto", "alto": "tall"}` |
| "She lives in Mexico" / "Ella vive en México" | `{"Mexico": "México", "México": "Mexico"}` |
| "We are going to study" / "Vamos a estudiar" | `{}` (empty) — every word is verb/pronoun/article. If a sentence has zero glossable content, that's fine. |

**Why:** the user is being tested on grammar (verb conjugation, agreement, etc.). Glossing the test target leaks the answer; glossing pronouns blunts the conjugation signal. Glosses exist to remove vocabulary friction so the user can focus on the grammar — they are NOT a general-purpose translator.

If you ever find yourself adding a verb form or pronoun to a glosses dict, stop. You are doing it wrong.
- **Every verb-chart intro_chart has a `recall` field** (`{verb, answers}`) referencing the lesson's first verb so the user gets a memory test before sentence drills.
- **Every conjugation form in `mini_table` rows, `rule_chart` cells, and `recall` answers is pipe-encoded** (`stem|ending`) so the FE renders endings in crimson via `ConjugationCell`. Drill `answers` are also pipe-encoded so the live drill VerbChart shows crimson endings too. Total-suppletion forms (`voy`, `soy`) use a leading-pipe (`|voy`) or in-word boundary (`v|oy`) — author by hand, not algorithmic.

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
