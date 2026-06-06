from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaKieliBase(BaseModel):
    id: int
    nimi: Optional[str] = None

class ListaKieliCreate(ListaKieliBase):
    pass

class ListaKieli(ListaKieliBase):
    model_config = ConfigDict(from_attributes=True)

class ListaKieliPage(BaseModel):
    items: List[ListaKieli]
    total: int
    page: int
    page_size: int
    pages: int
