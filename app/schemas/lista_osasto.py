from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ListaOsastoBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class ListaOsastoCreate(ListaOsastoBase):
    pass

class ListaOsasto(ListaOsastoBase):
    model_config = ConfigDict(from_attributes=True)
