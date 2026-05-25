from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ListaMillaisenasaatuBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class ListaMillaisenasaatuCreate(ListaMillaisenasaatuBase):
    pass

class ListaMillaisenasaatu(ListaMillaisenasaatuBase):
    model_config = ConfigDict(from_attributes=True)
