"""Seed the teachers portal: ensure the teacher nathalia@spanishforexpats.com
exists (is_teacher=True) and assign her roster of students. Idempotent.

Each student is resolved to a real app user by email, falling back to a
conservative name match; the row is created regardless (email + display name),
so a student who hasn't registered yet is still assignable and auto-links when
they later sign up under that email.

Run (uses DATABASE_URL from the app settings, same as seed_qa.py):
    NATHALIA_PASSWORD='...' python -m scripts.seed_nathalia_teacher
    # or: python -m scripts.seed_nathalia_teacher '<password>'
The password is only used when CREATING the account; ignored if she already
exists (she should reset via the normal flow afterward).
"""
import os
import sys

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from app.auth import get_password_hash
from app.config import settings
from app.models import TeacherStudent, User

TEACHER_EMAIL = "nathalia@spanishforexpats.com"

# The assignment list: (login email, display name from the customer roster).
STUDENTS = [
    ("tamra.mcchesney@yahoo.com", "Tamra McChesney Rist"),
    ("tmlinnean60@gmail.com", "Treva Linnean"),
    ("aaronwarkov@gmail.com", "Aaron Warkov"),
    ("cderocher07@gmail.com", "Christopher Derocher"),
    ("rohmans4@gmail.com", "Shelley Rohman"),
    ("mileyflowers@gmail.com", "Miley C Flowers"),
    ("laraolsha@me.com", "Lara Olsha"),
    ("hello@infinitefreedommastery.com", "Justin D Richards"),
    ("ljarensen1@yahoo.com", "Lisa Joy Arensen"),
]


def resolve_user(db, email: str, name: str):
    """Match a student to a real app user: email first, then a conservative
    first+last name match (only accepted when it's unambiguous)."""
    u = db.query(User).filter(func.lower(User.email) == email.lower()).first()
    if u:
        return u, "email"
    tokens = [t for t in name.replace(".", " ").split() if len(t) > 2]
    if len(tokens) >= 2:
        matches = (
            db.query(User)
            .filter(User.name.ilike(f"%{tokens[0]}%"), User.name.ilike(f"%{tokens[-1]}%"))
            .all()
        )
        if len(matches) == 1:
            return matches[0], "name"
    return None, None


def main() -> None:
    password = (sys.argv[1] if len(sys.argv) > 1 else os.environ.get("NATHALIA_PASSWORD", "")).strip()
    engine = create_engine(settings.database_url, pool_pre_ping=True)
    db = sessionmaker(bind=engine)()
    try:
        teacher = db.query(User).filter(func.lower(User.email) == TEACHER_EMAIL).first()
        if teacher is None:
            if not password:
                sys.exit(
                    "Nathalia doesn't exist yet — pass an initial password as argv[1] "
                    "or set NATHALIA_PASSWORD."
                )
            teacher = User(
                email=TEACHER_EMAIL,
                password_hash=get_password_hash(password),
                is_teacher=True,
                name="Nathalia",
            )
            db.add(teacher)
            db.flush()
            print(f"created teacher {TEACHER_EMAIL} ({teacher.id})")
        else:
            teacher.is_teacher = True
            print(f"teacher {TEACHER_EMAIL} exists ({teacher.id}) — ensured is_teacher=True")

        linked = unlinked = skipped = 0
        for email, name in STUDENTS:
            email_l = email.lower()
            exists = (
                db.query(TeacherStudent)
                .filter(
                    TeacherStudent.teacher_id == teacher.id,
                    TeacherStudent.student_email == email_l,
                )
                .first()
            )
            if exists:
                skipped += 1
                continue
            student, how = resolve_user(db, email_l, name)
            db.add(
                TeacherStudent(
                    teacher_id=teacher.id,
                    student_email=email_l,
                    student_name=name,
                    student_user_id=student.id if student else None,
                )
            )
            if student:
                linked += 1
                print(f"  + {name} <{email_l}> → linked by {how} ({student.id})")
            else:
                unlinked += 1
                print(f"  + {name} <{email_l}> → no account (email+name only)")

        db.commit()
        print(f"done: linked={linked} unlinked={unlinked} skipped(existing)={skipped}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
