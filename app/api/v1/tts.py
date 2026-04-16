"""Per-word TTS endpoint for alt-language pronunciations (Swedish, Catalan).

Spanish words use the browser's built-in speechSynthesis (free, instant).
Alt-language words hit this endpoint which generates via OpenAI TTS and
caches with a deterministic filename so each word is only generated once.
"""
import hashlib
import logging
from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app.models import User
from app.utils.audio import get_audio_path, AUDIO_DIR

logger = logging.getLogger(__name__)

router = APIRouter()

# Language → TTS instruction
_LANG_INSTRUCTIONS = {
    "swedish": "Pronounce this Swedish word clearly with a native Swedish accent. Say only the word, nothing else.",
    "catalan": "Pronounce this Catalan word clearly with a native Catalan accent. Say only the word, nothing else.",
}


def _word_filename(text: str, lang: str) -> str:
    """Deterministic filename: word_{lang}_{hash}.mp3"""
    h = hashlib.sha256(f"{lang}:{text}".encode()).hexdigest()[:12]
    return f"word_{lang}_{h}.mp3"


@router.get("/word")
async def tts_word(
    text: str = Query(..., max_length=100),
    lang: str = Query(..., pattern="^(swedish|catalan)$"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Generate or serve cached TTS audio for an alt-language word.

    Returns the MP3 file directly with long-lived cache headers.
    Only supports alt-languages (swedish, catalan) — Spanish uses browser TTS.
    """
    filename = _word_filename(text, lang)
    audio_path = get_audio_path(filename)

    # Serve from cache if already generated
    if audio_path.exists():
        return FileResponse(
            audio_path,
            media_type="audio/mpeg",
            headers={"Cache-Control": "public, max-age=31536000, immutable"},
        )

    # Generate via OpenAI TTS
    from app.services.openai_media_gateway import synthesize_speech

    instructions = _LANG_INSTRUCTIONS.get(lang, "")
    try:
        await synthesize_speech(
            text=text,
            output_path=str(audio_path),
            voice="alloy",
            instructions=instructions,
            request_id=f"word-tts-{filename}",
            user_id=str(current_user.id),
            db=db,
            learning_phase="word_pronunciation",
        )
    except Exception as e:
        logger.error(f"[WordTTS] Failed for '{text}' ({lang}): {e}")
        raise HTTPException(status_code=502, detail="TTS generation failed")

    logger.info(f"[WordTTS] Generated {filename} for '{text}' ({lang})")

    return FileResponse(
        audio_path,
        media_type="audio/mpeg",
        headers={"Cache-Control": "public, max-age=31536000, immutable"},
    )
