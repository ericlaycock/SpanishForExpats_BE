# Tense Quest editing policy — safe vs. unsafe content changes

- **Status**: Accepted
- **Date**: 2026-05-14
- **Confirmed by**: Eric
- **Supersedes**: —
- **Superseded by**: —

## Context

Tense Quest derives all of its drills, sentences, and verb charts from
`GRAMMAR_SITUATIONS` (see `docs/tense-quest.md` §"Content derivation"), so
edits to the grammar curriculum *also* edit Tense Quest. That coupling is
intentional — the system has no parallel content store to keep in sync — but
it makes some kinds of edits **silently destructive to existing users' SRS
deck state and coin history**.

Specifically, Tense Quest persists per-user state in four tables (migrations
`038`–`043`) keyed on string IDs that are *positional* in the source data:

- `tense_quest_drill_completions(user_id, drill_id)` — one row per finished drill; counts toward leaderboard.
- `tense_quest_sentence_completions(user_id, drill_id, sentence_id)` — one coin per correct in-drill sentence.
- `tense_quest_cards(user_id, card_key)` — the per-user SRS deck; `card_key = "{drill_id}:{sentence_id}"`. Holds Leitner `box`, `due_at`, `coins_earned`, `reps`, `lapses`.
- `tense_quest_diagnostic(user_id, tense_group_id)` — placement-test result per group; `tense_group_id` is keyed on `_TENSE_GROUP_DEFS` (not on a situation).

The card-lookup path silently drops orphan rows: `_review_deck()` filters out
any card whose `card_key` no longer resolves to a sentence
(`app/api/v1/tense_quest.py:386–414`). That means a destructive edit doesn't
crash — it just makes users' progress disappear with no warning, which is
exactly the failure mode this doc exists to prevent.

This decision codifies which kinds of grammar-data edits are safe, which need
care, and which must never happen without an explicit migration.

## Decision

Content authors editing `app/data/grammar_situations.py` (or the
`_EXTRA_SITUATIONS` table in `app/data/tense_quest.py`) MUST follow the rules
below. Every change is classified by its effect on the four keying surfaces:
**drill_id**, **sentence_id (positional)**, **drill_config.answers**, and
**tense_group_id**.

### ✅ Safe — make these freely

These changes have no effect on existing user state.

| Change | Why safe |
|---|---|
| Edit `title`, `opener_en`, `opener_es`, `video_embed_id`. | No keys depend on these. |
| Edit any `drill_sentences[i].en` field. | English glosses are display-only; no DB column stores them. |
| Edit any `drill_sentences[i].glosses` map. | Display-only. |
| Edit any `intro_chart` content (text bodies, mini-table layouts, recall lists). | No keys depend on these. |
| **Append** a new entry to the end of `drill_sentences`. | Positional `sentence_id` (`s{index}`) is stable for prior entries; new entries get a new `sN`. Adds a new card slot but doesn't disturb existing ones. |
| Add a brand-new grammar situation (new key in `GRAMMAR_SITUATIONS`). | New `drill_id`; nobody has progress on it yet. |
| Bump `grammar_level` of a non-shipped situation (one with no users on it yet). | If migrations / seeds re-derive `order_index` and no SRS state references it, this is free. |

### ⚠️ Care — needs deliberate review

These changes are not destructive on their own but interact with state.

| Change | What to watch | Mitigation |
|---|---|---|
| Edit `drill_sentences[i].es` (Spanish text) for an existing sentence. | The card_key still resolves, but users whose box-3 card had a different Spanish form will see a "new" sentence at next review. Pedagogically neutral; UX may be jarring. | Prefer appending a corrected sentence and marking the old one empty (see "Retire" below) when the change is substantive. |
| Edit `drill_config.answers[verb][pronoun]` for an existing pair. | Future card grading uses the new answer; users mid-deck experience a divergence between what they learned and what's now expected. No data corruption — but they may "fail" a card they remember as correct. | Acceptable for typo fixes (`hablo` ↔ `habló`). For semantic changes (changing the verb entirely), retire the drill — see below. |
| Bump `grammar_level` of a *shipped* situation. | DB `order_index` updates on next seed, but `tense_quest_diagnostic.tense_group_id` is `_TENSE_GROUP_DEFS[].id` (a logical label), not the GL — so diagnostic state survives. However, if the bump moves the situation into or out of a tense group's filter (the `only` substring in `_TENSE_GROUP_DEFS`), the group's drill list changes and `completion_percent` shifts. | OK for splits like GL 20 → 20.5 we shipped in May 2026. Document the bump in the migration's commit message so future readers know users' history maps to the old GL. |
| Rename a `_TENSE_GROUP_DEFS[].id`. | Orphans every row in `tense_quest_diagnostic`. The diagnostic flag silently disappears for affected users. | Don't rename — add a new group and let the old one fall out of `_TENSE_GROUP_DEFS`. |

