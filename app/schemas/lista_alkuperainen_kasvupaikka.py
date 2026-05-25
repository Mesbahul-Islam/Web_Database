from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ListaAlkuperainenKasvupaikkaBase(BaseModel):
    ID: int
    NIMI: Optional[str]
    KOODI: Optional[str]

class ListaAlkuperainenKasvupaikkaCreate(ListaAlkuperainenKasvupaikkaBase):
    pass

class ListaAlkuperainenKasvupaikka(ListaAlkuperainenKasvupaikkaBase):
    model_config = ConfigDict(from_attributes=True)
