from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import IntegrityError
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from app.api.api import api_router
from app.database import engine
from app.models.base import Base
import app.models  # This imports __init__.py, registering all models to Base
from app.core.limiter import limiter

# Create database tables that don't exist yet
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Garden Information System API", version="1.0")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.exception_handler(IntegrityError)
async def sqlalchemy_integrity_error_handler(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=409,
        content={"detail": "A conflict occurred with the database constraints (e.g., duplicate record or invalid foreign key).", "error": str(exc.orig) if hasattr(exc, "orig") else str(exc)}
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "http://localhost:8080", "https://gis-frontend-psi.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/api")
