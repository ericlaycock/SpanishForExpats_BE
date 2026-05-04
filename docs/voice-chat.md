<!-- UPDATE FREQUENTLY — This document is the single source of truth for the voice chat pipeline. Keep it current as the system evolves. -->

# Voice Chat System — Full Pipeline Reference

## Entry Points

The voice chat is reached from `/app/situation/[id]/voice-chat?phase=2` (with hints) or `?phase=3` (no hints). Three flows reach it:

- **First-encounter (non-grammar)** — `WordCardsPhase` learn+recall completes → router pushes phase 2.
- **Refresh (non-grammar)** — same path, with `&refresh=true` so backend creates `conversation_type="refresh"`. Refreshes used to short-circuit at recall; the chat is now the value of the lesson and runs every time.
- **Grammar (first-encounter or refresh)** — final pre-chat phase (1c, or earlier if 1c disabled) → router pushes phase 2 with `&refresh=true` if applicable.

`SpanishForExpats_FE/app/[locale]/app/situation/[id]/learn/hooks/useLearnFlow.ts` is the single source of truth for these transitions.

## Overview

The voice chat is the core learning experience. A user speaks into their phone, the backend transcribes + generates an AI response + synthesizes speech, and the frontend plays it back with synced typewriter text and character animation.

**Total round-trip budget: ~3-6 seconds** (STT ~0.5-2s, LLM ~1-3s, TTS ~1-2s)

---

## Frontend Flow

### State Machine (`ImmersiveVoiceScene.tsx`)

```
IDLE_LOOP → ASSISTANT_SPEAKING → USER_READY → RECORDING → UPLOADING → THINKING → ASSISTANT_SPEAKING → ...
                                                                                            ↓
                                                                                        COMPLETE (all words detected)
```

### Step-by-step

1. **User taps mic** (`handleMicClick`) — State: USER_READY → RECORDING
   - `useVoiceRecorder.startRecording()` opens `MediaRecorder`
   - Prefers `audio/mp4` (Safari-native), falls back to `audio/webm;codecs=opus` (Chrome)
   - `GlowingMicButton` shows recording pulse animation

