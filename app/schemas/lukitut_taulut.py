from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class LukitutTaulutBase(BaseModel):
    kayttajan_tunnus: str
    taulun_nimi: Optional[str] = None
    avainkentta: Optional[str] = None

class LukitutTaulutCreate(LukitutTaulutBase):
    pass

class LukitutTaulut(LukitutTaulutBase):
    model_config = ConfigDict(from_attributes=True)

class LukitutTaulutPage(BaseModel):
    items: List[LukitutTaulut]
    total: int
    page: int
    page_size: int
    pages: int
