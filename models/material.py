from sqlalchemy import Column, Integer, String, DateTime, Enum
import enum
from config.db import Base

class TypeMaterial(str, enum.Enum):
    Canon = "Canon"
    Computer = "Computer"
    Extension = "Extension"

class State(str, enum.Enum):
    Available = "Available"
    Borrowed = "Borrowed"
    Under_maintenance = "Under_maintenance"

class Material(Base):
    __tablename__ = "tbb_materials"

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String(60))
    model = Column(String(60))
    typeMaterial = Column(Enum(TypeMaterial))
    state = Column(Enum(State))
    registrationDate = Column(DateTime)
    updateDate = Column(DateTime)
