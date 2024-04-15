from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID

from app.database import Base

meta_data = Base.metadata


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"
