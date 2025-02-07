from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

class materialBase(BaseModel):
    typeMaterial: str
    brand: str
    model: str
    state: str
    registrationDate: datetime
    updateDate: datetime

class materialCreate(materialBase):
    pass

class materialUpdate(materialBase):
    pass

class materialr(materialBase):
    id: int
    class config:
        orm_mode = True
