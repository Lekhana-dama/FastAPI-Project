from sqlalchemy.orm import Session
from database_models.enrollment_models import EnrollmentDB
def create_enrollment(student_id:int,course_id:int,db:Session):
    new_enrollment=EnrollmentDB(
        student_id=student_id,
        course_id=course_id,
    )
    db.add(new_enrollment)
    return new_enrollment
def get_enrollment(student_id:int,course_id:int,db:Session):
    return db.query(EnrollmentDB).filter(
        EnrollmentDB.student_id==student_id,EnrollmentDB.course_id==course_id
        ).first()
def get_student_enrollments(student_id:int,db:Session):
    return db.query(EnrollmentDB).filter(EnrollmentDB.student_id==student_id).all()
def get_course_enrollments(course_id:int,db:Session):
    return db.query(EnrollmentDB).filter(EnrollmentDB.course_id==course_id).all()

def delete_enrollment(student_id:int,course_id:int,db:Session):
    return db.query(EnrollmentDB).filter(
        EnrollmentDB.student_id==student_id,EnrollmentDB.course_id==course_id
        ).first()