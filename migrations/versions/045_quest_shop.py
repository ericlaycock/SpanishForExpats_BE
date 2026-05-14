"""Quest Shop — spendable coins on Tense Quest avatar skins.

Revision ID: 045_quest_shop
Revises: 044_user_category_progress
Create Date: 2026-05-14

Adds three tables (avatar catalog, ownership, spend audit) plus a column on
`users` for the equipped avatar. Seeds 1 free default + 4 paid skins.

Hard invariant (user-set): spending coins MUST NOT affect leaderboard rank.
`_user_points()` continues to sum lifetime earned from the three existing
tense_quest_* tables — coin spends live in their own `tense_quest_coin_spends`
audit table and are only subtracted by `_user_balance()` (shop affordability).

Revision ID kept short — alembic_version.version_num is varchar(32).
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


revision = "045_quest_shop"
down_revision = "044_user_category_progress"
branch_labels = None
depends_on = None


# Starter catalog. Pixel art is rendered FE-side from <rect> grids in
# components/tensequest/Sprites.tsx (matches the existing HeroSprite style),
# so `image_path` is a sentinel the FE maps to an SVG renderer rather than
# a path to an actual PNG. Keeps the migration self-contained.
_CATALOG = [
    # (id,             name,                price, is_default, sort_order)
    ("hero",           "Hero (default)",        0,  True,  0),
    ("pixel-fox",      "Pixel Fox",            25,  False, 1),
    ("pixel-wizard",   "Pixel Wizard",         50,  False, 2),
    ("pixel-ninja",    "Pixel Ninja",          75,  False, 3),
    ("pixel-knight",   "Pixel Knight",        100,  False, 4),
]


def upgrade() -> None:
    # ── catalog ─────────────────────────────────────────────────────────────
    op.create_table(
        "quest_avatars",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("image_path", sa.String(), nullable=False),
        sa.Column("price_coins", sa.Integer(), nullable=False),
        sa.Column("is_default", sa.Boolean(), server_default=sa.text("false"), nullable=False),
        sa.Column("sort_order", sa.Integer(), server_default="0", nullable=False),
        sa.CheckConstraint("price_coins >= 0", name="ck_quest_avatars_price_nonneg"),
    )

    # ── ownership ───────────────────────────────────────────────────────────
    op.create_table(
        "user_quest_avatars",
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("avatar_id", sa.String(), sa.ForeignKey("quest_avatars.id"), nullable=False),
        sa.Column("acquired_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint("user_id", "avatar_id", name="pk_user_quest_avatars"),
    )
    op.create_index("ix_user_quest_avatars_user", "user_quest_avatars", ["user_id"])

    # ── spend audit (never deletes from existing coin-source tables; the
    # leaderboard's `_user_points` stays untouched) ─────────────────────────
    op.create_table(
        "tense_quest_coin_spends",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.Column("reason", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint("amount > 0", name="ck_tq_coin_spend_amount_positive"),
    )
    op.create_index("ix_tq_coin_spends_user", "tense_quest_coin_spends", ["user_id"])

    # ── equipped avatar on users (nullable → falls back to 'hero' in the FE) ─
    op.add_column(
        "users",
        sa.Column("tq_avatar_id", sa.String(), sa.ForeignKey("quest_avatars.id"), nullable=True),
    )

    # ── seed the catalog ────────────────────────────────────────────────────
    for (aid, name, price, is_default, sort_order) in _CATALOG:
        op.execute(
            sa.text(
                """
                INSERT INTO quest_avatars (id, name, image_path, price_coins, is_default, sort_order)
                VALUES (:id, :name, :image_path, :price, :is_default, :sort)
                """
            ).bindparams(
                id=aid,
                name=name,
                # The FE maps `image_path` (a sentinel like "pixel-fox") to an
                # SVG sprite renderer in components/tensequest/Sprites.tsx —
                # not a literal /public asset path.
                image_path=aid,
                price=price,
                is_default=is_default,
                sort=sort_order,
            )
        )

    # Grandfather every existing user with the default avatar (free) so the
    # leaderboard shows a sprite for everyone, not just future buyers.
    op.execute(
        """
        INSERT INTO user_quest_avatars (user_id, avatar_id)
        SELECT id, 'hero' FROM users
        ON CONFLICT (user_id, avatar_id) DO NOTHING
        """
    )


def downgrade() -> None:
    op.drop_column("users", "tq_avatar_id")
    op.drop_index("ix_tq_coin_spends_user", table_name="tense_quest_coin_spends")
    op.drop_table("tense_quest_coin_spends")
    op.drop_index("ix_user_quest_avatars_user", table_name="user_quest_avatars")
    op.drop_table("user_quest_avatars")
    op.drop_table("quest_avatars")
