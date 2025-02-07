'''
Module that defines the Loan schema in the database.
'''

from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

class loanBase(BaseModel):
    """
    Base class for loan data. Contains the core attributes for a loan, including 
    user ID, material ID, loan date, return date, and loan status.
    """
    id_user: int
    id_material: int
    loanDate: Optional[datetime]
    returnedDate: Optional[datetime]
    loanStatus: str

class loanCreate(loanBase):
    """
    Class for creating a new loan. Inherits from loanBase and allows for
    defining a new loan with all necessary attributes.
    """
    pass

class loanUpdate(loanBase):
    """
    Class for updating an existing loan. Inherits from loanBase and allows for 
    modifying loan attributes such as user, material, loan status, etc.
    """
    pass

class loan(loanBase):
    """
    Class representing a loan object, including the loan's ID. Inherits from 
    loanBase and adds the loan ID to the loan's data.
    """
    id: int

    class config:
        """
        Configuration for Pydantic to work with ORM models. Enables compatibility 
        with SQLAlchemy models by allowing automatic data conversion.
        """
        orm_mode = True
