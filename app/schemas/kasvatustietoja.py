from pydantic import BaseModel, ConfigDict
from typing import Optional
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
