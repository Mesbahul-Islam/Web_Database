from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaMaaritysmerkintaBase(BaseModel):
    id: int
    nimi: Optional[str]

class ListaMaaritysmerkintaCreate(ListaMaaritysmerkintaBase):
    pass

class ListaMaaritysmerkinta(ListaMaaritysmerkintaBase):
    model_config = ConfigDict(from_attributes=True)
