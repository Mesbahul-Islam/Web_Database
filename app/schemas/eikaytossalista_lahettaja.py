from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class EikaytossalistaLahettajaBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None

class EikaytossalistaLahettajaCreate(EikaytossalistaLahettajaBase):
    pass

class EikaytossalistaLahettaja(EikaytossalistaLahettajaBase):
    model_config = ConfigDict(from_attributes=True)
