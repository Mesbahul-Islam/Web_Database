import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv


from pydantic_settings import BaseSettings, SettingsConfigDict

_PROJECT_ROOT = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    DATABASE_URL: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=(".env", "app/.env"), 
        env_file_encoding="utf-8", 
        extra="ignore"
    )

settings = Settings()
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
DATABASE_URL = settings.DATABASE_URL if settings.DATABASE_URL else f"sqlite:///{_PROJECT_ROOT / 'sqlite-backup' / 'puutarhakanta2005.sqlite'}"
