# Teachers Portal

A teachers-only surface where a tutor tracks each assigned student's progress
per topic. It is a **manual tracking overlay** — fully decoupled from the
student's real SRS/mastery data. It never reads or writes student progress, and
works for students who have never created an app account.

## Model

- **Role:** `users.is_teacher` (boolean, like `is_admin`). Admins are implicitly
  allowed. Login responses (`/v1/auth/login`, `/register`) include `is_teacher`.
- **Roster:** `teacher_student(teacher_id, student_email, student_name,
  student_user_id?)`. The student is identified by email + display name;
  `student_user_id` links a real `users` row when one exists (nullable). Unique
  `(teacher_id, student_email)`.
- **Overlay:** `teacher_student_topic_state(teacher_student_id, topic_type,
  topic_id, state)`, keyed to the **roster row** (not a user). One row per
  topic. An **absent row = `no_aprendido`**; the API deletes rows set back to
  `no_aprendido` to keep the table sparse. Unique
  `(teacher_student_id, topic_type, topic_id)`.
  - `state ∈ { no_aprendido, aprendiendo, aprendido }` (CHECK).
  - `topic_type ∈ { vocab_module, tense_group }` (CHECK).
  - `topic_id` is opaque to the BE: a vocab module slug from the FE
    `components/tensequest/vocabData.ts` `VOCAB_BANDS` (e.g. `freq-500-514`,
    `banking-1-15`), or a tense-group id from `app/data/tense_quest.py`
    `list_tense_groups()` (e.g. `regular_present`, `present_subjunctive`).

Migration: `052_teacher_portal`.

## API (`/v1/teachers`, gated by `is_teacher` or `is_admin`)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/students` | The caller's roster (`id`, `student_email`, `student_name`, `has_account`). |
| GET | `/students/{roster_id}` | Roster row + its non-default `states[]`. 404 if not the caller's. |
| PUT | `/students/{roster_id}/state` | Upsert `{topic_type, topic_id, state}`. `no_aprendido` deletes the row. |
| GET | `/topics` | Static verb taxonomy (tense groups grouped by family) for the verb board. Vocab modules live in the FE. |

Code: `app/api/v1/teachers.py`, `app/models/teacher.py`. Tests: `tests/test_teachers.py`.

## Frontend (ExpatQuest surface)

- Routes: `app/[locale]/teachers/page.tsx` (roster), `app/[locale]/teachers/[rosterId]/page.tsx`
  (student board — header shows student name + login email). Gated by
  `useRequireTeacher()` in `contexts/AuthContext.tsx`. Teachers are redirected
  to `/teachers` on login.
- Components: `components/teachers/{TeacherStudentList,StudentTopicBoard,MasteryToggle}.tsx`.
  The board reuses `VOCAB_BANDS` (vocab) and `/v1/teachers/topics` (verbs),
  grouped by the same bands as the live maps.
- Data: `lib/api/teachers.ts` (raw fetch, not the openapi client — same pattern
  as `lib/api/tensequest.ts`), `lib/queries/teachers.ts`, `lib/mutations/teachers.ts`
  (`useSetTopicState`, optimistic).

## Seeding

`scripts/seed_nathalia_teacher.py` creates `nathalia@spanishforexpats.com`
(`is_teacher=True`) and assigns her roster, resolving each student by email then
name. Idempotent. Password supplied via argv/`NATHALIA_PASSWORD` on first
creation only.
