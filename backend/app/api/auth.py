from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import UserCreate
from app.models import User
from app.deps import get_db
from app.auth_utils import get_password_hash, verify_password, create_access_token
from pydantic import BaseModel
from datetime import timedelta

router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str

@router.post('/register', response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    token = create_access_token({"sub": str(db_user.id)}, expires_delta=timedelta(minutes=30))
    return {"access_token": token, "token_type": "bearer"}

class LoginInput(BaseModel):
    email: str
    password: str

@router.post('/login', response_model=Token)
def login(input: LoginInput, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == input.email).first()
    if not user or not verify_password(input.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    token = create_access_token({"sub": str(user.id)}, expires_delta=timedelta(minutes=30))
    return {"access_token": token, "token_type": "bearer"}
