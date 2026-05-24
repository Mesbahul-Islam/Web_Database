from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class KasvinKayttotarkoitusBase(BaseModel):
    kayttonro: int
    taksonin_nro: int
    kayton_tunnus: Optional[str]
    kaytto: Optional[str]
    selite: Optional[str]
    viitenro: Optional[int]
    taksoni: Optional['Taksoni'] = None
    viite: Optional['Viite']

class KasvinKayttotarkoitusCreate(KasvinKayttotarkoitusBase):
    pass

class KasvinKayttotarkoitus(KasvinKayttotarkoitusBase):
    model_config = ConfigDict(from_attributes=True)
