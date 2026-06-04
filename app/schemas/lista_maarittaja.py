from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaMaarittajaBase(BaseModel):
    id: int
    nimi: Optional[str]

class ListaMaarittajaCreate(ListaMaarittajaBase):
    pass

class ListaMaarittaja(ListaMaarittajaBase):
    model_config = ConfigDict(from_attributes=True)

class ListaMaarittajaPage(BaseModel):
    items: List[ListaMaarittaja]
    total: int
    page: int
    page_size: int
    pages: int
