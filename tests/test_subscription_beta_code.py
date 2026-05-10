from tests.conftest import register_user


def test_redeem_beta_code_valid(client, seed_data):
    _, headers = register_user(client, email="beta_valid@example.com")

    # Fresh free user — beta_redeemed defaults to False.
    status = client.get("/v1/subscription/status", headers=headers).json()
    assert status["beta_redeemed"] is False
    assert status["active"] is False

    resp = client.post(
        "/v1/subscription/redeem-beta-code",
        json={"code": "N1066"},
        headers=headers,
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["beta_redeemed"] is True

    # Persists across calls.
    again = client.get("/v1/subscription/status", headers=headers).json()
    assert again["beta_redeemed"] is True


def test_redeem_beta_code_case_insensitive_with_whitespace(client, seed_data):
    _, headers = register_user(client, email="beta_ci@example.com")
    resp = client.post(
        "/v1/subscription/redeem-beta-code",
        json={"code": "  n1066 "},
        headers=headers,
    )
    assert resp.status_code == 200
    assert resp.json()["beta_redeemed"] is True


def test_redeem_beta_code_invalid(client, seed_data):
    _, headers = register_user(client, email="beta_invalid@example.com")
    resp = client.post(
        "/v1/subscription/redeem-beta-code",
        json={"code": "WRONG"},
        headers=headers,
    )
    assert resp.status_code == 400
    assert "Invalid" in resp.json()["detail"]

    status = client.get("/v1/subscription/status", headers=headers).json()
    assert status["beta_redeemed"] is False


def test_redeem_beta_code_idempotent(client, seed_data):
    _, headers = register_user(client, email="beta_idem@example.com")

    first = client.post(
        "/v1/subscription/redeem-beta-code",
        json={"code": "N1066"},
        headers=headers,
    )
    assert first.status_code == 200

    # Second redemption succeeds and stays redeemed (timestamp doesn't reset).
    second = client.post(
        "/v1/subscription/redeem-beta-code",
        json={"code": "N1066"},
        headers=headers,
    )
    assert second.status_code == 200
    assert second.json()["beta_redeemed"] is True


def test_redeem_beta_code_requires_auth(client, seed_data):
    resp = client.post(
        "/v1/subscription/redeem-beta-code",
        json={"code": "N1066"},
    )
    assert resp.status_code in (401, 403)
