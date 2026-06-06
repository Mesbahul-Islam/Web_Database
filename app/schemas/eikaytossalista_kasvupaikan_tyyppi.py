from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class EikaytossalistaKasvupaikanTyyppiBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None
    NUMERO: Optional[str] = None

class EikaytossalistaKasvupaikanTyyppiCreate(EikaytossalistaKasvupaikanTyyppiBase):
    pass

class EikaytossalistaKasvupaikanTyyppi(EikaytossalistaKasvupaikanTyyppiBase):
    model_config = ConfigDict(from_attributes=True)
