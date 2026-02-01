# backend/app/api/endpoints/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from motor.motor_asyncio import AsyncIOMotorDatabase
from pydantic import BaseModel

from app.core.auth import create_access_token
from app.core.db import get_database
from app.services.auth_service import AuthService
from app.models.user import User

router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str

class UserOut(BaseModel):
    email: str

@router.post("/signup", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def signup(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncIOMotorDatabase = Depends(get_database)):
    """
    Handles user registration. Expects email in 'username' field and password in 'password' field.
    """
    service = AuthService(db)
    # The form uses 'username' as the key for the email field
    user = await service.register_user(email=form_data.username, password=form_data.password)
    return user

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncIOMotorDatabase = Depends(get_database)):
    """
    Authenticates the user and returns a JWT access token.
    """
    service = AuthService(db)
    user = await service.authenticate_user(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
