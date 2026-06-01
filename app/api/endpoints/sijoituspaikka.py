from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List, Annotated

from app.api.query import apply_filters
from app.api.crud import create_item, update_item, delete_item
from app.cache import cached_list, invalidate_endpoint_cache
from app.database import get_db
from app.security.utils import get_current_user
from app.models.user import User
from app.models.sijoituspaikka import Sijoituspaikka as Model  # sijoituspaikka: placement location
from app.schemas.sijoituspaikka import Sijoituspaikka as Schema, SijoituspaikkaCreate as SchemaCreate  # sijoituspaikka: placement location

router = APIRouter()

@router.get("/", response_model=List[Schema])
@cached_list("sijoituspaikka")
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

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

