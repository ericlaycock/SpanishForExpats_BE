# Tense Quest

> A standalone verb-conjugation mini-game. FE route `/tensequest`. Reuses the
> grammar curriculum as content (no new linguistic data) and adds a game layer:
> tense-group progress, an activity leaderboard, and an SRS review deck.

## What it is

A pixel-art (2D, quirky) game for intermediate learners that drills verb
conjugation across every verb-tense topic in the curriculum:

- **Main screen** (`/tensequest`): an activity **leaderboard** on the left, a
  scrollable grid of **tense-group tiles** in the middle (each tile shows its
  green-fill progress = drills completed / drills in the group), and a
  **Review Stack** on the right with a **Shuffle** button.
- **A quest** (click a tile → it serves the group's next unfinished drill):
  1. **Warmup** — verb rules + one or two verb charts, then a conjugation drill
     (~10 verb×pronoun prompts in **randomised order**, deterministic matching;
     on-screen accent bar; hint button). No "show translation" toggle here.
  2. **Generalize** — 10 sentences, response mode alternating **type** / **speak**
     (Whisper STT for the spoken ones, biased to the target sentence). Player
     produces the Spanish; graded by accent/case-insensitive fuzzy match against
     the known target. A **"show translation"** toggle (persisted in
     `localStorage`) reveals each sentence's `blank_es` scaffold — the Spanish
     sentence with the conjugated verb shown as `____`. **"Re-read the rules"**
     pops the rules/charts up in an overlay *without* restarting the warmup.
  3. **Complete** — celebration animation → **+1 coin** (coin = leaderboard
     point; the coin bar is visible on every Tense Quest screen) → the drill's
     **practice sentences** are added to the review deck → back to the main
     screen, tile fills further.
- **Review Stack (SRS)**: each card is one **practice sentence** (`{drill_id}:{sentence_id}`),
  inheriting that sentence's `type`/`speak` mode and the same `blank_es`
  scaffold under the "show translation" toggle. Reviewing is **timed
  client-side**: `<5s` = "very good" (box +2), `<10s & correct` = pass (box +1),
  `>10s` **or** wrong = a **lapse** — and the `>10s` lapse is *silent* (the UI
  still shows "correct!" if the answer matched, but internally the card resets to
  box 1 and resurfaces ~10 min later). **Shuffle** randomizes `deck_position`
  (the flip-through order). Due cards always surface before non-due ones, so
  recently-failed cards float up.

## Content derivation (no new content)

`app/data/tense_quest.py` derives everything from
`app.data.grammar_situations.GRAMMAR_SITUATIONS`:

- A **tense group** = a grammar level (GL) that has ≥1 playable drill. The set +
  display titles/blurbs/families are in `_TENSE_GROUP_DEFS` (~26 tiles across
  Present, Near Future & Modals, The Past, Future & Conditional, and
  Commands·-ing·Subjunctive). Non-verb GLs (pronouns, gender, por/para, object
  pronouns, gustar-only) are excluded. A GL can feed several tiles via an `only`
  drill-id substring filter (e.g. GL 20 splits into "Present Subjunctive" /
  "Imperfect Subjunctive").
- A **drill** = one grammar *situation* in that GL. Conjugation drills
  (`drill_type` `conjugation`/`ir_a_inf`, ≥4 `drill_sentences`) get the full
  rules → verb-chart warmup → sentences flow; a `rule`-type drill with an
  intro_chart (e.g. Preterite vs. Imperfect) becomes a rules-then-sentences
  quest with no conjugation warmup.
- **Hand-authored extras** (`_EXTRA_SITUATIONS`, accessed via `_situation()`):
  a couple of tenses the curriculum has no lesson for yet — currently the
  "Perfect — Irregular Participles" module (synthetic `grammar_level` 18.6).
  Shaped exactly like a `GRAMMAR_SITUATIONS` conjugation lesson; replace with a
  real lesson when one lands. Forms in extras and reference charts are pipe-
  encoded so the changing part renders red.
- **Verb charts** are built straight from the drill's `drill_config.answers`
  (5-row pronoun grouping). **Rule cards** are the `text`/`rule_pack` cards from
  the lesson's `intro_chart` (with a generic fallback). **Conjugation targets**
  use the lesson's authored `drill_targets`, falling back to a varied sample.
  Forms keep the `|` stem/ending pipe for display; the FE strips it for matching.
- **Sentences** get a stable `id` (`s{index}` over the es-non-empty list) and a
  `blank_es` — the `es` with the conjugated-verb span (1–3 words) located via the
  drill's `drill_config.answers` and replaced by `____` (null when not locatable;
  ~20 of ~1200 sentences). `blank_es` backs the "show translation" scaffold.

