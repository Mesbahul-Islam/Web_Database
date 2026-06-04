from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class NaytetietoBase(BaseModel):
    naytteen_nro: int
    taksonin_nro: int
    tyyppi: Optional[str]
    sijainti: Optional[str]
    tiedot: Optional[str]
    keraaja: Optional[str]
    paivays: Optional[str]
    viitenro: Optional[int]
    sijainnin_selite: Optional[str]
    viitteen_selite: Optional[str]

class NaytetietoCreate(NaytetietoBase):
    pass

class Naytetieto(NaytetietoBase):
    model_config = ConfigDict(from_attributes=True)

class NaytetietoPage(BaseModel):
    items: List[Naytetieto]
    total: int
    page: int
    page_size: int
    pages: int
