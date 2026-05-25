from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ListaKieliBase(BaseModel):
    id: int
    nimi: Optional[str]

class ListaKieliCreate(ListaKieliBase):
    pass

class ListaKieli(ListaKieliBase):
    model_config = ConfigDict(from_attributes=True)
