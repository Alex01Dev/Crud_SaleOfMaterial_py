'''
FastAPI routes for User management.
'''

from fastapi import APIRouter, HTTPException, Depends,  Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import crud.users
import config.db
from schemas.users import UserLogin, Token, userCreate, userUpdate
import schemas.users
from datetime import datetime, timedelta
from typing import List, Optional
from jose import JWTError, jwt
import models.user

from typing import List
from auth import authenticate_user, create_access_token, get_current_user
from datetime import timedelta
from auth import get_password_hash, ACCESS_TOKEN_EXPIRE_MINUTES

from typing import List

user = APIRouter()


models.user.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user.get("/user/", response_model=List[schemas.users.user], tags=["Users"])
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: models.user.User = Depends(get_current_user)):
    """
    Retrieves a list of users from the database, supporting optional pagination (skip and limit).
    This route is protected and requires authentication.
    """
    db_users = crud.users.get_users(db=db, skip=skip, limit=limit)
    return db_users

@user.get("/userOne/{id}", response_model=schemas.users.user, tags=["Usuarios"])
async def read_user(id: int, db: Session = Depends(get_db), current_user: models.user.User = Depends(get_current_user)):
    """
    Fetches a specific user by their ID.
    This route is protected and requires authentication.
    """
    db_user = crud.users.get_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user.post("/user/", response_model=schemas.users.user, tags=["Users"])
async def create_user(user: schemas.users.userCreate, db: Session = Depends(get_db), current_user: models.user.User = Depends(get_current_user)):
    """
    Creates a new user and ensures the provided email is not already registered.
    This route is protected and requires authentication.
    """
    existing_user = crud.users.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = crud.users.create_user(db, user)
    return new_user

@user.put("/update/{id}", response_model=schemas.users.user, tags=["Users"])
async def update_user(id: int, user_update: schemas.users.userUpdate, db: Session = Depends(get_db), current_user: models.user.User = Depends(get_current_user)):
    """
    Updates an existing user by their ID.
    This route is protected and requires authentication.
    """
    db_user = crud.users.update_user(db, id, user_update)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user.delete("/delete/{id}", response_model=schemas.users.user, tags=["Users"])
async def delete_user(id: int, db: Session = Depends(get_db), current_user: models.user.User = Depends(get_current_user)):
    """
    Deletes a user from the database by their ID.
    This route is protected and requires authentication.
    """
    db_user = crud.users.delete_user(db, id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
