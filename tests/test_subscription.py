from tests.conftest import register_user
from app.services.subscription_service import FREE_ENCOUNTERS_LIMIT


def test_get_subscription_status(client, seed_data):
    _, headers = register_user(client)
    resp = client.get("/v1/subscription/status", headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["active"] is False
    assert data["free_situations_limit"] == FREE_ENCOUNTERS_LIMIT
    assert data["free_situations_remaining"] == FREE_ENCOUNTERS_LIMIT
