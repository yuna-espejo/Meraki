import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String
from app.models.base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True)
    name = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    type = Column(String)