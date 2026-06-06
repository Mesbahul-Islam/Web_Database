from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaMaaritysmerkintaBase(BaseModel):
    id: int
    nimi: Optional[str] = None

class ListaMaaritysmerkintaCreate(ListaMaaritysmerkintaBase):
    pass

class ListaMaaritysmerkinta(ListaMaaritysmerkintaBase):
    model_config = ConfigDict(from_attributes=True)

class ListaMaaritysmerkintaPage(BaseModel):
    items: List[ListaMaaritysmerkinta]
    total: int
    page: int
    page_size: int
    pages: int
