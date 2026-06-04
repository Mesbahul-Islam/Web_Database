from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaKasvumuotoBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]
    NUMERO: Optional[str]

class ListaKasvumuotoCreate(ListaKasvumuotoBase):
    pass

class ListaKasvumuoto(ListaKasvumuotoBase):
    model_config = ConfigDict(from_attributes=True)

class ListaKasvumuotoPage(BaseModel):
    items: List[ListaKasvumuoto]
    total: int
    page: int
    page_size: int
    pages: int
