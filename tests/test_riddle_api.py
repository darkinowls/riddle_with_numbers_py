import httpx
from httpx import AsyncClient

from app.main import app
from tests.test_auth_api import test_login


async def test_get_condition_not_found(ac: AsyncClient):
    response = await ac.get("/riddle/condition/:get_id", params={"get_id": 1})
    assert response.status_code == 404


async def test_generate_riddle(ac: AsyncClient):
    response = await ac.post("/riddle/generate/:size", params={"size": 2})
    assert response.status_code == 200
    assert "conditions generated" in response.text

async def test_generate_riddle_wrong_size(ac: AsyncClient):
    response = await ac.post("/riddle/generate/:size", params={"size": 200})
    assert response.status_code == 400


async def test_get_condition(ac: AsyncClient):
    await test_generate_riddle(ac)
    response = await ac.get("/riddle/condition/:get_id", params={"get_id": 1})
    assert response.status_code == 200
    assert response.json()  # Assuming this route returns JSON data


async def test_solve_riddle_401_unathorized(ac: AsyncClient):
    data = {"matrix": [[1, 2], [3, 4]]}
    response = await ac.post("/riddle/solve", json=data)
    assert response.status_code == 401

async def test_solve_riddle_invalid_input(ac: AsyncClient):
    data = {"matrix": [[1, 2]]}
    response = await ac.post("/riddle/solve", json=data)
    assert response.status_code == 401

async def test_get_solution_without_solution(ac: AsyncClient):
    cookies = await test_login(ac)
    response = await ac.get("/riddle/solution", cookies={"JWT": cookies.get("JWT")})
    assert response.status_code == 400
    assert response.json()  # Assuming this route returns JSON data

async def test_solve_riddle(ac: AsyncClient) -> httpx.Cookies:
    data = {"matrix": [[1, 2], [3, 4]]}
    cookies = await test_login(ac)
    response = await ac.post("/riddle/solve", json=data, cookies={"JWT": cookies.get("JWT")})
    assert response.status_code == 200
    assert isinstance(response.json(), int)
    return cookies


async def test_get_solution(ac: AsyncClient):
    cookies = await test_solve_riddle(ac)
    response = await ac.get("/riddle/solution", cookies={"JWT": cookies.get("JWT")})
    assert response.status_code == 200
    assert response.json()  # Assuming this route returns JSON data
