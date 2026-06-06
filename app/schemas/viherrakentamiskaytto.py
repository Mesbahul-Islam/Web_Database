from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ViherrakentamiskayttoBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None

class ViherrakentamiskayttoCreate(ViherrakentamiskayttoBase):
    pass

class Viherrakentamiskaytto(ViherrakentamiskayttoBase):
    model_config = ConfigDict(from_attributes=True)
