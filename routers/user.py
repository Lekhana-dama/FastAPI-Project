from fastapi import APIRouter,Depends
from database import get_db
from services import user_service
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from dependencies import get_current_user
router=APIRouter(prefix="/user",tags=["User"])

@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return current_user

@router.post("/register")
def user_register(email:str,username:str,password:str,role:str,db:Session=Depends(get_db)):
    return user_service.create_user(username,email,password,role,db)

@router.post("/login")
def user_login(from_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    return user_service.login_user(
        from_data.username,
        from_data.password,
        db
    )

@router.get("/{id}")
def get_user_by_id(id:int,db:Session=Depends(get_db)):
    return user_service.get_user_by_id(id,db)