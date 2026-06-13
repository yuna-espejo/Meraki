from pydantic import BaseModel

class UserRegister(BaseModel):
    name: str
    email: str
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    username: str

    class Config:
        from_attributes = True