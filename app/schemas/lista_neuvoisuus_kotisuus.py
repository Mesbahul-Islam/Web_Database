from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ListaNeuvoisuusKotisuusBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class ListaNeuvoisuusKotisuusCreate(ListaNeuvoisuusKotisuusBase):
    pass

class ListaNeuvoisuusKotisuus(ListaNeuvoisuusKotisuusBase):
    model_config = ConfigDict(from_attributes=True)
