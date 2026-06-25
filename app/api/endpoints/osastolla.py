from fastapi import APIRouter, Depends, Query, Request
from math import ceil
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, func
from typing import List, Optional
from pydantic import BaseModel

from app.database import get_db
from app.models.sijoituspaikka import Sijoituspaikka as SijoituspaikkaModel
from app.models.osastopaikka import Osastopaikka as OsastopaikkaModel
from app.models.hankintatiedot import Hankintatiedot as HankintatiedotModel
from app.models.taksoni import Taksoni as TaksoniModel

router = APIRouter()

class OsastollaItem(BaseModel):
    sijoituspaikan_nro: int
    hankintaID: Optional[int]
    hankintanumero: Optional[str]
    tieteellinen_nimi: Optional[str]
    auktori: Optional[str]
    sijoituspaikan_nimi: Optional[str]
    osaston_nimi: Optional[str]

    class Config:
        from_attributes = True

class OsastollaPage(BaseModel):
    items: List[OsastollaItem]
    total: int
    page: int
    page_size: int
    pages: int

@router.get("/", response_model=OsastollaPage)
def get_osastolla(
    request: Request,
    page: int = Query(1, ge=1),
    page_size: int = Query(25, ge=1),
    search: Optional[str] = None,
    sort_by: Optional[str] = "sijoituspaikan_nimi",
    db: Session = Depends(get_db),
):
    query = db.query(
        SijoituspaikkaModel.sijoituspaikan_nro,
        HankintatiedotModel.hankintaID,
        HankintatiedotModel.hankintanumero,
        TaksoniModel.tieteellinen_nimi,
        func.coalesce(
            func.nullif(TaksoniModel.alatason_5_auktori, ''),
            func.nullif(TaksoniModel.alatason_4_auktori, ''),
            func.nullif(TaksoniModel.alatason_3_auktori, ''),
            func.nullif(TaksoniModel.alatason_2_auktori, ''),
            func.nullif(TaksoniModel.alatason_1_auktori, ''),
            func.nullif(TaksoniModel.lajin_auktori, ''),
            func.nullif(TaksoniModel.suvun_auktori, '')
        ).label('auktori'),
        SijoituspaikkaModel.sijoituspaikan_nimi,
        OsastopaikkaModel.osaston_nimi
    ).join(
        OsastopaikkaModel, OsastopaikkaModel.osaston_numero == SijoituspaikkaModel.osaston_numero
    ).join(
        HankintatiedotModel, HankintatiedotModel.hankintaID == OsastopaikkaModel.hankintaID
    ).join(
        TaksoniModel, TaksoniModel.taksonin_nro == HankintatiedotModel.taksonin_nro
    ).filter(
        SijoituspaikkaModel.kasvin_status == "OSASTOLLA"
    )

    if search:
        search_term = f"%{search}%"
        author_coalesce = func.coalesce(
            func.nullif(TaksoniModel.alatason_5_auktori, ''),
            func.nullif(TaksoniModel.alatason_4_auktori, ''),
            func.nullif(TaksoniModel.alatason_3_auktori, ''),
            func.nullif(TaksoniModel.alatason_2_auktori, ''),
            func.nullif(TaksoniModel.alatason_1_auktori, ''),
            func.nullif(TaksoniModel.lajin_auktori, ''),
            func.nullif(TaksoniModel.suvun_auktori, '')
        )
        query = query.filter(
            or_(
                HankintatiedotModel.hankintanumero.ilike(search_term),
                SijoituspaikkaModel.sijoituspaikan_nimi.ilike(search_term),
                OsastopaikkaModel.osaston_nimi.ilike(search_term),
                TaksoniModel.tieteellinen_nimi.ilike(search_term),
                author_coalesce.ilike(search_term)
            )
        )

    if sort_by == "sijoituspaikan_nimi":
        query = query.order_by(SijoituspaikkaModel.sijoituspaikan_nimi.asc())
    elif sort_by == "-sijoituspaikan_nimi":
        query = query.order_by(SijoituspaikkaModel.sijoituspaikan_nimi.desc())
    elif sort_by == "hankintanumero":
        query = query.order_by(HankintatiedotModel.hankintanumero.asc())
    elif sort_by == "-hankintanumero":
        query = query.order_by(HankintatiedotModel.hankintanumero.desc())
    elif sort_by == "osaston_nimi":
        query = query.order_by(OsastopaikkaModel.osaston_nimi.asc())
    elif sort_by == "-osaston_nimi":
        query = query.order_by(OsastopaikkaModel.osaston_nimi.desc())
    elif sort_by == "tieteellinen_nimi":
        query = query.order_by(TaksoniModel.tieteellinen_nimi.asc())
    elif sort_by == "-tieteellinen_nimi":
        query = query.order_by(TaksoniModel.tieteellinen_nimi.desc())
    else:
        query = query.order_by(SijoituspaikkaModel.sijoituspaikan_nro.desc())

    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()
    pages = ceil(total / page_size) if total else 0

    result_items = [
        OsastollaItem(
            sijoituspaikan_nro=row.sijoituspaikan_nro,
            hankintaID=row.hankintaID,
            hankintanumero=row.hankintanumero,
            tieteellinen_nimi=row.tieteellinen_nimi,
            auktori=row.auktori,
            sijoituspaikan_nimi=row.sijoituspaikan_nimi,
            osaston_nimi=row.osaston_nimi
        )
        for row in items
    ]

    return OsastollaPage(
        items=result_items,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages
    )
