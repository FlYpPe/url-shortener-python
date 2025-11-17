from fastapi import FastAPI
from app.database import Base, engine
from app.routers import url

Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener")

app.include_router(url.router)
app.include_router(url.redirect_router)