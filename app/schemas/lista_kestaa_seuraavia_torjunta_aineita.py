from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaKestaaSeuraaviaTorjuntaAineitaBase(BaseModel):
    id: int
    koodi: Optional[str] = None
    nimi: Optional[str] = None

class ListaKestaaSeuraaviaTorjuntaAineitaCreate(ListaKestaaSeuraaviaTorjuntaAineitaBase):
    pass

class ListaKestaaSeuraaviaTorjuntaAineita(ListaKestaaSeuraaviaTorjuntaAineitaBase):
    model_config = ConfigDict(from_attributes=True)

class ListaKestaaSeuraaviaTorjuntaAineitaPage(BaseModel):
    items: List[ListaKestaaSeuraaviaTorjuntaAineita]
    total: int
    page: int
    page_size: int
    pages: int
