from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters
from app.cache import cached_list
from app.database import get_db
from app.models.lista_levinneisyysalue_maailmalla import ListaLevinneisyysalueMaailmalla as Model  # lista_levinneisyysalue_maailmalla: list distribution area worldwide
from app.schemas.lista_levinneisyysalue_maailmalla import ListaLevinneisyysalueMaailmalla as Schema  # lista_levinneisyysalue_maailmalla: list distribution area worldwide

router = APIRouter()

@router.get("/", response_model=List[Schema])
@cached_list("lista_levinneisyysalue_maailmalla")
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/{id}", response_model=Schema)  # id: id
def read_one(id: int, db: Session = Depends(get_db)):  # id: id
    item = db.query(Model).filter(Model.ID == id).first()  # id: id
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item
