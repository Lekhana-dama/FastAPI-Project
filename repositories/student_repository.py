from database_models.student_models import StudentDB
from database_models.enrollment_models import EnrollmentDB
from sqlalchemy.orm import Session,joinedload
from sqlalchemy import  or_
from pydantic_models.student_model import Student
def create_student(student:Student,db:Session):
    new_student=StudentDB(
        id=student.id,
        name=student.name,
        branch=student.branch,
        year=student.year,
    )
    db.add(new_student)
    return new_student
def get_all_students(skip:int,limit:int,
                     branch:str|None,year:int|None,
                     sort:str|None,
                     search:str|None,db:Session):
    query=db.query(StudentDB)
    if branch:
        query=query.filter(StudentDB.branch==branch)
    if year:
        query=query.filter(StudentDB.year==year)
    if sort:
        if sort=="name":
            query=query.order_by(StudentDB.name)
        elif sort=="-name":
            query=query.order_by(StudentDB.name.desc())
        elif sort=="year":
            query=query.order_by(StudentDB.year)
        elif sort=="-year":
            query=query.order_by(StudentDB.year.desc())
    if search:
        query=query.filter(
            or_(
                StudentDB.name.ilike(f"%{search}%"),
                StudentDB.branch.ilike(f"%{search}%")
                )
        )
    return (query
            .offset(skip)
            .limit(limit)
            .all())
def get_student_by_id(id:int,db:Session):
    return db.query(StudentDB).filter(StudentDB.id==id).first()

def update_student(id:int,db:Session):
    return db.query(StudentDB).filter(StudentDB.id==id).first()

def delete_student(id:int,db:Session):
    return db.query(StudentDB).filter(StudentDB.id==id).first()

def get_enrollment(student_id:int,course_id:int,db:Session):
    return db.query(EnrollmentDB).filter(EnrollmentDB.student_id==student_id
             , EnrollmentDB.course_id==course_id).first()

def get_student_with_courses(id:int,db:Session):
    return ( db.query(StudentDB)
        .options(
        joinedload(StudentDB.enrollments)
        .joinedload(EnrollmentDB.course))
        .filter(StudentDB.id==id).first()
    )
    