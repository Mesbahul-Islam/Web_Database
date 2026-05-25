from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ListaKestaaSeuraaviaTorjuntaAineitaBase(BaseModel):
    id: int
    koodi: Optional[str]
    nimi: Optional[str]

class ListaKestaaSeuraaviaTorjuntaAineitaCreate(ListaKestaaSeuraaviaTorjuntaAineitaBase):
    pass

class ListaKestaaSeuraaviaTorjuntaAineita(ListaKestaaSeuraaviaTorjuntaAineitaBase):
    model_config = ConfigDict(from_attributes=True)
