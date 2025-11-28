from fastapi import FastAPI
from app.database import Base, engine
from app.routers import url, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener")

app.include_router(url.router)
app.include_router(url.redirect_router)
app.include_router(auth.router_validation)
app.include_router(auth.router)