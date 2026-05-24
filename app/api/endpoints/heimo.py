from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters
from app.database import get_db
from app.models.heimo import Heimo as Model  # heimo: family
from app.schemas.heimo import Heimo as Schema  # heimo: family

router = APIRouter()

@router.get("/", response_model=List[Schema])
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/{numero}", response_model=Schema)  # numero: number
def read_one(numero: int, db: Session = Depends(get_db)):  # numero: number
    item = db.query(Model).filter(Model.numero == numero).first()  # numero: number
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item
