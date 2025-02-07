'''
Module that defines the Material schema in the database.
'''

from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

class materialBase(BaseModel):
    """
    Base class for material data. Contains the core attributes for a material, 
    including type, brand, model, state, registration date, and update date.
    """
    typeMaterial: str
    brand: str
    model: str
    state: str
    registrationDate: datetime
    updateDate: datetime

class materialCreate(materialBase):
    """
    Class for creating a new material. Inherits from materialBase and allows for
    defining a new material with all necessary attributes.
    """
    pass

class materialUpdate(materialBase):
    """
    Class for updating an existing material. Inherits from materialBase and allows for
    modifying material attributes such as type, brand, model, etc.
    """
    pass

class materialr(materialBase):
    """
    Class representing a material object, including the material's ID. Inherits from 
    materialBase and adds the material ID to the material's data.
    """
    id: int

    class config:
        """
        Configuration for Pydantic to work with ORM models. Enables compatibility 
        with SQLAlchemy models by allowing automatic data conversion.
        """
        orm_mode = True
