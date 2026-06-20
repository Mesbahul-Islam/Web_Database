from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class AlkuperainenKasvupaikkaBase(BaseModel):
    alkuperaisen_kasvupaikan_nro: int
    taksonin_nro: int
    alkuperainen_kasvupaikka: Optional[str] = None
    kasvupaikan_tarkenne: Optional[str] = None
    viitenro: Optional[int] = None

class AlkuperainenKasvupaikkaCreate(AlkuperainenKasvupaikkaBase):
    alkuperaisen_kasvupaikan_nro: Optional[int] = None

class AlkuperainenKasvupaikka(AlkuperainenKasvupaikkaBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)

class AlkuperainenKasvupaikkaPage(BaseModel):
    items: List[AlkuperainenKasvupaikka]
    total: int
    page: int
    page_size: int
    pages: int  
