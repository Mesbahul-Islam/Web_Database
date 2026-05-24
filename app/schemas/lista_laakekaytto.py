from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaLaakekayttoBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class ListaLaakekayttoCreate(ListaLaakekayttoBase):
    pass

class ListaLaakekaytto(ListaLaakekayttoBase):
    model_config = ConfigDict(from_attributes=True)
