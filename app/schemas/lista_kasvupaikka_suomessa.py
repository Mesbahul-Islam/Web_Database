from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaKasvupaikkaSuomessaBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class ListaKasvupaikkaSuomessaCreate(ListaKasvupaikkaSuomessaBase):
    pass

class ListaKasvupaikkaSuomessa(ListaKasvupaikkaSuomessaBase):
    model_config = ConfigDict(from_attributes=True)
