from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaViljelynTarkoitusBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]
    NUMERO: Optional[str]

class ListaViljelynTarkoitusCreate(ListaViljelynTarkoitusBase):
    pass

class ListaViljelynTarkoitus(ListaViljelynTarkoitusBase):
    model_config = ConfigDict(from_attributes=True)
