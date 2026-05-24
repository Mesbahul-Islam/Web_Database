from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class TarkastajanimiListaBase(BaseModel):
    id: int
    lyhenne: Optional[str]
    nimi: Optional[str]

class TarkastajanimiListaCreate(TarkastajanimiListaBase):
    pass

class TarkastajanimiLista(TarkastajanimiListaBase):
    model_config = ConfigDict(from_attributes=True)
