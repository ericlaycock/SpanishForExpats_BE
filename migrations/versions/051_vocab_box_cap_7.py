"""Widen vocab_card box cap from 6 to 7 (unified SRS ladder).

Revision ID: 051_vocab_box_cap_7
Revises: 050_vocab_box_cap_6
Create Date: 2026-05-28

The two SRS implementations were merged into one engine (`app/services/srs.py`)
with a single 7-box ladder (4h, 1d, 3d, 1w, 16d, 35d, 60d). The vocab deck now
shares it, so a main-deck card can reach box 7. Migration 050 had only widened
the CHECK to <=6; widen it to <=7 so the top rung doesn't throw an
IntegrityError on commit.
"""
from alembic import op


revision = "051_vocab_box_cap_7"
down_revision = "050_vocab_box_cap_6"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_constraint("ck_vocab_card_box", "vocab_card", type_="check")
    op.create_check_constraint(
        "ck_vocab_card_box", "vocab_card", "box >= 1 AND box <= 7"
    )


def downgrade() -> None:
    # Clamp any box-7 cards before re-tightening, or the re-add fails on them.
    op.execute("UPDATE vocab_card SET box = 6 WHERE box > 6")
    op.drop_constraint("ck_vocab_card_box", "vocab_card", type_="check")
    op.create_check_constraint(
        "ck_vocab_card_box", "vocab_card", "box >= 1 AND box <= 6"
    )
