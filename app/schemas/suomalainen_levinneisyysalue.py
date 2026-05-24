from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class SuomalainenLevinneisyysalueBase(BaseModel):
    levinneisyysalueen_nro: int
    taksonin_nro: int
    levinneisyysalue: Optional[str]
    levinneisyysalueen_tarkenne: Optional[str]
    alkuperainen_vai_tulokas: Optional[str]
    viitenro: Optional[int]
    taksoni: Optional['Taksoni'] = None
    viite: Optional['Viite']

class SuomalainenLevinneisyysalueCreate(SuomalainenLevinneisyysalueBase):
    pass

class SuomalainenLevinneisyysalue(SuomalainenLevinneisyysalueBase):
    model_config = ConfigDict(from_attributes=True)
