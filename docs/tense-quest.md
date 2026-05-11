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
     (~10 verb×pronoun prompts, deterministic matching).
  2. **Generalize** — 10 sentences, response mode alternating **type** / **speak**
     (Whisper STT for the spoken ones, biased to the target sentence). Player
     produces the Spanish; graded by accent/case-insensitive fuzzy match against
     the known target (same matcher as the grammar drill).
  3. **Complete** — celebration animation → **+1 leaderboard point** → the
     drill's conjugation cards are added to the review deck → back to the main
     screen, tile fills further.
- **Review Stack (SRS)**: each card is a `(group, verb, pronoun)` conjugation
  prompt. Reviewing is **timed client-side**: `<5s` = "very good" (box +2),
  `<10s & correct` = pass (box +1), `>10s` **or** wrong = a **lapse** — and the
  `>10s` lapse is *silent* (the UI still shows "correct!" if the spelling was
  right, but internally the card resets to box 1 and resurfaces ~10 min later).
  **Shuffle** randomizes `deck_position` (the flip-through order). Due cards
  always surface before non-due ones, so recently-failed cards float up.

## Content derivation (no new content)

`app/data/tense_quest.py` derives everything from
`app.data.grammar_situations.GRAMMAR_SITUATIONS`:

- A **tense group** = a grammar level (GL) that has ≥1 playable conjugation
  drill. The set + display titles/blurbs/families are in `_TENSE_GROUP_DEFS`.
  Currently ~23 groups across families: Present, Near Future & Modals, The Past,
  Future & Conditional, and Commands·-ing·Subjunctive. Non-verb GLs (pronouns,
  gender, por/para, object pronouns, gustar-only, virtual GLs) are excluded.
- A **drill** = one grammar *situation* in that GL whose `drill_type` is
  `conjugation` or `ir_a_inf` and which has ≥4 `drill_sentences`.
- **Verb charts** are built straight from the drill's `drill_config.answers`
  (5-row pronoun grouping). **Rule cards** are the `text`/`rule_pack` cards from
  the lesson's `intro_chart` (with a generic fallback). **Conjugation targets**
  use the lesson's authored `drill_targets`, falling back to a varied sample.
  Forms keep the `|` stem/ending pipe for display; the FE strips it for matching.

If the underlying grammar data changes, Tense Quest changes with it — that's the
point. Tense-group **ids are stable** (used as `card_key` prefixes); don't rename
them. Drill ids are grammar situation ids (also stable per the "never rename
situation ids" rule).

## API (`/v1/tensequest/*`, all auth-required)

| Method & path | Purpose |
|---|---|
| `GET /overview` | Tense groups + progress, activity leaderboard (top 10 + you), review deck (due-first), your point total. |
| `GET /groups/{group_id}` | Group detail: ordered drills + completion, `next_drill_id`, `all_complete`. |
| `GET /drills/{drill_id}` | Quest payload: rule cards, verb charts, conjugation targets, 10 alternating sentences. |
| `POST /transcribe` | Thin Whisper STT proxy (multipart `audio` + `expected_text`) for the spoken-sentence phase. |
| `POST /drills/{drill_id}/complete` | Records completion (idempotent), awards a point, seeds the drill's cards into the deck. Returns updated progress/points/deck size + `next_drill_id`. |
| `GET /review` | The review deck (due-first, capped). |
| `POST /review/attempt` | `{card_key, correct, response_ms}` → applies the SRS transition. Returns `{result, box}`. |
| `POST /review/shuffle` | Randomizes `deck_position` for all your cards. |

Grading is **deterministic and FE-side** (mirrors the grammar-drill matcher);
the BE only records outcomes — the same split the rest of the app uses for
grammar drills. No LLM is involved anywhere in Tense Quest.

## Persistence

Two tables (migration `038_tense_quest`):

- `tense_quest_drill_completions` — one row per `(user, drill)`; row count == the
  user's leaderboard points.
- `tense_quest_cards` — the per-user SRS deck. `card_key = "{group}:{verb}:{pronoun}"`,
  Leitner `box` 1..5, `due_at`, `deck_position` (Shuffle target), `last_result`,
  `last_response_ms`, `reps`, `lapses`.

SRS transitions live in `app/services/tense_quest_srs.py`
(`FAST_MS=5000`, `SLOW_MS=10000`, `LAPSE_MINUTES=10`, `BOX_INTERVAL_HOURS`).

## Files

- BE: `app/data/tense_quest.py`, `app/models/tense_quest.py`,
  `app/services/tense_quest_srs.py`, `app/api/v1/tense_quest.py`,
  `migrations/versions/038_tense_quest.py`, tests in `tests/test_tense_quest.py`.
- FE: `app/[locale]/tensequest/` (page + `[groupId]` runner),
  `components/tensequest/*`, `lib/api/tensequest.ts`,
  `lib/queries/tenseQuest.ts` + `lib/mutations/tenseQuest.ts`,
  `app/tensequest.css` (scoped pixel theme), `messages/en/tensequest.json`.
