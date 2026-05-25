from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class KoristekayttoBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]
    NUMERO: Optional[str]

class KoristekayttoCreate(KoristekayttoBase):
    pass

class Koristekaytto(KoristekayttoBase):
    model_config = ConfigDict(from_attributes=True)
