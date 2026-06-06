from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class LaakekayttoBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None

class LaakekayttoCreate(LaakekayttoBase):
    pass

class Laakekaytto(LaakekayttoBase):
    model_config = ConfigDict(from_attributes=True)
