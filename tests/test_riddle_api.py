"""Main module for the FastAPI application."""

from httpx import AsyncClient

from tests.test_auth_api import test_login


async def test_get_condition_not_found(ac: AsyncClient):
    """Test if the route returns 404 when the condition is not found."""
    response = await ac.get("/riddle/condition/:get_id", params={"get_id": 1})
    assert response.status_code == 404


async def test_generate_riddle(ac: AsyncClient):
    """Test if the route generates conditions."""
    response = await ac.post("/riddle/generate/:size", params={"size": 2})
    assert response.status_code == 200
    assert "conditions generated" in response.text


async def test_generate_riddle_wrong_size(ac: AsyncClient):
    """Test if the route returns 400 when the size is not 2 or 3."""
    response = await ac.post("/riddle/generate/:size", params={"size": 200})
    assert response.status_code == 400


async def test_get_condition(ac: AsyncClient):
    """Test if the route returns the condition."""
    await test_generate_riddle(ac)
    response = await ac.get("/riddle/condition/:get_id", params={"get_id": 1})
    assert response.status_code == 200
    assert response.json()  # Assuming this route returns JSON data


async def test_solve_riddle_401_unathorized(ac: AsyncClient):
    """Test if the route returns 401 when the user is not logged in."""
    data = {"matrix": [[1, 2], [3, 4]]}
    ac.cookies.clear()
    response = await ac.post("/riddle/solve", json=data)
    assert response.status_code == 401


async def test_solve_riddle_invalid_input(ac: AsyncClient):
    """Test if the route returns 400 when the input is invalid."""
    await test_login(ac)
    data = {"matrix": [[1, 2]]}
    response = await ac.post("/riddle/solve", json=data)
    assert response.status_code == 400


async def test_get_solution_without_solution(ac: AsyncClient):
    """Test if the route returns 400 when there is no solution."""
    await test_login(ac)
    response = await ac.get("/riddle/solution")
    assert response.status_code == 400
    assert response.json()  # Assuming this route returns JSON data


async def test_solve_riddle(ac: AsyncClient):
    """Test if the route solves the riddle."""
    data = {"matrix": [[1, 2], [3, 4]]}
    await test_login(ac)
    response = await ac.post("/riddle/solve", json=data)
    assert response.status_code == 200
    assert isinstance(response.json(), int)


async def test_get_solution(ac: AsyncClient):
    """Test if the route returns the solution."""
    await test_solve_riddle(ac)
    response = await ac.get("/riddle/solution")
    assert response.status_code == 200
    assert response.json()  # Assuming this route returns JSON data
