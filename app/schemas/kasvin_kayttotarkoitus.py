from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class KasvinKayttotarkoitusBase(BaseModel):
    kayttonro: int
    taksonin_nro: int
    kayton_tunnus: Optional[str] = None
    kaytto: Optional[str] = None
    selite: Optional[str] = None
    viitenro: Optional[int] = None

class KasvinKayttotarkoitusCreate(KasvinKayttotarkoitusBase):
    pass

class KasvinKayttotarkoitus(KasvinKayttotarkoitusBase):
    model_config = ConfigDict(from_attributes=True)

class KasvinKayttotarkoitusPage(BaseModel):
    items: List[KasvinKayttotarkoitus]
    total: int
    page: int
    page_size: int
    pages: int
