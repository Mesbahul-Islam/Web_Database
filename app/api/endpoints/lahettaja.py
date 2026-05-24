from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters
from app.database import get_db
from app.models.lahettaja import Lahettaja as Model  # lahettaja: sender
from app.schemas.lahettaja import Lahettaja as Schema  # lahettaja: sender

router = APIRouter()

@router.get("/", response_model=List[Schema])
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/{lahettajanro}", response_model=Schema)  # lahettajanro: sender number
def read_one(lahettajanro: str, db: Session = Depends(get_db)):  # lahettajanro: sender number
    item = db.query(Model).filter(Model.lahettajanro == lahettajanro).first()  # lahettajanro: sender number
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item
