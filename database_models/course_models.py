from sqlalchemy import Column,Integer,String,ForeignKey,Index
from sqlalchemy.orm import relationship
from database_models.student_models import Base
class CourseDB(Base):
    __tablename__="courses"
    id=Column(Integer,primary_key=True,index=True)
    course_name=Column(String,nullable=False)
    course_code=Column(String,unique=True,nullable=False)
    credits=Column(Integer,nullable=False)
    teacher=Column(String,nullable=False)
    enrollments=relationship("EnrollmentDB",back_populates="course")
Index(
    "idx_course_code",
    CourseDB.course_code
) 


