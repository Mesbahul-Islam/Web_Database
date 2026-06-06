from fastapi import APIRouter, Depends, HTTPException, Request, Query
from math import ceil
from sqlalchemy.orm import Session
from typing import List, Annotated

from app.api.query import apply_filters, make_filter_dep
from app.api.crud import create_item, update_item, delete_item
from app.cache import cached_list, invalidate_endpoint_cache
from app.database import get_db
from app.security.utils import get_current_user
from app.models.user import User
from app.models.puutarhassa_viljelyn_tarkoitus import PuutarhassaViljelynTarkoitus as Model  # puutarhassa_viljelyn_tarkoitus: garden cultivation purpose
from app.schemas.puutarhassa_viljelyn_tarkoitus import (
    PuutarhassaViljelynTarkoitus as Schema,
    PuutarhassaViljelynTarkoitusCreate as SchemaCreate,
    PuutarhassaViljelynTarkoitusPage as SchemaPage,
)

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

@router.post("/", response_model=Schema, status_code=201)
async def create_one(
    payload: SchemaCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    invalidate_endpoint_cache("puutarhassa_viljelyn_tarkoitus")
    item = await create_item(payload, db, Model)

    # Update parent hankintatiedot lisaysPVM
    from app.models.hankintatiedot import Hankintatiedot
    from datetime import datetime
    hankinta = db.query(Hankintatiedot).filter(Hankintatiedot.hankintaID == payload.hankintaID).first()
    if hankinta:
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        hankinta.lisaysPVM = f"{timestamp} {current_user.username}"
        db.add(hankinta)
        db.commit()
        invalidate_endpoint_cache("hankintatiedot")

    return item

@router.put("/{viljely_nro}", response_model=Schema)
async def update_one(
    viljely_nro: int,
    payload: SchemaCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    invalidate_endpoint_cache("puutarhassa_viljelyn_tarkoitus")
    item = await update_item(payload, db, Model, "viljely_nro", viljely_nro)

    # Update parent hankintatiedot lisaysPVM
    from app.models.hankintatiedot import Hankintatiedot
    from datetime import datetime
    hankinta = db.query(Hankintatiedot).filter(Hankintatiedot.hankintaID == payload.hankintaID).first()
    if hankinta:
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        hankinta.lisaysPVM = f"{timestamp} {current_user.username}"
        db.add(hankinta)
        db.commit()
        invalidate_endpoint_cache("hankintatiedot")

    return item

@router.delete("/{viljely_nro}", status_code=204)
async def delete_one(
    viljely_nro: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    invalidate_endpoint_cache("puutarhassa_viljelyn_tarkoitus")
    await delete_item(db, Model, "viljely_nro", viljely_nro)