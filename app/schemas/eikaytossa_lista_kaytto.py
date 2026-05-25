from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class EikaytossaListaKayttoBase(BaseModel):
    id: int
    nimi: Optional[str]

class EikaytossaListaKayttoCreate(EikaytossaListaKayttoBase):
    pass

class EikaytossaListaKaytto(EikaytossaListaKayttoBase):
    model_config = ConfigDict(from_attributes=True)
