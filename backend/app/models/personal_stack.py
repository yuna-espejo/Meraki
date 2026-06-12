from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import Base

class PersonalStack(Base):
    __tablename__ = "personal_stack"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    stack_id = Column(Integer, ForeignKey("global_stack.id"))
    level = Column(String)