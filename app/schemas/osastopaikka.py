from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class OsastopaikkaBase(BaseModel):
    osaston_numero: int
    osaston_koodi: Optional[str]
    osaston_nimi: Optional[str]
    kasvin_status: Optional[str]
    kasvin_huomautuksia: Optional[str]
    hankintaID: Optional[int]
    hankintatiedot: Optional['Hankintatiedot']
    sijoituspaikka: list['Sijoituspaikka']

class OsastopaikkaCreate(OsastopaikkaBase):
    pass

class Osastopaikka(OsastopaikkaBase):
    model_config = ConfigDict(from_attributes=True)
