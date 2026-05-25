from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ListaKasvumuotoBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]
    NUMERO: Optional[str]

class ListaKasvumuotoCreate(ListaKasvumuotoBase):
    pass

class ListaKasvumuoto(ListaKasvumuotoBase):
    model_config = ConfigDict(from_attributes=True)
