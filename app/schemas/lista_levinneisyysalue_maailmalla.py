from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ListaLevinneisyysalueMaailmallaBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]
    LYHENNE: Optional[str]
    NUMERO: Optional[str]

class ListaLevinneisyysalueMaailmallaCreate(ListaLevinneisyysalueMaailmallaBase):
    pass

class ListaLevinneisyysalueMaailmalla(ListaLevinneisyysalueMaailmallaBase):
    model_config = ConfigDict(from_attributes=True)
