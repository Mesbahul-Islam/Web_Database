from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class EikaytossalistaLahettajaBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class EikaytossalistaLahettajaCreate(EikaytossalistaLahettajaBase):
    pass

class EikaytossalistaLahettaja(EikaytossalistaLahettajaBase):
    model_config = ConfigDict(from_attributes=True)
