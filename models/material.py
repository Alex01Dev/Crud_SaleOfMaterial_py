'''
Module that defines the Material model in the database.
'''

from sqlalchemy import Column, Integer, String, DateTime, Enum
import enum
from config.db import Base

class TypeMaterial(str, enum.Enum):
    """
    Enum class for material types. Defines the categories of materials available.
    """
    Canon = "Canon"
    Computer = "Computer"
    Extension = "Extension"

class State(str, enum.Enum):
    """
    Enum class for the state of the material. Specifies whether the material is 
    available, borrowed, or under maintenance.
    """
    Available = "Available"
    Borrowed = "Borrowed"
    Under_maintenance = "Under_maintenance"

class Material(Base):
    """
    Represents a material item in the database. Contains information about 
    its brand, model, type, state, and timestamps for registration and updates.
    """
    __tablename__ = "tbb_materials"

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String(60))
    model = Column(String(60))
    typeMaterial = Column(Enum(TypeMaterial))
    state = Column(Enum(State))
    registrationDate = Column(DateTime)
    updateDate = Column(DateTime)
