from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class SuunniteltuKasvupaikkaBase(BaseModel):
    kasvupaikan_nro: int
    taksonin_nro: int
    osasto: Optional[str] = None
    sijoituspaikka: Optional[str] = None

class SuunniteltuKasvupaikkaCreate(SuunniteltuKasvupaikkaBase):
    kasvupaikan_nro: Optional[int] = None

class SuunniteltuKasvupaikka(SuunniteltuKasvupaikkaBase):
    model_config = ConfigDict(from_attributes=True)

class SuunniteltuKasvupaikkaPage(BaseModel):
    items: List[SuunniteltuKasvupaikka]
    total: int
    page: int
    page_size: int
    pages: int
