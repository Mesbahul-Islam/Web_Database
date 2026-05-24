from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaLuonnonsuojeluarvoSuomessaBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class ListaLuonnonsuojeluarvoSuomessaCreate(ListaLuonnonsuojeluarvoSuomessaBase):
    pass

class ListaLuonnonsuojeluarvoSuomessa(ListaLuonnonsuojeluarvoSuomessaBase):
    model_config = ConfigDict(from_attributes=True)
