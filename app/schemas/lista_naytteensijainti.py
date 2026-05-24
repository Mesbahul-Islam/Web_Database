from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaNaytteensijaintiBase(BaseModel):
    id: int
    koodi: Optional[str]
    nimi: Optional[str]

class ListaNaytteensijaintiCreate(ListaNaytteensijaintiBase):
    pass

class ListaNaytteensijainti(ListaNaytteensijaintiBase):
    model_config = ConfigDict(from_attributes=True)
