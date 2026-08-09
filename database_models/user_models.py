from database_models.student_models import Base
from sqlalchemy import Column,Integer,String,Boolean
class UserDB(Base):
    __tablename__="User"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)
    hashed_password=Column(String,nullable=False)
    role=Column(String,nullable=False)
    is_active=Column(Boolean,default=True)
