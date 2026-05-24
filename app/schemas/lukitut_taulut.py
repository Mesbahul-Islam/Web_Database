from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class LukitutTaulutBase(BaseModel):
    kayttajan_tunnus: str
    taulun_nimi: Optional[str]
    avainkentta: Optional[str]

class LukitutTaulutCreate(LukitutTaulutBase):
    pass

class LukitutTaulut(LukitutTaulutBase):
    model_config = ConfigDict(from_attributes=True)
