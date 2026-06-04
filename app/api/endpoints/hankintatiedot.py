from fastapi import APIRouter, Depends, HTTPException, Request, Query
from math import ceil
from sqlalchemy.orm import Session
from typing import Annotated

from app.api.query import apply_filters, make_filter_dep
from app.api.crud import create_item, update_item, delete_item
from app.cache import cached_list, invalidate_endpoint_cache
from app.database import get_db
from app.security.utils import get_current_user
from app.models.user import User
from app.models.hankintatiedot import Hankintatiedot as Model  # hankintatiedot: acquisition_data
from app.schemas.hankintatiedot import (
    Hankintatiedot as Schema,
    HankintatiedotCreate as SchemaCreate,
    HankintatiedotPage as SchemaPage,
)  # hankintatiedot: acquisition_data

from app.models.alkuperaa_koskevat_tiedot import AlkuperaaKoskevatTiedot as AlkuperaaKoskevatTiedotModel
from app.schemas.alkuperaa_koskevat_tiedot import AlkuperaaKoskevatTiedotPage as AlkuperaaKoskevatTiedotPage
from app.models.kasvatustietoja import Kasvatustietoja as KasvatustietojaModel
from app.schemas.kasvatustietoja import KasvatustietojaPage as KasvatustietojaPage
from app.models.maaritysmerkinta import Maaritysmerkinta as MaaritysmerkintaModel
from app.schemas.maaritysmerkinta import MaaritysmerkintaPage as MaaritysmerkintaPage
from app.models.naytetietoja import Naytetietoja as NaytetietojaModel
from app.schemas.naytetietoja import NaytetietojaPage as NaytetietojaPage
from app.models.osastopaikka import Osastopaikka as OsastopaikkaModel
from app.schemas.osastopaikka import OsastopaikkaPage as OsastopaikkaPage
from app.models.puutarhassa_viljelyn_tarkoitus import PuutarhassaViljelynTarkoitus as PuutarhassaViljelynTarkoitusModel
from app.schemas.puutarhassa_viljelyn_tarkoitus import PuutarhassaViljelynTarkoitusPage as PuutarhassaViljelynTarkoitusPage
from app.models.toimenpide import Toimenpide as ToimenpideModel
from app.schemas.toimenpide import ToimenpidePage as ToimenpidePage
router = APIRouter()

@router.get("/", response_model=SchemaPage)
@cached_list("hankintatiedot")
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
    return {
        "items": items,
        "total": total,
        "page": page,
        "page_size": page_size,
        "pages": pages,
    }

@router.get("/{hankintaID}", response_model=Schema)  # hankintaID: acquisition id
def read_one(hankintaID: int, db: Session = Depends(get_db)):  # hankintaID: acquisition id
    item = db.query(Model).filter(Model.hankintaID == hankintaID).first()  # hankintaID: acquisition id
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("hankintatiedot")
    return await create_item(payload, db, Model)

@router.put("/{hankintaID}", response_model=Schema)
async def update_one(hankintaID: int, payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("hankintatiedot")
    return await update_item(payload, db, Model, "hankintaID", hankintaID)

@router.delete("/{hankintaID}", status_code=204)
async def delete_one(hankintaID: int, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("hankintatiedot")
    await delete_item(db, Model, "hankintaID", hankintaID)
@router.get("/{hankintaID}/alkuperaa_koskevat_tiedot", response_model=AlkuperaaKoskevatTiedotPage)
def read_alkuperaa_koskevat_tiedot_by_hankintaID(hankintaID: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(AlkuperaaKoskevatTiedotModel).filter(AlkuperaaKoskevatTiedotModel.hankintaID == hankintaID), AlkuperaaKoskevatTiedotModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return AlkuperaaKoskevatTiedotPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{hankintaID}/kasvatustietoja", response_model=KasvatustietojaPage)
def read_kasvatustietoja_by_hankintaID(hankintaID: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(KasvatustietojaModel).filter(KasvatustietojaModel.hankintaID == hankintaID), KasvatustietojaModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return KasvatustietojaPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{hankintaID}/maaritysmerkinta", response_model=MaaritysmerkintaPage)
def read_maaritysmerkinta_by_hankintaID(hankintaID: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(MaaritysmerkintaModel).filter(MaaritysmerkintaModel.hankintaID == hankintaID), MaaritysmerkintaModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return MaaritysmerkintaPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{hankintaID}/naytetietoja", response_model=NaytetietojaPage)
def read_naytetietoja_by_hankintaID(hankintaID: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(NaytetietojaModel).filter(NaytetietojaModel.hankintaID == hankintaID), NaytetietojaModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return NaytetietojaPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{hankintaID}/osastopaikka", response_model=OsastopaikkaPage)
def read_osastopaikka_by_hankintaID(hankintaID: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(OsastopaikkaModel).filter(OsastopaikkaModel.hankintaID == hankintaID), OsastopaikkaModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return OsastopaikkaPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{hankintaID}/puutarhassa_viljelyn_tarkoitus", response_model=PuutarhassaViljelynTarkoitusPage)
def read_puutarhassa_viljelyn_tarkoitus_by_hankintaID(hankintaID: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(PuutarhassaViljelynTarkoitusModel).filter(PuutarhassaViljelynTarkoitusModel.hankintaID == hankintaID), PuutarhassaViljelynTarkoitusModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return PuutarhassaViljelynTarkoitusPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{hankintaID}/toimenpide", response_model=ToimenpidePage)
def read_toimenpide_by_hankintaID(hankintaID: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(ToimenpideModel).filter(ToimenpideModel.hankintaID == hankintaID), ToimenpideModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return ToimenpidePage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )
