from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.materials
import config.db
import schemas.materials
import models.material

from typing import List

material = APIRouter()

models.material.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        print("Conectando a la base de datos...")
        yield db
    finally:
        db.close()
        print("Conexión cerrada.")

@material.get("/material/get", response_model=List[schemas.materials.materialr], tags=["Materials"])
async def read_materials(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_materials = crud.materials.get_materials(db=db, skip=skip, limit=limit)
    return db_materials

@material.get("/materialOne/{id}", response_model=schemas.materials.materialr, tags=["Materials"])
async def read_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.materials.get_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material

@material.post("/insertMaterial/", response_model=schemas.materials.materialr, tags=["Materials"])
async def create_material(material: schemas.materials.materialCreate, db: Session = Depends(get_db)):
    new_material = crud.materials.create_material(db, material)
    return new_material

@material.put("/updateMaterial/{id}", response_model=schemas.materials.materialr, tags=["Materials"])
async def update_material(id: int, material_update: schemas.materials.materialUpdate, db: Session = Depends(get_db)):
    db_material = crud.materials.update_material(db, id, material_update)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material

@material.delete("/deleteMaterial/{id}", response_model=schemas.materials.materialr, tags=["Materials"])
async def delete_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.materials.delete_material(db, id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material
