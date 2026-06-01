from fastapi import APIRouter, Depends, HTTPException, Request, Query
from math import ceil
from sqlalchemy.orm import Session
from typing import Annotated

from app.api.query import apply_filters
from app.api.crud import create_item, update_item, delete_item
from app.cache import cached_list, invalidate_endpoint_cache
from app.database import get_db
from app.security.utils import get_current_user
from app.models.user import User
from app.models.hankintatiedot import Hankintatiedot as Model  # hankintatiedot: acquisition_data
from app.schemas.hankintatiedot import (
    Hankintatiedot as Schema,
    HankintatiedotCreate as SchemaCreate,
    HankintatiedotPage as SchemaPage,
)  # hankintatiedot: acquisition_data

router = APIRouter()

@router.get("/", response_model=SchemaPage)
@cached_list("hankintatiedot")
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

@router.get("/{hankintaID}", response_model=Schema)  # hankintaID: acquisition id
def read_one(hankintaID: int, db: Session = Depends(get_db)):  # hankintaID: acquisition id
    item = db.query(Model).filter(Model.hankintaID == hankintaID).first()  # hankintaID: acquisition id
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("hankintatiedot")
    return await create_item(payload, db, Model)

@router.put("/{hankintaID}", response_model=Schema)
async def update_one(hankintaID: int, payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("hankintatiedot")
    return await update_item(payload, db, Model, "hankintaID", hankintaID)

@router.delete("/{hankintaID}", status_code=204)
async def delete_one(hankintaID: int, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("hankintatiedot")
    await delete_item(db, Model, "hankintaID", hankintaID)

