from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import date, datetime

class ListaAlkuperatyyppiBase(BaseModel):
    nimi: str
    id: int

class ListaAlkuperatyyppiCreate(ListaAlkuperatyyppiBase):
    pass

class ListaAlkuperatyyppi(ListaAlkuperatyyppiBase):
    model_config = ConfigDict(from_attributes=True)

class ListaAlkuperatyyppiPage(BaseModel):
    items: List[ListaAlkuperatyyppi]
    total: int
    page: int
    page_size: int
    pages: int
