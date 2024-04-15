from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI(
    default_response_class=ORJSONResponse
)

app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "pong"}


@app.on_event("startup")
async def startup_event():
    # just mongo
    await init_db()
