from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaTarkastajaBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None

class ListaTarkastajaCreate(ListaTarkastajaBase):
    pass

class ListaTarkastaja(ListaTarkastajaBase):
    model_config = ConfigDict(from_attributes=True)

class ListaTarkastajaPage(BaseModel):
    items: List[ListaTarkastaja]
    total: int
    page: int
    page_size: int
    pages: int
