import uuid

from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers

from app.auth.auth import auth_backend
from app.auth.models import User
from app.auth.user_dto import UserRead, UserCreate
from app.auth.user_manager import get_user_manager

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

auth_router = APIRouter(
    prefix="/auth/jwt",
    tags=["auth"],
)

auth_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
)

auth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)

current_user = fastapi_users.current_user(
    active=True,
)
