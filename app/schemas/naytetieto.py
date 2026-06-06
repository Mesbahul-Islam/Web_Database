from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class NaytetietoBase(BaseModel):
    naytteen_nro: int
    taksonin_nro: int
    tyyppi: Optional[str] = None
    sijainti: Optional[str] = None
    tiedot: Optional[str] = None
    keraaja: Optional[str] = None
    paivays: Optional[str] = None
    viitenro: Optional[int] = None
    sijainnin_selite: Optional[str] = None
    viitteen_selite: Optional[str] = None

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
