"""Database configuration."""

from typing import AsyncGenerator

import asyncpg
from asyncpg import DuplicateDatabaseError
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

from app.config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

Base = declarative_base()

meta_data = Base.metadata

my_engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)

_async_session_maker = async_sessionmaker(my_engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Get an async session."""
    async with _async_session_maker() as session:
        yield session


async def create_test_database(database_name: str):
    """Create the test database."""
    # Connect to the PostgreSQL server
    conn = await asyncpg.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database='postgres'  # Connect to the 'postgres' database for administrative tasks
    )

    try:
        # Create the test database
        await conn.execute(f"CREATE DATABASE {database_name}")
    except DuplicateDatabaseError:
        pass  # Database already exists, no need to create it again
    finally:
        # Close the connection
        await conn.close()
