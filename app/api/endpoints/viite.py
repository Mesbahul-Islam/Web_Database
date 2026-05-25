from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters
from app.api.crud import create_item, update_item, delete_item
from app.database import get_db
from app.models.viite import Viite as Model  # viite: reference
from app.schemas.viite import Viite as Schema, ViiteCreate as SchemaCreate  # viite: reference

router = APIRouter()

@router.get("/", response_model=List[Schema])
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/{viitteen_lyhenne}", response_model=Schema)  # viitteen_lyhenne: reference abbreviation
def read_one(viitteen_lyhenne: str, db: Session = Depends(get_db)):  # viitteen_lyhenne: reference abbreviation
    item = db.query(Model).filter(Model.viitteen_lyhenne == viitteen_lyhenne).first()  # viitteen_lyhenne: reference abbreviation
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, db: Session = Depends(get_db)):
    return await create_item(payload, db, Model)

@router.put("/{viitenro}", response_model=Schema)
async def update_one(viitenro: int, payload: SchemaCreate, db: Session = Depends(get_db)):
    return await update_item(payload, db, Model, "viitenro", viitenro)

@router.delete("/{viitenro}", status_code=204)
async def delete_one(viitenro: int, db: Session = Depends(get_db)):
    await delete_item(db, Model, "viitenro", viitenro)

