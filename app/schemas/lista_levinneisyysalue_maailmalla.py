from pydantic import BaseModel, ConfigDict
from typing import List, Optional
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

class ListaLevinneisyysalueMaailmallaPage(BaseModel):
    items: List[ListaLevinneisyysalueMaailmalla]
    total: int
    page: int
    page_size: int
    pages: int
