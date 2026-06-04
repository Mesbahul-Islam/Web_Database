from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class MaaritysmerkintaBase(BaseModel):
    maaritysnro: int
    maarityspvm: Optional[str]
    maarittaja: Optional[str]
    maaritystaso: Optional[str]
    huomautus: Optional[str]
    hankintaID: Optional[int]
    osasto: Optional[str]
    paikka: Optional[str]
    vanhataksoni: Optional[str]
    uusitaksoni: Optional[str]
    uus_maarityspvm: Optional[date]

class MaaritysmerkintaCreate(MaaritysmerkintaBase):
    pass

class Maaritysmerkinta(MaaritysmerkintaBase):
    model_config = ConfigDict(from_attributes=True)

class MaaritysmerkintaPage(BaseModel):
    items: List[Maaritysmerkinta]
    total: int
    page: int
    page_size: int
    pages: int
