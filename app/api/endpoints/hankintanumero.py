from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters, make_filter_dep
from app.cache import cached_list
from app.database import get_db
from app.models.hankintanumero import Hankintanumero as Model  # hankintanumero: acquisition number
from app.schemas.hankintanumero import Hankintanumero as Schema  # hankintanumero: acquisition number

router = APIRouter()

@router.get("/", response_model=List[Schema])
@cached_list("hankintanumero")
def read_all(request: Request, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.all()
