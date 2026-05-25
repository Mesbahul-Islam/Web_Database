from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters
from app.api.crud import create_item, update_item, delete_item
from app.database import get_db
from app.models.taksonin_viljelytiedot import TaksoninViljelytiedot as Model  # taksonin_viljelytiedot: taxon_cultivation_data
from app.schemas.taksonin_viljelytiedot import TaksoninViljelytiedot as Schema, TaksoninViljelytiedotCreate as SchemaCreate  # taksonin_viljelytiedot: taxon_cultivation_data

router = APIRouter()

@router.get("/", response_model=List[Schema])
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/{taksonin_nro}", response_model=Schema)  # taksonin_nro: taxon number
def read_one(taksonin_nro: str, db: Session = Depends(get_db)):  # taksonin_nro: taxon number
    item = db.query(Model).filter(Model.taksonin_nro == taksonin_nro).first()  # taksonin_nro: taxon number
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, db: Session = Depends(get_db)):
    return await create_item(payload, db, Model)

@router.put("/{lisatietojen_nro_viljely}", response_model=Schema)
async def update_one(lisatietojen_nro_viljely: int, payload: SchemaCreate, db: Session = Depends(get_db)):
    return await update_item(payload, db, Model, "lisatietojen_nro_viljely", lisatietojen_nro_viljely)

@router.delete("/{lisatietojen_nro_viljely}", status_code=204)
async def delete_one(lisatietojen_nro_viljely: int, db: Session = Depends(get_db)):
    await delete_item(db, Model, "lisatietojen_nro_viljely", lisatietojen_nro_viljely)

