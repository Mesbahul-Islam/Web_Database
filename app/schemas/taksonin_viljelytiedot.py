from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class TaksoninViljelytiedotBase(BaseModel):
    lisatietojen_nro_viljely: int
    taksonin_nro: int
    kasvitaudit_ja_tuholaiset: Optional[str]
    kestaa_seuraavia_torjuntaaineita: Optional[str]
    ei_kesta_seuraavia_torjunta_aineita: Optional[str]
    erityisia_kasvualustavaatimuksia: Optional[str]
    erityisia_valovaatimuksia: Optional[str]
    erityisia_lampotila_tai_talvehtimisvaatimuksia: Optional[str]
    lisaystapa: Optional[str]
    siementen_keruu: Optional[str]
    siementen_sailytys: Optional[str]
    tuulenkestavyys: Optional[str]
    ilmastollinen_kestavyys: Optional[str]
    viljelykasvien_ilmastollinen_kestavyys: Optional[str]
    varsi: Optional[str]
    kasvumuoto: Optional[str]
    kasvutapa: Optional[str]
    korkeus: Optional[str]
    polytystapa: Optional[str]
    neuvoisuus_ja_kotisuus: Optional[str]
    muita_viljelytietoja: Optional[str]
    rauhoitus: Optional[str]
    uhanalaisuusluokka_suomessa: Optional[str]
    uhanalaisuusluokka_maailmalla: Optional[str]
    muita_ominaisuuksia: Optional[str]
    haitallisuus: Optional[str]
    myrkyllisyys: Optional[str]
    sopimukset: Optional[str]
    vapaa_viite: Optional[str]

class TaksoninViljelytiedotCreate(TaksoninViljelytiedotBase):
    pass

class TaksoninViljelytiedot(TaksoninViljelytiedotBase):
    model_config = ConfigDict(from_attributes=True)
