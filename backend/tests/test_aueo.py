
import pytest


@pytest.mark.asyncio
async def test_signup(client):
    res = await client.post(
        "/auth/v1/register/",
        data={
            "firstname": "Anne",
            "lastname": "Maria",
            "email": "try@example.com",
            "password": "password123@@",
        },
    )
    print(res.json())
    assert res.status_code == 201
    assert res.json()["message"] =="User created successfully"

        
@pytest.mark.asyncio
async def test_login(client):
    res = await client.post(
        "/auth/v1/login/",
          data={"email": "try@example.com", "password":"password123@@"}
          )
    print(res.json())
    assert res.status_code == 200
    assert "access_token" in res.json()
    assert "refresh_token" in res.json()

    token = res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    org_res = await client.post(
        "/users/v1/register/organization/",
        json={
            "name": "Test Organization",
            "email": "test@example.com",
            "description": "The Test Organization"
            },
        headers=headers
    )
    assert org_res.status_code == 201
    org_id = org_res.json()["id"]


    event_res = await client.post(
        "/events/v1/create/",
        json={
            "name": "Test Event",
            "description": "The Event Description",
            "ticket_price": 30,
            "tickets_available": 500,
            "venue": "Maimi",
            "date": "2023-12-31",
            "address": "Test Location",
            "organization_id": org_id
        },
        headers=headers
    )
    assert event_res.status_code == 201
    assert event_res.json()["message"] == "Event created successfully"


@pytest.mark.asyncio
async def test_invalid_credentials(client):
    res = await client.post(
        "/auth/v1/login/",
          data={"email": "invalid@example.com", "password": "wrongpassword"})
    assert res.status_code == 401
    assert res.json()["detail"] == "Invalid email or password"

# async def test_signout():
#     pass


