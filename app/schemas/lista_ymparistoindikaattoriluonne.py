from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaYmparistoindikaattoriluonneBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]
    NUMERO: Optional[str]

class ListaYmparistoindikaattoriluonneCreate(ListaYmparistoindikaattoriluonneBase):
    pass

class ListaYmparistoindikaattoriluonne(ListaYmparistoindikaattoriluonneBase):
    model_config = ConfigDict(from_attributes=True)

class ListaYmparistoindikaattoriluonnePage(BaseModel):
    items: List[ListaYmparistoindikaattoriluonne]
    total: int
    page: int
    page_size: int
    pages: int
