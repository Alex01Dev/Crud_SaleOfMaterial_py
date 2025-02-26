'''
FastAPI routes for User management.
'''

from fastapi import APIRouter, HTTPException, Depends,  status, Header
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

user = APIRouter()

SECRET_KEY = "amauri_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

models.user.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    """
    Establishes a connection to the database and ensures it gets closed once the operation is completed.
    """
    db = config.db.SessionLocal()
    try:
        print("Conectando a la base de datos...")
        yield db
    finally:
        db.close()
        print("Conexión cerrada.")

def verify_token_simple(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token no proporcionado o inválido",
        )

    token = authorization.split("Bearer ")[1]  # Extrae el token
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
        return email
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido o expirado")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@user.get("/user/", response_model=List[schemas.users.user], tags=["Users"])
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieves a list of users from the database, supporting optional pagination (skip and limit).
    """
    db_users = crud.users.get_users(db=db, skip=skip, limit=limit)
    return db_users

@user.get("/userOne/{id}", response_model=schemas.users.user, tags=["Usuarios"])
async def read_user(id: int, db: Session = Depends(get_db)):
    """
    Fetches a specific user by their ID.
    """
    db_user = crud.users.get_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user.post("/user/", response_model=schemas.users.user, tags=["Users"])
async def create_user(user: schemas.users.userCreate, db: Session = Depends(get_db)):
    """
    Creates a new user and ensures the provided email is not already registered.
    """
    existing_user = crud.users.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = crud.users.create_user(db, user)
    return new_user

@user.put("/update/{id}", response_model=schemas.users.user, tags=["Users"])
async def update_user(id: int, user_update: schemas.users.userUpdate, db: Session = Depends(get_db)):
    """
    Updates an existing user by their ID.
    """
    db_user = crud.users.update_user(db, id, user_update)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user.delete("/delete/{id}", response_model=schemas.users.user, tags=["Users"])
async def delete_user(id: int, db: Session = Depends(get_db)):
    """
    Deletes a user from the database by their ID.
    """
    db_user = crud.users.delete_user(db, id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
