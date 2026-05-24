from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaAlkuperatyyppiBase(BaseModel):
    nimi: str
    id: int

class ListaAlkuperatyyppiCreate(ListaAlkuperatyyppiBase):
    pass

class ListaAlkuperatyyppi(ListaAlkuperatyyppiBase):
    model_config = ConfigDict(from_attributes=True)
