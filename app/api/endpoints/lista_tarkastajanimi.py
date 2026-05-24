from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from typing import List, Optional

from app.api.query import apply_filters
from app.database import get_db
from app.models.lista_tarkastajanimi import ListaTarkastajanimi as Model  # lista_tarkastajanimi: list_inspector_names
from app.schemas.lista_tarkastajanimi import ListaTarkastajanimi as Schema  # lista_tarkastajanimi: list_inspector_names

router = APIRouter()

@router.get("/", response_model=List[Schema])
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/by-key", response_model=List[Schema])
def read_by_key(
    id: Optional[int] = None,
    nimi: Optional[str] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Model)
    if id is not None:
        query = query.filter(Model.id == id)
    if nimi is not None:
        query = query.filter(Model.nimi == nimi)
    return query.all()
