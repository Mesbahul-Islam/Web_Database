from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class KansainvalisetSopimuksetBase(BaseModel):
    sopimus_id: int
    taksonin_nro: int
    Sopimuksen_nimi: Optional[str] = None
    selite: Optional[str] = None
    viitenro: Optional[int] = None

class KansainvalisetSopimuksetCreate(KansainvalisetSopimuksetBase):
    sopimus_id: Optional[int] = None

class KansainvalisetSopimukset(KansainvalisetSopimuksetBase):
    model_config = ConfigDict(from_attributes=True)

class KansainvalisetSopimuksetPage(BaseModel):
    items: List[KansainvalisetSopimukset]
    total: int
    page: int
    page_size: int
    pages: int
