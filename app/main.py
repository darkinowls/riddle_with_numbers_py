from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.auth.router import auth_router

app = FastAPI(
    default_response_class=ORJSONResponse
)

app.include_router(auth_router)

@app.get("/ping")
async def ping():
    return {"message": "pong"}


# @app.on_event("startup")
# async def startup_event():
#     pass
