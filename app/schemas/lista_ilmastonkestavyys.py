from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaIlmastonkestavyysBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None

class ListaIlmastonkestavyysCreate(ListaIlmastonkestavyysBase):
    pass

class ListaIlmastonkestavyys(ListaIlmastonkestavyysBase):
    model_config = ConfigDict(from_attributes=True)

class ListaIlmastonkestavyysPage(BaseModel):
    items: List[ListaIlmastonkestavyys]
    total: int
    page: int
    page_size: int
    pages: int
