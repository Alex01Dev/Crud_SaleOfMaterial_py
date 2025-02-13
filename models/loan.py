'''
Module that defines the Loan model in the database.
'''

from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from config.db import Base
from sqlalchemy.orm import relationship
import enum

class LoanStatus(str, enum.Enum):
    """
    Enum class representing the possible statuses of a loan.
    """
    Active = "Active"
    Returned = "Returned"
    Defeated = "Defeated"

class Loan(Base):
    """
    Represents a loan record in the database, inheriting from SQLAlchemy's Base class.
    Contains details about a loan, such as user, material, loan dates, status, and timestamps.
    """
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
