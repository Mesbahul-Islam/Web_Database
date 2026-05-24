from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class AlkuperaaKoskevatTiedotBase(BaseModel):
    alkupera_nro: int
    hankintaID: int
    alkuperatyyppi: Optional[str]
    maa: Optional[str]
    maan_ISOkoodi: Optional[str]
    alue: Optional[str]
    ala_alue: Optional[str]
    kunta: Optional[str]
    kyla: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    grid_27_E: Optional[str]
    kasvupaikka: Optional[str]
    korkeus: Optional[str]
    keraaja: Optional[str]
    kerayspvm: Optional[str]
    keraysnumero: Optional[str]
    muita_keraystietoja: Optional[str]
    keraysretki: Optional[str]
    hankintatiedot: Optional['Hankintatiedot'] = None

class AlkuperaaKoskevatTiedotCreate(AlkuperaaKoskevatTiedotBase):
    pass

class AlkuperaaKoskevatTiedot(AlkuperaaKoskevatTiedotBase):
    model_config = ConfigDict(from_attributes=True)
