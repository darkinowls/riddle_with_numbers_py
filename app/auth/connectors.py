from typing import AsyncGenerator

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.models import User
from app.database import get_async_session
from fastapi_users.db import SQLAlchemyUserDatabase


async def get_user_db(session: AsyncSession = Depends(get_async_session)) -> AsyncGenerator[AsyncSession, None]:
    yield SQLAlchemyUserDatabase(session, User)
