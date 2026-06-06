from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class HyotykayttoBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None
    NUMERO: Optional[str] = None

class HyotykayttoCreate(HyotykayttoBase):
    pass

class Hyotykaytto(HyotykayttoBase):
    model_config = ConfigDict(from_attributes=True)
