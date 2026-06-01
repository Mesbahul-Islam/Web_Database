from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters
from app.cache import cached_list
from app.database import get_db
from app.models.lista_maarittaja import ListaMaarittaja as Model  # lista_maarittaja: list identifier / determiner
from app.schemas.lista_maarittaja import ListaMaarittaja as Schema  # lista_maarittaja: list identifier / determiner

router = APIRouter()

@router.get("/", response_model=List[Schema])
@cached_list("lista_maarittaja")
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/{id}", response_model=Schema)  # id: id
def read_one(id: int, db: Session = Depends(get_db)):  # id: id
    item = db.query(Model).filter(Model.id == id).first()  # id: id
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item
