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
from app.models.heimo import Heimo as Model  # heimo: family
from app.schemas.heimo import Heimo as Schema, HeimoCreate as SchemaCreate, HeimoPage as SchemaPage  # heimo: family

from app.models.taksoni import Taksoni as TaksoniModel
from app.schemas.taksoni import TaksoniPage as TaksoniPage
router = APIRouter()

@router.get("/", response_model=SchemaPage)
@cached_list("heimo")
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

@router.get("/{jarjestysnumero}", response_model=Schema)  # jarjestysnumero: order number
def read_one(jarjestysnumero: int, db: Session = Depends(get_db)):  # jarjestysnumero: order number
    item = db.query(Model).filter(Model.jarjestysnumero == jarjestysnumero).first()  # jarjestysnumero: order number
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("heimo")
    return await create_item(payload, db, Model)

@router.put("/{jarjestysnumero}", response_model=Schema)
async def update_one(jarjestysnumero: int, payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("heimo")
    return await update_item(payload, db, Model, "jarjestysnumero", jarjestysnumero)

@router.delete("/{jarjestysnumero}", status_code=204)
async def delete_one(jarjestysnumero: int, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("heimo")
    await delete_item(db, Model, "jarjestysnumero", jarjestysnumero)

@router.get("/{jarjestysnumero}/taksoni", response_model=TaksoniPage)
def read_taksoni_by_jarjestysnumero(jarjestysnumero: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(TaksoniModel).filter(TaksoniModel.jarjestysnumero == jarjestysnumero), TaksoniModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return TaksoniPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )
