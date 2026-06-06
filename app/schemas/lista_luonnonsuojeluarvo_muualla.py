from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaLuonnonsuojeluarvoMuuallaBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None

class ListaLuonnonsuojeluarvoMuuallaCreate(ListaLuonnonsuojeluarvoMuuallaBase):
    pass

class ListaLuonnonsuojeluarvoMuualla(ListaLuonnonsuojeluarvoMuuallaBase):
    model_config = ConfigDict(from_attributes=True)

class ListaLuonnonsuojeluarvoMuuallaPage(BaseModel):
    items: List[ListaLuonnonsuojeluarvoMuualla]
    total: int
    page: int
    page_size: int
    pages: int
