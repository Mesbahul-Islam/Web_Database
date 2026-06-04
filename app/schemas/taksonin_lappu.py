from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class TaksoninLappuBase(BaseModel):
    Lappu_nro: int
    Lappu_teksti: Optional[str]
    taksonin_nro: Optional[int]

class TaksoninLappuCreate(TaksoninLappuBase):
    pass

class TaksoninLappu(TaksoninLappuBase):
    model_config = ConfigDict(from_attributes=True)

class TaksoninLappuPage(BaseModel):
    items: List[TaksoninLappu]
    total: int
    page: int
    page_size: int
    pages: int
