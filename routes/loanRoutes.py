from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
import crud.loans
import config.db
import schemas.loans
import models.loan