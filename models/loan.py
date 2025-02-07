from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class LoanStatus(str, enum.Enum):
    Active = "Active"
    Returned = "Returned"
    Defeated = "Defeated"

class Loan(Base):
    __tablename__ = "tbb_loans"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey("tbb_users.id"), nullable=False)
    id_material = Column(Integer, ForeignKey("tbb_materials.id"), nullable=False)
    loanDate = Column(DateTime)
    returnDate = Column(DateTime)
    loanStatus = Column(Enum(LoanStatus))
    registrationDate = Column(DateTime)
    updateDate = Column(DateTime)

    user = relationship("User", back_populates="loans")
    material = relationship("Material", back_populates="loans")
