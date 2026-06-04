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
from app.models.taksonin_viljelytiedot import TaksoninViljelytiedot as Model  # taksonin_viljelytiedot: taxon_cultivation_data
from app.schemas.taksonin_viljelytiedot import TaksoninViljelytiedot as Schema, TaksoninViljelytiedotCreate as SchemaCreate, TaksoninViljelytiedotPage as SchemaPage  # taksonin_viljelytiedot: taxon_cultivation_data

router = APIRouter()

@router.get("/", response_model=SchemaPage)
@cached_list("taksonin_viljelytiedot")
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

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("taksonin_viljelytiedot")
    return await create_item(payload, db, Model)

@router.put("/{lisatietojen_nro_viljely}", response_model=Schema)
async def update_one(lisatietojen_nro_viljely: int, payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("taksonin_viljelytiedot")
    return await update_item(payload, db, Model, "lisatietojen_nro_viljely", lisatietojen_nro_viljely)

@router.delete("/{lisatietojen_nro_viljely}", status_code=204)
async def delete_one(lisatietojen_nro_viljely: int, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("taksonin_viljelytiedot")
    await delete_item(db, Model, "lisatietojen_nro_viljely", lisatietojen_nro_viljely)