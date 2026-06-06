from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaNaytteentyyppiBase(BaseModel):
    id: int
    nimi: Optional[str] = None
    koodi: Optional[str] = None

class ListaNaytteentyyppiCreate(ListaNaytteentyyppiBase):
    pass

class ListaNaytteentyyppi(ListaNaytteentyyppiBase):
    model_config = ConfigDict(from_attributes=True)

class ListaNaytteentyyppiPage(BaseModel):
    items: List[ListaNaytteentyyppi]
    total: int
    page: int
    page_size: int
    pages: int
