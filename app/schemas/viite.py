from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ViiteBase(BaseModel):
    viitenro: int
    viitteen_lyhenne: Optional[str]
    tekija: Optional[str]
    kirjan_nimi: Optional[str]
    kirja_selite: Optional[str]
    kustantaja: Optional[str]
    painos: Optional[str]
    vuosi: Optional[str]
    ISBN: Optional[str]
    sijainti: Optional[str]

class ViiteCreate(ViiteBase):
    pass

class Viite(ViiteBase):
    model_config = ConfigDict(from_attributes=True)
