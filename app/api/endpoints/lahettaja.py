from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List, Annotated

from app.api.query import apply_filters
from app.api.crud import create_item, update_item, delete_item
from app.cache import cached_list, invalidate_endpoint_cache
from app.database import get_db
from app.security.utils import get_current_user
from app.models.user import User
from app.models.lahettaja import Lahettaja as Model  # lahettaja: sender
from app.schemas.lahettaja import Lahettaja as Schema, LahettajaCreate as SchemaCreate  # lahettaja: sender

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

