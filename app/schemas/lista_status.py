from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaStatusBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None

class ListaStatusCreate(ListaStatusBase):
    pass

class ListaStatus(ListaStatusBase):
    model_config = ConfigDict(from_attributes=True)

class ListaStatusPage(BaseModel):
    items: List[ListaStatus]
    total: int
    page: int
    page_size: int
    pages: int
