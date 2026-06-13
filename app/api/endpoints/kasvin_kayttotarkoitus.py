from fastapi import APIRouter, Depends, HTTPException, Request, Query
from math import ceil
from sqlalchemy.orm import Session
from typing import List, Annotated

from app.api.query import apply_filters, make_filter_dep
from app.cache import cached_list
from app.api.crud import create_item, update_item, delete_item
from app.database import get_db
from app.security.utils import get_current_user
from app.models.user import User
from app.models.kasvin_kayttotarkoitus import KasvinKayttotarkoitus as Model
from app.schemas.kasvin_kayttotarkoitus import KasvinKayttotarkoitus as Schema, KasvinKayttotarkoitusCreate as SchemaCreate, KasvinKayttotarkoitusPage as SchemaPage

router = APIRouter()

@router.get("/", response_model=SchemaPage)
@cached_list("kasvin_kayttotarkoitus")
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

@router.get("/{taksonin_nro}", response_model=List[Schema])
def read_one(taksonin_nro: str, db: Session = Depends(get_db)):
    items = db.query(Model).filter(Model.taksonin_nro == taksonin_nro).all()
    return items

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    return await create_item(payload, db, Model)

@router.put("/{kayttonro}", response_model=Schema)
async def update_one(kayttonro: int, payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    return await update_item(payload, db, Model, "kayttonro", kayttonro)

@router.delete("/{kayttonro}", status_code=204)
async def delete_one(kayttonro: int, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    await delete_item(db, Model, "kayttonro", kayttonro)