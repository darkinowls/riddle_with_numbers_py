import uuid

import orjson
from fastapi import APIRouter, Depends, HTTPException
from fastapi_users import FastAPIUsers
from pydantic import BaseModel, Field
from sqlalchemy import insert, select, text, Row

from app.auth.auth import auth_backend
from app.auth.models import User
from app.auth.router import current_user
from app.auth.user_manager import get_user_manager
from app.database import get_async_session
from app.riddle.logic.cell import Cell, translate_to_cells
from app.riddle.logic.condition_generator import generate_all_matrices
from app.riddle.logic.riddle import solve_matrix
from app.riddle.logic.util import validate_input_matrix
from app.riddle.models import Solution

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

riddle_router = APIRouter(
    prefix="/riddle",
    tags=["riddle"],
)


class MatrixRequest(BaseModel):
    matrix: list[list[int]] = Field(title="Quantity of operations")


results: list[list[list[Cell]]] = []


@riddle_router.get("/condition/:get_id")
async def get_condition(get_id: int, session=Depends(get_async_session)) -> list[list[int]]:
    query = select(Solution).where(Solution.id == get_id)
    res = await session.execute(query)
    solution: Solution = res.fetchone()[0]
    print(solution)
    if not solution:
        raise HTTPException(status_code=404, detail="Condition not found")
    return solution.condition


@riddle_router.post("/generate/:size")
async def generate_riddle(size: int, session=Depends(get_async_session)) -> str:
    if size < 2 or size > 3:
        raise HTTPException(status_code=400, detail="Size must be 2 or 3")

    await session.execute(text('TRUNCATE TABLE "solution" RESTART IDENTITY CASCADE;'))
    matrices = generate_all_matrices(size)
    for m in matrices:
        # j_bytes = orjson.dumps(m)
        st = insert(Solution).values({"condition": m})
        await session.execute(st)

    await session.commit()
    return f"{len(matrices)} conditions generated"


@riddle_router.post("/solve")
async def solve_riddle(r: MatrixRequest, _=Depends(current_user)) -> int:
    try:
        validate_input_matrix(r.matrix)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    cells = translate_to_cells(r.matrix)
    global results
    results = solve_matrix(cells)
    return len(results)


@riddle_router.get("/solution")
async def get_solution(_=Depends(current_user)) -> list[list[Cell]]:
    global results
    if not results:
        raise HTTPException(status_code=400, detail="No riddle was solved")
    res = results[0]
    results = results[1:]
    return res
