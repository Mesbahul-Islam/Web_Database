from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class AlkuperainenKasvupaikkaBase(BaseModel):
    alkuperaisen_kasvupaikan_nro: int
    taksonin_nro: int
    alkuperainen_kasvupaikka: Optional[str]
    kasvupaikan_tarkenne: Optional[str]
    viitenro: Optional[int]
    taksoni: Optional['Taksoni'] = None
    viite: Optional['Viite']

class AlkuperainenKasvupaikkaCreate(AlkuperainenKasvupaikkaBase):
    pass

class AlkuperainenKasvupaikka(AlkuperainenKasvupaikkaBase):
    model_config = ConfigDict(from_attributes=True)
