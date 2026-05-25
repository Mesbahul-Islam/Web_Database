from pydantic import BaseModel, ConfigDict
from datetime import date, datetime

class HankintanumeroBase(BaseModel):
    uusin_hankintanumero: str

class HankintanumeroCreate(HankintanumeroBase):
    pass

class Hankintanumero(HankintanumeroBase):
    model_config = ConfigDict(from_attributes=True)
