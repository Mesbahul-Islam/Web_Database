from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class EikaytossalistaViljelykasvitBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class EikaytossalistaViljelykasvitCreate(EikaytossalistaViljelykasvitBase):
    pass

class EikaytossalistaViljelykasvit(EikaytossalistaViljelykasvitBase):
    model_config = ConfigDict(from_attributes=True)
