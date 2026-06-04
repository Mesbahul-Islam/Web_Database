from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class MaailmanLevinneisyysalueBase(BaseModel):
    levinneisyysalueen_nro: int
    taksonin_nro: int
    levinneisyysalue: Optional[str]
    levinneisyysalueen_tarkenne: Optional[str]
    alkuperainen_vai_tulokas: Optional[str]
    viitenro: Optional[int]
    lisatietoja: Optional[str]

class MaailmanLevinneisyysalueCreate(MaailmanLevinneisyysalueBase):
    pass

class MaailmanLevinneisyysalue(MaailmanLevinneisyysalueBase):
    model_config = ConfigDict(from_attributes=True)

class MaailmanLevinneisyysaluePage(BaseModel):
    items: List[MaailmanLevinneisyysalue]
    total: int
    page: int
    page_size: int
    pages: int
