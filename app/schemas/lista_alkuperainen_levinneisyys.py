from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaAlkuperainenLevinneisyysBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None
    LYHENNE: Optional[str] = None
    NUMERO: Optional[str] = None

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
