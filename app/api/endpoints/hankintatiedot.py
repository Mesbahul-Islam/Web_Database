from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters
from app.api.crud import create_item, update_item, delete_item
from app.database import get_db
from app.models.hankintatiedot import Hankintatiedot as Model  # hankintatiedot: acquisition_data
from app.schemas.hankintatiedot import Hankintatiedot as Schema, HankintatiedotCreate as SchemaCreate  # hankintatiedot: acquisition_data

router = APIRouter()

@router.get("/", response_model=List[Schema])
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/{hankintaID}", response_model=Schema)  # hankintaID: acquisition id
def read_one(hankintaID: int, db: Session = Depends(get_db)):  # hankintaID: acquisition id
    item = db.query(Model).filter(Model.hankintaID == hankintaID).first()  # hankintaID: acquisition id
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, db: Session = Depends(get_db)):
    return await create_item(payload, db, Model)

@router.put("/{hankintaID}", response_model=Schema)
async def update_one(hankintaID: int, payload: SchemaCreate, db: Session = Depends(get_db)):
    return await update_item(payload, db, Model, "hankintaID", hankintaID)

@router.delete("/{hankintaID}", status_code=204)
async def delete_one(hankintaID: int, db: Session = Depends(get_db)):
    await delete_item(db, Model, "hankintaID", hankintaID)

