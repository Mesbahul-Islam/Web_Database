from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class TarkastajanimiListaBase(BaseModel):
    id: int
    lyhenne: Optional[str] = None
    nimi: Optional[str] = None

class TarkastajanimiListaCreate(TarkastajanimiListaBase):
    pass

class TarkastajanimiLista(TarkastajanimiListaBase):
    model_config = ConfigDict(from_attributes=True)
