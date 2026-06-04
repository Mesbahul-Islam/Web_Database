from fastapi import APIRouter, Depends, HTTPException, Request, Query
from math import ceil
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters, make_filter_dep
from app.cache import cached_list
from app.database import get_db
from app.models.kayttajatiedot import Kayttajatiedot as Model  # kayttajatiedot: user_data
from app.schemas.kayttajatiedot import Kayttajatiedot as Schema, KayttajatiedotPage as SchemaPage  # kayttajatiedot: user_data

router = APIRouter()

@router.get("/", response_model=SchemaPage)
@cached_list("kayttajatiedot")
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

@router.get("/{kayttajan_tunnus}", response_model=Schema)  # kayttajan_tunnus: user ID
def read_one(kayttajan_tunnus: str, db: Session = Depends(get_db)):  # kayttajan_tunnus: user ID
    item = db.query(Model).filter(Model.kayttajan_tunnus == kayttajan_tunnus).first()  # kayttajan_tunnus: user ID
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item
