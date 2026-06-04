from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import date, datetime

class ListaPuutarhanerikoiskokoelmaBase(BaseModel):
    id: int
    nimi: str

class ListaPuutarhanerikoiskokoelmaCreate(ListaPuutarhanerikoiskokoelmaBase):
    pass

class ListaPuutarhanerikoiskokoelma(ListaPuutarhanerikoiskokoelmaBase):
    model_config = ConfigDict(from_attributes=True)

class ListaPuutarhanerikoiskokoelmaPage(BaseModel):
    items: List[ListaPuutarhanerikoiskokoelma]
    total: int
    page: int
    page_size: int
    pages: int
