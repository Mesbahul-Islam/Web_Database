from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class KansainvalisetSopimuksetBase(BaseModel):
    sopimus_id: int
    taksonin_nro: int
    Sopimuksen_nimi: Optional[str]
    selite: Optional[str]
    viitenro: Optional[int]
    taksoni: Optional['Taksoni'] = None
    viite: Optional['Viite']

class KansainvalisetSopimuksetCreate(KansainvalisetSopimuksetBase):
    pass

class KansainvalisetSopimukset(KansainvalisetSopimuksetBase):
    model_config = ConfigDict(from_attributes=True)
