from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaTarkastajaBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class ListaTarkastajaCreate(ListaTarkastajaBase):
    pass

class ListaTarkastaja(ListaTarkastajaBase):
    model_config = ConfigDict(from_attributes=True)
