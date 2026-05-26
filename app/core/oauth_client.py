import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer


_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_APP_ENV_FILE = _PROJECT_ROOT / "app" / ".env"
_ROOT_ENV_FILE = _PROJECT_ROOT / ".env"

if _ROOT_ENV_FILE.exists():
    load_dotenv(_ROOT_ENV_FILE)

if _APP_ENV_FILE.exists():
    load_dotenv(_APP_ENV_FILE)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


