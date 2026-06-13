from fastapi import APIRouter, Depends, HTTPException, Request, Query
from math import ceil
from sqlalchemy.orm import Session
from typing import List
from app.api.crud import create_item, update_item, delete_item

from app.api.query import apply_filters, make_filter_dep
from app.cache import cached_list
from app.database import get_db
from app.models.lista_polytystapa import ListaPolytystapa as Model  # lista_polytystapa: list pollination method
from app.schemas.lista_polytystapa import ListaPolytystapa as Schema, ListaPolytystapaPage as SchemaPage, ListaPolytystapaCreate as SchemaCreate

router = APIRouter()

@router.get("/", response_model=SchemaPage)
@cached_list("lista_polytystapa")
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

@router.get("/{id}", response_model=Schema)  # id: id
def read_one(id: int, db: Session = Depends(get_db)):  # id: id
    item = db.query(Model).filter(Model.ID == id).first()  # id: id
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item


@router.post("/", response_model=Schema, status_code=201)
async def create(payload: SchemaCreate, db: Session = Depends(get_db)):
    return await create_item(payload, db, Model)

@router.put("/{id}", response_model=Schema)
async def update(id: int, payload: SchemaCreate, db: Session = Depends(get_db)):
    return await update_item(payload, db, Model, "ID", id)

@router.delete("/{id}", status_code=204)
async def delete(id: int, db: Session = Depends(get_db)):
    return await delete_item(db, Model, "ID", id)
