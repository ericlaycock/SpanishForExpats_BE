"""Teachers portal API — role gating, roster isolation, and the tri-state
overlay (upsert / read-back / clear-on-default)."""
import uuid

from app.models import TeacherStudent, TeacherStudentTopicState, User
from tests.conftest import register_user


def _make_teacher(client, db, email):
    """Register a user and flip is_teacher (the seed grants this in prod; the
    flag is read live from the DB by get_current_user, so the token still works)."""
    data, headers = register_user(client, email=email)
    db.query(User).filter(User.id == uuid.UUID(data["user_id"])).update({"is_teacher": True})
    db.flush()
    return uuid.UUID(data["user_id"]), headers


def _add_student(db, teacher_id, email, name=None, user_id=None):
    ts = TeacherStudent(
        teacher_id=teacher_id, student_email=email, student_name=name, student_user_id=user_id
    )
    db.add(ts)
    db.flush()
    return str(ts.id)


# ── gating ──────────────────────────────────────────────────────────────────

def test_non_teacher_is_forbidden(client):
    _, headers = register_user(client, email="student@example.com")  # is_teacher False
    assert client.get("/v1/teachers/students", headers=headers).status_code == 403


def test_teacher_can_list_roster(client, db):
    tid, headers = _make_teacher(client, db, "t@example.com")
    _add_student(db, tid, "a@example.com", "Ana")
    _add_student(db, tid, "b@example.com", "Beto")

    resp = client.get("/v1/teachers/students", headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert {s["student_email"] for s in body} == {"a@example.com", "b@example.com"}
    assert all(s["has_account"] is False for s in body)  # no student_user_id set


def test_roster_is_isolated_per_teacher(client, db):
    t1, h1 = _make_teacher(client, db, "t1@example.com")
    t2, h2 = _make_teacher(client, db, "t2@example.com")
    _add_student(db, t1, "only-mine@example.com", "Mine")
    rid2 = _add_student(db, t2, "theirs@example.com", "Theirs")

    mine = client.get("/v1/teachers/students", headers=h1).json()
    assert [s["student_email"] for s in mine] == ["only-mine@example.com"]
    # t1 cannot open t2's student.
    assert client.get(f"/v1/teachers/students/{rid2}", headers=h1).status_code == 404


def test_has_account_reflects_link(client, db):
    tid, headers = _make_teacher(client, db, "t@example.com")
    # A linked student: point at a real user row (the teacher themselves works as a stand-in user).
    rid = _add_student(db, tid, "linked@example.com", "Linked", user_id=tid)
    detail = client.get(f"/v1/teachers/students/{rid}", headers=headers).json()
    assert detail["has_account"] is True


# ── overlay state ─────────────────────────────────────────────────────────────

def test_default_state_is_empty(client, db):
    tid, headers = _make_teacher(client, db, "t@example.com")
    rid = _add_student(db, tid, "s@example.com", "S")
    detail = client.get(f"/v1/teachers/students/{rid}", headers=headers).json()
    assert detail["states"] == []  # absent row ⇒ no_aprendido


def test_set_then_read_state(client, db):
    tid, headers = _make_teacher(client, db, "t@example.com")
    rid = _add_student(db, tid, "s@example.com", "S")

    r = client.put(f"/v1/teachers/students/{rid}/state", headers=headers, json={
        "topic_type": "tense_group", "topic_id": "subjunctive_imperfect", "state": "aprendiendo",
    })
    assert r.status_code == 200 and r.json()["state"] == "aprendiendo"

    # A second topic, vocab this time, set to the fluent state.
    client.put(f"/v1/teachers/students/{rid}/state", headers=headers, json={
        "topic_type": "vocab_module", "topic_id": "freq-500-514", "state": "aprendido",
    })

    states = client.get(f"/v1/teachers/students/{rid}", headers=headers).json()["states"]
    by_id = {(s["topic_type"], s["topic_id"]): s["state"] for s in states}
    assert by_id == {
        ("tense_group", "subjunctive_imperfect"): "aprendiendo",
        ("vocab_module", "freq-500-514"): "aprendido",
    }


def test_update_overwrites_not_duplicates(client, db):
    tid, headers = _make_teacher(client, db, "t@example.com")
    rid = _add_student(db, tid, "s@example.com", "S")
    body = {"topic_type": "tense_group", "topic_id": "regular_present", "state": "aprendiendo"}
    client.put(f"/v1/teachers/students/{rid}/state", headers=headers, json=body)
    client.put(f"/v1/teachers/students/{rid}/state", headers=headers, json={**body, "state": "aprendido"})

    states = client.get(f"/v1/teachers/students/{rid}", headers=headers).json()["states"]
    assert states == [{"topic_type": "tense_group", "topic_id": "regular_present", "state": "aprendido"}]


def test_no_aprendido_clears_the_row(client, db):
    tid, headers = _make_teacher(client, db, "t@example.com")
    rid = _add_student(db, tid, "s@example.com", "S")
    body = {"topic_type": "tense_group", "topic_id": "regular_present"}
    client.put(f"/v1/teachers/students/{rid}/state", headers=headers, json={**body, "state": "aprendido"})
    client.put(f"/v1/teachers/students/{rid}/state", headers=headers, json={**body, "state": "no_aprendido"})

    assert client.get(f"/v1/teachers/students/{rid}", headers=headers).json()["states"] == []
    assert db.query(TeacherStudentTopicState).count() == 0  # sparse: no leftover row


def test_cannot_set_state_on_anothers_student(client, db):
    t1, h1 = _make_teacher(client, db, "t1@example.com")
    t2, _ = _make_teacher(client, db, "t2@example.com")
    rid2 = _add_student(db, t2, "s@example.com", "S")
    r = client.put(f"/v1/teachers/students/{rid2}/state", headers=h1, json={
        "topic_type": "tense_group", "topic_id": "regular_present", "state": "aprendiendo",
    })
    assert r.status_code == 404


def test_invalid_enums_are_rejected(client, db):
    tid, headers = _make_teacher(client, db, "t@example.com")
    rid = _add_student(db, tid, "s@example.com", "S")
    bad_state = client.put(f"/v1/teachers/students/{rid}/state", headers=headers, json={
        "topic_type": "tense_group", "topic_id": "x", "state": "mastered",
    })
    bad_type = client.put(f"/v1/teachers/students/{rid}/state", headers=headers, json={
        "topic_type": "lesson", "topic_id": "x", "state": "aprendiendo",
    })
    assert bad_state.status_code == 422 and bad_type.status_code == 422


# ── add / remove roster ───────────────────────────────────────────────────────

def test_add_student_links_to_existing_account(client, db):
    tid, headers = _make_teacher(client, db, "t@example.com")
    register_user(client, email="alice@example.com")  # a real app user to link to

    r = client.post("/v1/teachers/students", headers=headers,
                    json={"email": "Alice@Example.com", "name": "Alice"})
    assert r.status_code == 201
    body = r.json()
    assert body["student_email"] == "alice@example.com"  # normalised
    assert body["has_account"] is True
    # shows up in the roster
    emails = [s["student_email"] for s in client.get("/v1/teachers/students", headers=headers).json()]
    assert "alice@example.com" in emails


def test_add_student_without_account_is_allowed(client, db):
    _, headers = _make_teacher(client, db, "t@example.com")
    r = client.post("/v1/teachers/students", headers=headers,
                    json={"email": "ghost@nowhere.com", "name": "Ghost"})
    assert r.status_code == 201
    assert r.json()["has_account"] is False


def test_add_duplicate_is_conflict(client, db):
    _, headers = _make_teacher(client, db, "t@example.com")
    client.post("/v1/teachers/students", headers=headers, json={"email": "dup@x.com"})
    r2 = client.post("/v1/teachers/students", headers=headers, json={"email": "dup@x.com"})
    assert r2.status_code == 409


def test_add_invalid_email_rejected(client, db):
    _, headers = _make_teacher(client, db, "t@example.com")
    assert client.post("/v1/teachers/students", headers=headers, json={"email": "notanemail"}).status_code == 400


def test_remove_student_cascades_state(client, db):
    tid, headers = _make_teacher(client, db, "t@example.com")
    rid = _add_student(db, tid, "s@example.com", "S")
    client.put(f"/v1/teachers/students/{rid}/state", headers=headers, json={
        "topic_type": "tense_group", "topic_id": "regular_present", "state": "aprendido",
    })
    assert db.query(TeacherStudentTopicState).count() == 1

    assert client.delete(f"/v1/teachers/students/{rid}", headers=headers).status_code == 204
    assert client.get(f"/v1/teachers/students/{rid}", headers=headers).status_code == 404
    assert db.query(TeacherStudentTopicState).count() == 0  # FK cascade removed the overlay


def test_cannot_remove_anothers_student(client, db):
    _t1, h1 = _make_teacher(client, db, "t1@example.com")
    t2, _ = _make_teacher(client, db, "t2@example.com")
    rid2 = _add_student(db, t2, "s@example.com", "S")
    assert client.delete(f"/v1/teachers/students/{rid2}", headers=h1).status_code == 404


def test_roster_includes_progress_counts(client, db):
    tid, headers = _make_teacher(client, db, "t@example.com")
    rid = _add_student(db, tid, "s@example.com", "S")
    for tid_, st in [("regular_present", "aprendido"), ("imperfect", "aprendido"), ("conditional", "aprendiendo")]:
        client.put(f"/v1/teachers/students/{rid}/state", headers=headers,
                   json={"topic_type": "tense_group", "topic_id": tid_, "state": st})
    s = next(s for s in client.get("/v1/teachers/students", headers=headers).json() if s["id"] == rid)
    assert s["aprendido"] == 2 and s["aprendiendo"] == 1


# ── topics ────────────────────────────────────────────────────────────────────

def test_topics_lists_tense_groups(client, db):
    _, headers = _make_teacher(client, db, "t@example.com")
    body = client.get("/v1/teachers/topics", headers=headers).json()
    ids = {g["id"] for g in body["tense_groups"]}
    assert "regular_present" in ids and "present_subjunctive" in ids
    assert all({"id", "title", "family", "family_label"} <= g.keys() for g in body["tense_groups"])
