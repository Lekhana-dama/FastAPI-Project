from sqlalchemy.orm import Session
from pydantic_models.student_model import Student
from fastapi import HTTPException
from repositories import student_repository
from exceptions import custom_exceptions
import logging
import logging_config

logger=logging.getLogger(__name__)
def create_student(student:Student,db:Session):
    logger.info("Creating student with ID %s",student.id)
    existing=student_repository.get_student_by_id(student.id,db)
    if existing:
          logger.warning(
               "student with ID %s already exists",
               student.id
          )
          raise custom_exceptions.StudentAlreadyExistsException
    try:
          new_student=student_repository.create_student(student,db)
    
          db.commit()
          db.refresh(new_student)
          logger.info(
               "Student with ID %s created sucessfully",
               student.id
          )
          return new_student
    except Exception:
         db.rollback()
         logger.exception(
              "failed to create student with ID %s",
              student.id
         )
         raise
     
    

def get_all_students(skip:int,limit:int,
                     branch:str|None,
                     year:int|None,
                     sort:str|None,
                     search:str|None,db:Session):
    students=student_repository.get_all_students(skip,limit,branch,year,sort,search,db)
    return students

def get_student_by_id(id:int,db:Session):
    student=student_repository.get_student_by_id(id,db)
    if student is None:
        raise custom_exceptions.StudentNotFoundException
    return student
        

def update_student(id:int,student:Student,db:Session):
     # db=SessionLocal()
    existing_student=student_repository.update_student(id,db)
    if existing_student is None:
           raise custom_exceptions.StudentNotFoundException
    try:
          existing_student.name=student.name
          existing_student.branch=student.branch
          existing_student.year=student.year
          db.commit()
          db.refresh(existing_student)
          return existing_student
    except Exception:
         db.rollback()
         raise

def delete_student(id:int,db:Session):
     deleted=student_repository.delete_student(id,db)
     if deleted is None:
              raise custom_exceptions.StudentNotFoundException
     try:
        db.delete(deleted)
        db.commit()
        return {"message":"student deleted"}
     except Exception:
              db.rollback()
              raise
def get_student_courses(id:int,db:Session):
     student=student_repository.get_student_with_courses(id,db)
     if student is None:
          raise custom_exceptions.StudentNotFoundException
     course=[]
     for enrollment in student.enrollments:
          course.append(enrollment.course)
     return course

