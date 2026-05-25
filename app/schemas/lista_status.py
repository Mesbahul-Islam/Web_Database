from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ListaStatusBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class ListaStatusCreate(ListaStatusBase):
    pass

class ListaStatus(ListaStatusBase):
    model_config = ConfigDict(from_attributes=True)
