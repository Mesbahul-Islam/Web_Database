from fastapi import FastAPI

from app.api.api import api_router

app = FastAPI(title="Garden Information System API", version="1.0")
app.include_router(api_router)
