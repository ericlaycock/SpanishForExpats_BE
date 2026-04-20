from pydantic import BaseModel, EmailStr, Field
from typing import Any, Dict, List, Literal, Optional
from datetime import datetime
from uuid import UUID


WordStatus = Literal["learning", "mastered"]


# Pydantic 2 emits `{type: object}` for Dict[str, Any], which openapi-typescript
# interprets as `Record<string, never>`. These helpers post-process the JSON
# schema to inject `additionalProperties: true` *inside* the anyOf object
# variant so generated clients see a real "object with unknown values" shape.
def _freeform_object_schema(schema: dict) -> None:
    for variant in schema.get("anyOf", []):
        if variant.get("type") == "object":
            variant["additionalProperties"] = True
            return
    schema["additionalProperties"] = True


def _freeform_object_list_schema(schema: dict) -> None:
    for variant in schema.get("anyOf", []):
        if variant.get("type") == "array":
            variant.setdefault("items", {"type": "object"})["additionalProperties"] = True
            return


# Auth schemas
class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str
    invite_token: str = ""


class LoginResponse(BaseModel):
    access_token: str
    user_id: UUID
    is_admin: bool = False
    alt_language: Optional[str] = None
    email: str


class UserProfileResponse(BaseModel):
    email: str
    created_at: datetime
    is_admin: bool = False
    alt_language: Optional[str] = None


class AltLanguageRequest(BaseModel):
    language: Optional[str] = None


class TranslateRequest(BaseModel):
    text: str


# Subscription schemas
class SubscriptionStatusResponse(BaseModel):
    active: bool
    free_situations_limit: int = 5
    free_situations_completed: int
    free_situations_remaining: int


# Situation schemas
class WordSchema(BaseModel):
    id: str
    spanish: str
    english: str
    notes: Optional[str] = None

    class Config:
        from_attributes = True


class SituationListItem(BaseModel):
    id: str
    title: str
    is_locked: bool
    completed: bool
    free: bool

    class Config:
        from_attributes = True


class SituationDetail(BaseModel):
    id: str
    title: str
    free: bool
    encounter_number: int = 1
    animation_type: str = ""
    goal: Optional[str] = None
    words: List[WordSchema]

    class Config:
        from_attributes = True


class StartSituationResponse(BaseModel):
    words: List[WordSchema]
    encounter_number: int = 1
    animation_type: str = ""
    goal: Optional[str] = None


class CompleteSituationResponse(BaseModel):
    next_situation_id: Optional[str] = None


class AdminSkipEncounterResponse(BaseModel):
    situation_id: str
    situation_title: str
    words_set_known: int
    vocab_level: int
    next_situation_id: Optional[str] = None


# User Words schemas
class UserWordSchema(BaseModel):
    # `id` and `word_id` hold the same value. `id` is included so FE `Word`-based
    # types can read the field under its conventional name without casting;
    # `word_id` is kept for backward compatibility with existing consumers.
    id: str
    word_id: str
    spanish: str
    english: str
    notes: Optional[str] = None
    seen_count: int
    typed_correct_count: int
    spoken_correct_count: int
    hint_count: int = 0
    status: WordStatus
    mastery_level: int = 0
    next_refresh_at: Optional[datetime] = None
    word_category: Optional[Literal["high_frequency", "encounter"]] = None
    frequency_rank: Optional[int] = None

    class Config:
        from_attributes = True


class UnknownWordSchema(BaseModel):
    # Mirrors UserWordSchema's dual id/word_id so unknown/known words share a shape
    # on the FE side.
    id: str
    word_id: str
    spanish: str
    english: str
    word_category: Optional[Literal["high_frequency", "encounter"]] = None
    frequency_rank: Optional[int] = None


class UnknownWordsResponse(BaseModel):
    high_frequency: List[UnknownWordSchema]
    encounter: List[UnknownWordSchema]


class TypedCorrectRequest(BaseModel):
    word_ids: List[str]


class HintRequest(BaseModel):
    word_id: str


class HintResponse(BaseModel):
    hint_count: int


class DemoteWordResponse(BaseModel):
    word_id: str
    old_level: int
    new_level: int


