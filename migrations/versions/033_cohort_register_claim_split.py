"""Cohort registration: defer account creation to a claim step.

Revision ID: 033_cohort_register_claim
Revises: 032_cohort_registration
Create Date: 2026-05-05

Original v1 created the User account at registration time (password
required). Reworked flow collects only name + email at registration,
shows the confirmation screen with .ics download + email, and asks for
the password on the confirmation screen ("Activate app access"). The
password step calls /claim which creates the User account and links it
to the existing CohortRegistration row.

Schema changes:
- cohort_registrations.user_id → nullable
- drop unique(cohort_id, user_id), add unique(cohort_id, email) so
  duplicate-registration protection now keys off the email
- rename seeded "Morning" cohort to "Late Morning" (Early Morning
  already exists at 7am, so calling 10am "Morning" is misleading)
"""
from alembic import op
import sqlalchemy as sa


revision = "033_cohort_register_claim"
down_revision = "032_cohort_registration"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        "cohort_registrations", "user_id",
        existing_type=sa.dialects.postgresql.UUID(as_uuid=True),
        nullable=True,
    )
    op.drop_constraint("uq_cohort_user", "cohort_registrations", type_="unique")
    op.create_unique_constraint(
        "uq_cohort_email", "cohort_registrations", ["cohort_id", "email"]
    )
    op.execute("UPDATE cohorts SET name = 'Late Morning' WHERE name = 'Morning'")


def downgrade() -> None:
    op.execute("UPDATE cohorts SET name = 'Morning' WHERE name = 'Late Morning'")
    op.drop_constraint("uq_cohort_email", "cohort_registrations", type_="unique")
    op.create_unique_constraint(
        "uq_cohort_user", "cohort_registrations", ["cohort_id", "user_id"]
    )
    op.alter_column(
        "cohort_registrations", "user_id",
        existing_type=sa.dialects.postgresql.UUID(as_uuid=True),
        nullable=False,
    )
