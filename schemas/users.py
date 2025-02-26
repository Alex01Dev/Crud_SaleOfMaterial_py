'''
Module that defines the User schema in the database.
'''

from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

class userBase(BaseModel):
    """
    Base class for user data. Contains core attributes for a user, including personal 
    information (name, last name), account details (username, email, password), 
    contact information (phone number), status, and registration details.
    """
    name: str
    lastName: str
    typeUser: str
    userName: str
    email: str
    password: str
    phoneNumber: str
    status: str
    registrationDate: datetime
    updateDate: datetime

class userCreate(userBase):
    """
    Class for creating a new user. Inherits from userBase and allows for defining 
    new user attributes to register an account.
    """
    pass

class userUpdate(userBase):
    """
    Class for updating an existing user's data. Inherits from userBase and allows 
    for modifying user attributes such as name, email, password, and status.
    """
    pass

class user(userBase):
    """
    Class representing a user object with an ID. Inherits from userBase and adds 
    the user ID, representing a specific user in the database.
    """
    id: int

    class config:
        """
        Configuration for Pydantic to work with ORM models. Enables compatibility 
        with SQLAlchemy models by allowing automatic data conversion.
        """
        orm_mode = True

class UserLogin(BaseModel):
    correoElectronico: str
    contrasena: str

class Token(BaseModel):
    access_token: str
    token_type: str
