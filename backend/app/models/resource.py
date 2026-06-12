from sqlalchemy import Column, String, Integer

from app.models.base import Base

class Resource(Base):
    __tablename__ = "resource"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    url = Column(String)