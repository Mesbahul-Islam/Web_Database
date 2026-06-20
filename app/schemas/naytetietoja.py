from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class NaytetietojaBase(BaseModel):
    naytteen_nro: int
    naytteen_tyyppi: Optional[str] = None
    naytteen_sijainti: Optional[str] = None
    naytteen_tiedot: Optional[str] = None
    naytteen_keraaja: Optional[str] = None
    naytteen_paivays: Optional[str] = None
    hankintaID: Optional[int] = None
    sijainnin_selite: Optional[str] = None
    viitenro: Optional[int] = None
    viitteen_selite: Optional[str] = None
    uus_naytteen_paivays: Optional[date] = None

class NaytetietojaCreate(NaytetietojaBase):
    naytteen_nro: Optional[int] = None

class Naytetietoja(NaytetietojaBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)

class NaytetietojaPage(BaseModel):
    items: List[Naytetietoja]
    total: int
    page: int
    page_size: int
    pages: int
