from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List, Annotated

from app.api.query import apply_filters
from app.api.crud import create_item, update_item, delete_item
from app.cache import cached_list, invalidate_endpoint_cache
from app.database import get_db
from app.security.utils import get_current_user
from app.models.user import User
from app.models.tarkastusmerkinta import Tarkastusmerkinta as Model  # tarkastusmerkinta: inspection_entry
from app.schemas.tarkastusmerkinta import Tarkastusmerkinta as Schema, TarkastusmerkintaCreate as SchemaCreate  # tarkastusmerkinta: inspection_entry

router = APIRouter()

@router.get("/", response_model=List[Schema])
@cached_list("tarkastusmerkinta")
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/{sijoituspaikan_nro}", response_model=Schema)  # sijoituspaikan_nro: placement number
def read_one(sijoituspaikan_nro: str, db: Session = Depends(get_db)):  # sijoituspaikan_nro: placement number
    item = db.query(Model).filter(Model.sijoituspaikan_nro == sijoituspaikan_nro).first()  # sijoituspaikan_nro: placement number
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("tarkastusmerkinta")
    return await create_item(payload, db, Model)

@router.put("/{tarkastusnro}", response_model=Schema)
async def update_one(tarkastusnro: int, payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("tarkastusmerkinta")
    return await update_item(payload, db, Model, "tarkastusnro", tarkastusnro)

@router.delete("/{tarkastusnro}", status_code=204)
async def delete_one(tarkastusnro: int, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("tarkastusmerkinta")
    await delete_item(db, Model, "tarkastusnro", tarkastusnro)

