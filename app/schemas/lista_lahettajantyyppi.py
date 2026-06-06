from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaLahettajantyyppiBase(BaseModel):
    id: int
    nimi: Optional[str] = None

class ListaLahettajantyyppiCreate(ListaLahettajantyyppiBase):
    pass

class ListaLahettajantyyppi(ListaLahettajantyyppiBase):
    model_config = ConfigDict(from_attributes=True)

class ListaLahettajantyyppiPage(BaseModel):
    items: List[ListaLahettajantyyppi]
    total: int
    page: int
    page_size: int
    pages: int
