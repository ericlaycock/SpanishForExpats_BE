import json as json_module
import os
from datetime import datetime, timezone
from typing import Optional
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert as pg_insert
from app.database import get_db
from app.auth import get_current_user, get_current_user_from_query
from app.models import User, Conversation, Situation, Word, UserMilestoneEvent
from app.services.word_selection_service import select_words_for_situation, sort_words_encounter_first
from app.schemas import (
    CreateConversationRequest,
    CreateConversationResponse,
    MessageRequest,
    MessageResponse,
    RealtimeTurnRequest,
    RealtimeTurnResponse,
    VoiceTurnResponse,
    WordSchema
)
from app.services.llm_gateway import generate_conversation, ConversationContext, load_prompt
from app.services.openai_media_gateway import transcribe_audio as gateway_transcribe_audio, synthesize_speech as gateway_synthesize_speech
from fastapi import Request
from app.services.word_detection import detect_words_in_text, get_words_by_ids
from app.services.conversation_service import (
    check_conversation_complete,
    update_user_word_stats,
    get_missing_word_ids
)
from app.services.encounter_messages import get_initial_message_for_encounter
from app.api.v1.situations import get_vocab_level, get_grammar_level
from app.services.voice_turn_service import (
    build_transcription_prompt,
    build_conversation_prompt,
    build_grammar_system_prompt,
    build_grammar_user_prompt,
    get_language_mode,
    get_conversation_system_prompt,
    build_system_prompt,
    check_completion,
    persist_turn,
)
from app.data.grammar_situations import get_grammar_config
from app.services.alt_language_service import apply_alt_language, get_target_language_name
from app.utils.audio import generate_audio_filename, get_audio_path, get_audio_url, upload_to_r2
router = APIRouter()


