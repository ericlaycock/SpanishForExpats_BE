"""Memory Miracle free-trial variant — light AI guide turns.

Two short, public (pre-signup), rate-limited LLM turns that wrap the memory
utility with Eric's converting voice:

- `kind="reflection"` → a brief, warm "I see exactly where you are" beat after
  the user picks their goal (makes them feel SEEN; de-shames the struggle).
- `kind="roadmap"`   → a 3-4 line personalized path-to-fluent after they've
  memorized + said their phrase out loud, leading into the call CTA.

The AI is ONLY a guide/personalizer here — the memory utility does the teaching.
System prompt is light; a couple of distilled Eric-voice exemplars are passed as
few-shot context (NOT the whole transcript corpus). Mirrors the public + per-IP
rate-limit pattern in `memorize.py`.
"""
import logging
import time
from typing import Literal, Optional

from fastapi import APIRouter, HTTPException, Request
from openai import OpenAI
from pydantic import BaseModel, Field

from app.config import settings
from app.data.trial_phrases import phrase_for_goal

logger = logging.getLogger(__name__)
router = APIRouter()

TRIAL_MODEL = "gpt-4.1"  # matches the working public memorize endpoints

# Light voice guide + a few distilled exemplars (NOT the raw corpus). Eric's
# tone: warm, casual, de-shaming, "it's the tools not you", momentum-framed.
_VOICE = (
    "You are the warm, encouraging guide inside Eric's Spanish-for-Expats free "
    "trial. Eric helps expats in Latin America get fluent. Voice: warm, casual, "
    "concise, never corporate. You de-shame ('learning Spanish felt hard because "
    "the tools are bad, not you'), and you make people believe fluency is "
    "achievable. Never lecture or 'teach Spanish' in prose — the app's memory "
    "utility does the teaching. Latin American Spanish only (never vosotros). "
    "A couple of Eric's real lines for tone:\n"
    "- \"Learning Spanish is honestly easy — people just make it hard.\"\n"
    "- \"When you're fluent and feel like a local, the same city becomes a "
    "totally different place. No more English bubble.\"\n"
    "- \"You're going to watch your own sentences get longer every week.\""
)

_REFLECTION_INSTRUCTION = (
    "The user just told you what they most want to do in Spanish (their GOAL). "
    "Write 2-3 SHORT sentences (max ~45 words) that (1) reflect their exact goal "
    "back so they feel seen, (2) de-shame why it's felt hard, (3) build a flicker "
    "of belief. Then hand off to the activity, e.g. 'Let's lock in your first "
    "real phrase right now.' Plain text, no markdown, no emoji spam (one max)."
)

_ROADMAP_INSTRUCTION = (
    "The user just memorized their first phrase to 100% and said it out loud. "
    "Write a SHORT, punchy path-to-fluent (≤4 short lines): the few next steps "
    "(more core phrases → present tense → past/future + the rest of the vocab), "
    "tailored to THEIR goal (add a one-line tweak if relevant, e.g. real-estate "
    "vocab, or training on fast native speech). End by making them want Eric to "
    "map it to them on a quick free call. Plain text, no markdown headings."
)

# Public endpoint → per-IP in-memory rate limit (mirrors memorize.py).
_RATE_LIMIT = 30
_RATE_WINDOW = 3600.0
_hits: dict[str, list[float]] = {}

_client: Optional[OpenAI] = None


def _get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(api_key=settings.openai_api_key)
    return _client


def _client_ip(request: Request) -> str:
    fwd = request.headers.get("x-forwarded-for")
    if fwd:
        return fwd.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


def _enforce_rate_limit(request: Request) -> None:
    ip = _client_ip(request)
    now = time.time()
    hits = [t for t in _hits.get(ip, []) if now - t < _RATE_WINDOW]
    if len(hits) >= _RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Slow down a moment and try again.")
    hits.append(now)
    _hits[ip] = hits


class GuideRequest(BaseModel):
    kind: Literal["reflection", "roadmap"]
    goal_key: Optional[str] = Field(None, max_length=40)   # tapped option key, or "other"
    goal_text: str = Field("", max_length=300)             # human goal text (label or free text)
    level: Optional[str] = Field(None, max_length=40)      # "beginner" | "some" | None
    phrase_en: Optional[str] = Field(None, max_length=200)  # what they memorized (roadmap)


class GuideResponse(BaseModel):
    text: str
    # On reflection turns we return the goal-matched phrase the user will
    # memorize next (one source of truth — the FE feeds it to the utility).
    phrase_es: Optional[str] = None
    phrase_en: Optional[str] = None


@router.post("/guide", response_model=GuideResponse)
def trial_guide(body: GuideRequest, request: Request):
    """Light AI guide turn for the Memory Miracle trial. Public, rate-limited."""
    _enforce_rate_limit(request)

    goal = (body.goal_text or "").strip() or "get comfortable speaking Spanish in everyday life"
    phrase = phrase_for_goal(body.goal_key) if body.kind == "reflection" else None
    if body.kind == "reflection":
        instruction = _REFLECTION_INSTRUCTION
        user = f"GOAL: {goal}\nLEVEL: {body.level or 'unknown'}"
    else:
        instruction = _ROADMAP_INSTRUCTION
        user = f"GOAL: {goal}\nLEVEL: {body.level or 'unknown'}\nJUST MEMORIZED: {body.phrase_en or 'their first phrase'}"

    try:
        completion = _get_client().chat.completions.create(
            model=TRIAL_MODEL,
            messages=[
                {"role": "system", "content": f"{_VOICE}\n\n{instruction}"},
                {"role": "user", "content": user},
            ],
            temperature=0.7,
            max_tokens=220,
        )
        text = (completion.choices[0].message.content or "").strip()
    except Exception as exc:  # noqa: BLE001
        logger.error("trial/guide failed kind=%s: %s", body.kind, exc)
        # Graceful fallback so the trial never hard-stops on an LLM hiccup.
        text = (
            "Love it — that's exactly the kind of thing we'll get you saying. Let's "
            "lock in your first real phrase right now."
            if body.kind == "reflection"
            else (
                "Here's your path: nail a handful of core phrases like this one, then the "
                "present tense, then past/future + the rest of the everyday vocab — that's "
                "fluent. The fastest way is to have Eric map it to your exact Spanish on a "
                "quick free call."
            )
        )

    if not text:
        raise HTTPException(status_code=502, detail="Try again in a moment.")
    logger.info("trial/guide ok kind=%s goal=%r", body.kind, goal[:40])
    return GuideResponse(
        text=text,
        phrase_es=phrase["es"] if phrase else None,
        phrase_en=phrase["en"] if phrase else None,
    )
