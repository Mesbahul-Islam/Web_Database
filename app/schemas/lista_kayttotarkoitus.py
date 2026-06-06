from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaKayttotarkoitusBase(BaseModel):
    id: int
    nimi: Optional[str] = None

class ListaKayttotarkoitusCreate(ListaKayttotarkoitusBase):
    pass

class ListaKayttotarkoitus(ListaKayttotarkoitusBase):
    model_config = ConfigDict(from_attributes=True)

class ListaKayttotarkoitusPage(BaseModel):
    items: List[ListaKayttotarkoitus]
    total: int
    page: int
    page_size: int
    pages: int
