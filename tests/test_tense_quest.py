"""Tense Quest — data module and API endpoint tests. The shared SRS engine the
review deck rides on is exercised in `tests/test_srs.py`."""
from datetime import datetime, timedelta, timezone

import pytest

from app.data import tense_quest as tq
from tests.conftest import register_user


# ── data module ─────────────────────────────────────────────────────────────

def test_tense_groups_well_formed():
    groups = tq.list_tense_groups()
    assert len(groups) >= 15
    ids = [g["id"] for g in groups]
    assert len(ids) == len(set(ids)), "tense group ids must be unique"
    for g in groups:
        assert g["total_drills"] >= 1
        assert g["drill_ids"] and len(g["drill_ids"]) == g["total_drills"]
        assert g["family"] in tq.FAMILIES
        # round-trip
        assert tq.get_tense_group(g["id"])["id"] == g["id"]


def test_every_drill_has_a_playable_payload():
    saw_blank_es = False
    saw_conjugation_drill = False
    for g in tq.list_tense_groups():
        for did in g["drill_ids"]:
            p = tq.get_drill_payload(did)
            assert p is not None, f"{did} should be playable"
            assert p["tense_group_id"] == g["id"]
            assert p["rule_cards"], f"{did} should expose at least one rule card"
            assert len(p["sentences"]) >= 4
            # conjugation drills have charts + targets; rule-type quests (e.g.
            # Preterite vs. Imperfect) are rules + sentences only.
            if p["conjugation_targets"]:
                saw_conjugation_drill = True
                assert p["charts"], f"{did} should expose at least one verb chart"
                for t in p["conjugation_targets"]:
                    assert t["answer"], "target must carry an expected answer"
            modes = [s["response_mode"] for s in p["sentences"]]
            assert set(modes) <= {"type", "speak"}
            # Binary-choice drills (pret-vs-imperfect, subjunctive triggers)
            # serve all-type sentences since the learner taps A/B buttons —
            # there's no "speak" mode for a button choice. All other drills
            # alternate type/speak so the player practises both modalities.
            if p.get("drill_type") != "binary_choice":
                assert all(modes[i] != modes[i + 1] for i in range(len(modes) - 1))
            for s in p["sentences"]:
                assert "blank_es" in s  # may be None, but the key must exist
                if s["blank_es"]:
                    saw_blank_es = True
                    assert "____" in s["blank_es"]
    assert saw_conjugation_drill and saw_blank_es


def test_review_cards_are_sentences_and_round_trip():
    g = tq.list_tense_groups()[0]
    did = g["drill_ids"][0]
    cards = tq.review_cards_for_drill(did)
    assert cards
    keys = [c["card_key"] for c in cards]
    assert len(keys) == len(set(keys))
    # one card per practice sentence
    payload = tq.get_drill_payload(did)
    assert len(cards) == len(payload["sentences"])
    for c in cards:
        assert c["card_key"] == f"{c['drill_id']}:{c['sentence_id']}"
        assert c["es"] and c["en"]
        assert c["response_mode"] in {"type", "speak"}
        resolved = tq.lookup_sentence(c["card_key"])
        assert resolved is not None
        assert resolved["es"] == c["es"]
        assert resolved["response_mode"] == c["response_mode"]
    # card_display is the deck assembler's resolver
    assert tq.card_display(cards[0]["card_key"])["es"] == cards[0]["es"]


def test_unknown_ids_return_none():
    assert tq.get_tense_group("nope") is None
    assert tq.get_drill_payload("grammar_does_not_exist") is None
    assert tq.lookup_sentence("grammar_does_not_exist:s0") is None
    assert tq.lookup_sentence("malformed") is None
    assert tq.card_display("nope:s0") is None


# ── API ─────────────────────────────────────────────────────────────────────

def _first_group_and_drill():
    g = tq.list_tense_groups()[0]
    return g["id"], g["drill_ids"][0]


