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
    "conversation_agent",
    "grammar_agent",
]


class TestPromptsLoad:
    @pytest.mark.parametrize("agent_id", V2_PROMPTS)
    def test_all_prompts_load(self, agent_id):
        """Every prompt template in prompts.json loads successfully."""
        content = load_prompt(agent_id)
        assert isinstance(content, str)
        assert len(content) > 0

    def test_conversation_template_has_placeholders(self):
        """Conversation template contains required placeholders."""
        content = load_prompt("conversation_agent")
        assert "{ai_role}" in content
        assert "{language}" in content

    def test_grammar_template_loads(self):
        """Grammar template loads and contains key instructions."""
        content = load_prompt("grammar_agent")
        assert "grammar practice" in content.lower()
        assert "assistant messages" in content.lower()
        assert "{language}" in content

    def test_templates_speak_in_language(self):
        """Templates use {language} placeholder (always target language, no English mode)."""
        for agent_id in V2_PROMPTS:
            content = load_prompt(agent_id)
            assert "{language}" in content, f"{agent_id} missing {{language}}"
            assert "Speak only in English" not in content, f"{agent_id} should not enforce English"


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
        assert "Eric" in roles["ai_role"]


class TestBuildSystemPrompt:
    def test_spanish_default(self):
        """Default mode (no alt_language) says 'Speak in Spanish'."""
        prompt = build_system_prompt("banking", "bank_1", "spanish_text", alt_language=None)
        assert "Speak in Spanish" in prompt
        assert "bank teller" in prompt

    def test_catalan_mode(self):
        """alt_language='catalan' says 'Speak in Catalan'."""
        prompt = build_system_prompt("police", "pol_1", "catalan_text", alt_language="catalan")
        assert "Speak in Catalan" in prompt
        assert "police officer" in prompt

    def test_swedish_mode(self):
        """alt_language='swedish' says 'Speak in Swedish'."""
        prompt = build_system_prompt("banking", "bank_1", "swedish_text", alt_language="swedish")
        assert "Speak in Swedish" in prompt

    def test_grammar_prompt_is_concise(self):
        """Grammar system prompt is short — targeting is via injected assistant messages."""
        prompt = build_system_prompt("grammar", "grammar_regular_present_1", "spanish_text", alt_language=None)
        assert "grammar practice" in prompt.lower()
        assert "Speak in Spanish" in prompt
        assert "assistant messages" in prompt.lower()


class TestGetConversationSystemPrompt:
    def test_spanish_text_mode(self):
        """spanish_text → speaks Spanish."""
        prompt = get_conversation_system_prompt("spanish_text", alt_language=None)
        assert "Speak in Spanish" in prompt

    def test_catalan_text_mode(self):
        """catalan_text, alt_language='catalan' → speaks Catalan."""
        prompt = get_conversation_system_prompt("catalan_text", alt_language="catalan")
        assert "Speak in Catalan" in prompt

    def test_swedish_text_mode(self):
        """swedish_text, alt_language='swedish' → speaks Swedish."""
        prompt = get_conversation_system_prompt("swedish_text", alt_language="swedish")
        assert "Speak in Swedish" in prompt


class TestBuildConversationPrompt:
    def test_spanish_mode_default(self):
        """Default build_conversation_prompt says 'Spanish'."""
        prompt = build_conversation_prompt(
            situation_title="Test",
            words=[],
            used_spoken_word_ids=[],
            user_transcript="hello",
            alt_language=None,
        )
        assert "Spanish" in prompt
        assert "Catalan" not in prompt

    def test_catalan_mode(self):
        """alt_language='catalan' build_conversation_prompt says 'Catalan'."""
        prompt = build_conversation_prompt(
            situation_title="Test",
            words=[],
            used_spoken_word_ids=[],
            user_transcript="hello",
            alt_language="catalan",
        )
        assert "Catalan" in prompt
        assert "Spanish" not in prompt

    def test_swedish_mode(self):
        """alt_language='swedish' build_conversation_prompt says 'Swedish'."""
        prompt = build_conversation_prompt(
            situation_title="Test",
            words=[],
            used_spoken_word_ids=[],
            user_transcript="hello",
            alt_language="swedish",
        )
        assert "Swedish" in prompt
        assert "Spanish" not in prompt