If the underlying grammar data changes, Tense Quest changes with it — that's the
point. Drill ids are grammar situation ids (stable per the "never rename situation
ids" rule); sentence ids are positional within a drill. `card_key` is
`"{drill_id}:{sentence_id}"`; tense-group ids (in `_TENSE_GROUP_DEFS`) are stable.

## API (`/v1/tensequest/*`, all auth-required)

| Method & path | Purpose |
|---|---|
| `GET /overview` | Tense groups + progress, activity leaderboard (top 10 + you), review deck (due-first), your coin total. |
| `GET /groups/{group_id}` | Group detail: ordered drills + completion, `next_drill_id`, `all_complete`. |
| `GET /drills/{drill_id}` | Quest payload: rule cards, verb charts, conjugation targets, 10 alternating sentences (each with `en`/`es`/`blank_es`/`glosses`/`response_mode`). |
| `POST /transcribe` | Thin Whisper STT proxy (multipart `audio` + `expected_text`) for the spoken-sentence phase (quest + review). |
| `POST /drills/{drill_id}/complete` | Records completion (idempotent), mints a coin, seeds the drill's **practice sentences** into the deck. Returns updated progress/coins/deck size + `next_drill_id`. |
| `GET /review` | The review deck — sentence cards, due-first, capped. Each: `card_key`, `tense_group_id/title`, `tense_label`, `en`, `es`, `blank_es`, `glosses`, `response_mode`, `box`, `due`. |
| `POST /review/attempt` | `{card_key, correct, response_ms}` → applies the SRS transition. Returns `{result, box}`. |
| `POST /review/shuffle` | Randomizes `deck_position` for all your cards. |

Grading is **deterministic and FE-side** (mirrors the grammar-drill matcher);
the BE only records outcomes — the same split the rest of the app uses for
grammar drills. No LLM is involved anywhere in Tense Quest.

## Persistence

Two tables (migrations `038_tense_quest`, `039_tq_sentence_cards`):

- `tense_quest_drill_completions` — one row per `(user, drill)`; row count == the
  user's coin total (= leaderboard points).
- `tense_quest_cards` — the per-user SRS deck of **sentence cards**.
  `card_key = "{drill_id}:{sentence_id}"`, plus `tense_group_id`, `drill_id`,
  `sentence_id`, Leitner `box` 1..5, `due_at`, `deck_position` (Shuffle target),
  `last_result`, `last_response_ms`, `reps`, `lapses`. The sentence's text is
  resolved on read from the grammar data (`tq.lookup_sentence`), not stored.

SRS transitions live in `app/services/tense_quest_srs.py`
(`FAST_MS=5000`, `SLOW_MS=10000`, `LAPSE_MINUTES=10`, `BOX_INTERVAL_HOURS`).

## Files

- BE: `app/data/tense_quest.py`, `app/models/tense_quest.py`,
  `app/services/tense_quest_srs.py`, `app/api/v1/tense_quest.py`,
  `migrations/versions/{038_tense_quest,039_tq_sentence_cards}.py`,
  tests in `tests/test_tense_quest.py`.
- FE: `app/[locale]/tensequest/` (page + `[groupId]` runner + `layout.tsx` +
  `tensequest.css` scoped pixel theme), `components/tensequest/*` (incl.
  `AccentBar`, `CoinBar`, `StudyContent`), `lib/api/tensequest.ts`,
  `lib/queries/tenseQuest.ts` + `lib/mutations/tenseQuest.ts`.
