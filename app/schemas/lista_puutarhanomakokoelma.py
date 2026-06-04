from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import date, datetime

class ListaPuutarhanomakokoelmaBase(BaseModel):
    id: int
    nimi: str

class ListaPuutarhanomakokoelmaCreate(ListaPuutarhanomakokoelmaBase):
    pass

class ListaPuutarhanomakokoelma(ListaPuutarhanomakokoelmaBase):
    model_config = ConfigDict(from_attributes=True)

class ListaPuutarhanomakokoelmaPage(BaseModel):
    items: List[ListaPuutarhanomakokoelma]
    total: int
    page: int
    page_size: int
    pages: int
