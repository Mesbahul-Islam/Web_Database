from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaEiKestaSeuraaviaTorjuntaAineitaBase(BaseModel):
    id: int
    koodi: Optional[str]
    nimi: Optional[str]

class ListaEiKestaSeuraaviaTorjuntaAineitaCreate(ListaEiKestaSeuraaviaTorjuntaAineitaBase):
    pass

class ListaEiKestaSeuraaviaTorjuntaAineita(ListaEiKestaSeuraaviaTorjuntaAineitaBase):
    model_config = ConfigDict(from_attributes=True)

class ListaEiKestaSeuraaviaTorjuntaAineitaPage(BaseModel):
    items: List[ListaEiKestaSeuraaviaTorjuntaAineita]
    total: int
    page: int
    page_size: int
    pages: int
