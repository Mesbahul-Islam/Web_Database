from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class KayttajatiedotBase(BaseModel):
    id: int
    kayttajan_tunnus: Optional[str]
    kayttajan_nimi: Optional[str]
    kayttajan_taso: Optional[int]
    lisatietoja: Optional[str]

class KayttajatiedotCreate(KayttajatiedotBase):
    pass

class Kayttajatiedot(KayttajatiedotBase):
    model_config = ConfigDict(from_attributes=True)
