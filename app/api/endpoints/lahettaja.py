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
from app.models.lahettaja import Lahettaja as Model  # lahettaja: sender
from app.schemas.lahettaja import Lahettaja as Schema, LahettajaCreate as SchemaCreate  # lahettaja: sender

from app.models.hankintatiedot import Hankintatiedot as HankintatiedotModel
from app.schemas.hankintatiedot import HankintatiedotPage as HankintatiedotPage
router = APIRouter()

@router.get("/", response_model=List[Schema])
@cached_list("lahettaja")
def read_all(request: Request, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.all()

@router.get("/count", response_model=int)
def count_items(request: Request, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.count()

@router.get("/{lahettajanro}", response_model=Schema)  # lahettajanro: sender number
def read_one(lahettajanro: int, db: Session = Depends(get_db)):  # lahettajanro: sender number
    item = db.query(Model).filter(Model.lahettajanro == lahettajanro).first()  # lahettajanro: sender number
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("lahettaja")
    return await create_item(payload, db, Model)

@router.put("/{lahettajanro}", response_model=Schema)
async def update_one(lahettajanro: int, payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("lahettaja")
    return await update_item(payload, db, Model, "lahettajanro", lahettajanro)

@router.delete("/{lahettajanro}", status_code=204)
async def delete_one(lahettajanro: int, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("lahettaja")
    await delete_item(db, Model, "lahettajanro", lahettajanro)

@router.get("/{lahettajanro}/hankintatiedot", response_model=HankintatiedotPage)
def read_hankintatiedot_by_lahettajanro(lahettajanro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(HankintatiedotModel).filter(HankintatiedotModel.lahettajanro == lahettajanro), HankintatiedotModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return HankintatiedotPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )
