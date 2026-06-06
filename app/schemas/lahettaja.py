from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class LahettajaBase(BaseModel):
    lahettajanro: int
    lahettajatyyppi: Optional[str] = None
    lahettajan_tunnus_puutarha: Optional[str] = None
    lahettajan_tunnus_kansainvalinen: Optional[str] = None
    lahettajan_nimi: Optional[str] = None
    lahiosoite: Optional[str] = None
    postilokero: Optional[str] = None
    postinumero: Optional[str] = None
    postitoimipaikka: Optional[str] = None
    kaupunki: Optional[str] = None
    osavaltio: Optional[str] = None
    maa: Optional[str] = None
    kontaktihenkilo: Optional[str] = None
    e_mail: Optional[str] = None
    web_sivut: Optional[str] = None
    osoitteen_kirjauspvm: Optional[str] = None
    Rion_sopimus: Optional[str] = None
    lahettajan_lisatiedot: Optional[str] = None
    hakunimi: Optional[str] = None

class LahettajaCreate(LahettajaBase):
    pass

class Lahettaja(LahettajaBase):
    model_config = ConfigDict(from_attributes=True)
