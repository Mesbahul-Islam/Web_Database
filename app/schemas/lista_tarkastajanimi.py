from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

class ListaTarkastajanimi(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int] = None  # id: id
    nimi: Optional[str] = None  # nimi: name

