from fastapi import FastAPI
from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from app.api.api import api_router
from app.database import engine
from app.models.base import Base
import app.models  # This imports __init__.py, registering all models to Base



# Create database tables that don't exist yet
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Garden Information System API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/api")
