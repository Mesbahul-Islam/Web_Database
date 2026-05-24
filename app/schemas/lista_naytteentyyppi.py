from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaNaytteentyyppiBase(BaseModel):
    id: int
    nimi: Optional[str]
    koodi: Optional[str]

class ListaNaytteentyyppiCreate(ListaNaytteentyyppiBase):
    pass

class ListaNaytteentyyppi(ListaNaytteentyyppiBase):
    model_config = ConfigDict(from_attributes=True)
