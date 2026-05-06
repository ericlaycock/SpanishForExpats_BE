"""Unit tests for the lesson-context block injected into the realtime
system prompt.

Pure-Python tests — no DB needed. Hit `_render_lesson_block` directly
and `build_realtime_system_prompt` end-to-end with a known
animation_type so the role lookup resolves.

Run: python3.11 -m pytest tests/test_services/test_realtime_lesson_context.py --noconftest -v
"""
from __future__ import annotations

from app.services.voice_turn_service import (
    _render_lesson_block,
    build_realtime_system_prompt,
)


class TestRenderLessonBlock:
    def test_none_returns_empty_string(self):
        assert _render_lesson_block(None) == ""

    def test_empty_list_returns_empty_string(self):
        assert _render_lesson_block([]) == ""

    def test_list_with_only_blanks_returns_empty_string(self):
        assert _render_lesson_block(["", "  ", "\t"]) == ""

    def test_single_concept_renders_with_leading_space(self):
        result = _render_lesson_block(["boarding"])
        # The block must start with a space so it concatenates cleanly
        # after `{situation_description}.` in the template.
        assert result.startswith(" ")
        assert "boarding" in result

    def test_multiple_concepts_joined_by_comma(self):
        result = _render_lesson_block(["boarding", "gate", "departure time"])
        assert "boarding, gate, departure time" in result

    def test_strips_whitespace_around_concepts(self):
        result = _render_lesson_block(["  boarding  ", " gate"])
        assert "boarding, gate" in result
        # No double spaces or stray whitespace inside the joined list
        assert "  " not in result.split("concepts: ")[1].split(".")[0]

    def test_block_does_not_contain_spanish_target_forms(self):
        # Regression guard for the policy: no Spanish in prompt content.
        # Caller passes English glosses; the helper must not invent
        # Spanish.
        result = _render_lesson_block(["boarding", "gate"])
        # Sanity checks — these would only appear if someone hardcoded
        # Spanish examples in the helper.
        assert "embarque" not in result
        assert "puerta" not in result


class TestBuildRealtimeSystemPrompt:
    def test_no_lesson_concepts_renders_clean_prompt(self):
        result = build_realtime_system_prompt(
            animation_type="airport",
            situation_id="air_12",
            alt_language=None,
            lesson_concepts=None,
        )
        # Role still renders
        assert "airline check-in agent" in result
        # No lesson-block content
        assert "practicing how to talk about" not in result

    def test_lesson_concepts_appear_in_prompt(self):
        result = build_realtime_system_prompt(
            animation_type="airport",
            situation_id="air_12",
            alt_language=None,
            lesson_concepts=["boarding", "gate", "departure time"],
        )
        assert "practicing how to talk about" in result
        assert "boarding, gate, departure time" in result
        # Steering directive still present
        assert "do not tell them what to say" in result

    def test_empty_lesson_concepts_omits_block(self):
        result = build_realtime_system_prompt(
            animation_type="airport",
            situation_id="air_12",
            lesson_concepts=[],
        )
        assert "practicing how to talk about" not in result

    def test_default_no_lesson_concepts_arg_omits_block(self):
        # Call sites that haven't been updated yet must keep working.
        result = build_realtime_system_prompt(
            animation_type="airport",
            situation_id="air_12",
        )
        assert "practicing how to talk about" not in result
        assert "airline check-in agent" in result
