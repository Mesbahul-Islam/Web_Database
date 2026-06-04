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
from app.models.viite import Viite as Model  # viite: reference
from app.schemas.viite import Viite as Schema, ViiteCreate as SchemaCreate, ViitePage as SchemaPage  # viite: reference

from app.models.alkuperainen_kasvupaikka import AlkuperainenKasvupaikka as AlkuperainenKasvupaikkaModel
from app.schemas.alkuperainen_kasvupaikka import AlkuperainenKasvupaikkaPage as AlkuperainenKasvupaikkaPage
from app.models.kansainvaliset_sopimukset import KansainvalisetSopimukset as KansainvalisetSopimuksetModel
from app.schemas.kansainvaliset_sopimukset import KansainvalisetSopimuksetPage as KansainvalisetSopimuksetPage
from app.models.kasvin_kayttotarkoitus import KasvinKayttotarkoitus as KasvinKayttotarkoitusModel
from app.schemas.kasvin_kayttotarkoitus import KasvinKayttotarkoitusPage as KasvinKayttotarkoitusPage
from app.models.muunkielinen_nimi import MuunkielinenNimi as MuunkielinenNimiModel
from app.schemas.muunkielinen_nimi import MuunkielinenNimiPage as MuunkielinenNimiPage
from app.models.naytetieto import Naytetieto as NaytetietoModel
from app.schemas.naytetieto import NaytetietoPage as NaytetietoPage
from app.models.suomalainen_kasvupaikka import SuomalainenKasvupaikka as SuomalainenKasvupaikkaModel
from app.schemas.suomalainen_kasvupaikka import SuomalainenKasvupaikkaPage as SuomalainenKasvupaikkaPage
from app.models.suomalainen_levinneisyysalue import SuomalainenLevinneisyysalue as SuomalainenLevinneisyysalueModel
from app.schemas.suomalainen_levinneisyysalue import SuomalainenLevinneisyysaluePage as SuomalainenLevinneisyysaluePage
from app.models.synonyymi import Synonyymi as SynonyymiModel
from app.schemas.synonyymi import SynonyymiPage as SynonyymiPage
from app.models.taksoni import Taksoni as TaksoniModel
from app.schemas.taksoni import TaksoniPage as TaksoniPage
from app.models.ymparistoindikaattoriluonne import Ymparistoindikaattoriluonne as YmparistoindikaattoriluonneModel
from app.schemas.ymparistoindikaattoriluonne import YmparistoindikaattoriluonnePage as YmparistoindikaattoriluonnePage
router = APIRouter()

@router.get("/", response_model=SchemaPage)
@cached_list("viite")
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

@router.get("/{viitteen_lyhenne}", response_model=Schema)  # viitteen_lyhenne: reference abbreviation
def read_one(viitteen_lyhenne: str, db: Session = Depends(get_db)):  # viitteen_lyhenne: reference abbreviation
    item = db.query(Model).filter(Model.viitteen_lyhenne == viitteen_lyhenne).first()  # viitteen_lyhenne: reference abbreviation
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("viite")
    return await create_item(payload, db, Model)

@router.put("/{viitenro}", response_model=Schema)
async def update_one(viitenro: int, payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("viite")
    return await update_item(payload, db, Model, "viitenro", viitenro)

@router.delete("/{viitenro}", status_code=204)
async def delete_one(viitenro: int, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("viite")
    await delete_item(db, Model, "viitenro", viitenro)

@router.get("/{viitenro}/alkuperainen_kasvupaikka", response_model=AlkuperainenKasvupaikkaPage)
def read_alkuperainen_kasvupaikka_by_viitenro(viitenro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(AlkuperainenKasvupaikkaModel).filter(AlkuperainenKasvupaikkaModel.viitenro == viitenro), AlkuperainenKasvupaikkaModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return AlkuperainenKasvupaikkaPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{viitenro}/kansainvaliset_sopimukset", response_model=KansainvalisetSopimuksetPage)
def read_kansainvaliset_sopimukset_by_viitenro(viitenro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(KansainvalisetSopimuksetModel).filter(KansainvalisetSopimuksetModel.viitenro == viitenro), KansainvalisetSopimuksetModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return KansainvalisetSopimuksetPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{viitenro}/kasvin_kayttotarkoitus", response_model=KasvinKayttotarkoitusPage)
def read_kasvin_kayttotarkoitus_by_viitenro(viitenro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(KasvinKayttotarkoitusModel).filter(KasvinKayttotarkoitusModel.viitenro == viitenro), KasvinKayttotarkoitusModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return KasvinKayttotarkoitusPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{viitenro}/muunkielinen_nimi", response_model=MuunkielinenNimiPage)
def read_muunkielinen_nimi_by_viitenro(viitenro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(MuunkielinenNimiModel).filter(MuunkielinenNimiModel.viitenro == viitenro), MuunkielinenNimiModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return MuunkielinenNimiPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{viitenro}/naytetieto", response_model=NaytetietoPage)
def read_naytetieto_by_viitenro(viitenro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(NaytetietoModel).filter(NaytetietoModel.viitenro == viitenro), NaytetietoModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return NaytetietoPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{viitenro}/suomalainen_kasvupaikka", response_model=SuomalainenKasvupaikkaPage)
def read_suomalainen_kasvupaikka_by_viitenro(viitenro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(SuomalainenKasvupaikkaModel).filter(SuomalainenKasvupaikkaModel.viitenro == viitenro), SuomalainenKasvupaikkaModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return SuomalainenKasvupaikkaPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{viitenro}/suomalainen_levinneisyysalue", response_model=SuomalainenLevinneisyysaluePage)
def read_suomalainen_levinneisyysalue_by_viitenro(viitenro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(SuomalainenLevinneisyysalueModel).filter(SuomalainenLevinneisyysalueModel.viitenro == viitenro), SuomalainenLevinneisyysalueModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return SuomalainenLevinneisyysaluePage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{viitenro}/synonyymi", response_model=SynonyymiPage)
def read_synonyymi_by_viitenro(viitenro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(SynonyymiModel).filter(SynonyymiModel.viitenro == viitenro), SynonyymiModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return SynonyymiPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{viitenro}/taksoni", response_model=TaksoniPage)
def read_taksoni_by_viitenro(viitenro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(TaksoniModel).filter(TaksoniModel.viitenro == viitenro), TaksoniModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return TaksoniPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{viitenro}/ymparistoindikaattoriluonne", response_model=YmparistoindikaattoriluonnePage)
def read_ymparistoindikaattoriluonne_by_viitenro(viitenro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(YmparistoindikaattoriluonneModel).filter(YmparistoindikaattoriluonneModel.viitenro == viitenro), YmparistoindikaattoriluonneModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return YmparistoindikaattoriluonnePage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )
