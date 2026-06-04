from fastapi import APIRouter, Depends, HTTPException, Request, Query
from math import ceil
from sqlalchemy.orm import Session
from typing import List

from app.api.query import apply_filters, make_filter_dep
from app.cache import cached_list, invalidate_endpoint_cache
from app.database import get_db
from app.models.puutarhassa_viljelyn_tarkoitus import PuutarhassaViljelynTarkoitus as Model  # puutarhassa_viljelyn_tarkoitus: garden cultivation purpose
from app.schemas.puutarhassa_viljelyn_tarkoitus import PuutarhassaViljelynTarkoitus as Schema, PuutarhassaViljelynTarkoitusPage as SchemaPage  # puutarhassa_viljelyn_tarkoitus: garden cultivation purpose

router = APIRouter()

@router.get("/", response_model=SchemaPage)
@cached_list("puutarhassa_viljelyn_tarkoitus")
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

@router.get("/{hankintaid}", response_model=Schema)  # hankintaid: acquisition id
def read_one(hankintaid: str, db: Session = Depends(get_db)):  # hankintaid: acquisition id
    item = db.query(Model).filter(Model.hankintaID == hankintaid).first()  # hankintaid: acquisition id
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item