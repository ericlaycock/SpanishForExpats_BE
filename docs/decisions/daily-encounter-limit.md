# Daily encounter limit = 30/day

- **Status**: Accepted
- **Date**: 2026-04-30
- **Confirmed by**: Eric (existing code, recorded as decision)

## Context

Even subscribed users can over-grind in a single day, which is bad for retention and bad for spaced-repetition learning. A daily cap encourages spread-out practice.

## Decision

All users (free and paid) are capped at **30 encounters per calendar day**. The cap is independent of the lifetime free-tier limit (`docs/decisions/free-tier-limit.md`).

When the cap is reached, `POST /v1/situations/{id}/start` returns HTTP 429.

## Code references

- `SpanishForExpats_BE/app/services/daily_encounter_service.py:5` — `DAILY_ENCOUNTER_LIMIT = 30`.
- `SpanishForExpats_BE/app/services/daily_encounter_service.py:24-29` — `check_daily_limit()`.
- `SpanishForExpats_BE/app/api/v1/situations.py:489-496` — enforcement at `start_situation`, returns 429.

## Related docs

- `docs/learning-flow.md`
- `docs/decisions/free-tier-limit.md`