def test_overview_empty_state(client):
    _, headers = register_user(client)
    resp = client.get("/v1/tensequest/overview", headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["points"] == 0
    assert len(body["tense_groups"]) >= 15
    assert all(g["completed_drills"] == 0 and g["percent"] == 0 for g in body["tense_groups"])
    assert body["review"]["total_count"] == 0
    assert body["leaderboard"]["you_points"] == 0


def test_group_detail_and_drill_payload(client):
    _, headers = register_user(client)
    gid, did = _first_group_and_drill()
    resp = client.get(f"/v1/tensequest/groups/{gid}", headers=headers)
    assert resp.status_code == 200
    detail = resp.json()
    assert detail["id"] == gid
    assert detail["next_drill_id"] == did
    assert detail["all_complete"] is False
    assert detail["drills"][0]["drill_id"] == did

    resp = client.get(f"/v1/tensequest/drills/{did}", headers=headers)
    assert resp.status_code == 200
    payload = resp.json()
    assert payload["drill_id"] == did
    assert payload["tense_group_id"] == gid
    assert payload["charts"]
    assert payload["conjugation_targets"]
    assert payload["sentences"]
    s0 = payload["sentences"][0]
    assert "blank_es" in s0 and "glosses" in s0 and s0["response_mode"] in {"type", "speak"}


def test_unknown_group_and_drill_404(client):
    _, headers = register_user(client)
    assert client.get("/v1/tensequest/groups/nope", headers=headers).status_code == 404
    assert client.get("/v1/tensequest/drills/grammar_nope", headers=headers).status_code == 404


def test_complete_drill_awards_point_and_seeds_deck(client):
    _, headers = register_user(client)
    gid, did = _first_group_and_drill()

    resp = client.post(f"/v1/tensequest/drills/{did}/complete", headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["was_new"] is True
    assert body["points"] == 1
    assert body["completed_drills"] == 1
    assert body["cards_added"] >= 1
    assert body["deck_total"] == body["cards_added"]

    # Idempotent — second completion of the same drill adds no point, no new cards.
    resp2 = client.post(f"/v1/tensequest/drills/{did}/complete", headers=headers)
    body2 = resp2.json()
    assert body2["was_new"] is False
    assert body2["points"] == 1
    assert body2["cards_added"] == 0

    # Overview reflects progress + deck + leaderboard.
    overview = client.get("/v1/tensequest/overview", headers=headers).json()
    assert overview["points"] == 1
    grp = next(g for g in overview["tense_groups"] if g["id"] == gid)
    assert grp["completed_drills"] == 1
    assert grp["percent"] > 0
    assert overview["review"]["total_count"] == body["deck_total"]
    assert overview["leaderboard"]["you_points"] == 1
    assert overview["leaderboard"]["you_rank"] == 1
    assert any(e["is_you"] for e in overview["leaderboard"]["entries"])


def test_review_attempt_and_shuffle(client):
    _, headers = register_user(client)
    _, did = _first_group_and_drill()
    client.post(f"/v1/tensequest/drills/{did}/complete", headers=headers)

    deck = client.get("/v1/tensequest/review", headers=headers).json()
    assert deck["total_count"] >= 1
    c0 = deck["cards"][0]
    # cards are practice sentences now
    assert c0["en"] and c0["es"] and "blank_es" in c0
    assert c0["response_mode"] in {"type", "speak"}
    card_key = c0["card_key"]

    coins_before = client.get("/v1/tensequest/overview", headers=headers).json()["points"]

    # Slow-but-correct → silent lapse, 0 coins. 16s clears both the typed (15s)
    # and spoken (10s) ceilings, so this is a lapse regardless of the card's mode.
    resp = client.post("/v1/tensequest/review/attempt", headers=headers,
                       json={"card_key": card_key, "correct": True, "response_ms": 16000})
    assert resp.status_code == 200
    assert resp.json()["result"] == "lapse" and resp.json()["coins_earned"] == 0

    # Wrong → lapse, 0 coins.
    resp = client.post("/v1/tensequest/review/attempt", headers=headers,
                       json={"card_key": card_key, "correct": False, "response_ms": 1500})
    assert resp.json()["result"] == "lapse" and resp.json()["coins_earned"] == 0

    # Medium correct → good, 1 coin.
    resp = client.post("/v1/tensequest/review/attempt", headers=headers,
                       json={"card_key": card_key, "correct": True, "response_ms": 7000})
    assert resp.json()["result"] == "good" and resp.json()["coins_earned"] == 1

    # Fast correct → great, box bumps, 2 coins.
    resp = client.post("/v1/tensequest/review/attempt", headers=headers,
                       json={"card_key": card_key, "correct": True, "response_ms": 1500})
    assert resp.json()["result"] == "great" and resp.json()["coins_earned"] == 2
    assert resp.json()["box"] >= 2

    # Coins accumulate into the overview/leaderboard total.
    overview = client.get("/v1/tensequest/overview", headers=headers).json()
    assert overview["points"] == coins_before + 3  # 0 + 0 + 1 + 2
    assert overview["leaderboard"]["you_points"] == overview["points"]

    # Unknown card → 404.
    bad = client.post("/v1/tensequest/review/attempt", headers=headers,
                      json={"card_key": "grammar_nope:s0", "correct": True, "response_ms": 1000})
    assert bad.status_code == 404

    # Shuffle returns the deck size.
    resp = client.post("/v1/tensequest/review/shuffle", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["shuffled"] == deck["total_count"]


def test_endpoints_require_auth(client):
    assert client.get("/v1/tensequest/overview").status_code in (401, 403)
    assert client.post("/v1/tensequest/review/shuffle").status_code in (401, 403)


def test_diagnostic_flow(client):
    _, headers = register_user(client)

    # overview starts un-diagnosed
    ov = client.get("/v1/tensequest/overview", headers=headers).json()
    assert ov["diagnostic_taken"] is False
    assert all(g["diagnostic"] is None for g in ov["tense_groups"])

    quiz = client.get("/v1/tensequest/diagnostic", headers=headers).json()
    assert len(quiz["groups"]) >= 15
    saw_english = False
    for g in quiz["groups"]:
        assert 1 <= len(g["prompts"]) <= 3
        for p in g["prompts"]:
            assert p["verb"] and p["pronoun"] and p["answer"]
            assert "english" in p  # natural-English hint key always present (may be null)
            if p["english"]:
                saw_english = True
    assert saw_english  # at least the present-tense groups should have one

    # pass the first group, fail the second; ignore the rest
    g0, g1 = quiz["groups"][0]["tense_group_id"], quiz["groups"][1]["tense_group_id"]
    resp = client.post("/v1/tensequest/diagnostic", headers=headers, json={
        "results": [
            {"tense_group_id": g0, "passed": True},
            {"tense_group_id": g1, "passed": False},
            {"tense_group_id": "not_a_group", "passed": True},  # ignored
        ],
    })
    assert resp.status_code == 200 and resp.json()["ok"] is True

    ov = client.get("/v1/tensequest/overview", headers=headers).json()
    assert ov["diagnostic_taken"] is True
    by_id = {g["id"]: g for g in ov["tense_groups"]}
    assert by_id[g0]["diagnostic"] == "ok"
    assert by_id[g1]["diagnostic"] == "needs_work"

    # re-taking overwrites
    client.post("/v1/tensequest/diagnostic", headers=headers, json={
        "results": [{"tense_group_id": g0, "passed": False}],
    })
    ov = client.get("/v1/tensequest/overview", headers=headers).json()
    assert {g["id"]: g["diagnostic"] for g in ov["tense_groups"]}[g0] == "needs_work"

    # correct-but-slow → "ok_slow" (not done); fast-and-correct → "ok" reads as
    # fully complete on the map (full fraction, counts toward "tenses beaten").
    client.post("/v1/tensequest/diagnostic", headers=headers, json={"results": [
        {"tense_group_id": g0, "passed": True, "slow": True},
        {"tense_group_id": g1, "passed": True, "slow": False},
    ]})
    ov = client.get("/v1/tensequest/overview", headers=headers).json()
    by_id = {g["id"]: g for g in ov["tense_groups"]}
    assert by_id[g0]["diagnostic"] == "ok_slow"
    assert by_id[g0]["percent"] < 100  # "bit slow" is not "beaten"
    g1row = by_id[g1]
    assert g1row["diagnostic"] == "ok"
    assert g1row["completed_drills"] == g1row["total_drills"] and g1row["percent"] == 100
    assert sum(1 for g in ov["tense_groups"] if g["percent"] >= 100) >= 1


def test_sentence_completion_awards_coin(client):
    _, headers = register_user(client)
    _, did = _first_group_and_drill()
    payload = client.get(f"/v1/tensequest/drills/{did}", headers=headers).json()
    assert len(payload["sentences"]) >= 2
    sid, sid2 = payload["sentences"][0]["id"], payload["sentences"][1]["id"]
    pts0 = client.get("/v1/tensequest/overview", headers=headers).json()["points"]

    r = client.post(f"/v1/tensequest/drills/{did}/sentence", headers=headers, json={"sentence_id": sid, "correct": True})
    assert r.status_code == 200 and r.json() == {"was_new": True, "points": pts0 + 1}
    assert client.get("/v1/tensequest/overview", headers=headers).json()["points"] == pts0 + 1

    # idempotent — replaying the same sentence doesn't re-award
    r = client.post(f"/v1/tensequest/drills/{did}/sentence", headers=headers, json={"sentence_id": sid, "correct": True})
    assert r.json() == {"was_new": False, "points": pts0 + 1}

    # a wrong attempt is a no-op
    r = client.post(f"/v1/tensequest/drills/{did}/sentence", headers=headers, json={"sentence_id": sid2, "correct": False})
    assert r.json() == {"was_new": False, "points": pts0 + 1}

    # unknown drill / sentence → 404
    assert client.post("/v1/tensequest/drills/grammar_nope/sentence", headers=headers, json={"sentence_id": sid, "correct": True}).status_code == 404
    assert client.post(f"/v1/tensequest/drills/{did}/sentence", headers=headers, json={"sentence_id": "nope", "correct": True}).status_code == 404


def test_sentence_completion_requires_auth(client):
    assert client.post("/v1/tensequest/drills/whatever/sentence", json={"sentence_id": "x", "correct": True}).status_code in (401, 403)


def test_diagnostic_requires_auth(client):
    assert client.get("/v1/tensequest/diagnostic").status_code in (401, 403)
    assert client.post("/v1/tensequest/diagnostic", json={"results": []}).status_code in (401, 403)


def test_username_set_validate_and_uniqueness(client):
    _, h1 = register_user(client)

    # starts unset; leaderboard never leaks an email/real name
    assert client.get("/v1/tensequest/overview", headers=h1).json()["username"] is None

    # malformed names are rejected
    for bad in ["ab", "a" * 21, "has space", "bad-dash", "emoji😀", "___", "you"]:
        r = client.post("/v1/tensequest/username", headers=h1, json={"username": bad})
        assert r.status_code == 422, bad

    # a good name sticks and surfaces in the overview
    r = client.post("/v1/tensequest/username", headers=h1, json={"username": "  Sir_Conjugates  "})
    assert r.status_code == 200 and r.json()["username"] == "Sir_Conjugates"
    assert client.get("/v1/tensequest/overview", headers=h1).json()["username"] == "Sir_Conjugates"

    # case-insensitively unique across users
    _, h2 = register_user(client, email="rival@example.com")
    assert client.post("/v1/tensequest/username", headers=h2, json={"username": "sir_conjugates"}).status_code == 409

    # changing your own name to a casing variant of itself is fine
    assert client.post("/v1/tensequest/username", headers=h1, json={"username": "SIR_CONJUGATES"}).status_code == 200


def test_username_requires_auth(client):
    assert client.post("/v1/tensequest/username", json={"username": "whoever"}).status_code in (401, 403)
