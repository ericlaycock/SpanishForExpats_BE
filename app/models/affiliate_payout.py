"""Affiliate payout ledger.

One row per paying student who was referred by an affiliate. Created (status
'pending') by the Stripe webhook the moment a referred user first pays, then
flipped to 'paid' by an admin once the partner has actually been paid their
$100. A UniqueConstraint on user_id guarantees exactly one payout per student
and makes the webhook insert idempotent across event re-fires.
"""
import uuid

from sqlalchemy import (
    Column, DateTime, ForeignKey, Integer, String, UniqueConstraint, func,
)
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class AffiliatePayout(Base):
    __tablename__ = "affiliate_payouts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # The partner credited (matches User.affiliate_source / utm_source).
    affiliate_source = Column(String(64), nullable=False, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    # Stripe subscription id (string). Subscription's PK is user_id, not an `id`
    # column, so we store the Stripe key rather than a local FK.
    subscription_id = Column(String, nullable=True)
    amount_cents = Column(Integer, nullable=False, server_default="10000")  # $100
    currency = Column(String(8), nullable=False, server_default="usd")
    status = Column(String(16), nullable=False, server_default="pending", index=True)  # pending | paid
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    paid_at = Column(DateTime(timezone=True), nullable=True)

    __table_args__ = (UniqueConstraint("user_id", name="uq_affiliate_payout_user"),)
