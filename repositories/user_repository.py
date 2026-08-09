from database_models.user_models import UserDB
from sqlalchemy.orm import Session
def create_user(username:str,email:str,hashed_password:str,
                role:str,db:Session):
    new_user=UserDB(
        username=username,
        email=email,
        hashed_password=hashed_password,
        role=role
    )
    db.add(new_user)
    return new_user

def get_user_by_email(email:str,db:Session):
    return db.query(UserDB).filter(UserDB.email==email).first()

def get_user_by_username(username:str,db:Session):
    return db.query(UserDB).filter(UserDB.username==username).first()

def get_user_by_id(id:int,db:Session):
    return db.query(UserDB).filter(UserDB.id==id).first()
