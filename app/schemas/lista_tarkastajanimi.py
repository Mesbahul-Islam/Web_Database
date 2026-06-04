from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict

class ListaTarkastajanimi(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int] = None  # id: id
    nimi: Optional[str] = None  # nimi: name


class ListaTarkastajanimiPage(BaseModel):
    items: List[ListaTarkastajanimi]
    total: int
    page: int
    page_size: int
    pages: int
