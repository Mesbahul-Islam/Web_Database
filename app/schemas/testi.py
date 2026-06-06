from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class TestiBase(BaseModel):
    id: int
    pvm: Optional[str] = None
    uuspvm: Optional[date] = None

class TestiCreate(TestiBase):
    pass

class Testi(TestiBase):
    model_config = ConfigDict(from_attributes=True)
