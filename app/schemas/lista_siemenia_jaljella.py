from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaSiemeniaJaljellaBase(BaseModel):
    id: int
    nimi: Optional[str]

class ListaSiemeniaJaljellaCreate(ListaSiemeniaJaljellaBase):
    pass

class ListaSiemeniaJaljella(ListaSiemeniaJaljellaBase):
    model_config = ConfigDict(from_attributes=True)
