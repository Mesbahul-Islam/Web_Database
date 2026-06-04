from fastapi import APIRouter, Depends, Request, Query
from math import ceil
from sqlalchemy.orm import Session
from typing import List, Optional

from app.api.query import apply_filters, make_filter_dep
from app.cache import cached_list
from app.database import get_db
from app.models.lista_tarkastajanimi import ListaTarkastajanimi as Model  # lista_tarkastajanimi: list_inspector_names
from app.schemas.lista_tarkastajanimi import ListaTarkastajanimi as Schema, ListaTarkastajanimiPage as SchemaPage  # lista_tarkastajanimi: list_inspector_names

router = APIRouter()

@router.get("/", response_model=SchemaPage)
@cached_list("lista_tarkastajanimi")
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
