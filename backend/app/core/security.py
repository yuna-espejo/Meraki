from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def hash_password(password: str) -> str:
    pass_hash = pwd_context.hash(password)
    return pass_hash

def verify_password(password: str, pass_hash: str) -> bool:
    verify= pwd_context.verify(password, pass_hash)

    return verify

def create_access_token(data: dict) -> str:
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    payload.update({"exp": expire})
    token = jwt.encode(payload, os.getenv("SECRET_JWT"), algorithm=os.getenv("ALG_JWT"))
    return token