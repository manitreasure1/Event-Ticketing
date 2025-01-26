import json
from httpx import ASGITransport, AsyncClient
import pytest


@pytest.mark.asyncio
async def test_signup(client):
    res = await client.post(
        "/auth/v1/signup/",
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
async def test_login(client):
    res = await client.post(
        "/auth/v1/login/",
          data={"email": "try@example.com", "password":"password123@@"})
    assert res.status_code == 200
    assert "access_token" in res.json()
    

@pytest.mark.asyncio
async def test_invalid_credentials(client):
    res = await client.post(
        "/auth/v1/login/",
          data={"email": "invalid@example.com", "password": "wrongpassword"})
    assert res.status_code == 401
    assert res.json()["detail"] == "Invalid email or password" 

# async def test_signout():
#     pass


