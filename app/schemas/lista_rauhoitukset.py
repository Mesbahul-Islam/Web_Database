from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaRauhoituksetBase(BaseModel):
    id: int
    nimi: Optional[str]

class ListaRauhoituksetCreate(ListaRauhoituksetBase):
    pass

class ListaRauhoitukset(ListaRauhoituksetBase):
    model_config = ConfigDict(from_attributes=True)
