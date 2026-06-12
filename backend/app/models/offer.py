from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Boolean

from app.models.base import Base

class Offert(Base):
    __tablename__ = "offer"

    id = Column(Integer, primary_key=True, autoincrement=True)
    salary = Column(Integer)
    source = Column(String)
    rol_id = Column(Integer, ForeignKey("rol.id"))
    company = Column(String)
    desc = Column(String)
    create_at = Column(DateTime)
    url = Column(String)
    remote = Column(Boolean)