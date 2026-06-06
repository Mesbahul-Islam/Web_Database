from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class SuomalainenKasvupaikkaBase(BaseModel):
    suomalaisen_kasvupaikan_nro: int
    taksonin_nro: int
    kasvupaikka: Optional[str] = None
    kasvupaikan_tyyppi: Optional[str] = None
    viitenro: Optional[int] = None

class SuomalainenKasvupaikkaCreate(SuomalainenKasvupaikkaBase):
    pass

class SuomalainenKasvupaikka(SuomalainenKasvupaikkaBase):
    model_config = ConfigDict(from_attributes=True)

class SuomalainenKasvupaikkaPage(BaseModel):
    items: List[SuomalainenKasvupaikka]
    total: int
    page: int
    page_size: int
    pages: int
