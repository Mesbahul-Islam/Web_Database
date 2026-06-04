from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaSiemeniaJaljellaBase(BaseModel):
    id: int
    nimi: Optional[str]

class ListaSiemeniaJaljellaCreate(ListaSiemeniaJaljellaBase):
    pass

class ListaSiemeniaJaljella(ListaSiemeniaJaljellaBase):
    model_config = ConfigDict(from_attributes=True)

class ListaSiemeniaJaljellaPage(BaseModel):
    items: List[ListaSiemeniaJaljella]
    total: int
    page: int
    page_size: int
    pages: int
