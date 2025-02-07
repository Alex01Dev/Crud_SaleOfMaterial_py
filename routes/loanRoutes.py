from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.loans import get_loans, get_loan, create_loan, update_loan, delete_loan
from schemas.loans import loanCreate, loanUpdate, loan
import models.loan
import config.db

loans = APIRouter(prefix="/loans", tags=["loans"])

models.loan.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        print("Conectando a la base de datos...")
        yield db
    finally:
        db.close()
        print("Conexión cerrada.")

@loans.get("/", response_model=list[loan])
def read_loans(db: Session = Depends(get_db)):
    return get_loans(db)

@loans.get("/{loan_id}", response_model=loan)
def read_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan = get_loan(db, loan_id)
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan

@loans.post("/", response_model=loan)
def create_new_loan(loan_data: loanCreate, db: Session = Depends(get_db)):
    return create_loan(db, loan_data)

@loans.put("/{loan_id}", response_model=loan)
def update_existing_loan(loan_id: int, loan_data: loanUpdate, db: Session = Depends(get_db)):
    return update_loan(db, loan_id, loan_data)

@loans.delete("/{loan_id}", response_model=dict)
def delete_existing_loan(loan_id: int, db: Session = Depends(get_db)):
    return delete_loan(db, loan_id)
