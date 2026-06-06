from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class TaksoninViljelytiedotBase(BaseModel):
    lisatietojen_nro_viljely: int
    taksonin_nro: int
    kasvitaudit_ja_tuholaiset: Optional[str] = None
    kestaa_seuraavia_torjuntaaineita: Optional[str] = None
    ei_kesta_seuraavia_torjunta_aineita: Optional[str] = None
    erityisia_kasvualustavaatimuksia: Optional[str] = None
    erityisia_valovaatimuksia: Optional[str] = None
    erityisia_lampotila_tai_talvehtimisvaatimuksia: Optional[str] = None
    lisaystapa: Optional[str] = None
    siementen_keruu: Optional[str] = None
    siementen_sailytys: Optional[str] = None
    tuulenkestavyys: Optional[str] = None
    ilmastollinen_kestavyys: Optional[str] = None
    viljelykasvien_ilmastollinen_kestavyys: Optional[str] = None
    varsi: Optional[str] = None
    kasvumuoto: Optional[str] = None
    kasvutapa: Optional[str] = None
    korkeus: Optional[str] = None
    polytystapa: Optional[str] = None
    neuvoisuus_ja_kotisuus: Optional[str] = None
    muita_viljelytietoja: Optional[str] = None
    rauhoitus: Optional[str] = None
    uhanalaisuusluokka_suomessa: Optional[str] = None
    uhanalaisuusluokka_maailmalla: Optional[str] = None
    muita_ominaisuuksia: Optional[str] = None
    haitallisuus: Optional[str] = None
    myrkyllisyys: Optional[str] = None
    sopimukset: Optional[str] = None
    vapaa_viite: Optional[str] = None

class TaksoninViljelytiedotCreate(TaksoninViljelytiedotBase):
    pass

class TaksoninViljelytiedot(TaksoninViljelytiedotBase):
    model_config = ConfigDict(from_attributes=True)

class TaksoninViljelytiedotPage(BaseModel):
    items: List[TaksoninViljelytiedot]
    total: int
    page: int
    page_size: int
    pages: int
