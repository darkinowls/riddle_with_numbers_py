"""
Main FastAPI application
"""

from app.auth.router import auth_router
from app.config import DB_NAME
from app.database import create_test_database
from app.riddle.router import riddle_router

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI(
    default_response_class=ORJSONResponse
)

app.include_router(auth_router)
app.include_router(riddle_router)


@app.get("/ping")
async def ping():
    """Check if the server is running"""
    return {"message": "pong"}

@app.on_event("startup")
async def startup_event():
    """Init on startup"""
    await create_test_database(DB_NAME)
