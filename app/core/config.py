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

# SQLAlchemy 1.4+ requires postgresql://, but some providers (like Vercel) use postgres://
raw_db_url = settings.DATABASE_URL
if raw_db_url and raw_db_url.startswith("postgres://"):
    raw_db_url = raw_db_url.replace("postgres://", "postgresql://", 1)

DATABASE_URL = raw_db_url if raw_db_url else f"sqlite:///{_PROJECT_ROOT / 'sqlite-backup' / 'puutarhakanta2005.sqlite'}"
