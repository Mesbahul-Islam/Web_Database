from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaRauhoituksetBase(BaseModel):
    id: int
    nimi: Optional[str]

class ListaRauhoituksetCreate(ListaRauhoituksetBase):
    pass

class ListaRauhoitukset(ListaRauhoituksetBase):
    model_config = ConfigDict(from_attributes=True)

class ListaRauhoituksetPage(BaseModel):
    items: List[ListaRauhoitukset]
    total: int
    page: int
    page_size: int
    pages: int
