# Vocab module length is owned by the FE — the BE keeps no chapter-count constant

- **Status**: Accepted
- **Date**: 2026-08-13
- **Confirmed by**: Eric (recorded after a production incident)

## Context

The vocab module taxonomy — which modules exist, which words are in each, and
therefore how many 5-word chapters a module has — lives in the frontend at
`SpanishForExpats_FE/components/tensequest/vocabData.ts`, a generated file. The
backend deliberately stores no parallel copy: the FE submits the word list when
it completes a chapter and the BE records what it is told.

That contract was violated by a single constant. `app/api/v1/vocab.py` held:

```python
CHAPTERS_PER_MODULE = 3  # 3 chapters × 5 words = 15-word module cap
```

used only to validate `chapter_idx` on `POST /v1/vocab/chapter/{id}/{idx}/complete`.

It was a second copy of a fact the FE owns, and it drifted. When the vocab decks
grew from 15 words / 3 chapters to 30 words / 6 chapters, every learner who
finished chapter 3 got HTTP 400 on chapter 4 and saw *"Could not save your
progress — try again."* Worse, `ChapterSidebar` unlocks chapter N only once N-1
is recorded as complete, so chapters 5 and 6 became permanently unreachable —
the failure was silent from the backend's perspective and total from the
learner's.

The module docstring had already drifted in the other direction, claiming "the
cap is 25 words = 5 chapters of 5" while the constant said 3. Neither matched
reality. That is the tell: a fact duplicated across two repos will disagree, and
nothing fails loudly when it does.

## Decision

**The backend does not encode how long a vocab module is.** `chapter_idx` is
validated only for structural sanity, not against product policy:

```python
MAX_CHAPTER_INDEX = 200
```

The bound exists to reject negative and absurd indices. It is deliberately far
above any plausible module length so that content growth never requires a
coordinated backend deploy.

Corollaries:

- Do not reintroduce a `CHAPTERS_PER_MODULE`-style constant here.
- Growing a vocab deck is an FE-only change. It needs no BE release.
- If a real per-module limit is ever needed, it must be derived from data the
  BE actually owns, not from a hardcoded mirror of FE content.

## Code references

- `app/api/v1/vocab.py:56` — `MAX_CHAPTER_INDEX = 200`, with the incident recorded inline.
- `app/api/v1/vocab.py:230` — the guard: `if chapter_idx < 0 or chapter_idx > MAX_CHAPTER_INDEX`.
- `app/api/v1/vocab.py:1-14` — module docstring stating the FE owns the taxonomy.
- `tests/test_vocab.py::test_chapters_beyond_the_third_are_accepted` — regression test walking indices 0–5.
- `tests/test_vocab.py::test_absurd_chapter_index_still_rejected` — the bound is relaxed, not removed.
- `SpanishForExpats_FE/components/tensequest/vocabData.ts` — generated; `MAX_CHAPTERS` is derived from the longest module.
- `SpanishForExpats_FE/components/vocab/ChapterSidebar.tsx` — sequential unlock, which is why a rejected index blocks everything after it.

## Related docs

- `docs/learning-flow.md`
- `docs/tense-quest.md`
