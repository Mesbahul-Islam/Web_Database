from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ViherrakentamiskayttoBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class ViherrakentamiskayttoCreate(ViherrakentamiskayttoBase):
    pass

class Viherrakentamiskaytto(ViherrakentamiskayttoBase):
    model_config = ConfigDict(from_attributes=True)
