from pydantic_models.course_model import Course
from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories import course_repository
from exceptions import custom_exceptions,exception_handlers
import logging
import logging_config
logger=logging.getLogger(__name__)
def create_course(course:Course,db:Session):
    logger.info("created course %s sucesfully",course.id)
    existing = course_repository.get_course_by_code(
        course.course_code,
        db
    )

    if existing:
        logger.warning("course with id %s already exists",course.id)
        raise custom_exceptions.CourseAlreadyExistsException
    try:
        new_course=course_repository.create_course(course,db)
        db.commit()
        db.refresh(new_course)
        return new_course
    except Exception:
            db.rollback()
            raise

def get_all_courses(db:Session):
    return course_repository.get_all_courses(db)

def get_course_by_id(id:int,db:Session):
    course=course_repository.get_course_by_id(id,db)
    if course is None:
        raise custom_exceptions.CourseNotFoundException
    return course

def update_course(id:int,course:Course,db:Session):
    existed=course_repository.update_course(id,db)
    if existed is None:
        raise custom_exceptions.CourseNotFoundException
    duplicate=course_repository.get_course_by_code(course.course_code,db)
    if duplicate and duplicate.id!=id:
         raise custom_exceptions.CourseAlreadyExistsException
    try:
        existed.course_name=course.course_name
        existed.credits=course.credits
        existed.credits=course.course_code
        existed.teacher=course.teacher
        db.commit()
        db.refresh(existed)
        return existed
    except Exception:
        db.rollback()
        raise

def delete_course(id:int,db:Session):
    deleted=course_repository.delete_course(id,db)
    if deleted is None:
                  raise custom_exceptions.CourseNotFoundException
    try:
        db.delete(deleted)
        db.commit()
        return {"message":"Course deleted"}
    except Exception:
                  db.rollback()
                  raise

