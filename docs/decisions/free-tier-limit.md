# Free-tier encounter limit = 7

- **Status**: Accepted
- **Date**: 2026-04-30
- **Confirmed by**: Eric
- **Supersedes**: prior 25-encounter limit (referenced in pre-refactor `ARCHITECTURE.md`)

## Context

The free tier needed a sharper paywall to drive subscription conversion. The previous limit of 25 lifetime encounters was too generous; users were completing meaningful learning before being asked to subscribe.

## Decision

Free-tier users get **7 lifetime encounters** before hitting the paywall. After that, the situation start endpoint blocks until the user subscribes.

This is a separate concept from the daily encounter limit (see `docs/decisions/daily-encounter-limit.md`).

## Code references

- `SpanishForExpats_BE/app/services/subscription_service.py:4` — `FREE_ENCOUNTERS_LIMIT = 7`.
- `SpanishForExpats_BE/app/services/subscription_service.py:47-77` — `check_paywall()` enforcement.
- `SpanishForExpats_BE/app/api/v1/situations.py:417-441, 463-497` — endpoints that call `check_paywall()`.

## Related docs

- `docs/learning-flow.md` — describes the free-tier and daily limits side-by-side.
- `docs/decisions/daily-encounter-limit.md` — the per-day cap (separate concept).
