import os
from pathlib import Path

from dotenv import load_dotenv


_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_APP_ENV_FILE = _PROJECT_ROOT / "app" / ".env"
_ROOT_ENV_FILE = _PROJECT_ROOT / ".env"

if _ROOT_ENV_FILE.exists():
    load_dotenv(_ROOT_ENV_FILE)

if _APP_ENV_FILE.exists():
    load_dotenv(_APP_ENV_FILE)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("DB_NAME", "puutarhakanta2005")
DB_USER = os.getenv("DB_USER", "tarkastususer")
DB_PASSWORD = os.getenv("DB_PASSWORD", "tarkastususer")

DATABASE_URL = os.getenv("DATABASE_URL") or (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
