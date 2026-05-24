from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class LahettajaBase(BaseModel):
    lahettajanro: int
    lahettajatyyppi: Optional[str]
    lahettajan_tunnus_puutarha: Optional[str]
    lahettajan_tunnus_kansainvalinen: Optional[str]
    lahettajan_nimi: Optional[str]
    lahiosoite: Optional[str]
    postilokero: Optional[str]
    postinumero: Optional[str]
    postitoimipaikka: Optional[str]
    kaupunki: Optional[str]
    osavaltio: Optional[str]
    maa: Optional[str]
    kontaktihenkilo: Optional[str]
    e_mail: Optional[str]
    web_sivut: Optional[str]
    osoitteen_kirjauspvm: Optional[str]
    Rion_sopimus: Optional[str]
    lahettajan_lisatiedot: Optional[str]
    hakunimi: Optional[str]
    hankintatiedot: list['Hankintatiedot']

class LahettajaCreate(LahettajaBase):
    pass

class Lahettaja(LahettajaBase):
    model_config = ConfigDict(from_attributes=True)
