from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class MuunkielinenNimiBase(BaseModel):
    nimen_nro: int
    taksonin_nro: int
    nimi: Optional[str]
    kieli: Optional[str]
    viitenro: Optional[int]
    viite_2: Optional[int]

class MuunkielinenNimiCreate(MuunkielinenNimiBase):
    pass

class MuunkielinenNimi(MuunkielinenNimiBase):
    model_config = ConfigDict(from_attributes=True)

class MuunkielinenNimiPage(BaseModel):
    items: List[MuunkielinenNimi]
    total: int
    page: int
    page_size: int
    pages: int
