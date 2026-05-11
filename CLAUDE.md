# Spanish for Expats — Backend Context

> This file is auto-loaded by Claude when working in this directory.
> It serves two purposes: **(1)** it is the canonical project-context index for the whole project (BE + FE), and **(2)** it is the backend-specific file map. The project-context sections below are the same for everyone working on this codebase, regardless of which repo they're in.

---

# Project Context (canonical — applies to BE + FE)

## Project Layout

- `SpanishForExpats_BE/` — FastAPI backend (this repo). **Hosts the canonical `docs/` tree** at `docs/` so it deploys with the backend.
- `SpanishForExpats_FE/` — Next.js frontend (separate git repo, typically cloned as a sibling directory).
- `assets/` (Eric's local only) — experimental scripts and venvs, not deployed and not in any git repo.

## Documentation Map

> Update this table when you create, rename, or significantly change a doc. Keep summaries to one line.

| Document | Scope |
|----------|-------|
| `SpanishForExpats_BE/CLAUDE.md` (this file) | Project context index + backend file map. Auto-loaded in BE. |
| `SpanishForExpats_FE/CLAUDE.md` | Frontend file map, hooks, patterns. Auto-loaded in FE. Defers to this file for project-wide context. |
| `docs/architecture.md` | System architecture, infra, data model, auth, logging. |
| `docs/api-contracts.md` | HTTP API surface — single source of truth for routes/schemas. (Phase 2 — not yet created.) |
| `docs/learning-flow.md` | Phase model, mastery SRS, VL/GL gating, language modes, free-tier + daily limits. |
| `docs/grammar-curriculum.md` | Grammar group structure, lesson pattern, drill anatomy. (Phase 2 — not yet created.) |
| `docs/voice-chat.md` | **UPDATE FREQUENTLY** STT/TTS/LLM pipeline, R2, animation, realtime flag. |
| `docs/tense-quest.md` | Tense Quest mini-game (`/tensequest`): derived content, leaderboard, SRS review deck, API, tables. |
| `docs/design-system.md` | Brand identity, palette (`#28968C`), typography, component guidelines. |
| `docs/env-variables.md` | All FE + BE environment variables. |
| `docs/testing.md` | CI, pytest, vitest, Playwright. |
| `docs/decisions/` | Durable confirmed product/architecture decisions — authoritative for **intent**. |
| `docs/proposals/` | Speculative or historical docs — NEVER authoritative. |

> Paths above are relative to this repo (`SpanishForExpats_BE/`). From the FE repo, prepend `../SpanishForExpats_BE/`. From a parent project directory, prepend `SpanishForExpats_BE/`.

## Conflict-Resolution Order

The hierarchy distinguishes **what currently runs** from **what should run**.

**For "what currently runs":** source code → `docs/voice-chat.md` (UPDATE FREQUENTLY) → `docs/<topic>.md` → auto-loaded `CLAUDE.md` files.

**For "what should run":** `docs/decisions/<topic>.md` → `docs/<topic>.md` (intended model). `docs/proposals/*` is never authoritative.

**When code and an accepted decision disagree:** flag the mismatch explicitly in the relevant `docs/<topic>.md` (e.g. "Data migration needed" callout). Do NOT silently document code-as-is as if it were intended. Cross-link the decision and the runtime gap.

## Working Discipline

When you change code that affects business logic, update the relevant `docs/<topic>.md` in the same PR. When the user makes a new product/architecture call, capture it in `docs/decisions/<topic>.md` immediately so future agents inherit the intent. Auto-loaded `CLAUDE.md` files are indexes, not encyclopedias — depth lives in `docs/`.

**Significant FE changes require Playwright + screenshot verification before they are reported as done.** "Done" means: pushed to qa, QA preview redeployed, and a Playwright run captured the change rendering correctly from the user's perspective. Until those screenshots exist, assume the change is broken — even if the code compiles, tests pass, and the commit is on origin/qa. Backend data + FE render are two separate systems; a BE field that the FE conditionally hides is invisible to the user, and only an actual screenshot proves otherwise. This rule exists because of the chart/drill mismatch fix where the BE was correct but a `hideRuleChart={Boolean(introChart)}` flag silently suppressed the user-visible payload — and the regression went out unnoticed until a screenshot run caught it. Significant = anything touching what the user sees, hears, or interacts with on a screen the user actually visits. Trivial copy tweaks, dev-only logging, and admin-only surfaces are exempt.

For grammar-curriculum work specifically, the canonical verification harness is `SpanishForExpats_FE/scripts/grammar-pdf-generate.mjs` + `grammar-pdf-shrink.mjs` — they walk every lesson on QA, screenshot every slide / recall / drill, and assemble a single PDF (`/home/eric/Code/spanishforexpats/grammar_curriculum.pdf`) that the user reviews to spot regressions. Use it; do not reinvent.

## Git Workflow

- Always commit to `qa`, never `main` directly.
- Always add + commit + push after a change.
- `qa` → Railway QA + Vercel preview. `main` → production via PR after CI.
- Backend tests: `pytest` (Postgres required). Frontend tests: `vitest`.

## Tech Stack (one-line)

FastAPI (Python 3.11) + PostgreSQL on Railway · Next.js 16 + React 19 + TypeScript + Tailwind + shadcn/ui · OpenAI GPT-4.1-mini / Whisper / TTS · JWT auth · Better Stack logging.
Full details in `docs/architecture.md`.

## Key Concepts (terminology only — semantics live in `docs/learning-flow.md`)

- **Situation**: Real-world scenario the user learns through (banking, airport, etc.).
- **Encounter**: One run-through of a situation. Series typically 1-50 per situation.
- **Encounter words / High-frequency words**: Two word categories per encounter.
- **Vocab Level (VL) / Grammar Level (GL)**: Progress trackers that gate content.
- **Mastery levels (0-4)**: SRS-driven word progression.
- **Grammar group**: Topic (e.g. Present Tense Regular) containing alternating `[1-2 drill][1 chat]` lessons.

---

# Backend-Specific Context

## Quick Reference

- **Framework**: FastAPI (Python 3.11), Uvicorn
- **Database**: PostgreSQL (Railway), SQLAlchemy 2.0, Alembic migrations
- **Auth**: JWT via python-jose, bcrypt passwords
- **AI**: OpenAI GPT-4.1-mini (chat), Whisper (STT), TTS
- **Tests**: pytest (requires PostgreSQL — not SQLite-compatible due to UUID/JSONB)

## Key Files

| File | Purpose |
|------|---------|
| `app/main.py` | FastAPI app, lifespan, CORS, router registration |
| `app/config.py` | Pydantic Settings (DATABASE_URL, OPENAI_API_KEY, JWT_SECRET, mastery_spoken_threshold) |
| `app/models.py` | All SQLAlchemy models (User, Word, Situation, UserWord, Conversation, etc.) |
| `app/schemas.py` | Pydantic request/response schemas |
| `app/database.py` | Engine, SessionLocal, `get_db()` dependency |
| `app/auth.py` | JWT create/verify, password hashing, `get_current_user()` |

## API Routes (`app/api/v1/`)

| Module | Prefix | Key Endpoints |
|--------|--------|---------------|
| `auth.py` | `/v1/auth` | register, login |
| `situations.py` | `/v1/situations` | list, detail, start, complete, next, daily-usage, admin/ai-logs |
| `conversations.py` | `/v1/conversations` | create, voice-turn |
| `user_words.py` | `/v1/user/words` | get words, unknown words, typed-correct |
| `onboarding.py` | `/v1/onboarding` | status, save-selections, available-categories |
| `subscription.py` | `/v1/subscription` | status |
| `tense_quest.py` | `/v1/tensequest` | overview, groups/{id}, drills/{id}, drills/{id}/complete, review (+attempt/shuffle), transcribe — see `docs/tense-quest.md` |

## Services (`app/services/`)

| Service | Purpose |
|---------|---------|
| `word_selection_service.py` | Selects encounter + high-frequency words for a situation |
| `voice_turn_service.py` | Orchestrates STT → word detection → LLM → TTS pipeline |
| `conversation_service.py` | Word stat updates, mastery checks, completion detection |
| `word_detection.py` | Deterministic word matching in user text/transcript |
| `llm_gateway.py` | OpenAI chat completions wrapper |
| `openai_media_gateway.py` | Whisper STT + TTS wrapper |
| `subscription_service.py` | Free tier limit checking (25 encounters) |
| `daily_encounter_service.py` | 30/day encounter limit checking and recording |

## Patterns

- **Dependency injection**: `Depends(get_db)` for DB sessions, `Depends(get_current_user)` for auth
- **Upserts**: UserWord uses PostgreSQL `ON CONFLICT DO UPDATE`
- **Locking**: `.with_for_update()` on conversation lookups to prevent races
- **Mastery**: `spoken_correct_count >= settings.mastery_spoken_threshold` (default 2)
- **Word selection**: 3 encounter + 2 high-frequency per situation, ordered by frequency_rank

## Admin Analytics

- `GET /v1/situations/admin/ai-logs` — Admin-only endpoint returning aggregate TTS/STT/LLM latency stats (avg/min/max/count per model) plus recent 20 TTS and 20 STT calls with details (format, latency, errors). Useful for monitoring whisper-1 fallback rate and TTS performance.
- AI request logging tables: `llm_requests`, `stt_requests`, `tts_requests` (defined in `app/models/ai_requests.py`)
- Initial message TTS is cached in-memory by `(situation_id, alt_language)` in `conversations.py` — clears on deploy

## Database

- Migrations: `alembic upgrade head` (auto-runs on startup if `AUTO_MIGRATE=true`)
- QA seed: `scripts/seed_qa.py` (auto-runs when `ENVIRONMENT=qa`)
- Key constraint: `CheckConstraint` on UserWord.status ('learning'/'mastered'), Conversation.mode ('text'/'voice'), Conversation.status ('active'/'complete')
