"""Widen vocab_card box cap from 5 to 6.

Revision ID: 050_vocab_box_cap_6
Revises: 049_memorize_completions
Create Date: 2026-05-28

The main vocab deck's Leitner ladder grew from 5 boxes ([1,2,4,8,16] days) to
6 ([1,3,7,16,35,60] days) so a word the learner nails every time spaces out to
~2 months instead of recurring at 16 days. A correct+fast review can now
promote a card to box 6, which the old `box <= 5` CHECK constraint rejected
with an IntegrityError on commit. Widen the cap to 6.
"""
from alembic import op


revision = "050_vocab_box_cap_6"
down_revision = "049_memorize_completions"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_constraint("ck_vocab_card_box", "vocab_card", type_="check")
    op.create_check_constraint(
        "ck_vocab_card_box", "vocab_card", "box >= 1 AND box <= 6"
    )


def downgrade() -> None:
    # Clamp any box-6 cards before re-tightening the constraint, or the
    # re-add would fail on existing rows.
    op.execute("UPDATE vocab_card SET box = 5 WHERE box > 5")
    op.drop_constraint("ck_vocab_card_box", "vocab_card", type_="check")
    op.create_check_constraint(
        "ck_vocab_card_box", "vocab_card", "box >= 1 AND box <= 5"
    )
