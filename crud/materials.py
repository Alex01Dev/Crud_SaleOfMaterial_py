import models.material
import schemas.materials
from sqlalchemy.orm import Session

def get_materials(db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.material.Material).offset(skip).limit(limit).all()

def get_material(db: Session, id: int):
    return db.query(models.material.Material).filter(models.material.Material.id == id).first()

def create_material(db: Session, material: schemas.materials.materialCreate):
    new_material = models.material.Material(
        typeMaterial=material.typeMaterial,
        brand=material.brand,
        model=material.model,
        state=material.state,
        registrationDate=material.registrationDate,
        updateDate=material.updateDate
    )
    
    db.add(new_material)
    db.commit()
    db.refresh(new_material)
    return new_material

def update_material(db: Session, id: int, material: schemas.materials.materialUpdate):
    db_material = db.query(models.material.Material).filter(models.material.Material.id == id).first()
    if not db_material:
        return None
    
    for key, value in material.dict(exclude_unset=True).items():
        setattr(db_material, key, value)
    
    db.commit()
    db.refresh(db_material)
    return db_material

def delete_material(db: Session, id: int):
    db_material = db.query(models.material.Material).filter(models.material.Material.id == id).first()
    if not db_material:
        return None
    
    db.delete(db_material)
    db.commit()
    return db_material
