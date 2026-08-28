from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
from repositories import user_repository
from security import verify_access_token
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/user/login")
def get_current_user(
        token:str=Depends(oauth2_scheme),
        db:Session=Depends(get_db)
):
    payload=verify_access_token(token)
    email=payload.get("sub")
    if email is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    user=user_repository.get_user_by_email(email,db)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )
    return user
def get_current_admin(current_user=Depends(get_current_user)):
    if current_user.role.lower()!="admin":
        raise HTTPException(
            status_code=403,
            detail="only admin can perform this action"
        )
    return current_user