from pydantic import BaseModel, ConfigDict
from datetime import date, datetime

class ListaIsokoodiBase(BaseModel):
    id: int
    nimi: str

class ListaIsokoodiCreate(ListaIsokoodiBase):
    pass

class ListaIsokoodi(ListaIsokoodiBase):
    model_config = ConfigDict(from_attributes=True)
