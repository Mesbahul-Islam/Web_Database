from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class HuomoitaBase(BaseModel):
    paneeli: str
    huom: Optional[str]

class HuomoitaCreate(HuomoitaBase):
    pass

class Huomoita(HuomoitaBase):
    model_config = ConfigDict(from_attributes=True)
