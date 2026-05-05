# Environment Variables

> Single source of truth for FE + BE environment variables.
> When you add a new env var anywhere in the codebase, document it here in the same PR.

## Frontend (Vercel)

### `NEXT_PUBLIC_API_URL` (required)

Base URL of the backend API.

- **Production**: e.g. `https://encounterspanish-production.up.railway.app`
- **Development**: e.g. `http://localhost:3001`
- Must start with `http://` or `https://`. If no protocol is specified, `https://` is automatically prepended.
- Public (`NEXT_PUBLIC_` prefix) — exposed to the browser.

### `NEXT_PUBLIC_VOICE_REALTIME` (optional)

Feature flag for the WebRTC-based realtime voice chat (BE issue #10 / FE issue #39).

- **Values**: `true` | `false` (default: unset → treated as `false`)
- When `true`, the browser connects directly to OpenAI Realtime via an ephemeral token minted by `POST /v1/realtime/sessions`.
- When unset/`false`, voice chat uses the legacy push-to-talk + REST flow (`POST /v1/conversations/{id}/voice-turn`).
- Safe to flip per-environment. Legacy flow stays wired until issue #39 Phase 6 cleanup.
- Required wiring on BE: see `app/api/v1/realtime.py` and `app/services/realtime_session_service.py`.

### How to set in Vercel

1. Project → **Settings** → **Environment Variables**.
2. Add the variable, choose environments (Production / Preview / Development), Save.
3. Redeploy for the changes to take effect.

## Backend (Railway)

> Set in the Railway dashboard for each service/environment.

| Variable | Required | Purpose |
|----------|----------|---------|
| `DATABASE_URL` | yes | PostgreSQL connection string. Provided automatically by Railway when the Postgres plugin is attached. |
| `OPENAI_API_KEY` | yes | OpenAI API key — used for chat (GPT-4.1-mini), Whisper STT, TTS, and Realtime. |
| `JWT_SECRET` | yes | Secret used to sign JWT tokens. Must be set; do not use defaults in production. |
| `BETTERSTACK_HOST` | yes | Better Stack log ingestion host. |
| `BETTERSTACK_TOKEN` | yes | Better Stack auth token for log shipping. |
| `AUTO_MIGRATE` | optional | Set to `"true"` to run `alembic upgrade head` on startup. Recommended for QA, optional for production. |
| `ENVIRONMENT` | optional | Deployment environment name (e.g. `qa`, `production`). When set to `qa`, `start.py` auto-runs `scripts/seed_qa.py`. |
| `RAILWAY_ENVIRONMENT` | auto | Provided by Railway. Used as a fallback environment label. |
| `RELEASE_SHA` | optional | Git commit SHA for log tagging. |
| `R2_BUCKET_NAME` | optional | Cloudflare R2 bucket for TTS audio CDN cache. If unset, audio still serves from local `/tmp/audio/`. |
| `R2_ACCESS_KEY_ID` | optional | R2 access key. |
| `R2_SECRET_ACCESS_KEY` | optional | R2 secret. |
| `R2_ENDPOINT_URL` | optional | R2 endpoint. |
| `R2_PUBLIC_URL` | optional | Public base URL for R2-hosted audio. |
| `SMTP_EMAIL` | optional | Gmail address used as the FROM for outbound mail (password reset, cohort confirmation). Without it, sends are skipped. |
| `SMTP_APP_PASSWORD` | optional | Gmail app-specific password for `SMTP_EMAIL`. |
| `COHORT_ZOOM_URL` | optional | Single shared Zoom meeting URL embedded in cohort confirmation emails and `.ics` files. If unset, the email/.ics will say the link is TBD. |

## Notes

- The frontend uses `NEXT_PUBLIC_API_URL` for every API request. Make sure the backend's CORS settings allow the FE's origin.
- R2 is **not required** for voice playback — it's an opportunistic CDN. If the upload fails, audio still plays from the local URL.
- Storing JWTs and other secrets in `localStorage` is a known consideration; see `docs/architecture.md` for the auth flow.
