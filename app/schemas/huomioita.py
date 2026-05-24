from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class HuomioitaBase(BaseModel):
    paneeli: str
    huom: Optional[str]

class HuomioitaCreate(HuomioitaBase):
    pass

class Huomioita(HuomioitaBase):
    model_config = ConfigDict(from_attributes=True)
