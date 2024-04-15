from datetime import datetime

from sqlalchemy import Column, Integer, JSON, TIMESTAMP
from sqlalchemy.orm import mapped_column

from app.database import Base

meta_data = Base.metadata


class Solution(Base):
    __tablename__ = "solution"
    id = Column(Integer, primary_key=True)
    condition = Column(JSON, nullable=False)
    solution = Column(JSON, nullable=True)
    created_at = mapped_column(TIMESTAMP, default=datetime.now())
