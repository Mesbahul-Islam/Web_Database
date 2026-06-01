from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters
from app.cache import cached_list
from app.database import get_db
from app.models.kayttajatiedot import Kayttajatiedot as Model  # kayttajatiedot: user_data
from app.schemas.kayttajatiedot import Kayttajatiedot as Schema  # kayttajatiedot: user_data

router = APIRouter()

@router.get("/", response_model=List[Schema])
@cached_list("kayttajatiedot")
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/{kayttajan_tunnus}", response_model=Schema)  # kayttajan_tunnus: user ID
def read_one(kayttajan_tunnus: str, db: Session = Depends(get_db)):  # kayttajan_tunnus: user ID
    item = db.query(Model).filter(Model.kayttajan_tunnus == kayttajan_tunnus).first()  # kayttajan_tunnus: user ID
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item
