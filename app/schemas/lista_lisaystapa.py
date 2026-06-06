from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaLisaystapaBase(BaseModel):
    id: int
    koodi: Optional[str] = None
    nimi: Optional[str] = None

class ListaLisaystapaCreate(ListaLisaystapaBase):
    pass

class ListaLisaystapa(ListaLisaystapaBase):
    model_config = ConfigDict(from_attributes=True)

class ListaLisaystapaPage(BaseModel):
    items: List[ListaLisaystapa]
    total: int
    page: int
    page_size: int
    pages: int
