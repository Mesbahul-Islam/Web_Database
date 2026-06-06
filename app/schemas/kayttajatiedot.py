from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class KayttajatiedotBase(BaseModel):
    id: int
    kayttajan_tunnus: Optional[str] = None
    kayttajan_nimi: Optional[str] = None
    kayttajan_taso: Optional[int] = None
    lisatietoja: Optional[str] = None

class KayttajatiedotCreate(KayttajatiedotBase):
    pass

class Kayttajatiedot(KayttajatiedotBase):
    model_config = ConfigDict(from_attributes=True)

class KayttajatiedotPage(BaseModel):
    items: List[Kayttajatiedot]
    total: int
    page: int
    page_size: int
    pages: int
