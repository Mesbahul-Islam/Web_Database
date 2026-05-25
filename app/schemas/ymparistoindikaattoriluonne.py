from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class YmparistoindikaattoriluonneBase(BaseModel):
    indikaattorin_nro: int
    taksonin_nro: int
    ymparistoindikaattoriluonne: Optional[str]
    ymparistoindikaattorin_selite: Optional[str]
    viitenro: Optional[int]

class YmparistoindikaattoriluonneCreate(YmparistoindikaattoriluonneBase):
    pass

class Ymparistoindikaattoriluonne(YmparistoindikaattoriluonneBase):
    model_config = ConfigDict(from_attributes=True)
