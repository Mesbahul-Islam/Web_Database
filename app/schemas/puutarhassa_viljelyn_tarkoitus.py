from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class PuutarhassaViljelynTarkoitusBase(BaseModel):
    viljely_nro: int
    hankintaID: int
    puutarhassa_viljelyn_tarkoitus: Optional[str]
    puutarhassa_viljelyn_tarkenne: Optional[str]

class PuutarhassaViljelynTarkoitusCreate(PuutarhassaViljelynTarkoitusBase):
    pass

class PuutarhassaViljelynTarkoitus(PuutarhassaViljelynTarkoitusBase):
    model_config = ConfigDict(from_attributes=True)

class PuutarhassaViljelynTarkoitusPage(BaseModel):
    items: List[PuutarhassaViljelynTarkoitus]
    total: int
    page: int
    page_size: int
    pages: int
