# Monothematic encounters — every encounter in a situation shares one theme

- **Status**: Accepted (resolved — database restructured to comply)
- **Date**: 2026-04-30
- **Confirmed by**: Eric ("definitely sounds historical")
- **Supersedes**: `docs/proposals/monothematic-requirement.md`

## Context

An older version of the database mixed multiple themes within a single situation category (e.g. "Airport" included check-in, security, customs, baggage, etc. as separate encounters under one situation). This made encounter sequencing pedagogically incoherent — a user practicing "checking in" would suddenly be in customs.

## Decision

Every situation must be **monothematic**: all encounters within a situation are about the same theme. Multi-theme categories were split into separate situations, each with its own 50-encounter series.

The restructure has been completed. Current database state is monothematic.

## Code references

- `SpanishForExpats_BE/app/data/seed_bank.py` — situation definitions reflect the monothematic structure.
- (No specific enforcement code — this is a content/data invariant maintained at seed time.)

## Related docs

- `docs/learning-flow.md` — references encounter series and the 1-50 numbering.
- `docs/proposals/monothematic-requirement.md` — the original requirement document, preserved as historical context.
