from sqlalchemy import Column, String, Integer, ForeignKey

from app.models.base import Base

class GlobalStack(Base):
    __tablename__ = "global_stack"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    level = Column(String)