from typing import List, Optional
from app.models import Word, Situation
from app.data.grammar_situations import get_grammar_config
from app.data.situation_roles import (
    get_roles_for_situation,
    get_grammar_structure,
    GRAMMAR_SCENE_MAP,
)


def get_language_mode(encounter_number: int, vocab_level: int, grammar_level: float = 0) -> str:
    """Derive language mode from vocab level and grammar level.

    Spanish mode when BOTH: VL >= 500 AND GL >= 10.
    Otherwise English.
    """
    if vocab_level >= 500 and grammar_level >= 10:
        return "spanish_text"
    return "english"


def is_advanced_mode(language_mode: str) -> bool:
    """Return True if the language mode means the AI should speak in the target language."""
    return language_mode in (
        "spanish_text", "spanish_audio",
        "catalan_text", "catalan_audio",
    )


def build_system_prompt(
    animation_type: str,
    situation_id: str,
    language_mode: str = "english",
    catalan_mode: bool = False,
) -> str:
    """Build the system prompt for conversation or grammar agents.

    Uses role data from situation_roles.py and templates from prompts.json.
    """
    from app.services.llm_gateway import load_prompt

    language = "Catalan" if catalan_mode else "Spanish"
    roles = get_roles_for_situation(animation_type, situation_id)
    advanced = is_advanced_mode(language_mode)

    # Check if this is a grammar situation
    grammar_struct = get_grammar_structure(situation_id)
    grammar_config = get_grammar_config(situation_id)

    if grammar_struct or grammar_config:
        template_key = "grammar_agent_advanced" if advanced else "grammar_agent_beginner"
        template = load_prompt(template_key, "v2")

        # Build grammar_structure description
        structure_desc = grammar_struct["grammar_structure"] if grammar_struct else grammar_config.get("title", "")

        # Build examples from drill_targets if available (new multi-lesson format)
        drill_targets = grammar_config.get("drill_targets", []) if grammar_config else []
        if drill_targets and grammar_config and grammar_config.get("drill_config", {}).get("answers"):
            answers = grammar_config["drill_config"]["answers"]
            lines = []
            for t in drill_targets:
                verb = t.get("verb", "")
                pronoun = t.get("pronoun", "")
                conjugated = answers.get(verb, {}).get(pronoun, "")
                if conjugated:
                    lines.append(f"- {pronoun} + {verb} → {conjugated}")
            examples_text = "\n".join(lines)
        elif grammar_struct:
            examples_text = "\n".join(f"- \"{ex}\"" for ex in grammar_struct["examples"])
        else:
            examples_text = ""

        return template.format(
            ai_role=roles["ai_role"],
            user_role=roles["user_role"],
            situation_description=roles["situation_description"],
            language=language,
            grammar_structure=structure_desc,
            grammar_examples=examples_text,
        )
    else:
        template_key = "conversation_agent_advanced" if advanced else "conversation_agent_beginner"
        template = load_prompt(template_key, "v2")
        return template.format(
            ai_role=roles["ai_role"],
            user_role=roles["user_role"],
            situation_description=roles["situation_description"],
            language=language,
        )


def build_transcription_prompt(situation_title: str, words: List[Word], catalan_mode: bool = False) -> str:
    """Build a context prompt for STT transcription (whisper-style format).

    Benchmark showed this format gives 0.997 accuracy + 100% Spanish word
    detection on gpt-4o-mini-transcribe, beating both whisper-1 and
    gpt-4o-transcribe.
    """
    word_phrase_list = ", ".join([w.spanish for w in words])
    lang = "Catalan" if catalan_mode else "Spanish"
    return (
        f"This is a conversation about {situation_title}. "
        f"The user is learning {lang} and may use these {lang} words and phrases: {word_phrase_list}. "
        f"The conversation is in {lang} and English."
    )


# ── Legacy functions (kept for backward compatibility during transition) ──────

def build_grammar_system_prompt(situation_id: str, catalan_mode: bool = False) -> Optional[str]:
    """Build a system prompt for grammar conversation phases (2/3)."""
    config = get_grammar_config(situation_id)
    if not config:
        return None
    language_mode = "catalan_text" if catalan_mode else "spanish_text"
    return build_system_prompt("grammar", situation_id, language_mode, catalan_mode)


def build_grammar_user_prompt(
    situation_title: str,
    used_spoken_word_ids: List[str],
    user_transcript: str,
    config: dict,
) -> str:
    """Build user prompt for grammar conversation turn."""
    p2_config = config.get("phase_2_config", {}) or {}
    description = p2_config.get("description", "Practice grammar structures")

    return (
        f"Grammar Situation: {situation_title}\n"
        f"Goal: {description}\n"
        f"User said: {user_transcript}\n\n"
        f"Continue the practice session."
    )


def get_conversation_system_prompt(
    language_mode: str = "english",
    catalan_mode: bool = False,
    animation_type: str = "",
    situation_id: str = "",
) -> str:
    """Build the conversation system prompt with role context."""
    return build_system_prompt(animation_type, situation_id, language_mode, catalan_mode)


def build_conversation_prompt(
    situation_title: str,
    words: List[Word],
    used_spoken_word_ids: List[str],
    user_transcript: str,
    catalan_mode: bool = False,
) -> str:
    """Build the user prompt for the conversation LLM (used when no message history)."""
    used_words = [w.spanish for w in words if w.id in used_spoken_word_ids]
    missing_words_info = [
        f"{w.spanish} ({w.english})"
        for w in words
        if w.id not in used_spoken_word_ids
    ]
    lang = "Catalan" if catalan_mode else "Spanish"

    return (
        f"Situation: {situation_title}\n"
        f"Still need: {', '.join(missing_words_info) if missing_words_info else 'All words used'}\n"
        f"Already used: {', '.join(used_words) if used_words else 'None'}\n"
        f"User said: {user_transcript}\n\n"
        f"Ask a natural question requiring a missing {lang} word. Do NOT mention the {lang} word."
    )
