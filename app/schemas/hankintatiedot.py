from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class HankintatiedotBase(BaseModel):
    hankintaID: int
    taksonin_nro: int
    lahettajanro: int
    hankintanumero: Optional[str] = None
    saapumispvm: Optional[str] = None
    hankintanimi: Optional[str] = None
    millaisena_saatu: Optional[str] = None
    erikoiskokoelma_oma_puutarha: Optional[str] = None
    materiaalin_arvo: Optional[str] = None
    lisatiedot: Optional[str] = None
    jarjestysnro: Optional[str] = None
    vuosi: Optional[str] = None
    lisaysPVM: Optional[str] = None
    lisayshistoria: Optional[str] = None
    kasvin_huomautuksia: Optional[str] = None
    hankintahistoria: Optional[str] = None
    put: Optional[int] = None
    puttia: Optional[str] = None
    numero: Optional[int] = None
    vuosiluku: Optional[int] = None
    heimo: Optional[str] = None

class HankintatiedotCreate(HankintatiedotBase):
    pass

class Hankintatiedot(HankintatiedotBase):
    model_config = ConfigDict(from_attributes=True)

class HankintatiedotPage(BaseModel):
    items: List[Hankintatiedot]
    total: int
    page: int
    page_size: int
    pages: int
