from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaHyotykayttoBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]
    NUMERO: Optional[str]

class ListaHyotykayttoCreate(ListaHyotykayttoBase):
    pass

class ListaHyotykaytto(ListaHyotykayttoBase):
    model_config = ConfigDict(from_attributes=True)

class ListaHyotykayttoPage(BaseModel):
    items: List[ListaHyotykaytto]
    total: int
    page: int
    page_size: int
    pages: int