### 🛑 Forbidden — never do these without a migration

These changes silently destroy user state. Each one needs a dedicated Alembic
migration that either renames keys in the affected tables or explicitly
deletes / replays the stale rows.

| Change | What breaks |
|---|---|
| **Rename a `GRAMMAR_SITUATIONS` key** (drill ID). | Orphans `tense_quest_drill_completions.drill_id`, `tense_quest_sentence_completions.drill_id`, every `tense_quest_cards.card_key` starting with the old ID. Users lose drill credit, sentence-completion coins, and entire SRS cards. |
| **Delete a sentence** from `drill_sentences` (anywhere except the tail, and even there it's risky if it was previously seeded). | Shifts every later `sentence_id`. Every `tense_quest_cards.card_key` keyed to a now-shifted sentence orphans into the wrong sentence (or disappears). |
| **Reorder** `drill_sentences`. | Same as deletion — every position-keyed `sentence_id` now points to a different sentence. |
| **Insert a sentence in the middle** of `drill_sentences`. | Shifts every later `sentence_id` by +1. Same failure mode as deletion. |
| **Delete a grammar situation** that has any user with progress. | Every row in the four TQ tables keyed on its `drill_id` orphans. |

### Safe-edit playbook

Three idioms cover the vast majority of content updates:

1. **Retiring a bad sentence.** Set its `"es"` to `""` (empty string). The
   sentence is filtered out of every read path by `_drill_sentences()`
   (`app/data/tense_quest.py:235`). The positional `sentence_id` stays
   reserved; existing cards keyed to it become unresolvable and are silently
   dropped by `_review_deck()` (`app/api/v1/tense_quest.py:386`). The user
   simply loses that one card; the rest of their deck is untouched.

2. **Replacing a sentence.** Don't edit in place — *append* a corrected
   sentence and retire the bad one per (1). The new sentence gets a fresh
   `sentence_id`; existing cards on the bad one disappear cleanly; new cards
   on the corrected one start at box 1 as if it were a new entry.

3. **Adding a verb / target.** Append to `drill_config.answers` (new key in
   the dict) and `drill_targets`. Both are dict-keyed by verb name, so
   adding a new verb doesn't move anything else. New cards seeded from this
   drill will start mixing in the new verb at the next completion event.

### When you must rename a drill ID

Sometimes a typo or naming-convention drift makes a rename feel unavoidable.
**Do not rename it.** Instead:

- Define a NEW key in `GRAMMAR_SITUATIONS` with the desired ID.
- Mark the old one's `drill_sentences` empty (per playbook (1)) so it stops
  being playable, but leave the key in place so existing users' rows remain
  resolvable.
- Document the alias in a comment near both entries.

The grandfathered users will gradually drain out of the old drill through
review. New users only ever see the new drill.

## Code references

- `app/data/grammar_situations.py:GRAMMAR_SITUATIONS` — the canonical content store. Editing this is editing Tense Quest.
- `app/data/tense_quest.py:_drill_sentences` (~line 235) — filters out empty-`es` sentences. The pressure-release valve that makes the "retire by `es=''`" playbook work.
- `app/data/tense_quest.py:_TENSE_GROUP_DEFS` — `tense_group_id` source of truth for the diagnostic table.
- `app/api/v1/tense_quest.py:_review_deck` (~lines 386–414) — silently drops orphan cards. The mechanism by which destructive edits "look fine" until users notice their decks shrank.
- `app/api/v1/tense_quest.py:_user_points` (~lines 311–320) — aggregates from `tense_quest_drill_completions`, `tense_quest_sentence_completions`, `tense_quest_cards.coins_earned`. Renames of `drill_id` orphan all three sources.
- `app/models/tense_quest.py` — the four tables and their unique constraints. Reference when deciding whether a migration is needed.

## Related docs

- `docs/tense-quest.md` — runtime model, API surface, persistence shape.
- `docs/decisions/grammar-data-shape.md` — gloss invariants and the broader "never rename situation IDs" rule.
