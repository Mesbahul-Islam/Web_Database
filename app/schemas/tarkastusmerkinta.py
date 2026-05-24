from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class TarkastusmerkintaBase(BaseModel):
    tarkastusnro: int
    tarkastuspvm: Optional[str]
    elavia_yksiloita: Optional[str]
    menestymista_koskevat_havainnot: Optional[str]
    tarkastaja: Optional[str]
    kasvin_huomautuksia: Optional[str]
    sijoituspaikan_nro: Optional[int]
    uus_tarkastuspvm: Optional[date]
    sijoituspaikka: Optional['Sijoituspaikka']

class TarkastusmerkintaCreate(TarkastusmerkintaBase):
    pass

class Tarkastusmerkinta(TarkastusmerkintaBase):
    model_config = ConfigDict(from_attributes=True)
