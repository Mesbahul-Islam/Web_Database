from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class UserBase(BaseModel):
    username: str
    role_name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)

