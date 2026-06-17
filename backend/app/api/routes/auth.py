from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserRegister, UserResponse, UserLogin
from app.core.security import hash_password, create_access_token, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserResponse)
def register(user: UserRegister, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed = hash_password(user.password)
    new_user = User (
        name=user.name,
        email=user.email,
        username=user.username,
        password=hashed
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login")
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    login_user = db.query(User).filter(User.email == credentials.email).first()
    if not login_user:
        raise HTTPException(status_code=401, detail="Credenciales Incorrectas")
    else:
        is_valid = verify_password(credentials.password, login_user.password)
        if not is_valid:
             raise HTTPException(status_code=401, detail="Credenciales incorrectas")
        else:
            token = create_access_token({"sub": login_user.email})
    return {"access_token": token, "token_type": "bearer"}