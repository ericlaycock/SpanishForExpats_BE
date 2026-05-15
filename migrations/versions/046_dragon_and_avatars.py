"""Dragon kills + avatar catalog swap + 7-bucket category split.

Revision ID: 046_dragon_and_avatars
Revises: 045_quest_shop
Create Date: 2026-05-15

Three coordinated changes, bundled atomically so we don't ship one half of a
state without the other:

1. **Category split** — `user_category_progress` previously enforced 5 valid
   values: present / past / future / modals / subjunctive. The new model has
   7: subjunctive splits into `subjunctive_triggers`, `present_subjunctive`,
   `imperfect_subjunctive`. Existing rows (grandfathered or not) keyed on
   `subjunctive` are expanded — one source row becomes three target rows
   carrying the same unlocked_at / diagnostic_result / diagnostic_at — then
   the source row is deleted. Gerund (GL 18) is also moving from the Present
   to the Modals category, but that's purely a code-side mapping change in
   `app/data/grammar_categories.py`; no DB rows store GLs.

2. **Avatar catalog swap** — replaces the 4 generic "Pixel Fox / Wizard /
   Ninja / Knight" skins with 6 LATAM-fantasy hybrids: Llama Knight, Cactus
   Paladin, Calavera Mage, Jaguar Warrior, Toucan Archer, Mariachi Bard.
   The 4 old skins just shipped to prod a day ago so effectively no users
   own them — but if any do (test accounts), we clean dependants first.
   Hero (the default free avatar) stays in place; everyone who owned it
   continues to own it.

3. **Pixel Dragon kills** — new `tense_quest_dragon_kills` table feeds the
   leaderboard via `_user_points` as a 4th coin source (alongside drill
   completions, sentence completions, review-card coins). Each row is one
   slain dragon = +30 coins toward lifetime earned. Per the user-set
   invariant ("affects total coins"), this contributes to rank, NOT just to
   wallet balance.

Revision ID kept short — alembic_version.version_num is varchar(32).
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


revision = "046_dragon_and_avatars"
down_revision = "045_quest_shop"
branch_labels = None
depends_on = None


# Old avatar ids that we're retiring. Bundled here so the up + downgrade
# paths both reference the same list.
_OLD_PAID_AVATARS = ("pixel-fox", "pixel-wizard", "pixel-ninja", "pixel-knight")

# New paid catalog (sort_order is the on-screen ordering on the shop page).
_NEW_PAID_CATALOG = [
    # (id,                name,                price, sort_order)
    ("llama-knight",      "Llama Knight",         25,  1),
    ("cactus-paladin",    "Cactus Paladin",       50,  2),
    ("calavera-mage",     "Calavera Mage",        75,  3),
    ("jaguar-warrior",    "Jaguar Warrior",      100,  4),
    ("toucan-archer",     "Toucan Archer",       150,  5),
    ("mariachi-bard",     "Mariachi Bard",       200,  6),
]


def upgrade() -> None:
    # ── 1. Category split ────────────────────────────────────────────────────

    # The old constraint allows 'subjunctive'; the new one doesn't. We must
    # drop old → expand rows → delete old rows → add new, in that exact
    # order. If we add the new constraint while any 'subjunctive' row still
    # exists, ADD CONSTRAINT validates against existing data and aborts the
    # migration with CheckViolation (the QA crash that surfaced this fix).
    op.drop_constraint("ck_user_category_value", "user_category_progress", type_="check")

    # Expand every existing 'subjunctive' row into three. Preserves
    # unlocked_at / diagnostic_result / diagnostic_at on each child so
    # grandfathered users stay fully-unlocked across all three new buckets,
    # and mid-flow users (with unlocked_at NULL) stay consistently locked
    # across the three.
    op.execute(
        """
        INSERT INTO user_category_progress
          (id, user_id, category, diagnostic_result, unlocked_at, diagnostic_at, created_at)
        SELECT gen_random_uuid(),
               user_id,
               cat.category,
               diagnostic_result,
               unlocked_at,
               diagnostic_at,
               NOW()
        FROM user_category_progress
        CROSS JOIN (VALUES
          ('subjunctive_triggers'),
          ('present_subjunctive'),
          ('imperfect_subjunctive')
        ) AS cat(category)
        WHERE category = 'subjunctive'
        ON CONFLICT (user_id, category) DO NOTHING
        """
    )
    op.execute("DELETE FROM user_category_progress WHERE category = 'subjunctive'")

    op.create_check_constraint(
        "ck_user_category_value",
        "user_category_progress",
        "category IN ('present','past','future','modals',"
        "'subjunctive_triggers','present_subjunctive','imperfect_subjunctive')",
    )

    # ── 2. Avatar catalog swap ───────────────────────────────────────────────

    # Wipe ownership rows for the retiring skins so the catalog DELETE
    # doesn't FK-violate. If a user had one equipped, fall back to 'hero'
    # (the free default that everyone owns from migration 045).
    op.execute(
        """
        UPDATE users SET tq_avatar_id = 'hero'
        WHERE tq_avatar_id IN ('pixel-fox','pixel-wizard','pixel-ninja','pixel-knight')
        """
    )
    op.execute(
        """
        DELETE FROM user_quest_avatars
        WHERE avatar_id IN ('pixel-fox','pixel-wizard','pixel-ninja','pixel-knight')
        """
    )
    # Leave tense_quest_coin_spends rows alone — that's an audit log; the
    # reason text ("avatar:pixel-fox") still tells the story even after the
    # catalog row is gone.
    op.execute(
        """
        DELETE FROM quest_avatars
        WHERE id IN ('pixel-fox','pixel-wizard','pixel-ninja','pixel-knight')
        """
    )

    # Insert the new catalog. `image_path` is a sentinel (avatar id) the FE
    # AvatarSprite dispatcher maps to a <rect>-grid renderer — not a literal
    # /public asset path, so no PNGs are checked in.
    for (aid, name, price, sort_order) in _NEW_PAID_CATALOG:
        op.execute(
            sa.text(
                """
                INSERT INTO quest_avatars (id, name, image_path, price_coins, is_default, sort_order)
                VALUES (:id, :name, :image_path, :price, false, :sort)
                """
            ).bindparams(id=aid, name=name, image_path=aid, price=price, sort=sort_order)
        )

    # ── 3. tense_quest_dragon_kills table ───────────────────────────────────

    op.create_table(
        "tense_quest_dragon_kills",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("user_id", UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("coins_awarded", sa.Integer(), nullable=False),
        sa.Column("killed_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint("coins_awarded > 0", name="ck_tq_dragon_coins_positive"),
    )
    op.create_index("ix_tq_dragon_kills_user", "tense_quest_dragon_kills", ["user_id"])


def downgrade() -> None:
    # ── 3 reverse ────────────────────────────────────────────────────────────
    op.drop_index("ix_tq_dragon_kills_user", table_name="tense_quest_dragon_kills")
    op.drop_table("tense_quest_dragon_kills")

    # ── 2 reverse — restore the original 4 paid skins. ──────────────────────
    # Users who acquired any of the new 6 skins between this migration
    # running and the downgrade lose them; the audit log in
    # tense_quest_coin_spends still records the spend. Acceptable for a
    # downgrade path on a feature this fresh.
    op.execute(
        """
        UPDATE users SET tq_avatar_id = 'hero'
        WHERE tq_avatar_id IN ('llama-knight','cactus-paladin','calavera-mage',
                               'jaguar-warrior','toucan-archer','mariachi-bard')
        """
    )
    op.execute(
        """
        DELETE FROM user_quest_avatars
        WHERE avatar_id IN ('llama-knight','cactus-paladin','calavera-mage',
                            'jaguar-warrior','toucan-archer','mariachi-bard')
        """
    )
    op.execute(
        """
        DELETE FROM quest_avatars
        WHERE id IN ('llama-knight','cactus-paladin','calavera-mage',
                     'jaguar-warrior','toucan-archer','mariachi-bard')
        """
    )
    op.execute(
        """
        INSERT INTO quest_avatars (id, name, image_path, price_coins, is_default, sort_order)
        VALUES
          ('pixel-fox',    'Pixel Fox',     'pixel-fox',     25, false, 1),
          ('pixel-wizard', 'Pixel Wizard',  'pixel-wizard',  50, false, 2),
          ('pixel-ninja',  'Pixel Ninja',   'pixel-ninja',   75, false, 3),
          ('pixel-knight', 'Pixel Knight',  'pixel-knight', 100, false, 4)
        """
    )

    # ── 1 reverse — collapse the three new subjunctive buckets back to one. ──
    op.execute(
        """
        INSERT INTO user_category_progress
          (id, user_id, category, diagnostic_result, unlocked_at, diagnostic_at, created_at)
        SELECT gen_random_uuid(),
               user_id,
               'subjunctive',
               MIN(diagnostic_result),
               MIN(unlocked_at),
               MIN(diagnostic_at),
               NOW()
        FROM user_category_progress
        WHERE category IN ('subjunctive_triggers','present_subjunctive','imperfect_subjunctive')
        GROUP BY user_id
        ON CONFLICT (user_id, category) DO NOTHING
        """
    )
    op.execute(
        """
        DELETE FROM user_category_progress
        WHERE category IN ('subjunctive_triggers','present_subjunctive','imperfect_subjunctive')
        """
    )

    op.drop_constraint("ck_user_category_value", "user_category_progress", type_="check")
    op.create_check_constraint(
        "ck_user_category_value",
        "user_category_progress",
        "category IN ('present','past','future','modals','subjunctive')",
    )
