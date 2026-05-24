from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaLuonnonsuojeluarvoMuuallaBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class ListaLuonnonsuojeluarvoMuuallaCreate(ListaLuonnonsuojeluarvoMuuallaBase):
    pass

class ListaLuonnonsuojeluarvoMuualla(ListaLuonnonsuojeluarvoMuuallaBase):
    model_config = ConfigDict(from_attributes=True)
