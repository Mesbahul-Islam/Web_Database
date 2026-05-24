from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class TestiBase(BaseModel):
    id: int
    pvm: Optional[str]
    uuspvm: Optional[date]

class TestiCreate(TestiBase):
    pass

class Testi(TestiBase):
    model_config = ConfigDict(from_attributes=True)
