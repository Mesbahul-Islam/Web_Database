from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List, Annotated

from app.api.query import apply_filters
from app.api.crud import create_item, update_item, delete_item
from app.database import get_db
from app.security.utils import get_current_user
from app.models.user import User
from app.models.kasvatustietoja import Kasvatustietoja as Model  # kasvatustietoja: cultivation_data
from app.schemas.kasvatustietoja import Kasvatustietoja as Schema, KasvatustietojaCreate as SchemaCreate  # kasvatustietoja: cultivation_data

router = APIRouter()

@router.get("/", response_model=List[Schema])
def read_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.offset(skip).limit(limit).all()

@router.get("/{hankintaID}", response_model=Schema)  # hankintaID: acquisition id
def read_one(hankintaID: str, db: Session = Depends(get_db)):  # hankintaID: acquisition id
    item = db.query(Model).filter(Model.hankintaID == hankintaID).first()  # hankintaID: acquisition id
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.get("/hankinta/{hankintaID}", response_model=List[Schema])  # hankintaID: acquisition id
def read_and_filter_by_hankintaID(hankintaID: str, request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):  # hankintaID: acquisition id
    query = apply_filters(db.query(Model).filter(Model.hankintaID == hankintaID), Model, request.query_params)  # hankintaID: acquisition id
    return query.offset(skip).limit(limit).all()

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    return await create_item(payload, db, Model)

@router.put("/{lisatietojen_nro_kasvatus}", response_model=Schema)
async def update_one(lisatietojen_nro_kasvatus: int, payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    return await update_item(payload, db, Model, "lisatietojen_nro_kasvatus", lisatietojen_nro_kasvatus)

@router.delete("/{lisatietojen_nro_kasvatus}", status_code=204)
async def delete_one(lisatietojen_nro_kasvatus: int, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    await delete_item(db, Model, "lisatietojen_nro_kasvatus", lisatietojen_nro_kasvatus)

