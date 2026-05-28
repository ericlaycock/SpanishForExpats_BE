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


# ── topics ────────────────────────────────────────────────────────────────────

def test_topics_lists_tense_groups(client, db):
    _, headers = _make_teacher(client, db, "t@example.com")
    body = client.get("/v1/teachers/topics", headers=headers).json()
    ids = {g["id"] for g in body["tense_groups"]}
    assert "regular_present" in ids and "present_subjunctive" in ids
    assert all({"id", "title", "family", "family_label"} <= g.keys() for g in body["tense_groups"])
