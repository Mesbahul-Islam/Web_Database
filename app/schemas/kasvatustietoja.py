from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class KasvatustietojaBase(BaseModel):
    lisatietojen_nro_kasvatus: int
    hankintaID: int
    siemenpankki: Optional[str]
    siemenia_jaljella: Optional[str]
    siementen_varastoimistapa: Optional[str]
    tutkimus: Optional[str]
    huomautuksia: Optional[str]
    pvm: Optional[str]

class KasvatustietojaCreate(KasvatustietojaBase):
    pass

class Kasvatustietoja(KasvatustietojaBase):
    model_config = ConfigDict(from_attributes=True)

class KasvatustietojaPage(BaseModel):
    items: List[Kasvatustietoja]
    total: int
    page: int
    page_size: int
    pages: int
