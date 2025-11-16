from fastapi import FastAPI
from app.routers import url

app = FastAPI(title="URL Shortener")

app.include_router(url.router)