from fastapi import APIRouter, Depends, HTTPException, Request, Query
from math import ceil
from sqlalchemy.orm import Session
from typing import List, Annotated

from app.api.query import apply_filters
from app.api.crud import create_item, update_item, delete_item
from app.cache import cached_list, invalidate_endpoint_cache
from app.database import get_db
from app.security.utils import get_current_user
from app.models.user import User
from app.models.taksoni import Taksoni as Model  # taksoni: taxon
from app.schemas.taksoni import (
    Taksoni as Schema,
    TaksoniCreate as SchemaCreate,
    TaksoniPage as SchemaPage,
)  # taksoni: taxon

router = APIRouter()

@router.get("", response_model=SchemaPage, include_in_schema=False)
@router.get("/", response_model=SchemaPage)
@cached_list("taksoni")
def read_all(
    request: Request,
    page: int = Query(1, ge=1),
    page_size: int = Query(200, ge=1),
    db: Session = Depends(get_db),
):
    query = apply_filters(db.query(Model), Model, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return {
        "items": items,
        "total": total,
        "page": page,
        "page_size": page_size,
        "pages": pages,
    }

@router.get("/count", response_model=int)
def count_items(request: Request, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.count()

@router.get("/{taksonin_nro}", response_model=Schema)  # taksonin_nro: taxon number
def read_one(taksonin_nro: int, db: Session = Depends(get_db)):  # taksonin_nro: taxon number
    item = db.query(Model).filter(Model.taksonin_nro == taksonin_nro).first()  # taksonin_nro: taxon number
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("taksoni")
    return await create_item(payload, db, Model)

@router.put("/{taksonin_nro}", response_model=Schema)
async def update_one(taksonin_nro: int, payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("taksoni")
    return await update_item(payload, db, Model, "taksonin_nro", taksonin_nro)

@router.delete("/{taksonin_nro}", status_code=204)
async def delete_one(taksonin_nro: int, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("taksoni")
    await delete_item(db, Model, "taksonin_nro", taksonin_nro)
