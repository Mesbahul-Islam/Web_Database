from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaSopimuksetBase(BaseModel):
    id: int
    nimi: Optional[str]

class ListaSopimuksetCreate(ListaSopimuksetBase):
    pass

class ListaSopimukset(ListaSopimuksetBase):
    model_config = ConfigDict(from_attributes=True)