def _build_grammar_hint(pronoun: str, verb: str, verb_english: str) -> str:
    """Build a natural English hint question for a specific pronoun+verb target.

    Uses verb-specific overrides for irregular/awkward English, and a template
    fallback for regular verbs where 'Does your sister [verb]?' sounds natural.
    """
    # ── Verb-specific overrides (irregular English or verbs needing context) ──
    _VERB_QUESTIONS = {
        "ser": {
            "yo": "Are you from here?",
            "tú": "I'm from Mexico. Where am I from?",
            "él": "Is your brother tall?",
            "ella": "Is your sister a student?",
            "usted": "Is your boss strict?",
            "nosotros": "Are you and your friends from here?",
            "nosotras": "Are you and your sisters happy here?",
            "ellos": "Are your friends from this city?",
            "ellas": "Are your female friends students?",
            "ustedes": "Are you all from the same place?",
        },
        "estar": {
            "yo": "How are you feeling right now?",
            "tú": "I feel great today. How am I doing?",
            "él": "Is your brother feeling okay?",
            "ella": "Is your sister at home right now?",
            "usted": "Is your boss in the office today?",
            "nosotros": "Are you and your friends happy here?",
            "nosotras": "Are you and your sisters feeling well?",
            "ellos": "Are your friends at the party?",
            "ellas": "Are your female friends here today?",
            "ustedes": "Are you all ready to go?",
        },
        "ir": {
            "yo": "Where do you go on weekends?",
            "tú": "I go to the park every day. Where do I go?",
            "él": "Does your brother go to school?",
            "ella": "Does your sister go to work?",
            "usted": "Does your boss go on vacation?",
            "nosotros": "Do you and your friends go out together?",
            "nosotras": "Do you and your sisters go shopping?",
            "ellos": "Do your friends go to the beach?",
            "ellas": "Do your female friends go dancing?",
            "ustedes": "Do you all go to the same restaurant?",
        },
        "tener": {
            "yo": "Do you have any pets?",
            "tú": "I have a big family. What do I have?",
            "él": "Does your brother have a car?",
            "ella": "Does your sister have children?",
            "usted": "Does your boss have a lot of meetings?",
            "nosotros": "Do you and your friends have plans tonight?",
            "nosotras": "Do you and your sisters have similar taste?",
            "ellos": "Do your friends have jobs?",
            "ellas": "Do your female friends have kids?",
            "ustedes": "Do you all have the same schedule?",
        },
        "dar": {
            "yo": "Do you give gifts on birthdays?",
            "tú": "I give advice to my friends. What do I give?",
            "él": "Does your brother give you help?",
            "ella": "Does your sister give good advice?",
            "usted": "Does your boss give feedback?",
            "nosotros": "Do you and your friends give presents?",
            "nosotras": "Do you and your sisters give each other gifts?",
            "ellos": "Do your friends give you rides?",
            "ellas": "Do your female friends give parties?",
            "ustedes": "Do you all give tips at restaurants?",
        },
        "venir": {
            "yo": "Do you come here often?",
            "tú": "I come here every week. How often do I come?",
            "él": "Does your brother come to visit?",
            "ella": "Does your sister come to this area?",
            "usted": "Does your boss come to the office early?",
            "nosotros": "Do you and your friends come here together?",
            "nosotras": "Do you and your sisters come to this park?",
            "ellos": "Do your friends come to your house?",
            "ellas": "Do your female friends come to the party?",
            "ustedes": "Do you all come from the same town?",
        },
        "hacer": {
            "yo": "What do you do on weekends?",
            "tú": "I make breakfast every day. What do I make?",
            "él": "What does your brother do for work?",
            "ella": "What does your sister do after school?",
            "usted": "What does your boss do at meetings?",
            "nosotros": "What do you and your friends do for fun?",
            "nosotras": "What do you and your sisters do together?",
            "ellos": "What do your friends do on Friday nights?",
            "ellas": "What do your female friends do on weekends?",
            "ustedes": "What do you all do after class?",
        },
        "poder": {
            "yo": "Can you swim?",
            "tú": "I can cook really well. What can I do?",
            "él": "Can your brother drive?",
            "ella": "Can your sister play guitar?",
            "usted": "Can your boss speak English?",
            "nosotros": "Can you and your friends come tomorrow?",
            "nosotras": "Can you and your sisters help?",
            "ellos": "Can your friends play soccer?",
            "ellas": "Can your female friends join us?",
            "ustedes": "Can you all come to dinner?",
        },
        "querer": {
            "yo": "What do you want for dinner?",
            "tú": "I want pizza tonight. What do I want?",
            "él": "Does your brother want to come?",
            "ella": "Does your sister want coffee?",
            "usted": "Does your boss want the report today?",
            "nosotros": "Do you and your friends want to go out?",
            "nosotras": "Do you and your sisters want dessert?",
            "ellos": "Do your friends want to play?",
            "ellas": "Do your female friends want to join?",
            "ustedes": "Do you all want to go to the beach?",
        },
        "decir": {
            "yo": "What do you say when you greet someone?",
            "tú": "I always say 'good morning'. What do I say?",
            "él": "What does your brother say about it?",
            "ella": "What does your sister say?",
            "usted": "What does your boss say about the project?",
            "nosotros": "What do you and your friends say?",
            "nosotras": "What do you and your sisters say about it?",
            "ellos": "What do your friends say?",
            "ellas": "What do your female friends say?",
            "ustedes": "What do you all say when that happens?",
        },
        "salir": {
            "yo": "Do you go out on weekends?",
            "tú": "I go out every Friday. When do I go out?",
            "él": "Does your brother go out at night?",
            "ella": "Does your sister go out with friends?",
            "usted": "Does your boss leave the office early?",
            "nosotros": "Do you and your friends go out together?",
            "nosotras": "Do you and your sisters go out dancing?",
            "ellos": "Do your friends go out on Saturday?",
            "ellas": "Do your female friends go out often?",
            "ustedes": "Do you all go out together?",
        },
        "conocer": {
            "yo": "Do you know this neighborhood well?",
            "tú": "I know a great restaurant. Do you know what I know?",
            "él": "Does your brother know the area?",
            "ella": "Does your sister know my friend?",
            "usted": "Does your boss know about this?",
            "nosotros": "Do you and your friends know the city?",
            "nosotras": "Do you and your sisters know the neighbors?",
            "ellos": "Do your friends know the beach?",
            "ellas": "Do your female friends know the park?",
            "ustedes": "Do you all know each other well?",
        },
        "pedir": {
            "yo": "What do you order at restaurants?",
            "tú": "I always order coffee. What do I order?",
            "él": "What does your brother order?",
            "ella": "What does your sister order for lunch?",
            "usted": "What does your boss request?",
            "nosotros": "What do you and your friends order?",
            "nosotras": "What do you and your sisters order?",
            "ellos": "What do your friends order at the cafe?",
            "ellas": "What do your female friends ask for?",
            "ustedes": "What do you all order when you go out?",
        },
        "seguir": {
            "yo": "Do you follow any sports teams?",
            "tú": "I follow soccer. What do I follow?",
            "él": "Does your brother follow the news?",
            "ella": "Does your sister follow fashion?",
            "usted": "Does your boss keep going with the plan?",
            "nosotros": "Do you and your friends keep studying?",
            "nosotras": "Do you and your sisters keep practicing?",
            "ellos": "Do your friends keep playing?",
            "ellas": "Do your female friends keep exercising?",
            "ustedes": "Do you all keep going to class?",
        },
        "conseguir": {
            "yo": "Do you get good grades?",
            "tú": "I always get a good seat. What do I get?",
            "él": "Does your brother get tickets easily?",
            "ella": "Does your sister get good deals?",
            "usted": "Does your boss get results?",
            "nosotros": "Do you and your friends get together often?",
            "nosotras": "Do you and your sisters get what you need?",
            "ellos": "Do your friends get good jobs?",
            "ellas": "Do your female friends get discounts?",
            "ustedes": "Do you all manage to get there on time?",
        },
        "morir": {
            "yo": "Are you dying of hunger right now?",
            "tú": "I'm dying of thirst. What am I dying of?",
            "él": "Is your brother dying to see the movie?",
            "ella": "Is your sister dying to go on vacation?",
            "usted": "Is your boss dying to finish the project?",
            "nosotros": "Are you and your friends dying of laughter?",
            "nosotras": "Are you and your sisters dying to try it?",
            "ellos": "Are your friends dying to go to the concert?",
            "ellas": "Are your female friends dying to see it?",
            "ustedes": "Are you all dying of boredom?",
        },
        "abrir": {
            "yo": "Do you open the windows in the morning?",
            "tú": "I open my shop at nine. When do I open it?",
            "él": "Does your brother open the door for people?",
            "ella": "Does your sister open her gifts right away?",
            "usted": "Does your boss open the meeting?",
            "nosotros": "Do you and your friends open a bottle of wine?",
            "nosotras": "Do you and your sisters open presents together?",
            "ellos": "Do your friends open their books in class?",
            "ellas": "Do your female friends open the store early?",
            "ustedes": "Do you all open your laptops in class?",
        },
        "cerrar": {
            "yo": "Do you close the windows at night?",
            "tú": "I close the store at nine. When do I close it?",
            "él": "Does your brother close the door?",
            "ella": "Does your sister close her eyes to sleep?",
            "usted": "Does your boss close the office early?",
            "nosotros": "Do you and your friends close the restaurant?",
            "nosotras": "Do you and your sisters close up the house?",
            "ellos": "Do your friends close the gate?",
            "ellas": "Do your female friends close the shop?",
            "ustedes": "Do you all close everything before leaving?",
        },
        "caer": {
            "yo": "Do you fall asleep easily?",
            "tú": "I fall asleep late. When do I fall asleep?",
            "él": "Does your brother fall often when playing?",
            "ella": "Does your sister drop things a lot?",
            "usted": "Does your boss drop by unexpectedly?",
            "nosotros": "Do you and your friends fall behind in class?",
            "nosotras": "Do you and your sisters fall asleep watching movies?",
            "ellos": "Do your friends trip and fall sometimes?",
            "ellas": "Do your female friends drop their phones?",
            "ustedes": "Do you all fall asleep during long movies?",
        },
        "valer": {
            "yo": "How much is your phone worth?",
            "tú": "My watch is worth a lot. How much is it worth?",
            "él": "Is your brother's car worth a lot?",
            "ella": "Is your sister's painting worth something?",
            "usted": "Is your boss's advice worth following?",
            "nosotros": "Is your group's effort worth it?",
            "nosotras": "Is your sisters' collection worth something?",
            "ellos": "Are your friends' tickets worth the price?",
            "ellas": "Are your female friends' crafts worth selling?",
            "ustedes": "Is your team's work worth the time?",
        },
        "oír": {
            "yo": "Do you hear the music?",
            "tú": "I hear birds every morning. What do I hear?",
            "él": "Does your brother hear the neighbors?",
            "ella": "Does your sister hear the alarm?",
            "usted": "Does your boss hear the complaints?",
            "nosotros": "Do you and your friends hear the noise?",
            "nosotras": "Do you and your sisters hear the dog barking?",
            "ellos": "Do your friends hear the thunder?",
            "ellas": "Do your female friends hear the music?",
            "ustedes": "Do you all hear that sound?",
        },
        "poner": {
            "yo": "Where do you put your keys?",
            "tú": "I put my bag on the table. Where do I put it?",
            "él": "Does your brother put sugar in his coffee?",
            "ella": "Does your sister put music on?",
            "usted": "Does your boss put pressure on you?",
            "nosotros": "Do you and your friends set the table?",
            "nosotras": "Do you and your sisters put decorations up?",
            "ellos": "Do your friends put effort into studying?",
            "ellas": "Do your female friends put on makeup?",
            "ustedes": "Do you all set up the chairs?",
        },
        "traer": {
            "yo": "Do you bring lunch to work?",
            "tú": "I bring dessert to parties. What do I bring?",
            "él": "Does your brother bring his guitar?",
            "ella": "Does your sister bring food to share?",
            "usted": "Does your boss bring coffee to meetings?",
            "nosotros": "Do you and your friends bring snacks?",
            "nosotras": "Do you and your sisters bring presents?",
            "ellos": "Do your friends bring drinks?",
            "ellas": "Do your female friends bring their kids?",
            "ustedes": "Do you all bring something to the party?",
        },
        "producir": {
            "yo": "Do you produce any content online?",
            "tú": "I produce videos. What do I produce?",
            "él": "Does your brother produce music?",
            "ella": "Does your sister produce art?",
            "usted": "Does your boss produce reports?",
            "nosotros": "Do you and your friends produce a podcast?",
            "nosotras": "Do you and your sisters make crafts?",
            "ellos": "Do your friends produce content?",
            "ellas": "Do your female friends make things to sell?",
            "ustedes": "Do you all produce something together?",
        },
        "construir": {
            "yo": "Do you build things at home?",
            "tú": "I build furniture. What do I build?",
            "él": "Does your brother build model planes?",
            "ella": "Does your sister build websites?",
            "usted": "Does your boss build the team?",
            "nosotros": "Do you and your friends build projects?",
            "nosotras": "Do you and your sisters build things together?",
            "ellos": "Do your friends build houses?",
            "ellas": "Do your female friends build community?",
            "ustedes": "Do you all build something together?",
        },
        "recoger": {
            "yo": "Do you pick up your kids from school?",
            "tú": "I pick up the mail. What do I pick up?",
            "él": "Does your brother pick up after himself?",
            "ella": "Does your sister pick up her room?",
            "usted": "Does your boss pick up the phone?",
            "nosotros": "Do you and your friends clean up after?",
            "nosotras": "Do you and your sisters tidy up together?",
            "ellos": "Do your friends pick up trash at the park?",
            "ellas": "Do your female friends pick up supplies?",
            "ustedes": "Do you all pick up after the party?",
        },
        "dirigir": {
            "yo": "Do you manage a team at work?",
            "tú": "I direct the school play. What do I direct?",
            "él": "Does your brother run a business?",
            "ella": "Does your sister manage the project?",
            "usted": "Does your boss lead the department?",
            "nosotros": "Do you and your friends run the club?",
            "nosotras": "Do you and your sisters lead the group?",
            "ellos": "Do your friends manage the event?",
            "ellas": "Do your female friends run the organization?",
            "ustedes": "Do you all manage it together?",
        },
        "convencer": {
            "yo": "Do you convince people easily?",
            "tú": "I convince my friends to try new food. What do I do?",
            "él": "Does your brother convince you to go out?",
            "ella": "Does your sister convince you to exercise?",
            "usted": "Does your boss convince clients easily?",
            "nosotros": "Do you and your friends persuade each other?",
            "nosotras": "Do you and your sisters convince your parents?",
            "ellos": "Do your friends convince you to stay up late?",
            "ellas": "Do your female friends convince you to shop?",
            "ustedes": "Do you all convince the teacher to cancel homework?",
        },
    }

    # Check for verb-specific override
    if verb in _VERB_QUESTIONS and pronoun in _VERB_QUESTIONS[verb]:
        return _VERB_QUESTIONS[verb][pronoun]

    # ── Template fallback for regular verbs ──
    action = verb_english[3:] if verb_english.startswith("to ") else verb_english
    # Clean up parentheticals and slashes
    if "(" in action:
        action = action[:action.index("(")].strip()
    if "/" in action:
        action = action.split("/")[0].strip()

    _FRAMES = {
        "yo": f"Do you {action}?",
        "tú": f"I {action} every day. What do I {action}?",
        "él": f"Does your brother {action}?",
        "ella": f"Does your sister {action}?",
        "usted": f"Does your boss {action}?",
        "nosotros": f"Do you and your friends {action}?",
        "nosotras": f"Do you and your sisters {action}?",
        "ellos": f"Do your friends {action}?",
        "ellas": f"Do your female friends {action}?",
        "ustedes": f"Do you all {action}?",
    }
    return _FRAMES.get(pronoun, f"Do you {action}?")


