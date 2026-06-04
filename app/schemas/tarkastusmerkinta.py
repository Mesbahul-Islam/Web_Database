from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class TarkastusmerkintaBase(BaseModel):
    tarkastusnro: int
    tarkastuspvm: Optional[str]
    elavia_yksiloita: Optional[str]
    menestymista_koskevat_havainnot: Optional[str]
    tarkastaja: Optional[str]
    kasvin_huomautuksia: Optional[str]
    sijoituspaikan_nro: Optional[int]
    uus_tarkastuspvm: Optional[str]

class TarkastusmerkintaCreate(TarkastusmerkintaBase):
    pass

class Tarkastusmerkinta(TarkastusmerkintaBase):
    model_config = ConfigDict(from_attributes=True)

class TarkastusmerkintaPage(BaseModel):
    items: List[Tarkastusmerkinta]
    total: int
    page: int
    page_size: int
    pages: int
