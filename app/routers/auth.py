from fastapi import APIRouter, Depends, HTTPException
from app.utils.jwt_utils import create_jwt, verify_password, get_user
from app.database import get_db
from sqlalchemy.orm import Session
from app import models
from fastapi import APIRouter, Depends

router_validation = APIRouter()

@router_validation.get("/me")
def read_me(current_user = Depends(get_user)):
    return {"user_id": current_user}

router = APIRouter(prefix="/auth")

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    token = create_jwt({"sub": str(user.id)})

    return {"access_token": token, "token_type": "bearer"}