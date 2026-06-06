from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaOsastoBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None

class ListaOsastoCreate(ListaOsastoBase):
    pass

class ListaOsasto(ListaOsastoBase):
    model_config = ConfigDict(from_attributes=True)

class ListaOsastoPage(BaseModel):
    items: List[ListaOsasto]
    total: int
    page: int
    page_size: int
    pages: int
