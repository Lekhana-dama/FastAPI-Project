from repositories  import enrollment_repository,student_repository,course_repository
from sqlalchemy.orm import Session
from fastapi import HTTPException
from exceptions import custom_exceptions,exception_handlers

def create_enrollment(student_id:int,course_id:int,db:Session):
    student=student_repository.get_student_by_id(student_id,db)
    if student is None:
        raise custom_exceptions.EnrollmentNotFoundException
    course=course_repository.get_course_by_id(course_id,db)
    if course is None:
            raise  custom_exceptions.EnrollmentNotFoundException
    existing=enrollment_repository.get_enrollment(student_id,course_id,db)
    if existing :
        raise custom_exceptions.EnrollmentAlreadyExistsException
    try:
        new_enrollment=enrollment_repository.create_enrollment(student_id,course_id,db)
        db.commit()
        db.refresh(new_enrollment)
        return new_enrollment
    except Exception:
            db.rollback()
            raise

def get_enrollment(student_id:int,course_id:int,db:Session):
    enrollment=enrollment_repository.get_enrollment(student_id,course_id,db)
    if enrollment is None: 
        raise custom_exceptions.EnrollmentNotFoundException
    return enrollment

def get_student_enrollments(student_id:int,db:Session):
     student=student_repository.get_student_enrollments(student_id,db)
     if student is None:
          raise  custom_exceptions.EnrollmentNotFoundException
     return enrollment_repository.get_student_enrollments(student_id,db)

def get_course_enrollments(course_id:int,db:Session):
     course=course_repository.get_course_enrollments(course_id,db)
     if course is None:
          raise custom_exceptions.EnrollmentNotFoundException
     return enrollment_repository.get_course_enrollments(course_id,db)

def delete_enrollment(student_id:int,course_id:int,db:Session):
    deleted=enrollment_repository.delete_enrollment(student_id,course_id,db)
    if deleted is None:
        raise  custom_exceptions.EnrollmentNotFoundException
    try:
        db.delete(deleted)
        db.commit()
        return {"message":"Enrollment deleted"}
    except Exception:
            db.rollback()
            raise