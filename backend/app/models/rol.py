from sqlalchemy import Column, String, Integer

from app.models.base import Base

class Rol(Base):
    __tablename__ = "rol"

    id = Column(Integer, primary_key=True, autoincrement=True)
    rol_name = Column(String, unique=True)
    feature = Column(String)