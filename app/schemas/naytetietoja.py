from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class NaytetietojaBase(BaseModel):
    naytteen_nro: int
    naytteen_tyyppi: Optional[str]
    naytteen_sijainti: Optional[str]
    naytteen_tiedot: Optional[str]
    naytteen_keraaja: Optional[str]
    naytteen_paivays: Optional[str]
    hankintaID: Optional[int]
    sijainnin_selite: Optional[str]
    viitenro: Optional[int]
    viitteen_selite: Optional[str]
    uus_naytteen_paivays: Optional[date]
    hankintatiedot: Optional['Hankintatiedot']

class NaytetietojaCreate(NaytetietojaBase):
    pass

class Naytetietoja(NaytetietojaBase):
    model_config = ConfigDict(from_attributes=True)
