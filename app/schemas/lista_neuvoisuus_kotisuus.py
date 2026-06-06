from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaNeuvoisuusKotisuusBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None

class ListaNeuvoisuusKotisuusCreate(ListaNeuvoisuusKotisuusBase):
    pass

class ListaNeuvoisuusKotisuus(ListaNeuvoisuusKotisuusBase):
    model_config = ConfigDict(from_attributes=True)

class ListaNeuvoisuusKotisuusPage(BaseModel):
    items: List[ListaNeuvoisuusKotisuus]
    total: int
    page: int
    page_size: int
    pages: int
