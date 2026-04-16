"""HTTP-level tests for POST /v1/conversations/{id}/mark-word.

Covers the conj_* → grammar_<verb> normalization and the defensive filter
that together prevent FK violations on user_words when the frontend sends
synthetic conjugation chip ids (e.g. conj_vivir_nosotros).
"""
import uuid

from app.models import Conversation, Situation, UserWord, Word


def _seed_grammar_words(db):
    """Seed a few grammar base words (infinitives) into the words table."""
    words = [
        Word(id="grammar_vivir", spanish="vivir", english="to live", word_category="grammar"),
        Word(id="grammar_hablar", spanish="hablar", english="to speak", word_category="grammar"),
        Word(id="grammar_beber", spanish="beber", english="to drink", word_category="grammar"),
    ]
    for w in words:
        db.add(w)
    # Minimal grammar situation (we only need id + required cols)
    sit = Situation(
        id="grammar_regular_present_1",
        title="Regular Present (1/3)",
        animation_type="grammar",
        encounter_number=300,
        order_index=1300,
        is_free=True,
        situation_type="grammar",
    )
    db.add(sit)
    db.flush()


def _make_voice_conversation(db, user_id, target_word_ids):
    conv = Conversation(
        id=uuid.uuid4(),
        user_id=user_id,
        situation_id="grammar_regular_present_1",
        mode="voice",
        target_word_ids=target_word_ids,
        used_typed_word_ids=[],
        used_spoken_word_ids=[],
        status="active",
    )
    db.add(conv)
    db.flush()
    return conv


def test_mark_word_normalizes_conj_prefix(client, db, auth_user):
    """conj_vivir_nosotros should be mapped to grammar_vivir; no FK violation."""
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_grammar_words(db)
    conv = _make_voice_conversation(db, user_id, ["grammar_vivir", "grammar_hablar"])

    resp = client.post(
        f"/v1/conversations/{conv.id}/mark-word",
        data={"word_id": "conj_vivir_nosotros"},
        headers=headers,
    )

    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["word_id"] == "grammar_vivir", (
        f"Expected normalized response word_id, got {body!r}"
    )

    # Conversation state reflects the normalized id, not the synthetic chip id
    db.refresh(conv)
    assert "grammar_vivir" in conv.used_spoken_word_ids
    assert "conj_vivir_nosotros" not in conv.used_spoken_word_ids

    # user_words row exists for the base word; no synthetic row
    assert db.query(UserWord).filter_by(user_id=user_id, word_id="grammar_vivir").first() is not None
    assert db.query(UserWord).filter_by(word_id="conj_vivir_nosotros").first() is None


def test_mark_word_bogus_id_does_not_500(client, db, auth_user):
    """An unknown word_id is tolerated: 200 response, no user_words write."""
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_grammar_words(db)
    conv = _make_voice_conversation(db, user_id, ["grammar_vivir"])

    resp = client.post(
        f"/v1/conversations/{conv.id}/mark-word",
        data={"word_id": "some_completely_bogus_id_xyz"},
        headers=headers,
    )

    assert resp.status_code == 200, resp.text
    assert db.query(UserWord).filter_by(word_id="some_completely_bogus_id_xyz").first() is None


def test_mark_word_completes_conversation_via_conj_chain(client, db, auth_user):
    """Marking every target via conj_* chips still converges to 'complete'.

    The normalization must land on the same ids as target_word_ids
    (grammar_<verb>), otherwise check_conversation_complete never fires and
    the voice chat phase hangs — the real user-facing bug this plan fixes.
    """
    _, headers = auth_user
    user_id = _get_auth_user_id(headers)
    _seed_grammar_words(db)
    conv = _make_voice_conversation(
        db, user_id, ["grammar_vivir", "grammar_hablar", "grammar_beber"]
    )

    for synthetic_id in [
        "conj_vivir_nosotros",
        "conj_hablar_yo",
        "conj_beber_ustedes",
    ]:
        resp = client.post(
            f"/v1/conversations/{conv.id}/mark-word",
            data={"word_id": synthetic_id},
            headers=headers,
        )
        assert resp.status_code == 200, resp.text

    db.refresh(conv)
    assert conv.status == "complete", (
        f"Expected conversation to converge to 'complete' after all targets marked; "
        f"got status={conv.status}, used={conv.used_spoken_word_ids}"
    )


def _get_auth_user_id(headers):
    """Extract the authenticated user's UUID from the JWT's `sub` claim."""
    from jose import jwt
    token = headers["Authorization"].split()[1]
    payload = jwt.get_unverified_claims(token)
    return uuid.UUID(payload["sub"])
