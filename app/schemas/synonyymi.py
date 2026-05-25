from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class SynonyymiBase(BaseModel):
    synonyymin_nro: int
    taksonin_nro: int
    nimi: Optional[str]
    auktori: Optional[str]
    viitenro: Optional[int]
    viite_2: Optional[int]

class SynonyymiCreate(SynonyymiBase):
    pass

class Synonyymi(SynonyymiBase):
    model_config = ConfigDict(from_attributes=True)
