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
from app.models.alkuperainen_kasvupaikka import AlkuperainenKasvupaikka as Model
from app.schemas.alkuperainen_kasvupaikka import AlkuperainenKasvupaikka as Schema, AlkuperainenKasvupaikkaCreate as SchemaCreate, AlkuperainenKasvupaikkaPage as SchemaPage
router = APIRouter()

@router.get("/", response_model=SchemaPage)
@cached_list("alkuperainen_kasvupaikka")
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

@router.get("/{taksonin_nro}", response_model=Schema)  # taksonin_nro: taxon number
def read_one(taksonin_nro: str, db: Session = Depends(get_db)):  # taksonin_nro: taxon number
    item = db.query(Model).filter(Model.taksonin_nro == taksonin_nro).first()  # taksonin_nro: taxon number
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("alkuperainen_kasvupaikka")
    return await create_item(payload, db, Model)

@router.put("/{id}", response_model=Schema)
async def update_one(id: int, payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("alkuperainen_kasvupaikka")
    return await update_item(payload, db, Model, "alkuperaisen_kasvupaikan_nro", id)

@router.delete("/{id}", status_code=204)
async def delete_one(id: int, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("alkuperainen_kasvupaikka")
    await delete_item(db, Model, "alkuperaisen_kasvupaikan_nro", id)