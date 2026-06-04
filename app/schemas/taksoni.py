from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class TaksoniBase(BaseModel):
    taksonin_nro: int
    tieteellinen_nimi: str
    suku: Optional[str]
    suvun_auktori: Optional[str]
    laji: Optional[str]
    lajin_auktori: Optional[str]
    alataso_1: Optional[str]
    alatason_1_viite: Optional[int]
    alataso_2: Optional[str]
    alatason_2_auktori: Optional[str]
    alatason_1_auktori: Optional[str]
    alatason_2_viite: Optional[int]
    alataso_3: Optional[str]
    alatason_3_auktori: Optional[str]
    alatason_3_viite: Optional[int]
    alataso_4: Optional[str]
    alatason_4_auktori: Optional[str]
    alatason_4_viite: Optional[int]
    alataso_5: Optional[str]
    alatason_5_auktori: Optional[str]
    alatason_5_viite: Optional[int]
    risteymatiedot: Optional[str]
    risteymatietojen_auktori: Optional[str]
    viimeinen_paivityspvm: Optional[str]
    muita_tietoja: Optional[str]
    jarjestysnumero: Optional[int]
    viitenro: Optional[int]
    lajin_viite: Optional[str]
    lajin_viite2: Optional[str]
    yleis_viite: Optional[str]
    vap_yleis_viite: Optional[str]
    put: Optional[int]
    puttia: Optional[str]
    risteymaviite: Optional[str]

class TaksoniCreate(TaksoniBase):
    taksonin_nro: Optional[int] = None

class Taksoni(TaksoniBase):
    model_config = ConfigDict(from_attributes=True)

class TaksoniPage(BaseModel):
    items: List[Taksoni]
    total: int
    page: int
    page_size: int
    pages: int
