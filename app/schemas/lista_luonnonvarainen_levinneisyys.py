from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaLuonnonvarainenLevinneisyysBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None
    LYHENNE: Optional[str] = None
    NUMEROKOODI: Optional[str] = None
    NUMERO: Optional[str] = None

class ListaLuonnonvarainenLevinneisyysCreate(ListaLuonnonvarainenLevinneisyysBase):
    pass

class ListaLuonnonvarainenLevinneisyys(ListaLuonnonvarainenLevinneisyysBase):
    model_config = ConfigDict(from_attributes=True)

class ListaLuonnonvarainenLevinneisyysPage(BaseModel):
    items: List[ListaLuonnonvarainenLevinneisyys]
    total: int
    page: int
    page_size: int
    pages: int
