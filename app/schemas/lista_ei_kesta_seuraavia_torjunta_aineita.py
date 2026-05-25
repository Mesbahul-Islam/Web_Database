from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ListaEiKestaSeuraaviaTorjuntaAineitaBase(BaseModel):
    id: int
    koodi: Optional[str]
    nimi: Optional[str]

class ListaEiKestaSeuraaviaTorjuntaAineitaCreate(ListaEiKestaSeuraaviaTorjuntaAineitaBase):
    pass

class ListaEiKestaSeuraaviaTorjuntaAineita(ListaEiKestaSeuraaviaTorjuntaAineitaBase):
    model_config = ConfigDict(from_attributes=True)
