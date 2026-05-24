from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaPuutarhanerikoiskokoelmaBase(BaseModel):
    id: int
    nimi: str

class ListaPuutarhanerikoiskokoelmaCreate(ListaPuutarhanerikoiskokoelmaBase):
    pass

class ListaPuutarhanerikoiskokoelma(ListaPuutarhanerikoiskokoelmaBase):
    model_config = ConfigDict(from_attributes=True)
