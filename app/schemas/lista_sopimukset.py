from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaSopimuksetBase(BaseModel):
    id: int
    nimi: Optional[str] = None

class ListaSopimuksetCreate(ListaSopimuksetBase):
    pass

class ListaSopimukset(ListaSopimuksetBase):
    model_config = ConfigDict(from_attributes=True)

class ListaSopimuksetPage(BaseModel):
    items: List[ListaSopimukset]
    total: int
    page: int
    page_size: int
    pages: int
