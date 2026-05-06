"""Cohort schedule v2: 2 windows/week, 2 public + 1 business slots each.

Revision ID: 034_cohort_schedule_v2
Revises: 033_cohort_register_claim
Create Date: 2026-05-06

Replaces the v1 schedule (4 weekday types across Thu-Sat / Sun-Tue windows)
with a simpler structure:
  - Window 1: Mon-Wed
  - Window 2: Thu-Sat
  - Slots per window: 9am PT (public), 4pm PT (public), 7am PT (hidden BO)

Seeds 4 weeks of windows starting Mon May 11, 2026. The old W1/W2 cohorts
are deactivated (not deleted) so any existing registrations stay queryable.

Also creates cohort_waitlist for the picker's "all full" state.
"""
from datetime import date, timedelta

from alembic import op
import sqlalchemy as sa


revision = "034_cohort_schedule_v2"
down_revision = "033_cohort_register_claim"
branch_labels = None
depends_on = None


# All seed times are PDT (UTC-7) — May/early June 2026 is fully within DST.
# 7am PT  -> 14:00 UTC same day  (business owner)
# 9am PT  -> 16:00 UTC same day  (public)
# 4pm PT  -> 23:00 UTC same day  (public)

# Window start dates (Mon for W1, Thu for W2). 4 weeks × 2 windows = 8 windows.
_WINDOWS = [
    # (start_date, day_count_offsets) — sessions are start_date + 0/1/2 days
    "2026-05-11",  # Mon
    "2026-05-14",  # Thu
    "2026-05-18",  # Mon
    "2026-05-21",  # Thu
    "2026-05-25",  # Mon
    "2026-05-28",  # Thu
    "2026-06-01",  # Mon
    "2026-06-04",  # Thu
]

# (slug_prefix, name, visibility, utc_hour)
_SLOTS = [
    ("morning",   "Morning",                          "public",         "16:00:00+00"),
    ("afternoon", "Afternoon",                        "public",         "23:00:00+00"),
    ("bo",        "Early Morning (Business Owner)",   "business_owner", "14:00:00+00"),
]


def _build_seed():
    rows = []
    for start_date in _WINDOWS:
        # start_date is YYYY-MM-DD; sessions are start, start+1d, start+2d.
        y, m, d = (int(x) for x in start_date.split("-"))
        d0 = date(y, m, d)
        d1 = d0 + timedelta(days=1)
        d2 = d0 + timedelta(days=2)
        suffix = d0.strftime("%b%-d").lower()  # e.g. "may11"
        for slug_prefix, name, vis, utc_hour in _SLOTS:
            rows.append({
                "slug": f"{slug_prefix}-{suffix}",
                "name": name,
                "visibility": vis,
                "session_1_start": f"{d0.isoformat()} {utc_hour}",
                "session_2_start": f"{d1.isoformat()} {utc_hour}",
                "session_3_start": f"{d2.isoformat()} {utc_hour}",
            })
    return rows


def upgrade() -> None:
    # Deactivate v1 seeded cohorts (slugs ending in -w1 / -w2).
    op.execute(
        "UPDATE cohorts SET is_active = false "
        "WHERE slug LIKE '%-w1' OR slug LIKE '%-w2'"
    )

    # Waitlist table — used when every visible cohort is full.
    op.create_table(
        "cohort_waitlist",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(120), nullable=True),
        sa.Column("email", sa.String, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("email", name="uq_cohort_waitlist_email"),
    )
    op.create_index("ix_cohort_waitlist_email", "cohort_waitlist", ["email"])

    # Seed v2 cohorts. Idempotent on re-run via slug uniqueness.
    op.bulk_insert(
        sa.table(
            "cohorts",
            sa.column("slug", sa.String),
            sa.column("name", sa.String),
            sa.column("visibility", sa.String),
            sa.column("session_1_start", sa.DateTime(timezone=True)),
            sa.column("session_2_start", sa.DateTime(timezone=True)),
            sa.column("session_3_start", sa.DateTime(timezone=True)),
        ),
        _build_seed(),
    )


def downgrade() -> None:
    seed_slugs = [row["slug"] for row in _build_seed()]
    quoted = ", ".join(f"'{s}'" for s in seed_slugs)
    op.execute(f"DELETE FROM cohorts WHERE slug IN ({quoted})")

    op.drop_index("ix_cohort_waitlist_email", table_name="cohort_waitlist")
    op.drop_table("cohort_waitlist")

    op.execute(
        "UPDATE cohorts SET is_active = true "
        "WHERE slug LIKE '%-w1' OR slug LIKE '%-w2'"
    )
