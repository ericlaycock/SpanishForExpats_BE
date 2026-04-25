"""Idempotent placeholder for the original (reverted) grenade migration.

QA already ran a previous attempt at this migration (revision id
`023_add_daily_grenades`) that created `daily_grenades` and added
`user_words.last_seen_form`. The feature commit was reverted, deleting the
file, but `alembic_version` still pins QA to this revision id. We restore
the file so the chain resolves, and use IF NOT EXISTS so fresh databases
walk through the same step without conflict. The next migration (024)
restructures the schema into the production shape.

Revision ID: 023_add_daily_grenades
Revises: 022_add_word_type
Create Date: 2026-04-25
"""
from alembic import op


revision = "023_add_daily_grenades"
down_revision = "022_add_word_type"
branch_labels = None
depends_on = None


def upgrade():
    op.execute("ALTER TABLE user_words ADD COLUMN IF NOT EXISTS last_seen_form TEXT")
    op.execute("""
        CREATE TABLE IF NOT EXISTS daily_grenades (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            user_id UUID NOT NULL REFERENCES users(id),
            grenade_date DATE NOT NULL,
            user_word_id VARCHAR NOT NULL,
            word_id VARCHAR NOT NULL REFERENCES words(id),
            surface_form TEXT NOT NULL,
            audience VARCHAR(16) NOT NULL,
            sentence_es TEXT,
            sentence_en TEXT,
            generated_at TIMESTAMPTZ,
            used BOOLEAN,
            answered_at TIMESTAMPTZ,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            CONSTRAINT uq_daily_grenades_user_date UNIQUE (user_id, grenade_date),
            CONSTRAINT ck_daily_grenades_audience CHECK (audience IN ('friend', 'merchant'))
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_daily_grenades_user_date ON daily_grenades (user_id, grenade_date)")


def downgrade():
    op.execute("DROP INDEX IF EXISTS ix_daily_grenades_user_date")
    op.execute("DROP TABLE IF EXISTS daily_grenades")
    op.execute("ALTER TABLE user_words DROP COLUMN IF EXISTS last_seen_form")
