from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ViiteBase(BaseModel):
    viitenro: int
    viitteen_lyhenne: Optional[str] = None
    tekija: Optional[str] = None
    kirjan_nimi: Optional[str] = None
    kirja_selite: Optional[str] = None
    kustantaja: Optional[str] = None
    painos: Optional[str] = None
    vuosi: Optional[str] = None
    ISBN: Optional[str] = None
    sijainti: Optional[str] = None

class ViiteCreate(ViiteBase):
    pass

class Viite(ViiteBase):
    model_config = ConfigDict(from_attributes=True)

class ViitePage(BaseModel):
    items: List[Viite]
    total: int
    page: int
    page_size: int
    pages: int
