from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class TaksoniBase(BaseModel):
    taksonin_nro: int
    tieteellinen_nimi: Optional[str] = None
    suku: Optional[str] = None
    suvun_auktori: Optional[str] = None
    laji: Optional[str] = None
    lajin_auktori: Optional[str] = None
    alataso_1: Optional[str] = None
    alatason_1_viite: Optional[int] = None
    alataso_2: Optional[str] = None
    alatason_2_auktori: Optional[str] = None
    alatason_1_auktori: Optional[str] = None
    alatason_2_viite: Optional[int] = None
    alataso_3: Optional[str] = None
    alatason_3_auktori: Optional[str] = None
    alatason_3_viite: Optional[int] = None
    alataso_4: Optional[str] = None
    alatason_4_auktori: Optional[str] = None
    alatason_4_viite: Optional[int] = None
    alataso_5: Optional[str] = None
    alatason_5_auktori: Optional[str] = None
    alatason_5_viite: Optional[int] = None
    risteymatiedot: Optional[str] = None
    risteymatietojen_auktori: Optional[str] = None
    viimeinen_paivityspvm: Optional[str] = None
    muita_tietoja: Optional[str] = None
    jarjestysnumero: Optional[int] = None
    viitenro: Optional[int] = None
    lajin_viite: Optional[str] = None
    lajin_viite2: Optional[str] = None
    yleis_viite: Optional[str] = None
    vap_yleis_viite: Optional[str] = None
    put: Optional[int] = None
    puttia: Optional[str] = None
    risteymaviite: Optional[str] = None

class TaksoniCreate(TaksoniBase):
    taksonin_nro: Optional[int] = None

class Taksoni(TaksoniBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)

class TaksoniPage(BaseModel):
    items: List[Taksoni]
    total: int
    page: int
    page_size: int
    pages: int


class TaksoninHankintatiedotYhteenveto(BaseModel):
    taksonin_nro: int
    tieteellinen_nimi: Optional[str] = None
    suku: Optional[str] = None
    laji: Optional[str] = None
    hankintanumerot: str
    hankinnat_lkm: int
    searchId: str

class TaksoninHankintatiedotYhteenvetoPage(BaseModel):
    items: List[TaksoninHankintatiedotYhteenveto]
    total: int
    page: int
    page_size: int
    pages: int

