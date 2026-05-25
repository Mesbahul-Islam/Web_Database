from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class SuunniteltuKasvupaikkaBase(BaseModel):
    kasvupaikan_nro: int
    taksonin_nro: int
    osasto: Optional[str]
    sijoituspaikka: Optional[str]

class SuunniteltuKasvupaikkaCreate(SuunniteltuKasvupaikkaBase):
    pass

class SuunniteltuKasvupaikka(SuunniteltuKasvupaikkaBase):
    model_config = ConfigDict(from_attributes=True)
