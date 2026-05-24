from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class KayttotarkoitusBase(BaseModel):
    id: int
    nimi: Optional[str]

class KayttotarkoitusCreate(KayttotarkoitusBase):
    pass

class Kayttotarkoitus(KayttotarkoitusBase):
    model_config = ConfigDict(from_attributes=True)
