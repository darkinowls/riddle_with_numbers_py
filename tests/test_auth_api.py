import random
import string

from httpx import AsyncClient, Cookies

from tests.conftest import ac


# ORDER MATTERS

# async def test_add_role():
#     async with _async_session_maker() as session:
#         stmt = insert(Role).values(id=1, name="user")
#         await session.execute(stmt)
#         await session.commit()
#
#         query = select(Role)
#         result = await session.execute(query)
#         role_list = result.scalars().all()
#         assert len(role_list) == 1
#         assert role_list[0].name == "user"


async def test_register( ac: AsyncClient ) -> str:
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


async def test_login(ac: AsyncClient) -> Cookies:
    email = await test_register(ac)
    data = {
        "username": email,
        "password": "string"
    }

    res = await ac.post("/auth/jwt/login", data=data)

    assert res.status_code == 204
    jwt = res.cookies.get("JWT")
    assert jwt is not None
    return res.cookies
