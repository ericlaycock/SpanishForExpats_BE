"""Static checks that conversation_id was wired through the AI gateways.

The audit-row write paths need a real Postgres + OpenAI to exercise
end-to-end, but the contract is verifiable statically: the dataclass
field exists with the right default, the gateway signatures expose the
new kwarg, and the ORM models have the column.

Run: python3.11 -m pytest tests/test_services/test_ai_request_conversation_id.py --noconftest -v
"""
from __future__ import annotations

import inspect

from app.models import LLMRequest, STTRequest, TTSRequest
from app.services.llm_gateway import ConversationContext
from app.services.openai_media_gateway import synthesize_speech, transcribe_audio


class TestConversationContext:
    def test_conversation_id_field_exists_with_default_none(self):
        ctx = ConversationContext(
            request_id="r",
            user_id="u",
            system_prompt="",
            user_prompt="",
        )
        assert ctx.conversation_id is None

    def test_conversation_id_round_trips(self):
        ctx = ConversationContext(
            request_id="r",
            user_id="u",
            system_prompt="",
            user_prompt="",
            conversation_id="abc-123",
        )
        assert ctx.conversation_id == "abc-123"


class TestGatewaySignatures:
    """The kwarg must be optional and default to None so unrelated
    callers (sentence_hint pre-PR, /check-pronunciation, /v1/tts) keep
    working without modification."""

    def test_transcribe_audio_accepts_conversation_id_kwarg(self):
        sig = inspect.signature(transcribe_audio)
        assert "conversation_id" in sig.parameters
        assert sig.parameters["conversation_id"].default is None

    def test_synthesize_speech_accepts_conversation_id_kwarg(self):
        sig = inspect.signature(synthesize_speech)
        assert "conversation_id" in sig.parameters
        assert sig.parameters["conversation_id"].default is None


class TestORMModels:
    def test_llm_request_has_conversation_id_column(self):
        assert "conversation_id" in LLMRequest.__table__.columns
        col = LLMRequest.__table__.columns["conversation_id"]
        assert col.nullable is True
        assert col.index is True

    def test_stt_request_has_conversation_id_column(self):
        assert "conversation_id" in STTRequest.__table__.columns
        col = STTRequest.__table__.columns["conversation_id"]
        assert col.nullable is True
        assert col.index is True

    def test_tts_request_has_conversation_id_column(self):
        assert "conversation_id" in TTSRequest.__table__.columns
        col = TTSRequest.__table__.columns["conversation_id"]
        assert col.nullable is True
        assert col.index is True

    def test_columns_have_fk_to_conversations(self):
        for model in (LLMRequest, STTRequest, TTSRequest):
            col = model.__table__.columns["conversation_id"]
            fks = list(col.foreign_keys)
            assert len(fks) == 1
            assert fks[0].column.table.name == "conversations"
            # ON DELETE SET NULL so audit rows survive conversation deletion
            assert fks[0].ondelete == "SET NULL"
