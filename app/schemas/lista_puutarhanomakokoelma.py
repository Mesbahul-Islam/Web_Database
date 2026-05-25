from pydantic import BaseModel, ConfigDict
from datetime import date, datetime

class ListaPuutarhanomakokoelmaBase(BaseModel):
    id: int
    nimi: str

class ListaPuutarhanomakokoelmaCreate(ListaPuutarhanomakokoelmaBase):
    pass

class ListaPuutarhanomakokoelma(ListaPuutarhanomakokoelmaBase):
    model_config = ConfigDict(from_attributes=True)
