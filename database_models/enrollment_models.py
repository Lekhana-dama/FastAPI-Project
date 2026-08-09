from database_models.student_models import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,ForeignKey
class EnrollmentDB(Base):
    __tablename__="enrollments"
    id=Column(Integer,primary_key=True,index=True)
    student_id=Column(Integer,ForeignKey("students.id"),nullable=False)
    course_id=Column(Integer,ForeignKey("courses.id"),nullable=False)
    student=relationship("StudentDB",back_populates="enrollments")
    course=relationship("CourseDB",back_populates="enrollments")
