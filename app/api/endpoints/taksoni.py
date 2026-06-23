from fastapi import APIRouter, Depends, HTTPException, Request, Query
from math import ceil
from sqlalchemy.orm import Session
from typing import List, Annotated, Optional
from sqlalchemy import func, String, cast

from app.api.query import apply_filters, make_filter_dep
from app.api.crud import create_item, update_item, delete_item
from app.cache import cached_list, invalidate_endpoint_cache
from app.database import get_db
from app.security.utils import get_current_user
from app.models.user import User
from app.models.taksoni import Taksoni as Model  # taksoni: taxon
from app.schemas.taksoni import (
    Taksoni as Schema,
    TaksoniCreate as SchemaCreate,
    TaksoniPage as SchemaPage,
    TaksoninHankintatiedotYhteenvetoPage
)  # taksoni: taxon

from sqlalchemy.sql.expression import FunctionElement
from sqlalchemy.ext.compiler import compiles

class group_concat(FunctionElement):
    name = 'group_concat'
    inherit_cache = True

@compiles(group_concat)
def compile_group_concat(element, compiler, **kw):
    return "group_concat(%s)" % compiler.process(element.clauses, **kw)

@compiles(group_concat, 'postgresql')
def compile_group_concat_pg(element, compiler, **kw):
    if len(element.clauses) == 2:
        return "string_agg(%s, %s)" % (
            compiler.process(element.clauses.clauses[0], **kw),
            compiler.process(element.clauses.clauses[1], **kw)
        )
    return "string_agg(%s, ',')" % compiler.process(element.clauses.clauses[0], **kw)

from app.models.alkuperainen_kasvupaikka import AlkuperainenKasvupaikka as AlkuperainenKasvupaikkaModel
from app.schemas.alkuperainen_kasvupaikka import AlkuperainenKasvupaikkaPage as AlkuperainenKasvupaikkaPage
from app.models.hankintatiedot import Hankintatiedot as HankintatiedotModel
from app.schemas.hankintatiedot import HankintatiedotPage as HankintatiedotPage
from app.models.kansainvaliset_sopimukset import KansainvalisetSopimukset as KansainvalisetSopimuksetModel
from app.schemas.kansainvaliset_sopimukset import KansainvalisetSopimuksetPage as KansainvalisetSopimuksetPage
from app.models.kasvin_kayttotarkoitus import KasvinKayttotarkoitus as KasvinKayttotarkoitusModel
from app.schemas.kasvin_kayttotarkoitus import KasvinKayttotarkoitusPage as KasvinKayttotarkoitusPage
from app.models.maailman_levinneisyysalue import MaailmanLevinneisyysalue as MaailmanLevinneisyysalueModel
from app.schemas.maailman_levinneisyysalue import MaailmanLevinneisyysaluePage as MaailmanLevinneisyysaluePage
from app.models.muunkielinen_nimi import MuunkielinenNimi as MuunkielinenNimiModel
from app.schemas.muunkielinen_nimi import MuunkielinenNimiPage as MuunkielinenNimiPage
from app.models.naytetieto import Naytetieto as NaytetietoModel
from app.schemas.naytetieto import NaytetietoPage as NaytetietoPage
from app.models.suomalainen_kasvupaikka import SuomalainenKasvupaikka as SuomalainenKasvupaikkaModel
from app.schemas.suomalainen_kasvupaikka import SuomalainenKasvupaikkaPage as SuomalainenKasvupaikkaPage
from app.models.suomalainen_levinneisyysalue import SuomalainenLevinneisyysalue as SuomalainenLevinneisyysalueModel
from app.schemas.suomalainen_levinneisyysalue import SuomalainenLevinneisyysaluePage as SuomalainenLevinneisyysaluePage
from app.models.suunniteltu_kasvupaikka import SuunniteltuKasvupaikka as SuunniteltuKasvupaikkaModel
from app.schemas.suunniteltu_kasvupaikka import SuunniteltuKasvupaikkaPage as SuunniteltuKasvupaikkaPage
from app.models.synonyymi import Synonyymi as SynonyymiModel
from app.schemas.synonyymi import SynonyymiPage as SynonyymiPage
from app.models.taksonin_lappu import TaksoninLappu as TaksoninLappuModel
from app.schemas.taksonin_lappu import TaksoninLappuPage as TaksoninLappuPage
from app.models.taksonin_viljelytiedot import TaksoninViljelytiedot as TaksoninViljelytiedotModel
from app.schemas.taksonin_viljelytiedot import TaksoninViljelytiedotPage as TaksoninViljelytiedotPage
from app.models.ymparistoindikaattoriluonne import Ymparistoindikaattoriluonne as YmparistoindikaattoriluonneModel
from app.schemas.ymparistoindikaattoriluonne import YmparistoindikaattoriluonnePage as YmparistoindikaattoriluonnePage
from app.core.config import settings
from app.core.limiter import limiter


