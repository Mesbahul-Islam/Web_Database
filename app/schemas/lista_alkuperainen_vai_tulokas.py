from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class ListaAlkuperainenVaiTulokasBase(BaseModel):
    id: int
    nimi: Optional[str]

class ListaAlkuperainenVaiTulokasCreate(ListaAlkuperainenVaiTulokasBase):
    pass

class ListaAlkuperainenVaiTulokas(ListaAlkuperainenVaiTulokasBase):
    model_config = ConfigDict(from_attributes=True)
