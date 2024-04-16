"""User manager."""

import uuid
from typing import AsyncGenerator

from fastapi_users import BaseUserManager, UUIDIDMixin

from app.auth.connectors import get_user_db
from app.auth.models import User
from app.config import SECRET

from fastapi import Depends


# REMOVED UUID
class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]): # pylint: disable=too-few-public-methods
    """User manager."""
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET


async def get_user_manager(user_db=Depends(get_user_db)) -> AsyncGenerator[UserManager, None]:
    """Get user manager."""
    yield UserManager(user_db)
