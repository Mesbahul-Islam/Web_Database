from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ListaPolytystapaBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]
    NUMERO: Optional[str]

class ListaPolytystapaCreate(ListaPolytystapaBase):
    pass

class ListaPolytystapa(ListaPolytystapaBase):
    model_config = ConfigDict(from_attributes=True)
