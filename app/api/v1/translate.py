from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app.models import User
from app.schemas import TranslateRequest
from app.services.alt_language_service import get_target_language_name

router = APIRouter()


@router.post("")
async def translate_text(
    request: TranslateRequest,
    current_user: User = Depends(get_current_user),
):
    """Translate target-language text to English for comprehension.

    Uses GPT-4.1-mini for fast (<500ms) translation.
    """
    import logging
    logger = logging.getLogger(__name__)

    source_lang = get_target_language_name(current_user.alt_language)
    text = request.text.strip()

    if not text:
        return {"translation": ""}

    from openai import AsyncOpenAI
    from app.config import settings

    client = AsyncOpenAI(api_key=settings.openai_api_key)

    try:
        response = await client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"Translate the following {source_lang} text to English. "
                    "Return ONLY the English translation, nothing else. "
                    "Keep the same tone and register.",
                },
                {"role": "user", "content": text},
            ],
            max_tokens=300,
            temperature=0.1,
        )
        translation = response.choices[0].message.content.strip()
        logger.info(f"[Translate] {source_lang} → EN: '{text[:50]}...' → '{translation[:50]}...'")
        return {"translation": translation}

    except Exception as e:
        logger.error(f"[Translate] Failed: {e}")
        return {"translation": ""}
