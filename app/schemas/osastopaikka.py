from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class OsastopaikkaBase(BaseModel):
    osaston_numero: int
    osaston_koodi: Optional[str] = None
    osaston_nimi: Optional[str] = None
    kasvin_status: Optional[str] = None
    kasvin_huomautuksia: Optional[str] = None
    hankintaID: Optional[int] = None

class OsastopaikkaCreate(OsastopaikkaBase):
    pass

class Osastopaikka(OsastopaikkaBase):
    model_config = ConfigDict(from_attributes=True)

class OsastopaikkaPage(BaseModel):
    items: List[Osastopaikka]
    total: int
    page: int
    page_size: int
    pages: int
