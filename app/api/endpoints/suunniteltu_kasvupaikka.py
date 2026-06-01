from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters
from app.cache import cached_list
from app.database import get_db
from app.models.suunniteltu_kasvupaikka import SuunniteltuKasvupaikka as Model  # suunniteltu_kasvupaikka: planned_growing_site
from app.schemas.suunniteltu_kasvupaikka import SuunniteltuKasvupaikka as Schema  # suunniteltu_kasvupaikka: planned_growing_site

router = APIRouter()

@router.get("/", response_model=List[Schema])
@cached_list("suunniteltu_kasvupaikka")
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/{taksonin_nro}", response_model=Schema)  # taksonin_nro: taxon number
def read_one(taksonin_nro: str, db: Session = Depends(get_db)):  # taksonin_nro: taxon number
    item = db.query(Model).filter(Model.taksonin_nro == taksonin_nro).first()  # taksonin_nro: taxon number
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item
