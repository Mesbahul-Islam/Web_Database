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
from app.models.alkuperaa_koskevat_tiedot import AlkuperaaKoskevatTiedot as Model  # alkuperaa_koskevat_tiedot: origin-related_data
from app.schemas.alkuperaa_koskevat_tiedot import AlkuperaaKoskevatTiedot as Schema, AlkuperaaKoskevatTiedotCreate as SchemaCreate  # alkuperaa_koskevat_tiedot: origin-related_data
from app.schemas.alkuperaa_koskevat_tiedot import AlkuperaaKoskevatTiedotPage as SchemaPage  # alkuperaa_koskevat_tiedot: origin-related_data


router = APIRouter()

@router.get("/", response_model=SchemaPage)
@cached_list("alkuperaa_koskevat_tiedot")
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
        pages=pages
    )

@router.get("/{alkupera_nro}", response_model=Schema)  # alkupera_nro: origin number
def read_one(alkupera_nro: int, db: Session = Depends(get_db)):  # alkupera_nro: origin number
    item = db.query(Model).filter(Model.alkupera_nro == alkupera_nro).first()  # alkupera_nro: origin number
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("alkuperaa_koskevat_tiedot")
    return await create_item(payload, db, Model)

@router.put("/{alkupera_nro}", response_model=Schema)
async def update_one(alkupera_nro: int, payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("alkuperaa_koskevat_tiedot")
    return await update_item(payload, db, Model, "alkupera_nro", alkupera_nro)

@router.delete("/{alkupera_nro}", status_code=204)
async def delete_one(alkupera_nro: int, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("alkuperaa_koskevat_tiedot")
    await delete_item(db, Model, "alkupera_nro", alkupera_nro)