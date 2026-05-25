from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class KoeBase(BaseModel):
    id: int
    i: Optional[int]
    t: Optional[str]

class KoeCreate(KoeBase):
    pass

class Koe(KoeBase):
    model_config = ConfigDict(from_attributes=True)
