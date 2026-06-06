from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaLuonnonsuojeluarvoSuomessaBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None

class ListaLuonnonsuojeluarvoSuomessaCreate(ListaLuonnonsuojeluarvoSuomessaBase):
    pass

class ListaLuonnonsuojeluarvoSuomessa(ListaLuonnonsuojeluarvoSuomessaBase):
    model_config = ConfigDict(from_attributes=True)

class ListaLuonnonsuojeluarvoSuomessaPage(BaseModel):
    items: List[ListaLuonnonsuojeluarvoSuomessa]
    total: int
    page: int
    page_size: int
    pages: int
