from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class HankintatiedotBase(BaseModel):
    hankintaID: int
    taksonin_nro: int
    lahettajanro: int
    hankintanumero: Optional[str]
    saapumispvm: Optional[str]
    hankintanimi: Optional[str]
    millaisena_saatu: Optional[str]
    erikoiskokoelma_oma_puutarha: Optional[str]
    materiaalin_arvo: Optional[str]
    lisatiedot: Optional[str]
    jarjestysnro: Optional[str]
    vuosi: Optional[str]
    lisaysPVM: Optional[str]
    lisayshistoria: Optional[str]
    kasvin_huomautuksia: Optional[str]
    hankintahistoria: Optional[str]
    put: Optional[int]
    puttia: Optional[str]
    numero: Optional[int]
    vuosiluku: Optional[int]
    heimo: Optional[str]

class HankintatiedotCreate(HankintatiedotBase):
    pass

class Hankintatiedot(HankintatiedotBase):
    model_config = ConfigDict(from_attributes=True)
