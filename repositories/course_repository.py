from pydantic_models.course_model import Course
from sqlalchemy.orm import Session
from database_models.course_models import CourseDB
def create_course(course:Course,db:Session):
    new_course=CourseDB(
    id=course.id,
    course_name=course.course_name,
    course_code=course.course_code,
    credits=course.credits,
    teacher=course.teacher
    )
    db.add(new_course)
    return new_course
def get_all_courses(db:Session):
    return db.query(CourseDB).all()
def get_course_by_id(id:int,db:Session):
    return db.query(CourseDB).filter(CourseDB.id==id).first()
def update_course(id:int,db:Session):
    return db.query(CourseDB).filter(CourseDB.id==id).first()
def delete_course(id:int,db:Session):
    return db.query(CourseDB).filter(CourseDB.id==id).first()
def get_course_by_code(course_code:str,db:Session):
    return db.query(CourseDB).filter(CourseDB.course_code==course_code).first()
