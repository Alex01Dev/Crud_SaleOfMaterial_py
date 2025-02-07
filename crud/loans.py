from sqlalchemy.orm import Session
from models.loan import Loan
from schemas.loans import loanCreate, loanUpdate
from fastapi import HTTPException
from datetime import datetime

def get_loans(db: Session):
    return db.query(Loan).all()

def get_loan(db: Session, loan_id: int):
    return db.query(Loan).filter(Loan.id == loan_id).first()

def create_loan(db: Session, loan_data: loanCreate):
    new_loan = Loan(
        id_user=loan_data.id_user,
        id_material=loan_data.id_material,
        loanDate=loan_data.loanDate,
        returnDate=loan_data.returnedDate,
        loanStatus=loan_data.loanStatus,
        registrationDate=datetime.utcnow(),
        updateDate=datetime.utcnow(),
    )
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)
    return new_loan

def update_loan(db: Session, loan_id: int, loan_data: loanUpdate):
    db_loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if not db_loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    
    db_loan.id_user = loan_data.id_user
    db_loan.id_material = loan_data.id_material
    db_loan.loanDate = loan_data.loanDate
    db_loan.returnDate = loan_data.returnedDate
    db_loan.loanStatus = loan_data.loanStatus
    db_loan.updateDate = datetime.utcnow()

    db.commit()
    db.refresh(db_loan)
    return db_loan

def delete_loan(db: Session, loan_id: int):
    db_loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if not db_loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    
    db.delete(db_loan)
    db.commit()
    return {"message": "Loan deleted successfully"}