# Cache for initial message TTS audio URLs — avoids re-synthesizing the same audio
# Key: (situation_id, alt_language) → R2/local URL
_initial_tts_cache: dict[tuple[str, str | None], str] = {}

# OpenAI TTS voice + instructions per situation — keyed by animation_type
_ACCENT = "Speak with a Mexican Spanish accent."
_ALT_ACCENTS = {
    "catalan": "Speak with a Catalan accent.",
    "swedish": "Speak with a Swedish accent.",
}
SITUATION_VOICE_CONFIG = {
    "police": {
        "voice": "alloy",
        "instructions": f"{_ACCENT} Use an authoritative female voice, firm but professional.",
    },
    "banking": {
        "voice": "shimmer",
        "instructions": f"{_ACCENT} Use a professional, composed female voice with a warm undertone.",
    },
    "airport": {
        "voice": "shimmer",
        "instructions": f"{_ACCENT} Use a professional, clear female voice.",
    },
    "clothing": {
        "voice": "coral",
        "instructions": f"{_ACCENT} Use a casual, charming female voice.",
    },
    "small_talk": {
        "voice": "shimmer",
        "instructions": f"{_ACCENT} Use a warm, older female voice with a friendly, neighborly tone.",
    },
    "internet": {
        "voice": "coral",
        "instructions": f"{_ACCENT} Use a young, energetic female voice.",
    },
    "restaurant": {
        "voice": "ash",
        "instructions": f"{_ACCENT} Use a suave, charming male voice.",
    },
    "mechanic": {
        "voice": "ash",
        "instructions": f"{_ACCENT} Use a deep male voice.",
    },
    "groceries": {
        "voice": "ash",
        "instructions": f"{_ACCENT} Use a casual, charming male voice.",
    },
    "contractor": {
        "voice": "ash",
        "instructions": f"{_ACCENT} Use a deep, husky baritone male voice.",
    },
    "core": {
        "voice": "ash",
        "instructions": f"{_ACCENT} Use a casual, friendly male voice.",
    },
    "grammar": {
        "voice": "ash",
        "instructions": f"{_ACCENT} Use a casual, friendly male voice.",
    },
}


