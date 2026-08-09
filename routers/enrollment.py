from services import enrollment_service
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
from dependencies import get_current_admin,get_current_user
router=APIRouter(prefix="/enrollment",tags=["Enrollment"])
@router.post("/{student_id}/{course_id}")
def create(student_id:int,course_id:int,db:Session=Depends(get_db),current_user=Depends(get_current_admin)):
    return enrollment_service.create_enrollment(student_id,course_id,db)

@router.get("/{student_id}/{course_id}")
def get_enrollent(student_id:int,course_id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return enrollment_service.get_enrollment(student_id,course_id,db)

@router.delete("/{student_id}/{course_id}")
def delete_enrollment(student_id:int,course_id:int,db:Session=Depends(get_db),current_user=Depends(get_current_admin)):
    return enrollment_service.delete_enrollment(student_id,course_id,db)

@router.get("/student/{student_id}")
def get_student_enrollments(student_id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return enrollment_service.get_student_enrollments(student_id,db)
@router.get("/course/{course_id}")
def get_course_enrollments(course_id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return enrollment_service.get_course_enrollments(course_id,db)


