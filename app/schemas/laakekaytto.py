from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class LaakekayttoBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class LaakekayttoCreate(LaakekayttoBase):
    pass

class Laakekaytto(LaakekayttoBase):
    model_config = ConfigDict(from_attributes=True)
