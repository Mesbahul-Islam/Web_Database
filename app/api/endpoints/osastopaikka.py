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
from app.models.osastopaikka import Osastopaikka as Model  # osastopaikka: section_location
from app.schemas.osastopaikka import Osastopaikka as Schema, OsastopaikkaCreate as SchemaCreate, OsastopaikkaPage as SchemaPage  # osastopaikka: section_location

from app.models.sijoituspaikka import Sijoituspaikka as SijoituspaikkaModel
from app.schemas.sijoituspaikka import SijoituspaikkaPage as SijoituspaikkaPage
router = APIRouter()

@router.get("/", response_model=SchemaPage)
@cached_list("osastopaikka")
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

@router.get("/{osaston_numero}", response_model=Schema)  # osaston_numero: section number
def read_one(osaston_numero: int, db: Session = Depends(get_db)):  # osaston_numero: section number
    item = db.query(Model).filter(Model.osaston_numero == osaston_numero).first()  # osaston_numero: section number
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("osastopaikka")
    return await create_item(payload, db, Model)

@router.put("/{osaston_numero}", response_model=Schema)
async def update_one(osaston_numero: int, payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("osastopaikka")
    return await update_item(payload, db, Model, "osaston_numero", osaston_numero)

@router.delete("/{osaston_numero}", status_code=204)
async def delete_one(osaston_numero: int, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("osastopaikka")
    await delete_item(db, Model, "osaston_numero", osaston_numero)
@router.get("/{osaston_numero}/sijoituspaikka", response_model=SijoituspaikkaPage)
def read_sijoituspaikka_by_osaston_numero(osaston_numero: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(SijoituspaikkaModel).filter(SijoituspaikkaModel.osaston_numero == osaston_numero), SijoituspaikkaModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return SijoituspaikkaPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )
