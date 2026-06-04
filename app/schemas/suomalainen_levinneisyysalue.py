from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class SuomalainenLevinneisyysalueBase(BaseModel):
    levinneisyysalueen_nro: int
    taksonin_nro: int
    levinneisyysalue: Optional[str]
    levinneisyysalueen_tarkenne: Optional[str]
    alkuperainen_vai_tulokas: Optional[str]
    viitenro: Optional[int]

class SuomalainenLevinneisyysalueCreate(SuomalainenLevinneisyysalueBase):
    pass

class SuomalainenLevinneisyysalue(SuomalainenLevinneisyysalueBase):
    model_config = ConfigDict(from_attributes=True)

class SuomalainenLevinneisyysaluePage(BaseModel):
    items: List[SuomalainenLevinneisyysalue]
    total: int
    page: int
    page_size: int
    pages: int
