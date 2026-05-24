from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaHakuBase(BaseModel):
    id: int
    nimi: Optional[str]

class ListaHakuCreate(ListaHakuBase):
    pass

class ListaHaku(ListaHakuBase):
    model_config = ConfigDict(from_attributes=True)
