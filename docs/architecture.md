# Spanish for Expats - Architecture & Technical Reference

> **Last Updated**: March 2026
> Technical documentation for the Spanish for Expats codebase.
> For design/brand guidelines, see `design-system.md` (sibling).

---

## Table of Contents

1. [System Overview](#system-overview)
2. [Infrastructure](#infrastructure)
3. [Backend Architecture](#backend-architecture)
4. [Frontend Architecture](#frontend-architecture)
5. [Data Model](#data-model)
6. [API Surface](#api-surface)
7. [Authentication Flow](#authentication-flow)
8. [Core Business Logic](#core-business-logic)
9. [Logging & Observability](#logging--observability)
10. [Known Technical Debt](#known-technical-debt)

---

## System Overview

Spanish for Expats is a Spanish survival language learning app that teaches through real-world situational encounters. Users progress through situations (e.g., banking, groceries, airport), learning target vocabulary via a 3-phase learning flow (flashcards, typed quiz, spoken quiz) before engaging in AI voice conversation.

```
                    +------------------+
                    |   Next.js 16     |
                    |   (Vercel/etc)   |
                    +--------+---------+
                             |
                        HTTPS/REST
                             |
                    +--------+---------+
                    |   FastAPI        |
                    |   (Railway)      |
                    +--------+---------+
                             |
              +--------------+--------------+
              |              |              |
     +--------+--+   +------+------+  +----+--------+
     | PostgreSQL |   | OpenAI API  |  | Better Stack |
     | (Railway)  |   | GPT/STT/TTS |  | (Logging)    |
     +------------+   +-------------+  +-------------+
```

### Tech Stack Summary

| Layer          | Technology                                              |
|----------------|---------------------------------------------------------|
| Frontend       | Next.js 16.1.6, React 19, TypeScript, Tailwind CSS 3.4  |
| UI Components  | shadcn/ui (Radix UI primitives), Lucide icons           |
| Backend        | FastAPI (Python 3.11), Uvicorn                          |
| Database       | PostgreSQL (Railway-managed), SQLAlchemy 2.0, Alembic   |
| Auth           | JWT (python-jose), bcrypt password hashing              |
| AI Services    | OpenAI GPT-4.1-mini (chat), Whisper (STT), TTS           |
| Infrastructure | Railway (backend + DB), Docker                          |
| Logging        | Better Stack (structured JSON log shipping via httpx)    |
| Validation     | Pydantic v2 (backend), Zod + React Hook Form (frontend) |

---

## Infrastructure

### Railway

The backend and PostgreSQL database are both hosted on Railway.

- **Backend service**: FastAPI app running via Uvicorn
- **Database**: Railway-managed PostgreSQL instance
- **Environment variables** (set in Railway dashboard):
  - `DATABASE_URL` - PostgreSQL connection string (provided by Railway)
  - `OPENAI_API_KEY` - OpenAI API key
  - `JWT_SECRET` - Secret for signing JWT tokens
  - `BETTERSTACK_HOST` - Better Stack log ingestion host
  - `BETTERSTACK_TOKEN` - Better Stack auth token
  - `AUTO_MIGRATE` - Set to `"true"` to run Alembic migrations on startup
  - `RELEASE_SHA` - Git commit SHA (for log tagging)
  - `ENVIRONMENT` / `RAILWAY_ENVIRONMENT` - Deployment environment name
  - `NEXT_PUBLIC_API_URL` - Backend URL for the frontend

- **Startup behavior** (`main.py` lifespan):
  1. Tests DB connection with retries (5 attempts, 3s delay)
  2. If `AUTO_MIGRATE=true`, runs `alembic upgrade head`
  3. If migrations fail and no tables exist, falls back to `Base.metadata.create_all()`
  4. Registers all API routers

- **Endpoints for health/wake**:
  - `GET /health` - Health check
  - `GET /wakeup` - Wake sleeping Railway apps

### Deployment Pipeline

#### Branching Strategy

- `main` branch → Production (Railway + Vercel)
- `qa` branch → QA environments (Railway QA + Vercel preview)
- Development happens on `qa`. Merge to `main` via PR after tests pass.

#### Environments

| Environment | Backend | Frontend | Database |
|-------------|---------|----------|----------|
| Production | Railway (main branch) | Vercel (main branch) | Railway PostgreSQL (prod) |
| QA | Railway QA env (qa branch) | Vercel preview (qa branch) | Railway PostgreSQL (qa) |

#### CI/CD (GitHub Actions)

- **On push to `qa`**: Runs backend tests (pytest) and frontend tests (vitest + lint + build)
- **On PR to `main`**: Same tests run as a merge gate. Tests must pass before merge is allowed.
- Backend CI spins up a PostgreSQL service container for tests.
- Frontend CI runs lint, vitest, and a production build check.

#### QA Database

- QA database starts fresh each deployment (not a copy of production)
- `alembic upgrade head` runs all migrations from scratch
- `scripts/seed_qa.py` populates reference data (words, situations) and a test user. Data sourced from seed bank files: `app/data/seed_bank.py` (encounter words, situations), `app/data/hf_words.py` (1000 HF words), `app/data/grammar_situations.py` (grammar configs)
- Seed script runs automatically when `ENVIRONMENT=qa` (via `start.py`)
- Uses `ON CONFLICT DO NOTHING` — safe to re-run, never duplicates. After initial seed, no re-seeding needed
- Test credentials: `qa@test.com` / `testpassword123`

#### Test Suite

**Backend** (pytest): API endpoint tests for auth, situations, onboarding, user_words, subscription. Unit tests for word_selection_service. Does NOT test OpenAI integration (mocked/skipped).

**Frontend** (vitest): API client logic tests, component render tests, lint and build checks.

### Better Stack (Logging)

Structured JSON logs are shipped to Better Stack asynchronously via `httpx.AsyncClient`:

- **Module**: `app/core/betterstack.py`
- Uses a singleton `httpx.AsyncClient` with 1.5s timeout
- Fire-and-forget: errors are silently swallowed to avoid crashing the app
- Large payloads (transcripts, audio bytes, full JSON) are stripped before shipping
- `schedule_ship_log()` creates an `asyncio.Task` if an event loop is running

### CORS

CORS is handled via three layers (overly redundant, see tech debt):
1. FastAPI `CORSMiddleware` with `allow_origin_regex=r".*"`
2. A custom `@app.middleware("http")` that adds `Access-Control-Allow-Origin: *` to every response
3. Manual CORS headers in every exception handler response
4. Explicit `OPTIONS /{path}` handler

---

## Backend Architecture

### Directory Structure

```
SpanishForExpats_BE/
├── app/
│   ├── main.py              # FastAPI app, lifespan, CORS, exception handlers, router registration
│   ├── config.py            # Pydantic Settings (env vars: DATABASE_URL, OPENAI_API_KEY, JWT_SECRET)
│   ├── database.py          # SQLAlchemy engine, SessionLocal, get_db(), test_connection()
│   ├── auth.py              # JWT creation/verification, password hashing, create_user()
│   ├── models.py            # SQLAlchemy ORM models (User, Subscription, Word, Situation, etc.)
│   ├── schemas.py           # Pydantic request/response schemas
│   ├── dependencies.py      # FastAPI Depends() helpers (get_current_user)
│   ├── api/v1/
│   │   ├── auth.py          # POST /register, POST /login
│   │   ├── subscription.py  # GET /status
│   │   ├── situations.py    # GET /, GET /selected, GET /{id}, POST /{id}/start, POST /{id}/complete, POST /{id}/next
│   │   ├── conversations.py # POST /, POST /{id}/voice-turn
│   │   ├── user_words.py    # GET /, GET /unknown, POST /typed-correct
│   │   ├── onboarding.py    # POST /save-selections, GET /status, GET /available-categories
│   │   └── logs.py          # POST / (frontend log relay)
│   ├── services/
│   │   ├── llm_gateway.py           # OpenAI chat completions wrapper (GPT-4.1-mini)
│   │   ├── openai_media_gateway.py  # Whisper STT + TTS wrapper
│   │   ├── openai_service.py        # Higher-level OpenAI helpers (grading, chat)
│   │   ├── conversation_service.py  # Word stat updates, completion checks
│   │   ├── word_detection.py        # Detect target words in user transcript text
│   │   ├── encounter_messages.py    # Hardcoded initial messages per encounter category
│   │   └── subscription_service.py  # Free tier limit checking (25 encounters)
│   ├── core/
│   │   ├── logger.py         # log_event() - structured logging + Better Stack shipping
│   │   ├── betterstack.py    # Async HTTP client for Better Stack log ingestion
│   │   └── request_utils.py  # Extract user_id/request_id from Request objects
│   ├── middleware/
│   │   ├── request_id.py     # Injects X-Request-Id header if missing
│   │   └── request_logging.py # Logs request/response metadata
│   ├── utils/
│   │   └── audio.py          # Audio format conversion helpers
│   └── prompts/              # JSON prompt templates for LLM system messages
├── migrations/
│   └── versions/             # Alembic migration scripts
├── scripts/                  # Data management scripts
├── requirements.txt
├── Dockerfile
└── alembic.ini
```

### Key Patterns

- **No service layer abstraction**: Route handlers in `api/v1/` directly query SQLAlchemy. Business logic is mixed into endpoints.
- **Dependency injection**: FastAPI `Depends()` for `get_db()` (DB session) and `get_current_user()` (JWT auth).
- **OpenAI integration**: Two gateway modules — `llm_gateway.py` for chat completions, `openai_media_gateway.py` for STT/TTS.
- **Database sessions**: Created per-request via `get_db()` generator, auto-closed in `finally`.

---

## Frontend Architecture

### Directory Structure

```
SpanishForExpats_FE/
├── app/                              # Next.js App Router
│   ├── layout.tsx                    # Root layout (Montserrat font, ThemeProvider)
│   ├── login/page.tsx                # Login form
│   ├── register/page.tsx             # Registration form
│   ├── onboarding/
│   │   ├── page.tsx                  # Multi-step onboarding wizard (~1150 lines)
│   │   └── quiz-data.ts             # Grammar/vocab quiz tree
│   ├── page.tsx                      # Home dashboard (~418 lines) - situation cards with progress circles
│   ├── word-bank/page.tsx            # Word learning tracker
│   ├── profile/page.tsx              # User profile (placeholder)
│   ├── paywall/page.tsx              # Subscription paywall (placeholder)
│   └── situation/[id]/
│       ├── learn/page.tsx            # 3-phase learning flow (~1150 lines)
│       ├── voice-chat/page.tsx       # Voice conversation launcher
│       └── new-words/page.tsx        # Redirect to learn
├── components/
│   ├── ImmersiveVoiceScene.tsx       # Voice chat UI with state machine (~430 lines)
│   ├── VoiceChatOnboarding.tsx      # Phase 2 first-time tooltip sequence
│   ├── LearningProgressBar.tsx       # Multi-phase progress indicator
│   ├── progress-bar.tsx              # Simple progress bar
│   ├── word-card.tsx                 # Word display card
│   ├── theme-provider.tsx            # next-themes wrapper
│   ├── icons/                        # Custom SVG icon components
│   └── ui/                           # ~70 shadcn/ui Radix primitive wrappers
├── lib/
│   ├── api.ts                        # API client (fetchWithAuth, api object, logToBackend)
│   ├── types.ts                      # TypeScript interfaces (Word, Situation, etc.)
│   ├── utils.ts                      # cn() helper (clsx + tailwind-merge)
│   └── videoAssets.ts                # Category-to-video mapping (placeholder)
├── hooks/
│   ├── use-mobile.tsx                # Mobile breakpoint detection
│   └── use-toast.ts                  # Toast notification hook
├── styles/
│   └── globals.css                   # CSS variables, Tailwind base, animations
├── package.json
├── tailwind.config.ts
└── tsconfig.json
```

### Key Patterns

- **All pages are client components** (`'use client'`) — no SSR/RSC usage
- **No state management library** — all state is local `useState`/`useRef` per page
- **Auth**: JWT token stored in `localStorage`, checked manually on each page load
- **API client** (`lib/api.ts`): `fetchWithAuth()` wrapper that injects Bearer token and X-Request-Id, auto-redirects to `/login` on 401
- **No shared auth context** — every page independently reads `localStorage`

---

## Data Model

### Entity Relationship

```
User (1) ----< Subscription (1)
User (1) ----< UserWord (many)     >---- Word (1)
User (1) ----< UserSituation (many) >---- Situation (1)
User (1) ----< Conversation (many) >---- Situation (1)

Situation (1) ----< SituationWord (many) >---- Word (1)
```

### Core Tables

| Table | Primary Key | Purpose |
|-------|-------------|---------|
| `users` | UUID | User account, onboarding state, dialect preference, `is_admin` flag |
| `subscriptions` | `user_id` (FK) | Subscription tier and active status |
| `words` | String ID | Spanish/English vocabulary, category (encounter/high_frequency), frequency rank |
| `situations` | String ID | Learning scenarios. Each row = one encounter. `animation_type` = situation type, `encounter_number` = encounter # (1-50). 14 situations × 50 encounters = 700 rows |
| `situation_words` | Composite (situation_id, word_id) | Maps words to situations with position ordering |
| `user_words` | Composite (user_id, word_id) | Per-user word progress: seen/typed/spoken counts, `mastery_level` (0-4 SRS), `next_refresh_at`, status |
| `user_situations` | Composite (user_id, situation_id) | Tracks situation start/completion timestamps |
| `conversations` | UUID | Active conversation state: target words, used words (typed/spoken), mode, status |

### Word Mastery Lifecycle

```
(new) -> mastery_level 0 (UserWord created, status="learning")
      -> mastery_level 1 (lesson completed, refresh in 24h)
      -> mastery_level 2 (first refresh, refresh in 7d) — counts toward vocab level
      -> mastery_level 3 (second refresh, refresh in 30d)
      -> mastery_level 4 (final mastery, status="mastered", no more refreshes)
```

Managed by `refresh_service.py`. The `status` field ('learning'/'mastered') is a simplified view; `mastery_level` is the authoritative progression tracker.

### Conversation Status

```
"active" -> "complete" (all target words detected in user speech/text)
```

---

## API Surface

### Auth
| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/v1/auth/register` | No | Create account (email, password, confirm_password) |
| POST | `/v1/auth/login` | No | Login, returns JWT token |

### Onboarding
| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/v1/onboarding/status` | Yes | Check if onboarding is complete |
| GET | `/v1/onboarding/available-categories` | Yes | List available situation categories |
| POST | `/v1/onboarding/save-selections` | Yes | Save category, dialect, quiz scores |

### Situations
| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/v1/situations` | Yes | List all situations for user |
| GET | `/v1/situations/selected` | Yes | List situations in user's selected category. Returns `vocab_level`, `current_situation_goal`, dynamic `total_in_series` |
| GET | `/v1/situations/{id}` | Yes | Get situation details with words. Returns `series_number`, `category`, `goal` |
| POST | `/v1/situations/{id}/start` | Yes | Start situation: creates conversation, selects words. Returns `series_number`, `category`, `goal` |
| POST | `/v1/situations/{id}/complete` | Yes | Mark situation as completed |
| POST | `/v1/situations/{id}/next` | Yes | Get next situation in series |
| GET | `/v1/situations/admin/all` | Admin | List all situations grouped by category with series_number (admin only, no paywall) |

### Conversations
| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/v1/conversations` | Yes | Create voice conversation for a situation. Returns `language_mode` (english/spanish_text/spanish_audio) |
| POST | `/v1/conversations/{id}/voice-turn` | Yes | Send audio, get transcription + AI response + TTS. Uses language mode to select system prompt |

### User Words
| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/v1/user/words` | Yes | Get all user's word progress |
| GET | `/v1/user/words/unknown` | Yes | Get words user hasn't learned yet |
| POST | `/v1/user/words/typed-correct` | Yes | Mark words as typed correctly |

### Subscription
| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/v1/subscription/status` | Yes | Get subscription status + free tier remaining |

### Utility
| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/v1/log` | Optional | Frontend log relay to Better Stack |
| GET | `/health` | No | Health check |
| GET | `/wakeup` | No | Wake Railway sleeping app |

---

## Authentication Flow

1. User registers/logs in via `/v1/auth/register` or `/v1/auth/login`
2. Backend returns JWT token (24h expiry, HS256)
3. Frontend stores token in `localStorage` as `authToken`
4. Every API call via `fetchWithAuth()` attaches `Authorization: Bearer <token>`
5. On 401 response, frontend clears token and redirects to `/login`
6. Backend validates token via `get_current_user()` FastAPI dependency

---

## Core Business Logic

### Learning Flow (Per Situation)

> For full phase details and grammar-specific flows, see `learning-flow.md` (sibling).

1. **Start Situation** (`POST /situations/{id}/start`):
   - Selects words via `word_selection_service.py` (see below)
   - Reuses existing conversation's word IDs if one exists, otherwise creates new selection
   - Creates a Conversation record with `target_word_ids`
   - Upserts UserWord records (increments `seen_count`)
   - Creates UserSituation record

2. **Learn Phase** (frontend — differs by situation type):
   - **Main situations**: `WordCardsPhase` — combined learn + recall component. Learn mode shows Spanish + English + pronunciation; recall mode flips cards to English-only (shuffled). User records pronunciation via mic, API checks via Whisper. All cards must pass both modes.
   - **Grammar situations**: Configurable multi-phase pipeline (0a video → 0b drill → 1a typing → 1b written test → 1c spoken test). Each phase is individually toggled per grammar topic via `phases` config. Failures in 1b/1c reset to 1a.

3. **Voice Conversation** (`/situation/{id}/voice-chat`):
   - Phase 2 (with hints): word checklist shows Spanish + English
   - Phase 3 (no hints): word checklist shows English only
   - Full AI conversation using GPT-4.1-mini with situation context
   - Backend detects target words in user's speech
   - Conversation completes when all target words have been used
   - `POST /conversations/{id}/voice-turn` handles the full loop: STT → word detection → LLM response → TTS
   - Language mode (english/spanish_text/spanish_audio) derived from encounter number + vocab level (see `learning-flow.md`)
   - Goal displayed prominently in the voice chat UI

### Word Selection Algorithm

When starting a situation, words are selected via `word_selection_service.py`:
- **Main situations**: 3 encounter words (from `situation_words`, ordered by position) + 2 high-frequency words (ordered by `frequency_rank`, excluding already-seen). Total: 5 words.
- **Grammar situations**: All grammar words for the topic (e.g., 11 pronouns, 8 articles). No high-frequency words added.

### Mastery & Spaced Repetition

Managed by `refresh_service.py`:
- **Level 0 → 1**: `set_initial_mastery()` after lesson completion. Refresh due in 24h.
- **Level 1 → 2 → 3 → 4**: `bump_mastery_after_refresh()` when user revisits after `next_refresh_at`. Intervals: 24h → 7d → 30d → done.
- **Level 4**: `status` set to `"mastered"`, no more refreshes.
- **Vocab level (VL)**: Count of high-frequency words with `mastery_level >= 1` (computed in `situations.py:get_vocab_level()`).
- **Grammar level (GL)**: Highest `grammar_level` of completed grammar situations (computed in `situations.py:get_grammar_level()`).

### Free Tier

- `FREE_ENCOUNTERS_LIMIT = 25` (in `subscription_service.py`)
- Users get 25 free situation encounters before hitting the paywall
- Subscription check runs before starting a situation

---

## Logging & Observability

### Structured Logging

All backend logging goes through `app/core/logger.py` -> `log_event()`:

```python
log_event(
    level="info|warning|error",
    event="event_name",          # e.g., "voice_turn", "llm_request", "stt_request"
    message="Human readable message",
    request_id="uuid",           # From X-Request-Id header
    user_id="uuid|None",
    extra={...}                  # Arbitrary metadata
)
```

This:
1. Prints structured JSON to stdout (visible in Railway logs)
2. Fires `schedule_ship_log()` to send to Better Stack asynchronously

### Frontend Logging

Frontend can send logs via `logToBackend()` -> `POST /v1/log` -> Better Stack.
Used for tracking client-side events (voice recording, phase transitions, errors).

### Request Tracing

- `RequestIDMiddleware` injects `X-Request-Id` into every request if not present
- `RequestLoggingMiddleware` logs request/response metadata with timing
- Frontend generates its own UUIDs for request correlation

---

## Known Technical Debt

**Remaining:**
- Redundant CORS (three mechanisms still active — functional but messy)
- Some `console.log` debug statements remain in frontend
