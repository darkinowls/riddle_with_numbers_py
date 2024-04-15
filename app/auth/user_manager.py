import uuid
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users import IntegerIDMixin, BaseUserManager, UUIDIDMixin

from app.auth.connectors import get_user_db
from app.auth.models import User
from app.config import SECRET


# REMOVED UUID
class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET


async def get_user_manager(user_db=Depends(get_user_db)) -> AsyncGenerator[UserManager, None]:
    yield UserManager(user_db)
