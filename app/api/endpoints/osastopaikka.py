from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters
from app.api.crud import create_item, update_item, delete_item
from app.database import get_db
from app.models.osastopaikka import Osastopaikka as Model  # osastopaikka: section_location
from app.schemas.osastopaikka import Osastopaikka as Schema, OsastopaikkaCreate as SchemaCreate  # osastopaikka: section_location

router = APIRouter()

@router.get("/", response_model=List[Schema])
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/{osaston_numero}", response_model=Schema)  # osaston_numero: section number
def read_one(osaston_numero: int, db: Session = Depends(get_db)):  # osaston_numero: section number
    item = db.query(Model).filter(Model.osaston_numero == osaston_numero).first()  # osaston_numero: section number
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, db: Session = Depends(get_db)):
    return await create_item(payload, db, Model)

@router.put("/{osaston_numero}", response_model=Schema)
async def update_one(osaston_numero: int, payload: SchemaCreate, db: Session = Depends(get_db)):
    return await update_item(payload, db, Model, "osaston_numero", osaston_numero)

@router.delete("/{osaston_numero}", status_code=204)
async def delete_one(osaston_numero: int, db: Session = Depends(get_db)):
    await delete_item(db, Model, "osaston_numero", osaston_numero)