2. **User taps mic again** — State: RECORDING → UPLOADING
   - `MediaRecorder.stop()` fires `onstop`
   - Raw blob converted to 16kHz mono WAV via `convertToWav()` (OfflineAudioContext)
   - If WAV conversion fails (e.g., Safari can't decode webm), sends raw blob as fallback — **this triggers whisper-1 fallback on backend (slow!)**

3. **Audio uploaded** — `processAudio(blob)` called
   - `api.sendVoiceTurn()` sends FormData: audio file + messages_json (full conversation history)
   - State: UPLOADING → THINKING (thinking dots shown, 1s minimum)

4. **Response received** — Backend returns `VoiceTurnResponse`:
   - `user_transcript`, `assistant_text`, `assistant_audio_url`
   - `detected_word_ids`, `missing_word_ids`, `conversation_complete`
   - User bubble shown with transcript
   - AI audio preloaded in parallel with 1s thinking delay

5. **AI speaks** — State: THINKING → ASSISTANT_SPEAKING
   - Audio plays via `useAudioPlayback` (persistent HTMLAudioElement, unlocked during user gesture)
   - Typewriter reveals text synced to audio: CPS = textLength / audioDuration
   - `isSpeaking=true` triggers body animation jump from idle (1-499) to speech frames (500+)
   - If no audio URL: typewriter runs at default 15 CPS, no audio playback

6. **Audio ends** — State: ASSISTANT_SPEAKING → USER_READY
   - `onAudioEnded` callback fires
   - Character animation drains back to idle loop
   - Word checklist updates with detected words (green checkmarks)

### Key Frontend Files

| File | Purpose |
|------|---------|
| `components/ImmersiveVoiceScene.tsx` | Main orchestrator, state machine, processAudio |
| `hooks/useVoiceRecorder.ts` | MediaRecorder + WAV conversion |
| `hooks/useAudioPlayback.ts` | Audio preload, play, warmup (autoplay unlock) |
| `hooks/useTypewriter.ts` | Character-by-character reveal synced to CPS |
| `hooks/useBodyAnimation.ts` | Frame animation, idle/speech segments, demand loading |
| `components/voice-chat/CharacterScene.tsx` | Background + character canvas rendering |
| `components/voice-chat/SpeechBubble.tsx` | AI/user bubbles, font shrinking for long text |
| `components/voice-chat/GlowingMicButton.tsx` | Mic button visual states |
| `lib/api.ts` | `sendVoiceTurn()` — FormData POST to backend |

---

## Backend Flow

### `POST /v1/conversations/{id}/voice-turn` (`conversations.py`)

```
Audio file received
  → Read audio bytes
  → STT: transcribe_audio() → gpt-4o-mini-transcribe (fallback: whisper-1)
  → Word detection: detect_words_in_text() — deterministic substring matching
  → DB updates: update word stats (seen_count, spoken_correct_count)
  → LLM: generate_conversation() → gpt-4.1-mini (full message history)
  → TTS: gateway_synthesize_speech() → gpt-4o-mini-tts (per-situation voice)
  → R2 upload: background task (non-blocking)
  → Return VoiceTurnResponse with local audio URL
```

### STT — Speech-to-Text (`openai_media_gateway.py`)

- **Primary**: `gpt-4o-mini-transcribe` — fast (~0.5-1s), requires WAV or supported format
- **Fallback**: `whisper-1` — slower (~1-2s, up to 9.5s worst case), accepts any format
- Fallback triggers when primary rejects the audio format (usually raw webm from failed WAV conversion)
- Context prompt includes word list + situation for better recognition
- All requests logged to `stt_requests` table with model, latency, format, success

### LLM — Chat Completion (`llm_gateway.py`)

- **Model**: `gpt-4.1-mini` (production; config.py may still reference gpt-4o-mini — stale)
- System prompt built by `build_system_prompt()` in `voice_turn_service.py`
- Currently **hardcoded to "english" mode** — AI speaks mostly English with occasional Spanish
- Full conversation history sent each turn (system + all previous user/assistant messages)
- All requests logged to `llm_requests` table

### TTS — Text-to-Speech (`openai_media_gateway.py`)

- **Model**: `gpt-4o-mini-tts`
- Voice varies by situation (defined in `TTS_CONFIG` dict in `conversations.py`):
  - airport: ash, banking: ballad, clothing: shimmer, restaurant: coral
  - mechanic: fable, police: onyx, groceries: sage, small_talk: verse
  - internet: echo, contractor: onyx, core: echo
- Instructions include accent directive: "Speak with a clear Latin American (Mexican) Spanish accent..."
- Catalan mode overrides accent to "central Catalan (Barcelona)"
- All requests logged to `tts_requests` table

### R2 Audio Storage (`utils/audio.py`)

- **Purpose**: CDN caching via Cloudflare R2 (S3-compatible)
- **NOT required for playback** — audio serves from local `/tmp/audio/` path via `GET /audio/{filename}`
- **Upload is a background task** (FastAPI `BackgroundTasks`) — does NOT block the response
- First upload after deploy can be slow (boto3 cold start + Cloudflare TLS handshake)
- If R2 fails silently, audio still plays from local URL
- R2 configured via env vars: `R2_BUCKET_NAME`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_ENDPOINT_URL`, `R2_PUBLIC_URL`

### Key Backend Files

| File | Purpose |
|------|---------|
| `app/api/v1/conversations.py` | voice_turn endpoint, TTS_CONFIG, conversation creation |
| `app/services/openai_media_gateway.py` | `transcribe_audio()`, `synthesize_speech()` |
| `app/services/llm_gateway.py` | `generate_conversation()` with OpenAI chat completions |
| `app/services/voice_turn_service.py` | `build_system_prompt()`, `get_language_mode()` |
| `app/services/conversation_service.py` | `detect_words_in_text()`, `check_conversation_complete()` |
| `app/services/word_detection.py` | Deterministic word matching with accent normalization |
| `app/utils/audio.py` | `upload_to_r2()`, `get_audio_url()`, local file management |
| `app/models/ai_requests.py` | LLMRequest, STTRequest, TTSRequest DB models |

---

## Character Animation Integration

- `isSpeaking` prop on `CharacterScene` drives the body animation state machine
- **Idle**: frames 1-499 (looped at 25fps), only first 100 frames pinned in cache
- **Speech**: frames 500-820 (varies per scene), played forward when `isSpeaking=true`
- On speech start: animation **jumps** directly to frame 500 (avoids 20s crawl through idle)
- On speech end: DRAINING_TO_IDLE state plays forward until wrapping back to idle segment
- Frame cache: MAX_DECODED=300, demand-loaded, holds current frame if next isn't loaded yet
- Character2 frames deployed as WebP in `public/assets/characters/{scene}/body-frames/`

---

## Known Issues & Fixes Applied (as of 2026-03-29)

| Issue | Fix | Status |
|-------|-----|--------|
| Initial message TTS slow (2s+ on every page load) | Removed TTS from createConversation — typewriter-only | Deployed |
| R2 upload blocking voice_turn response (55s+ cold start) | Moved to FastAPI BackgroundTasks | Deployed |
| Whisper-1 fallback on 62% of STT calls | Was historical (before WAV conversion). Added mp4 preference for Safari | Deployed |
| Speech animation not playing (frames not loaded) | Jump to speech segment, cap pinned frames at 100, hold frame until loaded | Deployed |
| AI bubble pushing word checklist off screen on mobile | 25dvh max + overflow-y-auto + font shrinking | Deployed |
| Language mode using Spanish prompts for beginners | Hardcoded get_language_mode() to return "english" | Deployed |

---

## Monitoring

- **Admin endpoint**: `GET /v1/situations/admin/ai-logs` (admin-only)
  - Aggregate stats per model (avg/min/max latency, call count, cost)
  - Last 20 TTS calls with voice, chars, latency
  - Last 20 STT calls with model, format, bytes, latency
- **DB tables**: `llm_requests`, `stt_requests`, `tts_requests` (in `app/models/ai_requests.py`)
- **Frontend logs**: `[Scene +Xs]` prefixed console logs with state transitions, turn numbers, timing

---

## Future Considerations

- **Streaming TTS**: Stream audio chunks as they're generated instead of waiting for full synthesis. Would reduce perceived latency by ~1-2s.
- **Streaming STT**: Send audio chunks during recording for real-time transcription.
- **Streaming LLM**: Stream text tokens for progressive typewriter display before TTS.
- **R2 removal**: R2 adds complexity for marginal CDN benefit. Local audio URLs work fine. Consider removing if R2 continues to cause cold-start issues.
- **Pre-warm OpenAI connections**: Make a dummy API call on startup to establish TLS connections before user requests arrive.

<!-- UPDATE FREQUENTLY — This document is the single source of truth for the voice chat pipeline. Keep it current as the system evolves. -->
