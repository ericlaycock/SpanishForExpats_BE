"""Prompt integrity tests for the v2 template prompt system.

Pure Python tests (no DB needed) that validate prompt templates,
role data, and system prompt generation.
Run with: python3.11 -m pytest tests/test_prompts.py --noconftest -v
"""

import pytest

from app.services.llm_gateway import load_prompt
from app.services.voice_turn_service import (
    get_conversation_system_prompt,
    build_conversation_prompt,
    build_system_prompt,
)
from app.data.situation_roles import (
    SITUATION_ROLES,
    GRAMMAR_SCENE_MAP,
    GRAMMAR_STRUCTURES,
    get_roles_for_situation,
    get_grammar_structure,
)
from app.data.grammar_situations import GRAMMAR_SITUATIONS


# ── v2 template prompt IDs ──────────────────────────────────────────────────

V2_PROMPTS = [
    "conversation_agent_beginner",
    "conversation_agent_advanced",
    "grammar_agent_beginner",
    "grammar_agent_advanced",
]


class TestPromptsLoad:
    @pytest.mark.parametrize("agent_id", V2_PROMPTS)
    def test_all_prompts_load(self, agent_id):
        """Every prompt template in prompts.json loads successfully."""
        content = load_prompt(agent_id)
        assert isinstance(content, str)
        assert len(content) > 0

    def test_conversation_templates_have_ai_role(self):
        """Conversation templates contain {ai_role} placeholder."""
        for agent_id in ["conversation_agent_beginner", "conversation_agent_advanced"]:
            content = load_prompt(agent_id)
            assert "{ai_role}" in content

    def test_grammar_templates_have_examples(self):
        """Grammar templates contain {grammar_examples} placeholder."""
        for agent_id in ["grammar_agent_beginner", "grammar_agent_advanced"]:
            content = load_prompt(agent_id)
            assert "{grammar_examples}" in content

    def test_advanced_templates_have_language_placeholder(self):
        """Advanced templates contain {language} placeholder for Spanish/Catalan."""
        for agent_id in ["conversation_agent_advanced", "grammar_agent_advanced"]:
            content = load_prompt(agent_id)
            assert "{language}" in content, f"{agent_id} missing {{language}}"

    def test_beginner_conversation_speaks_english(self):
        """Beginner conversation template says 'Speak only in English'."""
        content = load_prompt("conversation_agent_beginner")
        assert "Speak only in English" in content

    def test_beginner_grammar_speaks_english(self):
        """Beginner grammar template enforces English."""
        content = load_prompt("grammar_agent_beginner")
        assert "English" in content


class TestSituationRoles:
    def test_all_main_situations_defined(self):
        """All 11 scene types (10 main + core) have role definitions."""
        expected = {"airport", "banking", "clothing", "contractor", "groceries",
                    "mechanic", "police", "restaurant", "small_talk", "internet", "core"}
        assert set(SITUATION_ROLES.keys()) == expected

    def test_each_role_has_required_fields(self):
        """Every role dict has ai_role, user_role, situation_description."""
        for anim_type, roles in SITUATION_ROLES.items():
            assert "ai_role" in roles, f"{anim_type} missing ai_role"
            assert "user_role" in roles, f"{anim_type} missing user_role"
            assert "situation_description" in roles, f"{anim_type} missing situation_description"

    def test_all_grammar_situations_mapped(self):
        """All grammar situations map to a valid scene."""
        assert len(GRAMMAR_SCENE_MAP) == len(GRAMMAR_SITUATIONS)
        for grammar_id, scene in GRAMMAR_SCENE_MAP.items():
            assert scene in SITUATION_ROLES, f"{grammar_id} maps to unknown scene '{scene}'"

    def test_legacy_grammar_situations_have_structures(self):
        """Grammar situations without drill_targets have GRAMMAR_STRUCTURES entries."""
        for grammar_id in GRAMMAR_SCENE_MAP:
            cfg = GRAMMAR_SITUATIONS.get(grammar_id, {})
            has_drill_targets = bool(cfg.get("drill_targets"))
            if not has_drill_targets:
                struct = GRAMMAR_STRUCTURES.get(grammar_id)
                # Allow fallback to base name (e.g., grammar_regular_present for grammar_regular_present_1)
                if struct is None:
                    base_name = "_".join(grammar_id.rsplit("_", 1)[:-1]) if grammar_id[-1].isdigit() else grammar_id
                    struct = GRAMMAR_STRUCTURES.get(base_name)
                assert struct is not None, f"{grammar_id} has no drill_targets and no GRAMMAR_STRUCTURES entry"
                assert "grammar_structure" in struct
                assert "examples" in struct

    def test_get_roles_for_main_situation(self):
        """get_roles_for_situation returns correct roles for main situations."""
        roles = get_roles_for_situation("banking")
        assert "bank teller" in roles["ai_role"]

    def test_get_roles_for_grammar_situation(self):
        """get_roles_for_situation maps grammar situations to their scene."""
        roles = get_roles_for_situation("grammar", "grammar_pronouns")
        # grammar_pronouns maps to "core"
        assert "Eric" in roles["ai_role"]