def get_tts_instructions(
    animation_type: str,
    alt_language: str | None = None,
    situation_id: str | None = None,
) -> tuple[str, str | None]:
    """Return (voice, instructions) for TTS, adjusted for alt language mode.

    Grammar lessons all carry animation_type='grammar', but each chat lesson
    is mapped to a specific scene/character in GRAMMAR_SCENE_MAP (small_talk
    neighbor, restaurant waiter, contractor, etc.). When a situation_id is
    supplied for a grammar lesson, defer to the mapped scene's voice config
    so the audio matches the visual character — without this, every grammar
    chat speaks in the male `ash` core voice regardless of who's on screen.
    """
    key = animation_type
    if animation_type == "grammar" and situation_id:
        from app.data.situation_roles import GRAMMAR_SCENE_MAP
        mapped = GRAMMAR_SCENE_MAP.get(situation_id)
        if mapped:
            key = mapped
    cfg = SITUATION_VOICE_CONFIG.get(key, {})
    voice = cfg.get("voice", "alloy")
    instructions = cfg.get("instructions")
    if alt_language and instructions and alt_language in _ALT_ACCENTS:
        instructions = instructions.replace(_ACCENT, _ALT_ACCENTS[alt_language])
    return voice, instructions


@router.post("", response_model=CreateConversationResponse)
async def create_conversation(
    request: CreateConversationRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new conversation"""
    import logging
    logger = logging.getLogger(__name__)
    logger.info(f"🔍 POST /v1/conversations - User: {current_user.id}, Situation: {request.situation_id}, Mode: {request.mode}")
    situation = db.query(Situation).filter(Situation.id == request.situation_id).first()
    if not situation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Situation not found"
        )
    
    # Voice mode only - reuse words from existing conversation created by startSituation
    # startSituation creates a "text" mode conversation as the source of truth for words
    existing_conv = db.query(Conversation).filter(
        Conversation.user_id == current_user.id,
        Conversation.situation_id == request.situation_id,
        Conversation.mode == "text"
    ).order_by(Conversation.created_at.desc()).with_for_update().first()
    
    if existing_conv and existing_conv.target_word_ids:
        # Reuse existing conversation's words
        target_word_ids = existing_conv.target_word_ids
        words = get_words_by_ids(db, target_word_ids)
        final_words = sort_words_encounter_first(words, request.situation_id, db, target_word_ids)
        
        # Create or get voice conversation with same words
        voice_conv = db.query(Conversation).filter(
            Conversation.user_id == current_user.id,
            Conversation.situation_id == request.situation_id,
            Conversation.mode == "voice",
            Conversation.status == "active"
        ).order_by(Conversation.created_at.desc()).with_for_update().first()

        if voice_conv:
            # Reset spoken words so backend + frontend start from same empty state.
            # Without this, reused conversations carry stale used_spoken_word_ids
            # which causes completion to fire before all word chips show checkmarks.
            voice_conv.used_spoken_word_ids = []
            db.commit()

        if not voice_conv:
            voice_conv = Conversation(
                user_id=current_user.id,
                situation_id=request.situation_id,
                mode="voice",
                target_word_ids=target_word_ids,
                used_typed_word_ids=[],
                used_spoken_word_ids=[]
            )
            db.add(voice_conv)
            db.commit()
            db.refresh(voice_conv)
        
        vocab_level = get_vocab_level(db, current_user.id)
        grammar_level = get_grammar_level(db, current_user.id)
        language_mode = get_language_mode(situation.encounter_number, vocab_level, grammar_level)
        initial_message = get_initial_message_for_encounter(situation.id, situation.title, language_mode, alt_language=current_user.alt_language)

        # Alt language mode: swap words + adjust language_mode
        final_words = apply_alt_language(final_words, current_user.alt_language, db)
        if current_user.alt_language and language_mode in ("spanish_text", "spanish_audio"):
            language_mode = language_mode.replace("spanish_", f"{current_user.alt_language}_")

        # Use pre-generated R2 audio for initial message (no TTS call needed).
        # Audio files are uploaded by scripts/pregenerate_initial_audio.py with
        # deterministic filenames: initial_msg_{situation_id}.mp3
        from app.config import settings as _cfg
        initial_audio_url = f"{_cfg.r2_public_url}/initial_msg_{situation.id}.mp3" if _cfg.r2_public_url else None

        system_prompt = build_system_prompt(
            situation.animation_type, situation.id, language_mode,
            alt_language=current_user.alt_language,
        )
        return CreateConversationResponse(
            conversation_id=voice_conv.id,
            words=[WordSchema(id=w.id, spanish=w.spanish, english=w.english, notes=w.notes) for w in final_words],
            initial_message=initial_message,
            initial_audio_url=initial_audio_url,
            language_mode=language_mode,
            vocab_level=vocab_level,
            system_prompt=system_prompt,
        )
    else:
        # No existing conversation - this shouldn't happen if startSituation was called first
        # But create one anyway as fallback
        encounter_word_ids, high_freq_word_ids = select_words_for_situation(db, current_user.id, request.situation_id)
        target_word_ids = encounter_word_ids + high_freq_word_ids
        all_words = db.query(Word).filter(Word.id.in_(target_word_ids)).all()
        final_words = sort_words_encounter_first(all_words, request.situation_id, db, target_word_ids)
        
        conversation = Conversation(
            user_id=current_user.id,
            situation_id=request.situation_id,
            mode=request.mode,
            target_word_ids=target_word_ids,
            used_typed_word_ids=[],
            used_spoken_word_ids=[]
        )
        db.add(conversation)
        db.commit()
        db.refresh(conversation)
        
        vocab_level = get_vocab_level(db, current_user.id)
        grammar_level = get_grammar_level(db, current_user.id)
        language_mode = get_language_mode(situation.encounter_number, vocab_level, grammar_level)
        initial_message = get_initial_message_for_encounter(situation.id, situation.title, language_mode, alt_language=current_user.alt_language)

        # Alt language mode: swap words + adjust language_mode
        final_words = apply_alt_language(final_words, current_user.alt_language, db)
        if current_user.alt_language and language_mode in ("spanish_text", "spanish_audio"):
            language_mode = language_mode.replace("spanish_", f"{current_user.alt_language}_")

        # Use pre-generated R2 audio for initial message
        from app.config import settings as _cfg2
        initial_audio_url = f"{_cfg2.r2_public_url}/initial_msg_{situation.id}.mp3" if _cfg2.r2_public_url else None

        system_prompt = build_system_prompt(
            situation.animation_type, situation.id, language_mode,
            alt_language=current_user.alt_language,
        )
        return CreateConversationResponse(
            conversation_id=conversation.id,
            words=[WordSchema(id=w.id, spanish=w.spanish, english=w.english) for w in final_words],
            initial_message=initial_message,
            initial_audio_url=initial_audio_url,
            language_mode=language_mode,
            vocab_level=vocab_level,
            system_prompt=system_prompt,
        )


# Text chat endpoints removed - only voice chat is used now

@router.post("/check-pronunciation")
async def check_pronunciation(
    audio: UploadFile = File(...),
    expected_word: str = Form(...),
    current_user: User = Depends(get_current_user),
):
    """Lightweight pronunciation check: STT + string match. No LLM, no TTS."""
    import logging
    import re
    import unicodedata
    logger = logging.getLogger(__name__)

    audio_bytes = await audio.read()
    logger.info(f"[PronCheck] Checking pronunciation: expected='{expected_word}', audio={len(audio_bytes)} bytes")

    transcript = await gateway_transcribe_audio(
        audio_bytes=audio_bytes,
        filename=audio.filename or "audio.mp3",
        prompt=f"The user is saying a {get_target_language_name(current_user.alt_language)} word or phrase: {expected_word}. Transcribe exactly what they say.",
        language=None,
        request_id=str(current_user.id),
        user_id=str(current_user.id),
    )

    # Normalize for comparison: lowercase, strip accents, remove punctuation
    def normalize(s: str) -> str:
        s = s.lower().strip()
        s = unicodedata.normalize('NFD', s)
        s = re.sub(r'[\u0300-\u036f]', '', s)  # Remove accent marks
        s = s.replace('ñ', 'n')
        s = re.sub(r'[.,!?;:\'"¿¡]', '', s)
        s = re.sub(r'\s+', ' ', s).strip()
        return s

    norm_transcript = normalize(transcript)
    norm_expected = normalize(expected_word)
    is_correct = norm_transcript == norm_expected

    logger.info(f"[PronCheck] transcript='{transcript}' norm='{norm_transcript}' expected_norm='{norm_expected}' correct={is_correct}")

    return {"transcript": transcript, "is_correct": is_correct}


def _normalize_word_id(word_id: str) -> str:
    """Map synthetic frontend chip ids to their persisted base word_id.

    Grammar conjugation chips are synthesized client-side as `conj_<verb>_<pronoun>`
    (e.g. `conj_vivir_nosotros`) and never exist in the `words` table. Mastery
    tracking for grammar situations lives on the infinitive (`grammar_<verb>`),
    so we collapse the conjugation back to the base before any DB write.
    """
    if word_id.startswith("conj_"):
        parts = word_id.split("_")
        if len(parts) >= 3:
            return f"grammar_{parts[1]}"
    return word_id


@router.post("/{conversation_id}/mark-word")
async def mark_word_detected(
    conversation_id: str,
    word_id: str = Form(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Manually mark a word as detected (user override for STT failures)."""
    import logging
    logger = logging.getLogger(__name__)

    conversation = db.query(Conversation).filter(
        Conversation.id == conversation_id,
        Conversation.user_id == current_user.id,
    ).first()
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    normalized_word_id = _normalize_word_id(word_id)

    was_empty = len(conversation.used_spoken_word_ids or []) == 0
    current_used = set(conversation.used_spoken_word_ids or [])
    current_used.add(normalized_word_id)
    conversation.used_spoken_word_ids = list(current_used)

    from app.services.conversation_service import update_user_word_stats, check_conversation_complete, get_missing_word_ids
    update_user_word_stats(db, str(current_user.id), [normalized_word_id], "voice")

    if was_empty and conversation.conversation_type == "lesson":
        target_set = set(conversation.target_word_ids or [])
        if normalized_word_id in target_set:
            db.execute(
                pg_insert(UserMilestoneEvent)
                .values(
                    user_id=current_user.id,
                    milestone_key="first_word",
                    situation_id=conversation.situation_id,
                    conversation_id=conversation.id,
                )
                .on_conflict_do_nothing(constraint="uq_user_milestone_situation")
            )

    conversation_complete = check_conversation_complete(conversation, "voice")
    if conversation_complete:
        conversation.status = "complete"
        conversation.completed_at = datetime.now(timezone.utc)

    db.commit()
    missing_word_ids = get_missing_word_ids(conversation, "voice")
    logger.info(f"[MarkWord] User {current_user.id} marked word {word_id} (normalized={normalized_word_id}) in conversation {conversation_id}")

    return {
        "word_id": normalized_word_id,
        "missing_word_ids": missing_word_ids,
        "conversation_complete": conversation_complete,
    }


def _sync_tts(text, output_path, voice, instructions, request_id, user_id, db, learning_phase):
    """Synchronous TTS wrapper for use with run_in_executor."""
    import asyncio
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(gateway_synthesize_speech(
            text=text, output_path=output_path,
            voice=voice, instructions=instructions,
            request_id=request_id, user_id=user_id,
            db=db, learning_phase=learning_phase,
        ))
    finally:
        loop.close()


@router.get("/debug/stream-test")
async def stream_test():
    """Diagnostic: test if NDJSON streaming actually flushes through middleware.
    Yields two events 3s apart. If the client receives them 3s apart, streaming works.
    If both arrive together after 3s, middleware is buffering."""
    import asyncio
    async def generate():
        yield json_module.dumps({"type": "ping", "time": "t=0s", "message": "If you see this immediately, streaming works"}) + "\n"
        await asyncio.sleep(3)
        yield json_module.dumps({"type": "pong", "time": "t=3s", "message": "This should arrive 3s after ping"}) + "\n"
    return StreamingResponse(generate(), media_type="application/x-ndjson")


@router.post("/{conversation_id}/voice-turn")
async def voice_turn_transcribe(
    conversation_id: str,
    request: Request,
    audio: UploadFile = File(...),
    messages_json: Optional[str] = Form(None),
    # When set, the FE knows exactly what sentence the user is being asked
    # to produce (drill phase). Bias STT toward that exact sentence the same
    # way /check-pronunciation does — without the bias Whisper free-runs and
    # routinely garbles short target sentences (e.g. "nuestras familias"
    # transcribed as "¿Cómo estás, Daniel?").
    expected_text: Optional[str] = Form(None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Step 1: STT → word detection → DB update. Returns transcript immediately.
    Frontend then calls /voice-turn/respond with the transcript for LLM+TTS."""
    import time
    import logging
    logger = logging.getLogger(__name__)
    start_time = time.time()
    request_id = getattr(request.state, "request_id", "unknown")
    learning_phase = request.headers.get("X-Learning-Phase", "2")
    request.state.user_id = current_user.id

    conversation = db.query(Conversation).filter(
        Conversation.id == conversation_id,
        Conversation.user_id == current_user.id
    ).first()
    if not conversation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")
    if conversation.mode != "voice":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This endpoint is for voice mode only")

    audio_bytes = await audio.read()
    words = get_words_by_ids(db, conversation.target_word_ids)
    situation = db.query(Situation).filter(Situation.id == conversation.situation_id).first()

    alt_language = current_user.alt_language
    words = apply_alt_language(words, alt_language, db)

    if expected_text:
        # Drill mode — bias STT to the exact sentence so a near-miss doesn't
        # come back as a wildly off transcript. Phrasing mirrors the
        # benchmarked /check-pronunciation prompt (see line 653) exactly,
        # only swapping "word or phrase" for "sentence".
        transcription_prompt = (
            f"The user is saying a {get_target_language_name(alt_language)} sentence: "
            f"{expected_text}. Transcribe exactly what they say."
        )
    else:
        transcription_prompt = build_transcription_prompt(
            situation.title if situation else "a situation", words, alt_language=alt_language,
        )

    stt_start = time.time()
    user_transcript = await gateway_transcribe_audio(
        audio_bytes=audio_bytes, filename=audio.filename or "audio.mp3",
        prompt=transcription_prompt, language=None,
        request_id=request_id, user_id=str(current_user.id),
        db=db, learning_phase=learning_phase,
    )
    stt_time = time.time() - stt_start
    logger.info(f"[Voice Turn] STT: {stt_time:.2f}s, transcript: '{user_transcript}'")
    if stt_time > 2.0:
        logger.warning(f"[Voice Turn] STT exceeded 2s threshold: {stt_time:.2f}s")

    # Shared with /realtime-turn: detects words (grammar-aware when applicable),
    # extends used_spoken_word_ids, upserts user_words counters, records the
    # first_word milestone, and increments turn_count.
    _, detected_word_ids = persist_turn(
        db=db,
        conversation=conversation,
        user_id=current_user.id,
        user_transcript=user_transcript,
        assistant_text="",
        alt_language=alt_language,
    )
    missing_word_ids = get_missing_word_ids(conversation, "voice")
    db.commit()

    total = time.time() - start_time
    logger.info(f"[Voice Turn] Transcribe total: {total:.2f}s (stt: {stt_time:.2f}s)")

    return {
        "user_transcript": user_transcript,
        "detected_word_ids": detected_word_ids,
        "missing_word_ids": missing_word_ids,
    }


from pydantic import BaseModel as _BaseModel

class _RespondRequest(_BaseModel):
    user_transcript: str
    messages_json: Optional[str] = None


@router.post("/{conversation_id}/voice-turn/respond")
async def voice_turn_respond(
    conversation_id: str,
    body: _RespondRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Step 2: LLM → TTS → R2 upload. Returns AI response + audio URL."""
    import time
    import logging
    logger = logging.getLogger(__name__)
    start_time = time.time()
    request_id = getattr(request.state, "request_id", "unknown")
    learning_phase = request.headers.get("X-Learning-Phase", "2")
    request.state.user_id = current_user.id

    conversation = db.query(Conversation).filter(
        Conversation.id == conversation_id,
        Conversation.user_id == current_user.id
    ).first()
    if not conversation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")

    words = get_words_by_ids(db, conversation.target_word_ids)
    situation = db.query(Situation).filter(Situation.id == conversation.situation_id).first()
    alt_language = current_user.alt_language
    words = apply_alt_language(words, alt_language, db)

    user_transcript = body.user_transcript

    # Parse frontend messages
    frontend_messages = None
    if body.messages_json:
        try:
            frontend_messages = json_module.loads(body.messages_json)
        except (json_module.JSONDecodeError, TypeError):
            pass

    vocab_level = get_vocab_level(db, current_user.id)
    grammar_level = get_grammar_level(db, current_user.id)
    language_mode = get_language_mode(situation.encounter_number, vocab_level, grammar_level)
    if alt_language and language_mode in ("spanish_text", "spanish_audio"):
        language_mode = language_mode.replace("spanish_", f"{alt_language}_")

    # Word guidance — steer AI toward unused target words
    missing_ids = get_missing_word_ids(conversation, "voice")
    word_guidance_system = ""

    # For grammar situations with drill_targets, build specific verb+pronoun guidance
    grammar_cfg = get_grammar_config(conversation.situation_id)
    drill_targets = grammar_cfg.get("drill_targets", []) if grammar_cfg else []
    grammar_inject_message = None  # assistant "thinking" message for grammar targeting
    if drill_targets and grammar_cfg.get("drill_config", {}).get("answers"):
        answers = grammar_cfg["drill_config"]["answers"]
        # Find which conjugated forms the user has already said
        import re as _re
        def _extract_words(text: str) -> set:
            return set(_re.sub(r'[.,!?¿¡]', '', text.lower()).split())
        transcript_words = set()
        if body.messages_json:
            try:
                for msg in json_module.loads(body.messages_json):
                    if msg.get("role") == "user":
                        transcript_words.update(_extract_words(msg["content"]))
            except (json_module.JSONDecodeError, TypeError):
                pass
        transcript_words.update(_extract_words(user_transcript))

        # Find first remaining target
        next_target = None
        for t in drill_targets:
            verb, pronoun = t["verb"], t["pronoun"]
            conjugated = answers.get(verb, {}).get(pronoun, "")
            if conjugated and conjugated.lower() not in transcript_words:
                next_target = {"verb": verb, "pronoun": pronoun, "conjugated": conjugated}
                break

        if next_target:
            from app.data.grammar_situations import GRAMMAR_WORD_TRANSLATIONS
            v, p, c = next_target["verb"], next_target["pronoun"], next_target["conjugated"]
            eng = GRAMMAR_WORD_TRANSLATIONS.get(v, v)
            # Build a pronoun-appropriate hint question
            hint = _build_grammar_hint(p, v, eng)
            grammar_inject_message = (
                f"Next I need to get the student to say '{c}' ({p} + {v}). "
                f"I'll ask exactly: \"{hint}\""
            )
    elif missing_ids:
        missing_words = get_words_by_ids(db, missing_ids)
        lang = get_target_language_name(alt_language)
        missing_pairs = [f"{w.spanish} ({w.english})" for w in missing_words]
        word_guidance_system = (
            f"\n\nThe student still needs to say these {lang} words: {', '.join(missing_pairs)}. "
            f"Steer the conversation toward topics where they'd naturally use them. "
            f"Don't say the target {lang} words yourself."
        )

    # Build messages for Realtime API
    # Always build the system prompt — frontend messages don't include it
    grammar_config_for_prompt = get_grammar_config(conversation.situation_id)
    if grammar_config_for_prompt:
        system_prompt = build_grammar_system_prompt(conversation.situation_id, language_mode=language_mode, alt_language=alt_language)
    else:
        system_prompt = get_conversation_system_prompt(
            language_mode, alt_language=alt_language,
            animation_type=situation.animation_type if situation else "",
            situation_id=conversation.situation_id,
        )

    # Append word guidance to system prompt (non-grammar situations only)
    if not grammar_inject_message:
        system_prompt += word_guidance_system

    if frontend_messages:
        llm_messages = [{"role": "system", "content": system_prompt}]
        for msg in frontend_messages:
            if msg["role"] != "system":
                llm_messages.append(msg)
        if grammar_inject_message:
            # Grammar: inject assistant "thinking" with the next target + hint
            llm_messages.append({"role": "user", "content": user_transcript})
            llm_messages.append({"role": "assistant", "content": grammar_inject_message})
        else:
            llm_messages.append({"role": "user", "content": user_transcript})
    else:
        grammar_config = get_grammar_config(conversation.situation_id)
        if grammar_config:
            system_prompt = build_grammar_system_prompt(conversation.situation_id, language_mode=language_mode, alt_language=alt_language)
            user_prompt = build_grammar_user_prompt(
                situation.title, conversation.used_spoken_word_ids or [],
                user_transcript, grammar_config,
            )
        else:
            system_prompt = get_conversation_system_prompt(
                language_mode, alt_language=alt_language,
                animation_type=situation.animation_type if situation else "",
                situation_id=conversation.situation_id,
            ) + word_guidance_system
            user_prompt = build_conversation_prompt(
                situation.title, words, conversation.used_spoken_word_ids or [],
                user_transcript, alt_language=alt_language,
            )
        llm_messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        if grammar_inject_message:
            llm_messages.append({"role": "assistant", "content": grammar_inject_message})

    # TTS voice config
    tts_voice, tts_instructions = get_tts_instructions(
        situation.animation_type if situation else "",
        alt_language=alt_language,
        situation_id=situation.id if situation else None,
    )

    # Log full messages object for debugging
    logger.info(f"[Voice Turn] Realtime messages for {conversation.situation_id} (voice={tts_voice}):\n"
                 + json_module.dumps(llm_messages, indent=2, ensure_ascii=False))

    # ── Realtime API: stream LLM + TTS as NDJSON ──
    # Audio chunks arrive at ~0.8s. Frontend plays PCM16 via Web Audio API.
    from app.services.realtime_service import stream_realtime
    import base64 as _base64

    async def generate_stream():
        assistant_text = ""
        try:
            async for event in stream_realtime(
                messages=llm_messages,
                voice=tts_voice,
                tts_instructions=tts_instructions,
                request_id=request_id,
            ):
                if event["type"] == "audio":
                    yield json_module.dumps({
                        "type": "audio",
                        "data": _base64.b64encode(event["data"]).decode(),
                    }) + "\n"

                elif event["type"] == "text":
                    assistant_text = event["text"]
                    yield json_module.dumps({
                        "type": "text",
                        "text": assistant_text,
                    }) + "\n"

                elif event["type"] == "done":
                    # Refresh conversation from DB to ensure we have latest used_spoken_word_ids
                    db.refresh(conversation)
                    conv_complete, _ = check_completion(conversation)
                    logger.info(
                        f"[Voice Turn] Completion check: target={conversation.target_word_ids}, "
                        f"spoken={conversation.used_spoken_word_ids}, turns={conversation.turn_count}, "
                        f"complete={conv_complete}"
                    )
                    if conv_complete:
                        conversation.status = "complete"
                        conversation.completed_at = datetime.now(timezone.utc)
                    db.commit()

                    total = time.time() - start_time
                    logger.info(f"[Voice Turn] Realtime stream: {total:.2f}s, text='{assistant_text[:60]}'")

                    yield json_module.dumps({
                        "type": "done",
                        "conversation_complete": conv_complete,
                    }) + "\n"

        except Exception as e:
            logger.error(f"[Voice Turn] Realtime stream failed: {e}")
            yield json_module.dumps({"type": "error", "message": str(e)}) + "\n"

    return StreamingResponse(generate_stream(), media_type="application/x-ndjson")


@router.post(
    "/{conversation_id}/realtime-turn",
    response_model=RealtimeTurnResponse,
)
async def realtime_turn(
    conversation_id: str,
    body: RealtimeTurnRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Ingest one completed realtime-voice turn.

    The browser streams audio directly to OpenAI over WebRTC (see
    `POST /v1/realtime/sessions`), so the backend doesn't see the audio or
    control endpointing. After each turn the FE POSTs the finalized
    transcripts here so we can:
      - run deterministic word detection against the conversation's targets,
      - extend `used_spoken_word_ids` and bump mastery counters,
      - increment `turn_count` and enforce the 30-turn hard limit,
      - record the `first_word` milestone for new lesson conversations,
      - report back the current state so the FE can update chips,
        countdowns, and close the peer connection on completion.

    Parity note: the word detection, persistence, and completion logic are
    the same helpers `/voice-turn` calls — splitting by flow would be a
    parity bug waiting to happen.
    """
    request.state.user_id = current_user.id

    conversation = db.query(Conversation).filter(
        Conversation.id == conversation_id,
        Conversation.user_id == current_user.id,
    ).first()
    if not conversation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found"
        )
    if conversation.mode != "voice":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This endpoint is for voice mode only",
        )

    _, detected_word_ids = persist_turn(
        db=db,
        conversation=conversation,
        user_id=current_user.id,
        user_transcript=body.user_transcript,
        assistant_text=body.assistant_text,
        alt_language=current_user.alt_language,
    )

    complete, turns_remaining = check_completion(conversation)
    if complete and conversation.status != "complete":
        conversation.status = "complete"
        conversation.completed_at = datetime.now(timezone.utc)

    db.commit()
    missing_word_ids = get_missing_word_ids(conversation, "voice")

    return RealtimeTurnResponse(
        detected_word_ids=detected_word_ids,
        missing_word_ids=missing_word_ids,
        conversation_complete=complete,
        turns_remaining=turns_remaining,
    )
