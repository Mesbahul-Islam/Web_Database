from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ListaKayttotarkoitusBase(BaseModel):
    id: int
    nimi: Optional[str]

class ListaKayttotarkoitusCreate(ListaKayttotarkoitusBase):
    pass

class ListaKayttotarkoitus(ListaKayttotarkoitusBase):
    model_config = ConfigDict(from_attributes=True)
