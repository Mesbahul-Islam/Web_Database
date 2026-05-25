from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class AlkuperainenKasvupaikkaBase(BaseModel):
    alkuperaisen_kasvupaikan_nro: int
    taksonin_nro: int
    alkuperainen_kasvupaikka: Optional[str]
    kasvupaikan_tarkenne: Optional[str]
    viitenro: Optional[int]

class AlkuperainenKasvupaikkaCreate(AlkuperainenKasvupaikkaBase):
    pass

class AlkuperainenKasvupaikka(AlkuperainenKasvupaikkaBase):
    model_config = ConfigDict(from_attributes=True)
