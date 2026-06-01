from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List, Annotated

from app.api.query import apply_filters
from app.api.crud import create_item, update_item, delete_item
from app.cache import cached_list, invalidate_endpoint_cache
from app.database import get_db
from app.security.utils import get_current_user
from app.models.user import User
from app.models.naytetietoja import Naytetietoja as Model  # naytetietoja: specimen_information
from app.schemas.naytetietoja import Naytetietoja as Schema, NaytetietojaCreate as SchemaCreate  # naytetietoja: specimen_information

router = APIRouter()

@router.get("/", response_model=List[Schema])
@cached_list("naytetietoja")
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/{hankintaid}", response_model=Schema)  # hankintaid: acquisition id
def read_one(hankintaid: str, db: Session = Depends(get_db)):  # hankintaid: acquisition id
    item = db.query(Model).filter(Model.hankintaID == hankintaid).first()  # hankintaid: acquisition id
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("naytetietoja")
    return await create_item(payload, db, Model)

@router.put("/{naytteen_nro}", response_model=Schema)
async def update_one(naytteen_nro: int, payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("naytetietoja")
    return await update_item(payload, db, Model, "naytteen_nro", naytteen_nro)

@router.delete("/{naytteen_nro}", status_code=204)
async def delete_one(naytteen_nro: int, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("naytetietoja")
    await delete_item(db, Model, "naytteen_nro", naytteen_nro)

