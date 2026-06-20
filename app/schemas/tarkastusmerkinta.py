from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class TarkastusmerkintaBase(BaseModel):
    tarkastuspvm: Optional[str] = None
    elavia_yksiloita: Optional[str] = None
    menestymista_koskevat_havainnot: Optional[str] = None
    tarkastaja: Optional[str] = None
    kasvin_huomautuksia: Optional[str] = None
    sijoituspaikan_nro: Optional[int] = None
    uus_tarkastuspvm: Optional[str] = None

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
