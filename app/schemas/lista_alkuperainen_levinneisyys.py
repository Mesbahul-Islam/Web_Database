from pydantic import BaseModel, ConfigDict
from typing import List, Optional
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

class ListaAlkuperainenLevinneisyysPage(BaseModel):
    items: List[ListaAlkuperainenLevinneisyys]
    total: int
    page: int
    page_size: int
    pages: int
