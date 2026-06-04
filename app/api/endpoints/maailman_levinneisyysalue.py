from fastapi import APIRouter, Depends, HTTPException, Request, Query
from math import ceil
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters, make_filter_dep
from app.cache import cached_list
from app.database import get_db
from app.models.maailman_levinneisyysalue import MaailmanLevinneisyysalue as Model  # maailman_levinneisyysalue: world_distribution_area
from app.schemas.maailman_levinneisyysalue import MaailmanLevinneisyysalue as Schema, MaailmanLevinneisyysaluePage as SchemaPage  # maailman_levinneisyysalue: world_distribution_area

router = APIRouter()

@router.get("/", response_model=SchemaPage)
@cached_list("maailman_levinneisyysalue")
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

@router.get("/{taksonin_nro}", response_model=Schema)  # taksonin_nro: taxon number
def read_one(taksonin_nro: str, db: Session = Depends(get_db)):  # taksonin_nro: taxon number
    item = db.query(Model).filter(Model.taksonin_nro == taksonin_nro).first()  # taksonin_nro: taxon number
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item