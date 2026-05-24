from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaHyotykayttoBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]
    NUMERO: Optional[str]

class ListaHyotykayttoCreate(ListaHyotykayttoBase):
    pass

class ListaHyotykaytto(ListaHyotykayttoBase):
    model_config = ConfigDict(from_attributes=True)
