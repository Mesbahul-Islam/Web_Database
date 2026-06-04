from fastapi import APIRouter, Depends, HTTPException, Request, Query
from math import ceil
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters, make_filter_dep
from app.cache import cached_list
from app.database import get_db
from app.models.lista_kasvumuoto import ListaKasvumuoto as Model  # lista_kasvumuoto: list growth form
from app.schemas.lista_kasvumuoto import ListaKasvumuoto as Schema, ListaKasvumuotoPage as SchemaPage  # lista_kasvumuoto: list growth form

router = APIRouter()

@router.get("/", response_model=SchemaPage)
@cached_list("lista_kasvumuoto")
def read_all(
    request: Request,
    page: int = Query(1, ge=1),
    page_size: int = Query(200, ge=1),
    _filters: dict = Depends(make_filter_dep(Model)),
    db: Session = Depends(get_db),
):
    query = apply_filters(db.query(Model), Model, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return SchemaPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{id}", response_model=Schema)  # id: id
def read_one(id: int, db: Session = Depends(get_db)):  # id: id
    item = db.query(Model).filter(Model.ID == id).first()  # id: id
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item
