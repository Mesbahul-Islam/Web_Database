from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaKasvinsaapuminenBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class ListaKasvinsaapuminenCreate(ListaKasvinsaapuminenBase):
    pass

class ListaKasvinsaapuminen(ListaKasvinsaapuminenBase):
    model_config = ConfigDict(from_attributes=True)

class ListaKasvinsaapuminenPage(BaseModel):
    items: List[ListaKasvinsaapuminen]
    total: int
    page: int
    page_size: int
    pages: int
