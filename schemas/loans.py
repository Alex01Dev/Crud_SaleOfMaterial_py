from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

class loanBase(BaseModel):
    id_user: int
    id_material: int
    loanDate: Optional[datetime]
    returnedDate: Optional[datetime]
    loanStatus: str

class loanCreate(loanBase):
    pass

class loanUpdate(loanBase):
    pass

class loan(loanBase):
    id: int
    class config:
        orm_mode = True

