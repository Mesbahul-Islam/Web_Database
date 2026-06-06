from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaHyotykayttoBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None
    NUMERO: Optional[str] = None

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
