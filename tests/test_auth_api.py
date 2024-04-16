"""Tests for the auth API."""

import random
import string

from httpx import AsyncClient


# ORDER MATTERS


async def test_register(ac: AsyncClient) -> str:
    """Test if the route registers a user."""
    email = f"{''.join(random.choices(string.ascii_letters, k=20))}@example.com"

    data = {
        "email": email,
        "password": "string"
    }

    res = await ac.post("/auth/jwt/register", json=data)
    data = res.json()

    assert res.status_code == 201
    assert data == {
        'id': data['id'],
        'email': email,
        'is_active': True,
        'is_superuser': False,
        'is_verified': False}

    return email


async def test_login(ac: AsyncClient):
    """Test if the route logs in a user."""
    email = await test_register(ac)
    data = {
        "username": email,
        "password": "string"
    }

    res = await ac.post("/auth/jwt/login", data=data)

    assert res.status_code == 204
    jwt = res.cookies.get("JWT")
    assert jwt is not None
    ac.cookies.set("JWT", jwt)
