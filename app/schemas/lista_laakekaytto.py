from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaLaakekayttoBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None

class ListaLaakekayttoCreate(ListaLaakekayttoBase):
    pass

class ListaLaakekaytto(ListaLaakekayttoBase):
    model_config = ConfigDict(from_attributes=True)

class ListaLaakekayttoPage(BaseModel):
    items: List[ListaLaakekaytto]
    total: int
    page: int
    page_size: int
    pages: int
