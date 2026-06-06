from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class HeimoBase(BaseModel):
    jarjestysnumero: int
    nimi: Optional[str] = None
    synonyymi: Optional[str] = None
    numero: Optional[str] = None
    lahko: Optional[str] = None
    lahkonnumero: Optional[str] = None
    alaluokka: Optional[str] = None
    alaluokannumero: Optional[str] = None
    luokka: Optional[str] = None
    luokannumero: Optional[str] = None
    paaryhma: Optional[str] = None
    paaryhmannumero: Optional[str] = None
    suom_nimi: Optional[str] = None

class HeimoCreate(HeimoBase):
    pass

class Heimo(HeimoBase):
    model_config = ConfigDict(from_attributes=True)

class HeimoPage(BaseModel):
    items: List[Heimo]
    total: int
    page: int
    page_size: int
    pages: int
