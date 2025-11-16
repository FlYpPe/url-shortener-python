from fastapi import APIRouter

router = APIRouter(prefix="/url", tags=["URLs"])

@router.get("/")
def root():
    return {"message": "Welcome to the URL Shortener API"}