from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class SuomalainenKasvupaikkaBase(BaseModel):
    suomalaisen_kasvupaikan_nro: int
    taksonin_nro: int
    kasvupaikka: Optional[str]
    kasvupaikan_tyyppi: Optional[str]
    viitenro: Optional[int]

class SuomalainenKasvupaikkaCreate(SuomalainenKasvupaikkaBase):
    pass

class SuomalainenKasvupaikka(SuomalainenKasvupaikkaBase):
    model_config = ConfigDict(from_attributes=True)
