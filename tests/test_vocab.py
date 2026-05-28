"""Vocab Map API — chapter seeding + the two-tier SRS (module deck → promote →
main deck). Both tiers ride the shared engine in `app/services/srs.py`; these
tests drive it through the HTTP surface a learner actually hits."""
from datetime import datetime, timedelta, timezone

from app.models import VocabCard
from tests.conftest import register_user

MODULE = "banking"
WORDS = [
    {"es": "cuenta", "en": "account"},
    {"es": "tarjeta", "en": "card"},
    {"es": "saldo", "en": "balance"},
]


def _complete_chapter(client, headers, module=MODULE, idx=0, words=WORDS):
    return client.post(
        f"/v1/vocab/chapter/{module}/{idx}/complete",
        headers=headers,
        json={"words": words},
    )


def _seed_and_open_module_deck(client, headers):
    """Complete chapter 0, then return the module review deck JSON."""
    _complete_chapter(client, headers)
    return client.get(f"/v1/vocab/module/{MODULE}/review", headers=headers).json()


def _card(db, es):
    """The single test user's card for a given Spanish word."""
    return db.query(VocabCard).filter(VocabCard.word_es == es).one()


# ── chapter completion seeds the module deck ────────────────────────────────────

def test_complete_chapter_seeds_module_cards_idempotently(client):
    _, headers = register_user(client)

    r = _complete_chapter(client, headers).json()
    assert r["was_new"] is True
    assert r["cards_seeded"] == len(WORDS)
    assert r["coins_awarded"] == len(WORDS)

    # Replaying the chapter neither re-credits completion nor duplicates cards.
    r2 = _complete_chapter(client, headers).json()
    assert r2["was_new"] is False
    assert r2["cards_seeded"] == 0

    prog = client.get("/v1/vocab/progress", headers=headers).json()
    deck = next(d for d in prog["module_decks"] if d["module_id"] == MODULE)
    assert deck["total"] == len(WORDS)
    assert deck["due"] == len(WORDS)          # freshly-seeded cards are due immediately
    assert prog["main_deck"]["total"] == 0


# ── module deck: promote vs. re-queue ───────────────────────────────────────────

def test_fast_correct_promotes_module_card_to_main_at_box1(client, db):
    _, headers = register_user(client)
    deck = _seed_and_open_module_deck(client, headers)
    assert len(deck["cards"]) == len(WORDS)   # all due right after the chapter
    card0 = deck["cards"][0]

    r = client.post(
        f"/v1/vocab/module/{MODULE}/review/attempt",
        headers=headers,
        json={"card_id": card0["card_id"], "correct": True, "response_ms": 2000},
    ).json()
    assert r["promoted"] is True and r["requeued"] is False

    row = _card(db, card0["word_es"])
    assert row.status == "main"
    assert row.box == 1
    # Enters the shared ladder at box 1 → first main review ~4h out, so it is NOT
    # immediately due again (the old bug surfaced mastered cards too soon).
    assert row.due_at > datetime.now(timezone.utc) + timedelta(hours=3)

    prog = client.get("/v1/vocab/progress", headers=headers).json()
    assert prog["main_deck"]["total"] == 1
    assert prog["main_deck"]["due"] == 0      # spaced into the future


def test_slow_answer_requeues_module_card_with_spacing(client, db):
    _, headers = register_user(client)
    deck = _seed_and_open_module_deck(client, headers)
    card0 = deck["cards"][0]

    # Correct but past the 15s typed ceiling → silent lapse → re-queue, no promote.
    r = client.post(
        f"/v1/vocab/module/{MODULE}/review/attempt",
        headers=headers,
        json={"card_id": card0["card_id"], "correct": True, "response_ms": 20_000},
    ).json()
    assert r["requeued"] is True and r["promoted"] is False

    row = _card(db, card0["word_es"])
    assert row.status == "module"             # stayed in the module deck
    assert row.due_at > datetime.now(timezone.utc) + timedelta(minutes=5)  # ~10 min out

    # …and it drops out of the immediately-due module deck.
    deck2 = client.get(f"/v1/vocab/module/{MODULE}/review", headers=headers).json()
    surfaced = [c["word_es"] for c in deck2["cards"]]
    assert card0["word_es"] not in surfaced
    assert len(deck2["cards"]) == len(WORDS) - 1


# ── main deck: the shared ladder ────────────────────────────────────────────────

def _promote_one(client, headers):
    """Seed + promote a single card to the main deck; return its id and word."""
    deck = _seed_and_open_module_deck(client, headers)
    card0 = deck["cards"][0]
    client.post(
        f"/v1/vocab/module/{MODULE}/review/attempt",
        headers=headers,
        json={"card_id": card0["card_id"], "correct": True, "response_ms": 2000},
    )
    return card0["card_id"], card0["word_es"]


def test_main_deck_climbs_to_box_7_then_caps(client):
    # Regression: a main card reaching box 7 must commit. Before the unified
    # ladder + migration the vocab box CHECK capped at 5/6 and a high-box
    # promotion threw an IntegrityError → 500 on this endpoint.
    _, headers = register_user(client)
    cid, _ = _promote_one(client, headers)

    boxes = []
    for _ in range(5):
        r = client.post(
            "/v1/vocab/review/attempt",
            headers=headers,
            json={"card_id": cid, "correct": True, "response_ms": 1000},  # great = +2
        )
        assert r.status_code == 200, r.text
        boxes.append(r.json()["box"])
    # box 1 → 3 → 5 → 7 → 7 → 7 (double-bumps, then holds at the cap)
    assert boxes == [3, 5, 7, 7, 7]


def test_main_deck_lapse_demotes_by_two_not_to_one(client):
    _, headers = register_user(client)
    cid, _ = _promote_one(client, headers)
    # Climb to box 5 (1 → 3 → 5) with two fast hits…
    for _ in range(2):
        client.post("/v1/vocab/review/attempt", headers=headers,
                    json={"card_id": cid, "correct": True, "response_ms": 1000})
    # …then miss: box 5 → 3, not back to 1.
    r = client.post("/v1/vocab/review/attempt", headers=headers,
                    json={"card_id": cid, "correct": False, "response_ms": 1000}).json()
    assert r["box"] == 3


def test_main_review_deck_only_returns_due_cards(client, db):
    _, headers = register_user(client)
    cid, es = _promote_one(client, headers)

    # Just promoted → due ~4h out → absent from the due review deck.
    main = client.get("/v1/vocab/review", headers=headers).json()
    assert main["total"] == 1 and main["due"] == 0 and main["cards"] == []

    # Simulate the 4h passing; the card reappears in the due deck.
    row = _card(db, es)
    row.due_at = datetime.now(timezone.utc) - timedelta(minutes=1)
    db.flush()
    main2 = client.get("/v1/vocab/review", headers=headers).json()
    assert main2["due"] == 1
    assert [c["card_id"] for c in main2["cards"]] == [cid]
