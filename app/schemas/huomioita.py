from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class HuomioitaBase(BaseModel):
    paneeli: str
    huom: Optional[str]

class HuomioitaCreate(HuomioitaBase):
    pass

class Huomioita(HuomioitaBase):
    model_config = ConfigDict(from_attributes=True)

class HuomioitaPage(BaseModel):
    items: List[Huomioita]
    total: int
    page: int
    page_size: int
    pages: int
