from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ListaIlmastonkestavyysBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class ListaIlmastonkestavyysCreate(ListaIlmastonkestavyysBase):
    pass

class ListaIlmastonkestavyys(ListaIlmastonkestavyysBase):
    model_config = ConfigDict(from_attributes=True)
