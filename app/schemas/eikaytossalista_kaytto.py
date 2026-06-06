from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class EikaytossalistaKayttoBase(BaseModel):
    id: int
    nimi: Optional[str] = None

class EikaytossalistaKayttoCreate(EikaytossalistaKayttoBase):
    pass

class EikaytossalistaKaytto(EikaytossalistaKayttoBase):
    model_config = ConfigDict(from_attributes=True)
