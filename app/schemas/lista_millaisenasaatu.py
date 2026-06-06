from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaMillaisenasaatuBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None

class ListaMillaisenasaatuCreate(ListaMillaisenasaatuBase):
    pass

class ListaMillaisenasaatu(ListaMillaisenasaatuBase):
    model_config = ConfigDict(from_attributes=True)

class ListaMillaisenasaatuPage(BaseModel):
    items: List[ListaMillaisenasaatu]
    total: int
    page: int
    page_size: int
    pages: int
