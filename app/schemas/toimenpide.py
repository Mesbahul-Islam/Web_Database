from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ToimenpideBase(BaseModel):
    toimenpide_nro: int
    pvm: Optional[str] = None
    toimenpide: Optional[str] = None
    hankintaID: Optional[int] = None
    uus_pvm: Optional[str] = None

class ToimenpideCreate(ToimenpideBase):
    pass

class Toimenpide(ToimenpideBase):
    model_config = ConfigDict(from_attributes=True)

class ToimenpidePage(BaseModel):
    items: List[Toimenpide]
    total: int
    page: int
    page_size: int
    pages: int
