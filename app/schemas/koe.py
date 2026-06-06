from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class KoeBase(BaseModel):
    id: int
    i: Optional[int] = None
    t: Optional[str] = None

class KoeCreate(KoeBase):
    pass

class Koe(KoeBase):
    model_config = ConfigDict(from_attributes=True)
