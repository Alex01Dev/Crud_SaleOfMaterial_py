from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

class loanBase(BaseModel):
    id_user: str
    id_material: str
    loanDate: datetime
    returnedDate: datetime
    loanStatus: str

class loanCreate(loanBase):
    pass

class loanUpdate(loanBase):
    pass

class loan(loanBase):
    id: int
    class config:
        orm_mode = True

