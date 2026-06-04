from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaTuulenkestavyysBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class ListaTuulenkestavyysCreate(ListaTuulenkestavyysBase):
    pass

class ListaTuulenkestavyys(ListaTuulenkestavyysBase):
    model_config = ConfigDict(from_attributes=True)

class ListaTuulenkestavyysPage(BaseModel):
    items: List[ListaTuulenkestavyys]
    total: int
    page: int
    page_size: int
    pages: int
