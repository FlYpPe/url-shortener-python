from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import models, schemas, utils
from app.database import get_db
from fastapi.responses import RedirectResponse

router = APIRouter(prefix="/url", tags=["URLs"])
redirect_router = APIRouter(tags=["Redirect"])

@router.post("/", response_model=schemas.URLResponse)
def create_url(url_data: schemas.URLCreate, db:Session = Depends(get_db)):
    short_code = utils.generate_short_url()

    existing = db.query(models.URL).filter(models.URL.short_code == short_code).first()
    if existing:
        short_code = utils.generate_short_url()
    
    new_url = models.URL(
        original_url=str(url_data.original_url),
        short_code=short_code
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return new_url
    
@redirect_router.get("/{short_code}")
def Redirect_to_original(short_code: str, db: Session = Depends(get_db)):
    url_record = db.query(models.URL).filter(models.URL.short_code == short_code).first()

    if not url_record:
        raise HTTPException(status_code=404, detail="URL not found")

    return RedirectResponse(url=url_record.original_url)

@router.get("/info")
def url_info(url: str = Query(..., alias="url"), db: Session = Depends(get_db)):
    print(url)
    short_url = db.query(models.URL).filter(models.URL.original_url == url).first()
    if not short_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return {
        "original_url": short_url.original_url,
        "short_code": short_url.short_code,
        "created_at": short_url.created_at
    }

@router.get("/")
def root():
    return {"message": "Welcome to the URL Shortener API"}