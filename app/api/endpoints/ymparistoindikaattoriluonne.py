from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters
from app.database import get_db
from app.models.ymparistoindikaattoriluonne import Ymparistoindikaattoriluonne as Model  # ymparistoindikaattoriluonne: environmental indicator trait
from app.schemas.ymparistoindikaattoriluonne import Ymparistoindikaattoriluonne as Schema  # ymparistoindikaattoriluonne: environmental indicator trait

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
