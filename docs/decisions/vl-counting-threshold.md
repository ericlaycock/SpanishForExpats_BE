# Vocab Level (VL) counts mastery_level >= 1

- **Status**: Accepted
- **Date**: 2026-04-30
- **Confirmed by**: Eric (existing code, recorded as decision after audit found stale doc claiming `>= 2`)

## Context

Pre-refactor docs disagreed about the VL threshold. `LEARNING_FLOW.md` line 25 said `>= 1`; line 200 of the same file and `ARCHITECTURE.md` line 294 said `>= 2`. Code is authoritative.

## Decision

Vocab Level (VL) is the count of `UserWord` rows where:
- `Word.word_category = 'high_frequency'`, AND
- `UserWord.mastery_level >= 1` (i.e. the user has learned the word at least once, even if not yet refreshed).

Grammar-category words do NOT count toward VL.

## Code references

- `SpanishForExpats_BE/app/api/v1/situations.py:164-170` — `get_vocab_level()`:
  ```python
  return db.query(UserWord).join(Word).filter(
      UserWord.user_id == user_id,
      Word.word_category == 'high_frequency',
      UserWord.mastery_level >= 1,
  ).count()
  ```

## Related docs

- `docs/learning-flow.md` — VL/GL gating, mastery SRS.
