from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters
from app.database import get_db
from app.models.osastopaikka import Osastopaikka as Model  # osastopaikka: section_location
from app.schemas.osastopaikka import Osastopaikka as Schema  # osastopaikka: section_location

router = APIRouter()

@router.get("/", response_model=List[Schema])
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/{hankintaid}", response_model=Schema)  # hankintaid: acquisition id
def read_one(hankintaid: str, db: Session = Depends(get_db)):  # hankintaid: acquisition id
    item = db.query(Model).filter(Model.hankintaid == hankintaid).first()  # hankintaid: acquisition id
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item
