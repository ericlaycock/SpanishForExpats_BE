"""Seed the missing Thu May 7 - Sat May 9 cohort window (v2 schedule).

Revision ID: 035_cohort_seed_thu_may7
Revises: 034_cohort_schedule_v2
Create Date: 2026-05-06

The 034 seed started Mon May 11. The user surfaced today (Wed May 6)
that the Thu May 7 window — which fits the same Mon-Wed / Thu-Sat
pattern — should be visible to anyone landing on the picker now. Adds
the three v2 slots (9am, 4pm, 7am-BO) for May 7-9.
"""
from alembic import op
import sqlalchemy as sa


revision = "035_cohort_seed_thu_may7"
down_revision = "034_cohort_schedule_v2"
branch_labels = None
depends_on = None


_SEED = [
    # slug, name, visibility, s1, s2, s3 (UTC; all PDT in May 2026)
    ("morning-may7",   "Morning",                        "public",         "2026-05-07 16:00:00+00", "2026-05-08 16:00:00+00", "2026-05-09 16:00:00+00"),
    ("afternoon-may7", "Afternoon",                      "public",         "2026-05-07 23:00:00+00", "2026-05-08 23:00:00+00", "2026-05-09 23:00:00+00"),
    ("bo-may7",        "Early Morning (Business Owner)", "business_owner", "2026-05-07 14:00:00+00", "2026-05-08 14:00:00+00", "2026-05-09 14:00:00+00"),
]


def upgrade() -> None:
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
        [
            {
                "slug": slug,
                "name": name,
                "visibility": vis,
                "session_1_start": s1,
                "session_2_start": s2,
                "session_3_start": s3,
            }
            for (slug, name, vis, s1, s2, s3) in _SEED
        ],
    )


def downgrade() -> None:
    quoted = ", ".join(f"'{s}'" for (s, *_rest) in _SEED)
    op.execute(f"DELETE FROM cohorts WHERE slug IN ({quoted})")
