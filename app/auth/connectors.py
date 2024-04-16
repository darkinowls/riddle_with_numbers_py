"""Connectors for authentication."""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.models import User
from app.database import get_async_session
from fastapi_users.db import SQLAlchemyUserDatabase

from fastapi import Depends


async def get_user_db(session: AsyncSession = Depends(get_async_session)) \
        -> AsyncGenerator[AsyncSession, None]:
    """Get user database."""
    yield SQLAlchemyUserDatabase(session, User)
