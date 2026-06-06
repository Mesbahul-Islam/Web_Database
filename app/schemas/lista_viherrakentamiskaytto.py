from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaViherrakentamiskayttoBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None

class ListaViherrakentamiskayttoCreate(ListaViherrakentamiskayttoBase):
    pass

class ListaViherrakentamiskaytto(ListaViherrakentamiskayttoBase):
    model_config = ConfigDict(from_attributes=True)

class ListaViherrakentamiskayttoPage(BaseModel):
    items: List[ListaViherrakentamiskaytto]
    total: int
    page: int
    page_size: int
    pages: int
