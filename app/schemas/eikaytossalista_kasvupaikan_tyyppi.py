from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class EikaytossalistaKasvupaikanTyyppiBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]
    NUMERO: Optional[str]

class EikaytossalistaKasvupaikanTyyppiCreate(EikaytossalistaKasvupaikanTyyppiBase):
    pass

class EikaytossalistaKasvupaikanTyyppi(EikaytossalistaKasvupaikanTyyppiBase):
    model_config = ConfigDict(from_attributes=True)
