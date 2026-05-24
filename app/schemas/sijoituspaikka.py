from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class SijoituspaikkaBase(BaseModel):
    sijoituspaikan_nro: int
    osaston_numero: int
    sijoituspvm: Optional[str]
    ruutu: Optional[str]
    sijoituspaikan_nimi: Optional[str]
    kasvin_status: Optional[str]
    sijoituspaikan_koordinaatit: Optional[str]
    sijoituspaikka_vanhat_tiedot: Optional[str]
    kasvin_huomautuksia: Optional[str]
    osastopaikka: Optional['Osastopaikka'] = None
    tarkastusmerkinta: Optional[list['Tarkastusmerkinta']] = None

class SijoituspaikkaCreate(SijoituspaikkaBase):
    pass

class Sijoituspaikka(SijoituspaikkaBase):
    model_config = ConfigDict(from_attributes=True)
