from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ViiteBase(BaseModel):
    viitenro: int
    viitteen_lyhenne: Optional[str]
    tekija: Optional[str]
    kirjan_nimi: Optional[str]
    kirja_selite: Optional[str]
    kustantaja: Optional[str]
    painos: Optional[str]
    vuosi: Optional[str]
    ISBN: Optional[str]
    sijainti: Optional[str]
    taksoni: list['Taksoni']
    alkuperainen_kasvupaikka: list['AlkuperainenKasvupaikka']
    kansainvaliset_sopimukset: list['KansainvalisetSopimukset']
    kasvin_kayttotarkoitus: list['KasvinKayttotarkoitus']
    muunkielinen_nimi: list['MuunkielinenNimi']
    naytetieto: list['Naytetieto']
    suomalainen_kasvupaikka: list['SuomalainenKasvupaikka']
    suomalainen_levinneisyysalue: list['SuomalainenLevinneisyysalue']
    synonyymi: list['Synonyymi']
    ymparistoindikaattoriluonne: list['Ymparistoindikaattoriluonne']

class ViiteCreate(ViiteBase):
    pass

class Viite(ViiteBase):
    model_config = ConfigDict(from_attributes=True)
