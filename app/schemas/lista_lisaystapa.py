from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ListaLisaystapaBase(BaseModel):
    id: int
    koodi: Optional[str]
    nimi: Optional[str]

class ListaLisaystapaCreate(ListaLisaystapaBase):
    pass

class ListaLisaystapa(ListaLisaystapaBase):
    model_config = ConfigDict(from_attributes=True)
