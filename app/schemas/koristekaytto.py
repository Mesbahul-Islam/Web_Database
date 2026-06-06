from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class KoristekayttoBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None
    NUMERO: Optional[str] = None

class KoristekayttoCreate(KoristekayttoBase):
    pass

class Koristekaytto(KoristekayttoBase):
    model_config = ConfigDict(from_attributes=True)
