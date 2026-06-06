from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaNaytteensijaintiBase(BaseModel):
    id: int
    koodi: Optional[str] = None
    nimi: Optional[str] = None

class ListaNaytteensijaintiCreate(ListaNaytteensijaintiBase):
    pass

class ListaNaytteensijainti(ListaNaytteensijaintiBase):
    model_config = ConfigDict(from_attributes=True)

class ListaNaytteensijaintiPage(BaseModel):
    items: List[ListaNaytteensijainti]
    total: int
    page: int
    page_size: int
    pages: int
