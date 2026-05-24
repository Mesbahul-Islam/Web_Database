from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class SuunniteltuKasvupaikkaBase(BaseModel):
    kasvupaikan_nro: int
    taksonin_nro: int
    osasto: Optional[str]
    sijoituspaikka: Optional[str]
    taksoni: Optional['Taksoni'] = None

class SuunniteltuKasvupaikkaCreate(SuunniteltuKasvupaikkaBase):
    pass

class SuunniteltuKasvupaikka(SuunniteltuKasvupaikkaBase):
    model_config = ConfigDict(from_attributes=True)
