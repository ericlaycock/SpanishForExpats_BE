"""Tests for the GET /v1/subscription/invoices endpoint."""
from datetime import datetime, timezone
from types import SimpleNamespace
from unittest.mock import patch

from app.models import Subscription, User
from tests.conftest import register_user


def _ensure_customer(db, user_email, customer_id="cus_test_inv"):
    user = db.query(User).filter(User.email == user_email).one()
    sub = db.query(Subscription).filter(Subscription.user_id == user.id).first()
    if sub is None:
        sub = Subscription(user_id=user.id)
        db.add(sub)
    sub.stripe_customer_id = customer_id
    db.commit()
    return sub


def test_invoices_empty_when_no_customer(client):
    _, headers = register_user(client, email="inv_a@test.com")
    resp = client.get("/v1/subscription/invoices", headers=headers)
    assert resp.status_code == 200
    assert resp.json() == {"invoices": []}


def test_invoices_returns_mapped_rows(client, db):
    data, headers = register_user(client, email="inv_b@test.com")
    _ensure_customer(db, data["email"])

    fake_inv = SimpleNamespace(
        id="in_test_1",
        amount_paid=9900,
        currency="USD",
        status="paid",
        hosted_invoice_url="https://invoice.stripe.com/test",
        invoice_pdf="https://invoice.stripe.com/test/pdf",
        created=int(datetime.now(timezone.utc).timestamp()),
    )
    fake_list = SimpleNamespace(data=[fake_inv])

    with patch("app.config.settings.stripe_secret_key", "sk_test_fake"), \
         patch("stripe.Invoice.list", return_value=fake_list):
        resp = client.get("/v1/subscription/invoices", headers=headers)

    assert resp.status_code == 200
    body = resp.json()
    assert len(body["invoices"]) == 1
    item = body["invoices"][0]
    assert item["id"] == "in_test_1"
    assert item["amount_paid"] == 9900
    assert item["currency"] == "usd"  # normalized to lowercase
    assert item["status"] == "paid"
    assert item["hosted_invoice_url"].startswith("https://")
