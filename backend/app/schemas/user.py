from pydantic import BaseModel
from uuid import UUID
class UserRegister(BaseModel):
    name: str
    email: str
    username: str
    password: str

class UserResponse(BaseModel):
    id: UUID
    name: str
    email: str
    username: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: str
    password: str