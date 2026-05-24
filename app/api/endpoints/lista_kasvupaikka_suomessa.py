from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters
from app.database import get_db
from app.models.lista_kasvupaikka_suomessa import ListaKasvupaikkaSuomessa as Model  # lista_kasvupaikka_suomessa: list growing site in finland
from app.schemas.lista_kasvupaikka_suomessa import ListaKasvupaikkaSuomessa as Schema  # lista_kasvupaikka_suomessa: list growing site in finland

router = APIRouter()

@router.get("/", response_model=List[Schema])
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/{id}", response_model=Schema)  # id: id
def read_one(id: int, db: Session = Depends(get_db)):  # id: id
    item = db.query(Model).filter(Model.id == id).first()  # id: id
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item
