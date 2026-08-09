from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories import user_repository
from security import verify_password,hash_password,create_access_token

def create_user(username:str,email:str,password:str,
                role:str,db:Session):
    existing_username=user_repository.get_user_by_username(username,db)
    if existing_username:
        raise HTTPException(
            status_code=409,
            detail="User alreay exists"
        )
    existing_email=user_repository.get_user_by_email(email,db)
    if existing_email:
            raise HTTPException(
                status_code=409,
                detail="Email alreay exists"
            )
    hashed_pass=hash_password(password)
    
    new_user=user_repository.create_user(username,email,hashed_pass,role,db)
    db.commit()
    db.refresh(new_user)
    return new_user
def get_user_by_id(id:int,db:Session):
    existed=user_repository.get_user_by_id(id,db)
    if existed is None:
        raise HTTPException(
            status_code=404,
            detail="No user is found"
        )
    return existed

def login_user(username:str,password:str,db:Session):
    user=user_repository.get_user_by_email(username,db)

    if user is None:
         raise HTTPException(
              status_code=401,
              detail="Invalid email or password"
         )
    
    if not verify_password(password,user.hashed_password) :
             raise HTTPException(
                  status_code=401,
                  detail="Incorrect email or password"
             )
    data={
    "sub":user.email,
    "role":user.role
    }
    token=create_access_token(data)
    return {
         "access_token":token,
         "token_type":"bearer"

    }

     