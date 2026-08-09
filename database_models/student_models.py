from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
Base=declarative_base()
class StudentDB(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    branch=Column(String,nullable=False)
    year=Column(Integer,nullable=False)

    enrollments=relationship("EnrollmentDB",back_populates="student")
