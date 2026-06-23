from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ToimenpideBase(BaseModel):
    toimenpide_nro: int
    pvm: Optional[str] = None
    toimenpide: Optional[str] = None
    hankintaID: Optional[int] = None
    uus_pvm: Optional[str] = None
    deleted_at: Optional[datetime] = None

class ToimenpideCreate(ToimenpideBase):
    toimenpide_nro: Optional[int] = None

class Toimenpide(ToimenpideBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)

class ToimenpidePage(BaseModel):
    items: List[Toimenpide]
    total: int
    page: int
    page_size: int
    pages: int
