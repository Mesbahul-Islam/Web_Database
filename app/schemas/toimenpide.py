from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ToimenpideBase(BaseModel):
    toimenpide_nro: int
    pvm: Optional[str]
    toimenpide: Optional[str]
    hankintaID: Optional[int]
    uus_pvm: Optional[date]

class ToimenpideCreate(ToimenpideBase):
    pass

class Toimenpide(ToimenpideBase):
    model_config = ConfigDict(from_attributes=True)
