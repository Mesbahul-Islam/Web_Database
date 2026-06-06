from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaHakuBase(BaseModel):
    id: int
    nimi: Optional[str] = None

class ListaHakuCreate(ListaHakuBase):
    pass

class ListaHaku(ListaHakuBase):
    model_config = ConfigDict(from_attributes=True)

class ListaHakuPage(BaseModel):
    items: List[ListaHaku]
    total: int
    page: int
    page_size: int
    pages: int