class MessageOnlyResponse(BaseModel):
    message: str


# Conversation schemas
class CreateConversationRequest(BaseModel):
    situation_id: str
    mode: str  # 'text' or 'voice'


class CreateConversationResponse(BaseModel):
    conversation_id: UUID
    words: List[WordSchema]  # Return the words used in this conversation
    initial_message: str  # Custom initial message for this encounter
    initial_audio_url: Optional[str] = None  # TTS audio for the initial message
    language_mode: str = "english"  # "english", "spanish_text", or "spanish_audio"
    vocab_level: int = 0
    system_prompt: Optional[str] = None  # System prompt for multi-turn message history


class MessageRequest(BaseModel):
    text: str


class MessageResponse(BaseModel):
    detected_word_ids: List[str]
    missing_word_ids: List[str]


class VoiceTurnResponse(BaseModel):
    user_transcript: str
    detected_word_ids: List[str]
    missing_word_ids: List[str]
    assistant_text: str
    assistant_audio_url: str
    conversation_complete: bool


# Grammar config schemas
# drill_config / phase_*_config shapes differ per drill_type (article_matching,
# conjugation, skip, …). Keep them as free-form dicts but typed as
# Dict[str, Any] so generated clients see an object-with-unknown-values instead
# of an empty-shape marker.
class GrammarConfigResponse(BaseModel):
    situation_type: str
    video_embed_id: Optional[str] = None
    drill_type: Optional[str] = None
    tense: Optional[str] = None
    phases: Dict[str, bool]
    drill_config: Optional[Dict[str, Any]] = Field(default=None, json_schema_extra=_freeform_object_schema)
    drill_targets: Optional[List[Dict[str, Any]]] = Field(default=None, json_schema_extra=_freeform_object_list_schema)
    phase_1c_config: Optional[Dict[str, Any]] = Field(default=None, json_schema_extra=_freeform_object_schema)
    phase_2_config: Optional[Dict[str, Any]] = Field(default=None, json_schema_extra=_freeform_object_schema)


# Grammar gate / completion schemas
class GrammarGate(BaseModel):
    grammar_level: float
    situation_id: Optional[str] = None
    title: str
    vl_threshold: int
    has_content: bool
    total_lessons: Optional[int] = None
    resume_phase: Optional[Literal["learn", "voice-chat"]] = None


class GrammarGatesResponse(BaseModel):
    vocab_level: int
    grammar_level: float
    is_gated: bool
    gate: Optional[GrammarGate] = None


class GrammarUnit(BaseModel):
    grammar_level: float
    title: str
    vl_threshold: int
    has_content: bool
    completed: bool
    total_lessons: int
    completed_lessons: int


class GrammarCompletedResponse(BaseModel):
    grammar_units: List[GrammarUnit]


# Daily usage schemas
class DailyUsageResponse(BaseModel):
    encounters_used: int
    encounters_limit: int
    encounters_remaining: int


# Onboarding schemas
class AvailableCategory(BaseModel):
    id: str
    name: str
    description: str


class AvailableCategoriesResponse(BaseModel):
    categories: List[AvailableCategory]


class UpdateAnimationTypesResponse(BaseModel):
    selected_animation_types: List[str]


# Auth schemas (reset)
class ResetProgressResponse(BaseModel):
    reset: bool
    deleted_words: int
    deleted_situations: int
    deleted_conversations: int


class ResetPasswordResponse(BaseModel):
    reset: bool
    email: str


# Refresh (SRS) schemas
class PendingRefreshSituation(BaseModel):
    situation_id: str
    title: str
    animation_type: str
    due_word_count: int

class PendingRefreshesResponse(BaseModel):
    refreshes: List[PendingRefreshSituation]

class StartRefreshResponse(BaseModel):
    conversation_id: UUID
    words: List[WordSchema]
    initial_message: str
    language_mode: str = "english"
    conversation_type: str = "refresh"

class CompleteRefreshResponse(BaseModel):
    words_refreshed: int
    new_mastery_level: int


# Error schemas
class ErrorResponse(BaseModel):
    error: str


