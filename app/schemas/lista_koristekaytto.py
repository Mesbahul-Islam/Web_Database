from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaKoristekayttoBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None
    NUMERO: Optional[str] = None

class ListaKoristekayttoCreate(ListaKoristekayttoBase):
    pass

class ListaKoristekaytto(ListaKoristekayttoBase):
    model_config = ConfigDict(from_attributes=True)

class ListaKoristekayttoPage(BaseModel):
    items: List[ListaKoristekaytto]
    total: int
    page: int
    page_size: int
    pages: int
