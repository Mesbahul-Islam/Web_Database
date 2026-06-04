from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, datetime

class ListaAlkuperainenVaiTulokasBase(BaseModel):
    id: int
    nimi: Optional[str]

class ListaAlkuperainenVaiTulokasCreate(ListaAlkuperainenVaiTulokasBase):
    pass

class ListaAlkuperainenVaiTulokas(ListaAlkuperainenVaiTulokasBase):
    model_config = ConfigDict(from_attributes=True)

class ListaAlkuperainenVaiTulokasPage(BaseModel):
    items: List[ListaAlkuperainenVaiTulokas]
    total: int
    page: int
    page_size: int
    pages: int
