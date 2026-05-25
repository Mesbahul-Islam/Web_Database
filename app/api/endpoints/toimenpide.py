from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters
from app.api.crud import create_item, update_item, delete_item
from app.database import get_db
from app.models.toimenpide import Toimenpide as Model  # toimenpide: action
from app.schemas.toimenpide import Toimenpide as Schema, ToimenpideCreate as SchemaCreate  # toimenpide: action

router = APIRouter()

@router.get("/", response_model=List[Schema])
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/{hankintaid}", response_model=Schema)  # hankintaid: acquisition id
def read_one(hankintaid: str, db: Session = Depends(get_db)):  # hankintaid: acquisition id
    item = db.query(Model).filter(Model.hankintaID == hankintaid).first()  # hankintaid: acquisition id
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, db: Session = Depends(get_db)):
    return await create_item(payload, db, Model)

@router.put("/{toimenpide_nro}", response_model=Schema)
async def update_one(toimenpide_nro: int, payload: SchemaCreate, db: Session = Depends(get_db)):
    return await update_item(payload, db, Model, "toimenpide_nro", toimenpide_nro)

@router.delete("/{toimenpide_nro}", status_code=204)
async def delete_one(toimenpide_nro: int, db: Session = Depends(get_db)):
    await delete_item(db, Model, "toimenpide_nro", toimenpide_nro)

