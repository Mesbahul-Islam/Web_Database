from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class AlkuperaaKoskevatTiedotBase(BaseModel):
    alkupera_nro: int
    hankintaID: int
    alkuperatyyppi: Optional[str] = None
    maa: Optional[str] = None
    maan_ISOkoodi: Optional[str] = None
    alue: Optional[str] = None
    ala_alue: Optional[str] = None
    kunta: Optional[str] = None
    kyla: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    grid_27_E: Optional[str] = None
    kasvupaikka: Optional[str] = None
    korkeus: Optional[str] = None
    keraaja: Optional[str] = None
    kerayspvm: Optional[str] = None
    keraysnumero: Optional[str] = None
    muita_keraystietoja: Optional[str] = None
    keraysretki: Optional[str] = None

class AlkuperaaKoskevatTiedotCreate(AlkuperaaKoskevatTiedotBase):
    alkupera_nro: Optional[int] = None

class AlkuperaaKoskevatTiedot(AlkuperaaKoskevatTiedotBase):
    model_config = ConfigDict(from_attributes=True)

class AlkuperaaKoskevatTiedotPage(BaseModel):
    items: List[AlkuperaaKoskevatTiedot]
    total: int
    page: int
    page_size: int
    pages: int  
