from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaViljelynTarkoitusBase(BaseModel):
    ID: int
    NIMI: Optional[str] = None
    KOODI: Optional[str] = None
    NUMERO: Optional[str] = None

class ListaViljelynTarkoitusCreate(ListaViljelynTarkoitusBase):
    pass

class ListaViljelynTarkoitus(ListaViljelynTarkoitusBase):
    model_config = ConfigDict(from_attributes=True)

class ListaViljelynTarkoitusPage(BaseModel):
    items: List[ListaViljelynTarkoitus]
    total: int
    page: int
    page_size: int
    pages: int
