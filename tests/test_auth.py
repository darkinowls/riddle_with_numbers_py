from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)
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


def test_register():
    # TODO : user already exsits
    data = {
        "email": "user@example.com",
        "password": "string"
    }

    res = client.post("/auth/jwt/register", json=data)

    print(res.json())

    assert res.status_code == 201
    assert res.json() == {'email': 'user@example.com', 'is_active': True, 'is_superuser': False,
                          'is_verified': False, 'role_id': 1,}