router = APIRouter()

@router.get("", response_model=SchemaPage, include_in_schema=False)
@router.get("/", response_model=SchemaPage)
@cached_list("taksoni")
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

@router.get("/hankintatiedot_yhteenveto", response_model=TaksoninHankintatiedotYhteenvetoPage)
def read_hankintatiedot_yhteenveto(
    request: Request,
    page: int = Query(1, ge=1),
    page_size: int = Query(25, ge=1),
    search: Optional[str] = None,
    sort_by: str = Query("default"),
    db: Session = Depends(get_db),
):
    subq = db.query(
        Model.taksonin_nro.label("taksonin_nro"),
        Model.tieteellinen_nimi.label("tieteellinen_nimi"),
        Model.suku.label("suku"),
        Model.laji.label("laji"),
        func.coalesce(group_concat(HankintatiedotModel.hankintanumero, ", "), "").label("hankintanumerot"),
        func.count(HankintatiedotModel.hankintaID).label("hankinnat_lkm")
    ).outerjoin(
        HankintatiedotModel, Model.taksonin_nro == HankintatiedotModel.taksonin_nro
    ).group_by(
        Model.taksonin_nro,
        Model.tieteellinen_nimi,
        Model.suku,
        Model.laji
    ).subquery()
    
    query = db.query(subq)
    
    if search:
        s = f"%{search.lower()}%"
        query = query.filter(
            func.lower(subq.c.tieteellinen_nimi).like(s) |
            func.lower(subq.c.suku).like(s) |
            func.lower(subq.c.laji).like(s) |
            cast(subq.c.taksonin_nro, String).like(s) |
            func.lower(subq.c.hankintanumerot).like(s)
        )
    
    if sort_by == "acquisitions-desc":
        query = query.order_by(subq.c.hankinnat_lkm.desc(), subq.c.taksonin_nro.asc())
    elif sort_by == "acquisitions-asc":
        query = query.order_by(subq.c.hankinnat_lkm.asc(), subq.c.taksonin_nro.asc())
    else:
        query = query.order_by(subq.c.taksonin_nro.asc())
        
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    
    res_items = []
    for item in items:
        res_items.append({
            "taksonin_nro": item.taksonin_nro,
            "tieteellinen_nimi": item.tieteellinen_nimi,
            "suku": item.suku,
            "laji": item.laji,
            "hankintanumerot": item.hankintanumerot if item.hankintanumerot is not None else "",
            "hankinnat_lkm": item.hankinnat_lkm if item.hankinnat_lkm is not None else 0,
            "searchId": str(item.taksonin_nro)
        })

    return {
        "items": res_items,
        "total": total,
        "page": page,
        "page_size": page_size,
        "pages": pages,
    }

@router.get("/count", response_model=int)
def count_items(request: Request, db: Session = Depends(get_db)):
    query = apply_filters(db.query(Model), Model, request.query_params)
    return query.count()

