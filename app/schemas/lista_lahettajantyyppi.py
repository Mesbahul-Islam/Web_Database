from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime

class ListaLahettajantyyppiBase(BaseModel):
    id: int
    nimi: Optional[str]

class ListaLahettajantyyppiCreate(ListaLahettajantyyppiBase):
    pass

class ListaLahettajantyyppi(ListaLahettajantyyppiBase):
    model_config = ConfigDict(from_attributes=True)
