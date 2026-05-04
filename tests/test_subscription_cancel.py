"""Tests for the in-app cancel/reactivate flow + lifecycle webhook updates."""
from datetime import datetime, timedelta, timezone
from unittest.mock import patch
from types import SimpleNamespace

from app.models import Subscription, User
from tests.conftest import register_user


def _activate_sub(db, user_email, *, stripe_sub_id="sub_test_123"):
    """Helper: flip a freshly-registered user to an active premium sub."""
    user = db.query(User).filter(User.email == user_email).one()
    sub = db.query(Subscription).filter(Subscription.user_id == user.id).first()
    if sub is None:
        sub = Subscription(user_id=user.id)
        db.add(sub)
    sub.active = True
    sub.tier = "pro"
    sub.plan = "pro"
    sub.billing_cycle = "monthly"
    sub.stripe_customer_id = "cus_test_123"
    sub.stripe_subscription_id = stripe_sub_id
    db.commit()
    return sub


def test_cancel_requires_active_subscription(client):
    _, headers = register_user(client)
    resp = client.post("/v1/subscription/cancel", json={}, headers=headers)
    assert resp.status_code == 400
    assert "no active subscription" in resp.json()["detail"].lower()


def test_cancel_sets_cancel_at_period_end(client, db):
    data, headers = register_user(client, email="cancel_a@test.com")
    _activate_sub(db, data["email"], stripe_sub_id="sub_cancel_a")

    period_end_epoch = int((datetime.now(timezone.utc) + timedelta(days=14)).timestamp())
    fake_stripe_sub = SimpleNamespace(
        id="sub_cancel_a",
        status="active",
        cancel_at_period_end=True,
        current_period_end=period_end_epoch,
        canceled_at=int(datetime.now(timezone.utc).timestamp()),
    )

    with patch("app.config.settings.stripe_secret_key", "sk_test_fake"), \
         patch("stripe.Subscription.modify", return_value=fake_stripe_sub) as mock_modify:
        resp = client.post(
            "/v1/subscription/cancel",
            json={"reason": "too_expensive", "note": "saving money"},
            headers=headers,
        )

    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["cancel_at_period_end"] is True
    assert body["active"] is True  # still active until period end
    assert body["current_period_end"] is not None
    assert body["canceled_at"] is not None
    mock_modify.assert_called_once()
    _, kwargs = mock_modify.call_args
    assert kwargs["cancel_at_period_end"] is True

    # Reason persisted on the row for analytics
    sub = db.query(Subscription).filter(Subscription.stripe_subscription_id == "sub_cancel_a").one()
    assert sub.cancel_reason and "too_expensive" in sub.cancel_reason
    assert "saving money" in sub.cancel_reason


def test_reactivate_clears_pending_cancel(client, db):
    data, headers = register_user(client, email="cancel_b@test.com")
    sub = _activate_sub(db, data["email"], stripe_sub_id="sub_cancel_b")
    sub.cancel_at_period_end = True
    sub.canceled_at = datetime.now(timezone.utc)
    sub.cancel_reason = "too_expensive"
    db.commit()

    with patch("app.config.settings.stripe_secret_key", "sk_test_fake"), \
         patch("stripe.Subscription.modify") as mock_modify:
        resp = client.post("/v1/subscription/reactivate", headers=headers)

    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["cancel_at_period_end"] is False
    assert body["canceled_at"] is None
    mock_modify.assert_called_once()
    _, kwargs = mock_modify.call_args
    assert kwargs["cancel_at_period_end"] is False


def test_reactivate_idempotent_when_not_canceled(client, db):
    data, headers = register_user(client, email="cancel_c@test.com")
    _activate_sub(db, data["email"], stripe_sub_id="sub_cancel_c")  # cancel_at_period_end=False

    with patch("app.config.settings.stripe_secret_key", "sk_test_fake"), \
         patch("stripe.Subscription.modify") as mock_modify:
        resp = client.post("/v1/subscription/reactivate", headers=headers)

    assert resp.status_code == 200
    # No Stripe call needed when there's nothing to undo
    mock_modify.assert_not_called()


def test_webhook_subscription_updated_persists_lifecycle(client, db):
    data, _ = register_user(client, email="cancel_d@test.com")
    _activate_sub(db, data["email"], stripe_sub_id="sub_cancel_d")

    period_end_epoch = int((datetime.now(timezone.utc) + timedelta(days=10)).timestamp())
    canceled_epoch = int(datetime.now(timezone.utc).timestamp())

    payload = {
        "id": "evt_test",
        "object": "event",
        "type": "customer.subscription.updated",
        "data": {
            "object": {
                "id": "sub_cancel_d",
                "object": "subscription",
                "status": "active",
                "cancel_at_period_end": True,
                "current_period_end": period_end_epoch,
                "canceled_at": canceled_epoch,
            },
        },
    }

    # Use stub mode (no signature secret) — matches the dev branch in the route
    with patch("app.config.settings.stripe_webhook_secret", None):
        resp = client.post("/v1/subscription/webhook", json=payload)

    assert resp.status_code == 200
    sub = db.query(Subscription).filter(Subscription.stripe_subscription_id == "sub_cancel_d").one()
    assert sub.cancel_at_period_end is True
    assert sub.active is True
    assert sub.current_period_end is not None
    assert sub.canceled_at is not None


def test_webhook_subscription_deleted_flips_active(client, db):
    data, _ = register_user(client, email="cancel_e@test.com")
    sub = _activate_sub(db, data["email"], stripe_sub_id="sub_cancel_e")
    sub.cancel_at_period_end = True
    db.commit()

    payload = {
        "id": "evt_del",
        "object": "event",
        "type": "customer.subscription.deleted",
        "data": {"object": {"id": "sub_cancel_e", "object": "subscription", "status": "canceled"}},
    }
    with patch("app.config.settings.stripe_webhook_secret", None):
        resp = client.post("/v1/subscription/webhook", json=payload)

    assert resp.status_code == 200
    refreshed = db.query(Subscription).filter(Subscription.stripe_subscription_id == "sub_cancel_e").one()
    assert refreshed.active is False
    assert refreshed.cancel_at_period_end is False
    assert refreshed.canceled_at is not None