@router.get("/{taksonin_nro}", response_model=Schema)  # taksonin_nro: taxon number
def read_one(taksonin_nro: int, db: Session = Depends(get_db)):  # taksonin_nro: taxon number
    item = db.query(Model).filter(Model.taksonin_nro == taksonin_nro).first()  # taksonin_nro: taxon number
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@router.post("/", response_model=Schema, status_code=201)
async def create_one(payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("taksoni")
    return await create_item(payload, db, Model)

@router.put("/{taksonin_nro}", response_model=Schema)
async def update_one(taksonin_nro: int, payload: SchemaCreate, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("taksoni")
    return await update_item(payload, db, Model, "taksonin_nro", taksonin_nro)

@router.delete("/{taksonin_nro}", status_code=204)
async def delete_one(taksonin_nro: int, current_user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)):
    invalidate_endpoint_cache("taksoni")
    await delete_item(db, Model, "taksonin_nro", taksonin_nro)
@router.get("/{taksonin_nro}/alkuperainen_kasvupaikka", response_model=AlkuperainenKasvupaikkaPage)
def read_alkuperainen_kasvupaikka_by_taksonin_nro(taksonin_nro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(AlkuperainenKasvupaikkaModel).filter(AlkuperainenKasvupaikkaModel.taksonin_nro == taksonin_nro), AlkuperainenKasvupaikkaModel, request.query_params)
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

@router.get("/{taksonin_nro}/hankintatiedot", response_model=HankintatiedotPage)
def read_hankintatiedot_by_taksonin_nro(taksonin_nro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(HankintatiedotModel).filter(HankintatiedotModel.taksonin_nro == taksonin_nro), HankintatiedotModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return HankintatiedotPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{taksonin_nro}/kansainvaliset_sopimukset", response_model=KansainvalisetSopimuksetPage)
def read_kansainvaliset_sopimukset_by_taksonin_nro(taksonin_nro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(KansainvalisetSopimuksetModel).filter(KansainvalisetSopimuksetModel.taksonin_nro == taksonin_nro), KansainvalisetSopimuksetModel, request.query_params)
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

@router.get("/{taksonin_nro}/kasvin_kayttotarkoitus", response_model=KasvinKayttotarkoitusPage)
def read_kasvin_kayttotarkoitus_by_taksonin_nro(taksonin_nro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(KasvinKayttotarkoitusModel).filter(KasvinKayttotarkoitusModel.taksonin_nro == taksonin_nro), KasvinKayttotarkoitusModel, request.query_params)
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

@router.get("/{taksonin_nro}/maailman_levinneisyysalue", response_model=MaailmanLevinneisyysaluePage)
def read_maailman_levinneisyysalue_by_taksonin_nro(taksonin_nro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(MaailmanLevinneisyysalueModel).filter(MaailmanLevinneisyysalueModel.taksonin_nro == taksonin_nro), MaailmanLevinneisyysalueModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return MaailmanLevinneisyysaluePage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{taksonin_nro}/muunkielinen_nimi", response_model=MuunkielinenNimiPage)
def read_muunkielinen_nimi_by_taksonin_nro(taksonin_nro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(MuunkielinenNimiModel).filter(MuunkielinenNimiModel.taksonin_nro == taksonin_nro), MuunkielinenNimiModel, request.query_params)
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

@router.get("/{taksonin_nro}/naytetieto", response_model=NaytetietoPage)
def read_naytetieto_by_taksonin_nro(taksonin_nro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(NaytetietoModel).filter(NaytetietoModel.taksonin_nro == taksonin_nro), NaytetietoModel, request.query_params)
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

@router.get("/{taksonin_nro}/suomalainen_kasvupaikka", response_model=SuomalainenKasvupaikkaPage)
def read_suomalainen_kasvupaikka_by_taksonin_nro(taksonin_nro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(SuomalainenKasvupaikkaModel).filter(SuomalainenKasvupaikkaModel.taksonin_nro == taksonin_nro), SuomalainenKasvupaikkaModel, request.query_params)
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

@router.get("/{taksonin_nro}/suomalainen_levinneisyysalue", response_model=SuomalainenLevinneisyysaluePage)
def read_suomalainen_levinneisyysalue_by_taksonin_nro(taksonin_nro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(SuomalainenLevinneisyysalueModel).filter(SuomalainenLevinneisyysalueModel.taksonin_nro == taksonin_nro), SuomalainenLevinneisyysalueModel, request.query_params)
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

@router.get("/{taksonin_nro}/suunniteltu_kasvupaikka", response_model=SuunniteltuKasvupaikkaPage)
def read_suunniteltu_kasvupaikka_by_taksonin_nro(taksonin_nro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(SuunniteltuKasvupaikkaModel).filter(SuunniteltuKasvupaikkaModel.taksonin_nro == taksonin_nro), SuunniteltuKasvupaikkaModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return SuunniteltuKasvupaikkaPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{taksonin_nro}/synonyymi", response_model=SynonyymiPage)
def read_synonyymi_by_taksonin_nro(taksonin_nro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(SynonyymiModel).filter(SynonyymiModel.taksonin_nro == taksonin_nro), SynonyymiModel, request.query_params)
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

@router.get("/{taksonin_nro}/taksonin_lappu", response_model=TaksoninLappuPage)
def read_taksonin_lappu_by_taksonin_nro(taksonin_nro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(TaksoninLappuModel).filter(TaksoninLappuModel.taksonin_nro == taksonin_nro), TaksoninLappuModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return TaksoninLappuPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{taksonin_nro}/taksonin_viljelytiedot", response_model=TaksoninViljelytiedotPage)
def read_taksonin_viljelytiedot_by_taksonin_nro(taksonin_nro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(TaksoninViljelytiedotModel).filter(TaksoninViljelytiedotModel.taksonin_nro == taksonin_nro), TaksoninViljelytiedotModel, request.query_params)
    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0
    return TaksoninViljelytiedotPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
    )

@router.get("/{taksonin_nro}/ymparistoindikaattoriluonne", response_model=YmparistoindikaattoriluonnePage)
def read_ymparistoindikaattoriluonne_by_taksonin_nro(taksonin_nro: int, request: Request, page: int = Query(1, ge=1), page_size: int = Query(200, ge=1), db: Session = Depends(get_db)):
    query = apply_filters(db.query(YmparistoindikaattoriluonneModel).filter(YmparistoindikaattoriluonneModel.taksonin_nro == taksonin_nro), YmparistoindikaattoriluonneModel, request.query_params)
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
