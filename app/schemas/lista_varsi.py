from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaVarsiBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class ListaVarsiCreate(ListaVarsiBase):
    pass

class ListaVarsi(ListaVarsiBase):
    model_config = ConfigDict(from_attributes=True)

class ListaVarsiPage(BaseModel):
    items: List[ListaVarsi]
    total: int
    page: int
    page_size: int
    pages: int
