from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class SijoituspaikkaBase(BaseModel):
    sijoituspaikan_nro: int
    osaston_numero: int
    sijoituspvm: Optional[str] = None
    ruutu: Optional[str] = None
    sijoituspaikan_nimi: Optional[str] = None
    kasvin_status: Optional[str] = None
    sijoituspaikan_koordinaatit: Optional[str] = None
    sijoituspaikka_vanhat_tiedot: Optional[str] = None
    kasvin_huomautuksia: Optional[str] = None

class SijoituspaikkaCreate(SijoituspaikkaBase):
    pass

class Sijoituspaikka(SijoituspaikkaBase):
    model_config = ConfigDict(from_attributes=True)

class SijoituspaikkaPage(BaseModel):
    items: List[Sijoituspaikka]
    total: int
    page: int
    page_size: int
    pages: int