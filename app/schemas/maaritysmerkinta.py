from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class MaaritysmerkintaBase(BaseModel):
    maaritysnro: int
    maarityspvm: Optional[str] = None
    maarittaja: Optional[str] = None
    maaritystaso: Optional[str] = None
    huomautus: Optional[str] = None
    hankintaID: Optional[int] = None
    osasto: Optional[str] = None
    paikka: Optional[str] = None
    vanhataksoni: Optional[str] = None
    uusitaksoni: Optional[str] = None
    uus_maarityspvm: Optional[date] = None

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
