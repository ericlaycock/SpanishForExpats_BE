# Testing

This document covers all testing layers for Spanish for Expats.

---

## 1. GitHub Actions CI

Both repos run CI on **push to `qa`** and **PRs to `main`**.

### Backend CI (`SpanishForExpats_BE/.github/workflows/ci.yml`)

- Spins up a **PostgreSQL 16** service container
- Installs Python 3.11 dependencies
- Runs Alembic migrations (`alembic upgrade head`)
- Runs `pytest tests/ -v` — 9 test files covering auth, onboarding, subscription, seed data, prompts, refreshes, situations, word selection, user words
- Uses a fake OpenAI key (no real API calls)

### Frontend CI (`SpanishForExpats_FE/.github/workflows/ci.yml`)

- Uses **pnpm 9** + **Node 20**
- Runs `pnpm run lint` (Next.js linter)
- Runs `pnpm run test` (vitest — 2 test files: API client, ErrorBoundary)
- Runs `pnpm run build` (catches TypeScript/build errors)

---

## 2. Backend Integration Tests (pytest)

Requires PostgreSQL — UUID and JSONB columns are not SQLite-compatible.

**Run locally:**

```bash
cd SpanishForExpats_BE && source .venv/bin/activate && pytest tests/ -v
```

### Test files

| File | Coverage |
|------|----------|
| `test_auth.py` | Registration, JWT login |
| `test_onboarding.py` | Onboarding status, save-selections |
| `test_subscription.py` | Free tier limits (25 encounters) |
| `test_seed_data.py` | Data integrity (14 sub-situations, 700 encounters) |
| `test_prompts.py` | LLM prompt content and routing |
| `test_refreshes.py` | SRS refresh lifecycle |
| `test_situations.py` | Situation list/detail endpoints |
| `test_services/test_word_selection.py` | Encounter + high-frequency word selection |
| `test_user_words.py` | Word tracking and mastery status |

---

## 3. Frontend Unit Tests (vitest)

**Run locally:**

```bash
cd SpanishForExpats_FE && npm run test
```

### Test files

| File | Coverage |
|------|----------|
| `lib/__tests__/api.test.ts` | API client, `fetchWithAuth`, 401 redirect |
| `components/__tests__/ErrorBoundary.test.tsx` | Error boundary rendering |

---

## 4. E2E Tests (Playwright)

**Run locally:**

```bash
cd SpanishForExpats_FE && npm run test:e2e
```

Playwright auto-starts the backend (port 8000) and frontend (port 3000) via `webServer` config in `playwright.config.ts`. Runs against the **remote QA database** — no local DB setup needed.

**QA test user:** `qa@test.com` / `testpassword123`

### Test suites (5 suites, 13 tests)

| File | Coverage |
|------|----------|
| `e2e/01-auth.spec.ts` | Login page, valid/invalid credentials, register page |
| `e2e/02-onboarding.spec.ts` | Full onboarding wizard (fresh user registration → dashboard) |
| `e2e/03-dashboard.spec.ts` | Greeting, situation cards, Word Bank navigation |
| `e2e/04-learn-phase.spec.ts` | Phase 1a typing (single word + full 5-word completion) |
| `e2e/05-word-bank.spec.ts` | Tabs, Unknown sub-tabs, Home navigation |

### Notes

- Screenshots are captured for every test in `e2e/screenshots/` (gitignored)
- Voice phases (1c, 2, 3) are **not covered** — they require real microphone/audio input
- **Not run in CI** — requires a running backend + QA database access
