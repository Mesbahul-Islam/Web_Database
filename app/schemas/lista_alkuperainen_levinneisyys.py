from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaAlkuperainenLevinneisyysBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]
    LYHENNE: Optional[str]
    NUMERO: Optional[str]

class ListaAlkuperainenLevinneisyysCreate(ListaAlkuperainenLevinneisyysBase):
    pass

class ListaAlkuperainenLevinneisyys(ListaAlkuperainenLevinneisyysBase):
    model_config = ConfigDict(from_attributes=True)
