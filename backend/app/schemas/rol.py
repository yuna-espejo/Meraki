from pydantic import BaseModel
from uuid import UUID

class CreateRol(BaseModel):
    rol_name: str
    feature: str | None = None

class ResponseRol(BaseModel):
    id: int
    rol_name: str
    feature: str | None = None

    class Config:
        from_attributes = True