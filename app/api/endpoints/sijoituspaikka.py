from fastapi import APIRouter, Depends, HTTPException, Request, Query
from sqlalchemy.orm import Session
from typing import List, Annotated
from math import ceil

from app.api.query import apply_filters, make_filter_dep
from app.api.crud import create_item, update_item, delete_item
from app.cache import cached_list, invalidate_endpoint_cache
from app.database import get_db
from app.security.utils import get_current_user
from app.models.user import User
from app.models.sijoituspaikka import Sijoituspaikka as Model  # sijoituspaikka: placement location
from app.schemas.sijoituspaikka import Sijoituspaikka as Schema, SijoituspaikkaCreate as SchemaCreate
from app.schemas.sijoituspaikka import SijoituspaikkaPage as SchemaPage  # sijoituspaikka: placement location

from app.models.tarkastusmerkinta import Tarkastusmerkinta as TarkastusmerkintaModel
from app.schemas.tarkastusmerkinta import TarkastusmerkintaPage as TarkastusmerkintaPage
router = APIRouter()

@router.get("/", response_model=SchemaPage)
@cached_list("sijoituspaikka")
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

@router.get("/{sijoituspaikan_nro}", response_model=Schema)  # sijoituspaikan_nro: placement number
def read_one(sijoituspaikan_nro: int, db: Session = Depends(get_db)):  # sijoituspaikan_nro: placement number
    item = db.query(Model).filter(Model.sijoituspaikan_nro == sijoituspaikan_nro).first()  # sijoituspaikan_nro: placement number
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("sijoituspaikka")
    return await create_item(payload, db, Model)

@router.put("/{sijoituspaikan_nro}", response_model=Schema)
async def update_one(sijoituspaikan_nro: int, payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("sijoituspaikka")
    return await update_item(payload, db, Model, "sijoituspaikan_nro", sijoituspaikan_nro)

@router.delete("/{sijoituspaikan_nro}", status_code=204)
async def delete_one(sijoituspaikan_nro: int, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("sijoituspaikka")
    await delete_item(db, Model, "sijoituspaikan_nro", sijoituspaikan_nro)
@router.get("/{sijoituspaikan_nro}/tarkastusmerkinta", response_model=TarkastusmerkintaPage)
def read_tarkastusmerkinta_by_sijoituspaikan_nro(sijoituspaikan_nro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(TarkastusmerkintaModel).filter(TarkastusmerkintaModel.sijoituspaikan_nro == sijoituspaikan_nro), TarkastusmerkintaModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return TarkastusmerkintaPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )
