from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaPolytystapaBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None
    NUMERO: Optional[str] = None

class ListaPolytystapaCreate(ListaPolytystapaBase):
    pass

class ListaPolytystapa(ListaPolytystapaBase):
    model_config = ConfigDict(from_attributes=True)

class ListaPolytystapaPage(BaseModel):
    items: List[ListaPolytystapa]
    total: int
    page: int
    page_size: int
    pages: int
