from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class KasvatustietojaBase(BaseModel):
    lisatietojen_nro_kasvatus: int
    hankintaID: int
    siemenpankki: Optional[str] = None
    siemenia_jaljella: Optional[str] = None
    siementen_varastoimistapa: Optional[str] = None
    tutkimus: Optional[str] = None
    huomautuksia: Optional[str] = None
    pvm: Optional[str] = None

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
