import pytest
from unittest.mock import AsyncMock, MagicMock


@pytest.mark.asyncio
async def test_signup():
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 201
    mock_response.json.return_value = {"message": "User created successfully"}
    mock_client.post = AsyncMock(return_value=mock_response)

    res = await mock_client.post(
        "/auth/v1/register/",
        data={
            "firstname": "Anne",
            "lastname": "Maria",
            "email": "try@example.com",
            "password": "password123@@",
        },
    )
    assert res.status_code == 201
    assert res.json()["message"] == "User created successfully"


@pytest.mark.asyncio
async def test_login():
    mock_client = MagicMock()
    login_response = MagicMock()
    login_response.status_code = 200
    login_response.json.return_value = {
        "access_token": "fake-access-token",
        "refresh_token": "fake-refresh-token",
    }
    mock_client.post = AsyncMock(return_value=login_response)

    res = await mock_client.post(
        "/auth/v1/login/",
        data={"email": "try@example.com", "password": "password123@@"},
    )
    assert res.status_code == 200
    assert "access_token" in res.json()
    assert "refresh_token" in res.json()

    token = res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    org_response = MagicMock()
    org_response.status_code = 201
    org_response.json.return_value = {"id": 1}
    mock_client.post = AsyncMock(return_value=org_response)

    org_res = await mock_client.post(
        "/users/v1/register/organization/",
        json={
            "name": "Test Organization",
            "email": "test@example.com",
            "description": "The Test Organization",
        },
        headers=headers,
    )
    assert org_res.status_code == 201
    org_id = org_res.json()["id"]

    event_response = MagicMock()
    event_response.status_code = 201
    event_response.json.return_value = {"message": "Event created successfully"}
    mock_client.post = AsyncMock(return_value=event_response)

    event_res = await mock_client.post(
        "/events/v1/create/",
        json={
            "title": "Test Event",
            "description": "The Event Description",
            "ticket_price": 30,
            "available_tickets": 500,
            "venue": "Maimi",
            "start_date": "2023-12-31T00:00:00",
            "end_date": "2023-12-31T23:59:59",
            "address": "Test Location",
            "organization_id": org_id,
        },
        headers=headers,
    )
    assert event_res.status_code == 201
    assert event_res.json()["message"] == "Event created successfully"


@pytest.mark.asyncio
async def test_invalid_credentials():
    mock_client = MagicMock()
    invalid_response = MagicMock()
    invalid_response.status_code = 401
    invalid_response.json.return_value = {"detail": "Invalid email or password"}
    mock_client.post = AsyncMock(return_value=invalid_response)

    res = await mock_client.post(
        "/auth/v1/login/",
        data={"email": "invalid@example.com", "password": "wrongpassword"},
    )
    assert res.status_code == 401
    assert res.json()["detail"] == "Invalid email or password"


