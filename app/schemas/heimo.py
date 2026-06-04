from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class HeimoBase(BaseModel):
    jarjestysnumero: int
    nimi: Optional[str]
    synonyymi: Optional[str]
    numero: Optional[str]
    lahko: Optional[str]
    lahkonnumero: Optional[str]
    alaluokka: Optional[str]
    alaluokannumero: Optional[str]
    luokka: Optional[str]
    luokannumero: Optional[str]
    paaryhma: Optional[str]
    paaryhmannumero: Optional[str]
    suom_nimi: Optional[str]

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
