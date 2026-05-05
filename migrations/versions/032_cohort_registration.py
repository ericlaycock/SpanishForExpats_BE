"""Add cohorts and cohort_registrations tables; seed 8 initial cohorts.

Revision ID: 032_cohort_registration
Revises: 031_realtime_steering_state
Create Date: 2026-05-05

Backs the cohort-registration step that replaces the standalone signup at
the end of the marketing webflow. Each Cohort holds 3 timezone-aware
session timestamps (stored UTC); the FE renders Pacific Time + the user's
local zone. Initial seed: 4 cohort types (Morning / Afternoon / Evening /
Early Morning Business Owner) across 2 weeks (May 7-9 and May 10-12, 2026).
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


revision = "032_cohort_registration"
down_revision = "031_realtime_steering"
branch_labels = None
depends_on = None


# All times are PDT (UTC-7) in May 2026.
# 7am PT  -> 14:00 UTC same day
# 10am PT -> 17:00 UTC same day
# 1pm PT  -> 20:00 UTC same day
# 5pm PT  -> 00:00 UTC next day
_SEED = [
    # slug, name, visibility, s1, s2, s3
    ("morning-w1",        "Morning",        "public",         "2026-05-07 17:00:00+00", "2026-05-08 17:00:00+00", "2026-05-09 17:00:00+00"),
    ("afternoon-w1",      "Afternoon",      "public",         "2026-05-07 20:00:00+00", "2026-05-08 20:00:00+00", "2026-05-09 20:00:00+00"),
    ("evening-w1",        "Evening",        "public",         "2026-05-08 00:00:00+00", "2026-05-09 00:00:00+00", "2026-05-10 00:00:00+00"),
    ("early-morning-bo-w1","Early Morning (Business Owner)","business_owner","2026-05-07 14:00:00+00","2026-05-08 14:00:00+00","2026-05-09 14:00:00+00"),
    ("morning-w2",        "Morning",        "public",         "2026-05-10 17:00:00+00", "2026-05-11 17:00:00+00", "2026-05-12 17:00:00+00"),
    ("afternoon-w2",      "Afternoon",      "public",         "2026-05-10 20:00:00+00", "2026-05-11 20:00:00+00", "2026-05-12 20:00:00+00"),
    ("evening-w2",        "Evening",        "public",         "2026-05-11 00:00:00+00", "2026-05-12 00:00:00+00", "2026-05-13 00:00:00+00"),
    ("early-morning-bo-w2","Early Morning (Business Owner)","business_owner","2026-05-10 14:00:00+00","2026-05-11 14:00:00+00","2026-05-12 14:00:00+00"),
]


def upgrade() -> None:
    op.create_table(
        "cohorts",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("slug", sa.String(64), nullable=False),
        sa.Column("name", sa.String(64), nullable=False),
        sa.Column("visibility", sa.String(32), nullable=False, server_default="public"),
        sa.Column("capacity", sa.Integer, nullable=False, server_default="8"),
        sa.Column("timezone", sa.String(64), nullable=False, server_default="America/Los_Angeles"),
        sa.Column("session_1_start", sa.DateTime(timezone=True), nullable=False),
        sa.Column("session_2_start", sa.DateTime(timezone=True), nullable=False),
        sa.Column("session_3_start", sa.DateTime(timezone=True), nullable=False),
        sa.Column("duration_minutes", sa.Integer, nullable=False, server_default="60"),
        sa.Column("is_active", sa.Boolean, nullable=False, server_default=sa.text("true")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("slug", name="uq_cohorts_slug"),
        sa.CheckConstraint(
            "visibility IN ('public', 'business_owner')",
            name="ck_cohorts_visibility",
        ),
    )

    op.create_table(
        "cohort_registrations",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("cohort_id", sa.Integer, sa.ForeignKey("cohorts.id"), nullable=False),
        sa.Column(
            "user_id",
            UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("email", sa.String, nullable=False),
        sa.Column("confirmation_token", sa.String(64), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("confirmation_token", name="uq_cohort_reg_token"),
        sa.UniqueConstraint("cohort_id", "user_id", name="uq_cohort_user"),
    )
    op.create_index("ix_cohort_reg_cohort", "cohort_registrations", ["cohort_id"])
    op.create_index("ix_cohort_reg_user", "cohort_registrations", ["user_id"])
    op.create_index("ix_cohort_reg_email", "cohort_registrations", ["email"])

    # Seed initial cohorts. Idempotent on re-run via slug uniqueness check.
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
    op.drop_index("ix_cohort_reg_email", table_name="cohort_registrations")
    op.drop_index("ix_cohort_reg_user", table_name="cohort_registrations")
    op.drop_index("ix_cohort_reg_cohort", table_name="cohort_registrations")
    op.drop_table("cohort_registrations")
    op.drop_table("cohorts")