class TestBuildSystemPrompt:
    def test_beginner_spanish(self):
        """Beginner mode says 'Speak only in English'."""
        prompt = build_system_prompt("banking", "bank_1", "english", catalan_mode=False)
        assert "Speak only in English" in prompt
        assert "bank teller" in prompt

    def test_advanced_spanish(self):
        """Advanced mode says 'Speak in Spanish'."""
        prompt = build_system_prompt("banking", "bank_1", "spanish_text", catalan_mode=False)
        assert "Speak in Spanish" in prompt
        assert "Speak only in English" not in prompt

    def test_beginner_catalan(self):
        """Catalan beginner mode still says 'Speak only in English' (beginner = English)."""
        prompt = build_system_prompt("police", "pol_1", "english", catalan_mode=True)
        assert "Speak only in English" in prompt
        assert "police officer" in prompt

    def test_advanced_catalan(self):
        """Catalan advanced mode says 'Speak in Catalan'."""
        prompt = build_system_prompt("police", "pol_1", "catalan_text", catalan_mode=True)
        assert "Speak in Catalan" in prompt

    def test_grammar_prompt_includes_examples(self):
        """Grammar prompts include drill target examples."""
        prompt = build_system_prompt("grammar", "grammar_pronouns", "english", catalan_mode=False)
        assert "My wife" in prompt  # One of the legacy examples

    def test_grammar_prompt_with_drill_targets(self):
        """Grammar prompts for multi-lesson situations include verb+pronoun targets."""
        prompt = build_system_prompt("grammar", "grammar_regular_present_1", "english", catalan_mode=False)
        assert "grammar practice" in prompt.lower()
        assert "hablar" in prompt  # One of the target verbs
        assert "pronoun" in prompt.lower()  # Has pronoun guide


class TestGetConversationSystemPrompt:
    def test_english_mode_default(self):
        """english mode → beginner template, speaks English."""
        prompt = get_conversation_system_prompt("english", catalan_mode=False)
        assert "Speak only in English" in prompt

    def test_english_mode_catalan(self):
        """english mode, catalan_mode=True → beginner template, speaks English."""
        prompt = get_conversation_system_prompt("english", catalan_mode=True)
        assert "Speak only in English" in prompt

    def test_spanish_text_mode(self):
        """spanish_text → advanced template, speaks Spanish."""
        prompt = get_conversation_system_prompt("spanish_text", catalan_mode=False)
        assert "Speak in Spanish" in prompt
        assert "Speak only in English" not in prompt

    def test_spanish_audio_mode(self):
        """spanish_audio → advanced template."""
        prompt = get_conversation_system_prompt("spanish_audio", catalan_mode=False)
        assert "Speak in Spanish" in prompt

    def test_catalan_text_mode(self):
        """catalan_text, catalan_mode=True → advanced template with Catalan."""
        prompt = get_conversation_system_prompt("catalan_text", catalan_mode=True)
        assert "Speak in Catalan" in prompt

    def test_catalan_audio_mode(self):
        """catalan_audio, catalan_mode=True → advanced template with Catalan."""
        prompt = get_conversation_system_prompt("catalan_audio", catalan_mode=True)
        assert "Speak in Catalan" in prompt


class TestBuildConversationPrompt:
    def test_spanish_mode_default(self):
        """Default build_conversation_prompt says 'Spanish'."""
        prompt = build_conversation_prompt(
            situation_title="Test",
            words=[],
            used_spoken_word_ids=[],
            user_transcript="hello",
            catalan_mode=False,
        )
        assert "Spanish" in prompt
        assert "Catalan" not in prompt

    def test_catalan_mode(self):
        """catalan_mode=True build_conversation_prompt says 'Catalan'."""
        prompt = build_conversation_prompt(
            situation_title="Test",
            words=[],
            used_spoken_word_ids=[],
            user_transcript="hello",
            catalan_mode=True,
        )
        assert "Catalan" in prompt
        assert "Spanish" not in prompt
