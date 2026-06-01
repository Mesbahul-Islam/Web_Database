from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters
from app.cache import cached_list
from app.database import get_db
from app.models.huomioita import Huomioita as Model  # huomioita: notes
from app.schemas.huomioita import Huomioita as Schema  # huomioita: notes

router = APIRouter()

@router.get("/", response_model=List[Schema])
@cached_list("huomioita")
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    query = query.filter(Model.paneeli.isnot(None))
    return query.offset(skip).limit(limit).all()
